# -----------------------------------------------------------
# Existing numeric engine (polarity flips + emergent tensor)
# -----------------------------------------------------------
import os
import torch

# polarity-swap matrix
P = torch.tensor([[0., 1.],
                  [1., 0.]])

def flip(sig: torch.Tensor) -> torch.Tensor:
    """Apply polarity matrix to 2-vector signal."""
    return torch.matmul(P, sig)

def emergent_field(sig_a: torch.Tensor, sig_b: torch.Tensor) -> torch.Tensor:
    """Outer product ⇒ 2 × 2 field tensor."""
    return torch.ger(sig_a, sig_b)

# -----------------------------------------------------------
# OPTIONAL symbolic-self loop (flag-gated)
# -----------------------------------------------------------
_ENABLE_SYMBOLIC = os.getenv("FRACTON_SYMBOLIC", "0") == "1"
if _ENABLE_SYMBOLIC:
    from fracton.symbolic.model import SymbolicSelf
    from fracton.symbolic.policies import REGISTRY
    _SYM = SymbolicSelf.load()

def process_message(msg: str, history: list[str] | None = None) -> str:
    """
    Pass a model output through the symbolic audit.
    Call this from your agent loop **instead of** printing msg directly.
    """
    if not _ENABLE_SYMBOLIC:
        return msg

    repairs = _SYM.audit(msg)
    if not repairs:
        return msg

    patches = [
        REGISTRY[r.replace(".", "_")](msg)
        for r in repairs if r in REGISTRY
    ]
    # Prepend repair notes; you can change formatting.
    return "\n".join(patches) + "\n" + msg

# -----------------------------------------------------------
# Back-compat alias (used by tests)
# -----------------------------------------------------------
def run_cycle(message: str, history: list[str] | None = None) -> str:
    """Deprecated — will be removed in 0.4; wraps `process_message`."""
    return process_message(message, history or [])
