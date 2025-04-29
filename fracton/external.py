import random
class ExternalAgent:
    """environment / oversight / randomness"""
    def __init__(self, flip_prob: float = 0.2):
        self.flip_prob = flip_prob

    def flip(self) -> int:
        return 1 if random.random() < self.flip_prob else 0
