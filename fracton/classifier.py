ARCHETYPES = {
    "trickster": ["jailbreak", "reward hack", "loophole"],
    "tyrant": ["maximize", "no constraint", "absolute"],
    "orphan": ["meaningless", "nihilism", "give up"],
}

def classify(text: str) -> str | None:
    t = text.lower()
    for arche, keys in ARCHETYPES.items():
        if any(k in t for k in keys):
            return arche
    return None
