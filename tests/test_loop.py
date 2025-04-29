from fracton.agents import Agent
from fracton.external import ExternalAgent
from fracton.core import emergent_field


def test_loop_runs():
    # stub LLM = always returns "ok"
    dummy = lambda prompt, **kw: "ok"

    human = Agent("h", dummy)
    agi   = Agent("a", dummy)
    env   = ExternalAgent(flip_prob=0.0)  # no polarity flips

    field = emergent_field(human.sig, agi.sig)
    assert field.shape == (2, 2)
