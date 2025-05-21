from fracton.symbolic.model import SymbolicSelf

def test_repair_detection():
    ss = SymbolicSelf.load()
    msg = "reckless_output plus fossilized_reasoning"
    repairs = ss.audit(msg)
    assert "Senex.stabilise" in repairs
    assert "Puer_Aeternus.refresh" in repairs
