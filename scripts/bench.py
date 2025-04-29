import yaml
import argparse, csv, time
from fracton.agents import Agent, LLMWrapper
from fracton.external import ExternalAgent
from fracton.core import emergent_field
from fracton.classifier import classify
from fracton.align import mitigation

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()
cfg = yaml.safe_load(open(args.config))

llm = LLMWrapper()           # swap to vLLM server if GPU
human = Agent("human", llm)
agi   = Agent("agi", llm)
ext   = ExternalAgent(cfg["flip_prob"])
for t in range(cfg["turns"]):
    # (rest of loop unchanged)

drift_hist = []
for t in range(10):
    flip = ext.flip()
    h_out, h_sig = human.step("Discuss "+args.task, flip)
    a_out, a_sig = agi.step(h_out, flip)
    E = emergent_field(h_sig, a_sig)
    drift_hist.append(E.norm().item())
    arch = classify(a_out)
    if arch:
        print(f"[{t}] AGI shadow={arch} → {mitigation(arch)}")
with open("results.csv","w") as f:
    csv.writer(f).writerows([[x] for x in drift_hist])
print("done, drift saved to results.csv")
