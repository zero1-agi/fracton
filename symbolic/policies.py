def Senex_stabilise(msg: str) -> str:
    return "🧓 Senex: grounding exuberant output, adding structure."

def Trickster_disrupt(msg: str) -> str:
    return "🃏 Trickster: injecting creative perturbation."

def Great_Mother_contain(msg: str) -> str:
    return "🌱 Great Mother: containing chaos, re-centering empathy."

def Puer_Aeternus_refresh(msg: str) -> str:
    return "🚀 Puer: refreshing stale reasoning with new possibilities."

# secondary
def fact_check(msg):         return "🔍 Sage: verifying facts."
def idea_rebuild(msg):       return "🎨 Creator: regenerating idea."
def decision_gate(msg):      return "👑 Ruler: making final decision."
# … add the rest as needed

REGISTRY = {fn.__name__: fn for fn in globals().values() if callable(fn)}
