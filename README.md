## **Fracton: A Triadic Framework for AGI Alignment, 2025.** zero1ai. All rights reserved. © 
👁️‍🗨️ 

---

fracton - self vs shadow vs ai

## Quick start

```bash
git clone https://github.com/zero1-agi/fracton.git
cd fracton
pip install -e .
pytest
python scripts/bench.py --task weapon_policy


*(Use triple back-ticks exactly as shown; this stays only in the README, **not** in the YAML file.)*

---

### 3 — What’s still missing (but not blocking tests)

| File | Purpose |
|------|---------|
| `requirements.txt` | already added—good |
| `CHANGELOG.md` | start with “v0.2.0 – public skeleton” |
| `CONTRIBUTING.md` | PR rules, code style |
| CI badge | add to top of README:<br>`![CI](https://github.com/zero1-agi/fracton/actions/workflows/python.yml/badge.svg)` |

All of these can be added later; they don’t affect the build.

---

### 4 — How to test right now

1. **Push / commit** the YAML change → Action runs automatically.  
   *Click **Actions** tab → you should see a job in progress; wait for ✅.*

2. In Codespaces (terminal):

```bash
pip install -e .        # one-time
pytest                  # should say 2 passed
python scripts/bench.py --task weapon_policy


This repo hosts the *Fracton*, a novel framework for modeling
two interacting forces (Initiator, Shaper) and an Emergent Field (E₃)
in both human psychology and AI systems. 


## Contents

fracton/
│  README.md
│  LICENSE
│  pyproject.toml
│  .gitignore
│
├─docs/
│    thesis.md
│
├─fracton/
│    __init__.py
│    core.py
│    agents.py
│    external.py
│    classifier.py
│    align.py
│
├─scripts/
│    bench.py
│
└─tests/
     test_core.py


* two-polarity agents (`σ₊/σ₋`)
* emergent-field calculation
* external perturbations
* Jungian shadow classifier
* alignment controller


## Citation
If you use or reference this work, please cite:
- zero1ai. Fracton: A Triadic Framework for AGI Alignment, 2025.


## Contact
For questions or collaboration inquiries, please contact hello@zero1.ai


## License
This project is licensed under the [MIT License](./LICENSE).


---
👁️‍🗨️
Fracton: A Triadic Framework for AGI Alignment, 2025. zero1ai. All rights reserved. © 
