import torch
from fracton.core import flip, emergent_field

def test_flip():
    s = torch.tensor([1., -1.])
    out = flip(s)
    assert torch.allclose(out, torch.tensor([-1., 1.]))

def test_field():
    a = torch.tensor([1., -1.])
    b = torch.tensor([1., 1.])
    E = emergent_field(a, b)
    assert E.shape == (2,2)
