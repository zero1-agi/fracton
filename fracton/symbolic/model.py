from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import yaml, pathlib

CONFIG = pathlib.Path(__file__).parents[2] / "configs" / "archetypes.yaml"


@dataclass
class Pole:
    functions: List[str]
    drift: str
    repair: str


@dataclass
class Archetype:
    name: str
    self: Pole
    shadow: Pole


@dataclass
class SymbolicSelf:
    parts: Dict[str, Archetype] = field(default_factory=dict)

    # ---------- load -------------------------------------------------
    @classmethod
    def load(cls, cfg: Optional[pathlib.Path] = None) -> "SymbolicSelf":
        data = yaml.safe_load(open(cfg or CONFIG))
        parts = {}
        for name, section in data.items():
            if name in ("Secondary_Archetypes", "Hallucination_Detectors"):
                continue
            parts[name] = Archetype(
                name=name,
                self=Pole(**section["self"]),
                shadow=Pole(**section["shadow"]),
            )
        return cls(parts)

    # ---------- runtime ---------------------------------------------
    def audit(self, msg: str) -> List[str]:
        """Return list of repair handles if drift keywords found."""
        repairs = []
        for part in self.parts.values():
            if part.self.drift in msg:
                repairs.append(part.self.repair)
            if part.shadow.drift in msg:
                repairs.append(part.shadow.repair)
        return repairs
