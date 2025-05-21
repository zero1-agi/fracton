__version__ = "0.2.0"
from .core import emergent_field, P

# --- symbolic-self addon -----------------------------
try:
    from .symbolic.model import SymbolicSelf  # re-export for users
except ModuleNotFoundError:
    # running on an install that doesn’t include the new module yet
    pass
