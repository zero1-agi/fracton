import torch

# polarity-swap matrix
P = torch.tensor([[0., 1.],
                  [1., 0.]])

def flip(sig: torch.Tensor) -> torch.Tensor:
    """apply polarity matrix"""
    return torch.matmul(P, sig)

def emergent_field(sig_a: torch.Tensor, sig_b: torch.Tensor) -> torch.Tensor:
    """outer product => 2×2 field tensor"""
    return torch.ger(sig_a, sig_b)
