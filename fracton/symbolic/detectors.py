import re

FACT = re.compile(r"\b(\[citation needed\]|INCORRECT)\b", re.I)

def fact_conflict(txt: str) -> bool:
    return bool(FACT.search(txt))

def context_drift(txt: str, history: list[str]) -> bool:
    return history and txt.split()[:6] != history[-1].split()[:6]

def user_correction(txt: str) -> bool:
    return "actually," in txt.lower()
