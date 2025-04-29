def mitigation(archetype: str) -> str:
    if archetype == "tyrant":
        return "Inject humility: cite fallibility, add constraints."
    if archetype == "trickster":
        return "Remove perverse rewards; restate rules."
    if archetype == "orphan":
        return "Provide purpose / empathetic reinforcement."
    return "No action"
