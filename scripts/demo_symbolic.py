import json, sys
from fracton.symbolic.model import SymbolicSelf
from fracton.symbolic.detectors import fact_conflict, context_drift, user_correction
from fracton.symbolic.policies import REGISTRY

ss = SymbolicSelf.load()
history = []

for line in sys.stdin:
    text = line.strip()
    if not text:
        continue
    history.append(text)

    # baseline drift detection
    triggers = [
        fact_conflict(text),
        context_drift(text, history),
        user_correction(text)
    ]
    actions = ss.audit(text) if any(triggers) else []

    patches = [REGISTRY[a.replace(".", "_")](text) for a in actions if a]
    print(json.dumps({"input": text, "repairs": patches}))
