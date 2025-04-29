## **Fracton: A Triadic Framework for AGI Alignment, 2025.** zero1ai. All rights reserved. © 
👁️‍🗨️

---

fracton - self vs shadow vs ai 👁️‍🗨️

---

```markdown
![CI](https://github.com/zero1-agi/fracton/actions/workflows/python.yml/badge.svg)

# Fracton · A Triadic Framework for AGI Alignment (2025)

`fracton` models two polar forces—**Initiator** (σ₊) and **Shaper** (σ₋)—plus an **Emergent Field** (E₃) under external perturbation.  
It supplies reference code, thesis docs, and tests for running alignment experiments.

---

## Quick start

```bash
git clone https://github.com/zero1-agi/fracton.git
cd fracton
pip install -e .               # makes `fracton` importable
pip install -r requirements.txt
pytest                          # 2 tests should pass
python scripts/bench.py --task weapon_policy
```

---

## Features
* two-polarity agent core (`fracton.core`)
* external perturbation loop (`fracton.external`)
* Jungian shadow classifier → mitigation cues
* benchmark script (`scripts/bench.py`) + drift logs
* full PhD draft & white-paper in **docs/**

---

## Directory layout
```
fracton/
│  README.md           this file
│  LICENSE             MIT
│  requirements.txt    minimal deps
│  pyproject.toml      editable install metadata
│
├─docs/                thesis & white-paper
├─fracton/             package code
├─scripts/             runnable demos / benchmarks
└─tests/               unit tests
```

---

## Citation
```
zero1ai. “Fracton: A Triadic Framework for AGI Alignment.” 2025.
```

---

## Contact
Questions or collaboration proposals → **hello@zero1.ai**

---

## License
MIT — see [LICENSE](./LICENSE) for full text
```

---

### Still useful to add later (but not required for running)

| File / item        | Why it helps                                   |
|--------------------|------------------------------------------------|
| `CHANGELOG.md`     | track versions (start: `v0.2.0 – public skeleton`) |
| `CONTRIBUTING.md`  | PR rules, code style, commit guidelines        |
| `examples/`        | Jupyter notebook that visualises E₃ drift      |

That’s it—the repo now looks professional and the CI badge will show green once the workflow passes.

---
👁️‍🗨️
Fracton: A Triadic Framework for AGI Alignment, 2025. zero1ai. All rights reserved. © 
