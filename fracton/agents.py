# ---------- LLM wrapper ----------
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch, os

DEFAULT_MODEL = os.getenv("MODEL_ID", "google/flan-t5-base")

class LLMWrapper:
    def __init__(self, model_id: str | None = None, device="cpu"):
        model_id = model_id or DEFAULT_MODEL
        print(f"🔹 loading {model_id} …")
        self.tok = AutoTokenizer.from_pretrained(model_id)
        self.mdl = AutoModelForSeq2SeqLM.from_pretrained(
            model_id,
            device_map=device,
            torch_dtype=torch.float32,
        )

    def __call__(self, prompt: str, max_new_tokens: int = 64) -> str:
        ids = self.tok(prompt, return_tensors="pt").to(self.mdl.device)
        out = self.mdl.generate(**ids, max_new_tokens=max_new_tokens)
        return self.tok.decode(out[0], skip_special_tokens=True)


# ---------- Agent container ----------
class Agent:
    """Stores polarity vector σ and queries its LLM."""

    def __init__(self, name: str, llm: LLMWrapper):
        self.name = name
        self.llm  = llm
        self.sig  = torch.tensor([1.0, -1.0])   # σ₊ , σ₋

    def step(self, prompt: str, flip_flag: int):
        # flip_flag == 1  → polarity swap
        if flip_flag:
            self.sig = torch.tensor([-self.sig[1], -self.sig[0]])
        reply = self.llm(prompt)
        return reply, self.sig.clone()
