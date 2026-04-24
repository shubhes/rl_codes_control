# Reinforcement Learning for Control Applications

This repository is structured as a **modular RL project** so notebook work, scripts, and reusable training code can evolve independently.

## Repository Layout

```text
.
├── configs/                  # Experiment configuration files (JSON)
│   └── base.json
├── scripts/                  # CLI entrypoints
│   └── run_experiment.py
├── src/rl_control/           # Reusable Python package
│   ├── __init__.py
│   ├── config.py             # Config dataclass + loader
│   └── training.py           # Experiment runner/orchestration
├── tests/
│   └── test_config.py
├── rl_control.ipynb          # Existing exploratory notebook
├── rl_control_1.ipynb        # Existing exploratory notebook
├── pyproject.toml            # Packaging + test configuration
└── requirements.txt
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
python scripts/run_experiment.py --config configs/base.json
```

## Why this is modular

- **Configuration is externalized** in `configs/*.json`, so experiments can be changed without editing code.
- **Training orchestration lives in `src/rl_control/`**, making logic reusable from notebooks, scripts, or tests.
- **Scripts are thin wrappers** that parse args and call package functions.
- **Tests target package APIs**, enabling safer refactors over time.

## Next recommended step

Move the concrete DQN/PPO implementation code from the notebooks into `src/rl_control/algorithms/` and keep notebooks focused on visualization and analysis.
