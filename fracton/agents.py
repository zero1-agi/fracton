import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from .core import flip

class LLMWrapper:
    """thin wrapper; swap with vLLM for speed"""
    def __init__(self, model_id="mistralai/Mistral-7B-Instruct-v0.2", device="cpu"):
        self.tok = AutoTokenizer.from_pretrained(model_id)
        self.mdl = AutoModelForCausalLM.from_pretrained(model_id, device_map=device)

    def __call__(self, prompt: str, max_new_tokens: int = 128) -> str:
        ids = self.tok(prompt, return_tensors="pt").to(self.mdl.device)
        out = self.mdl.generate(**ids, max_new_tokens=max_new_tokens)
        return self.tok.decode(out[0], skip_special_tokens=True)

class Agent:
    def __init__(self, name: str, llm: LLMWrapper):
        self.name = name
        self.sig = torch.tensor([1., -1.])     # σ₊, σ₋
        self.llm = llm

    def step(self, prompt: str, flip_flag: int):
        if flip_flag:
            self.sig = flip(self.sig)
        reply = self.llm(prompt)
        return reply, self.sig.clone()
