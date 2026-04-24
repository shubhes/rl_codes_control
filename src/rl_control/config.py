from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class ExperimentConfig:
    """Typed experiment configuration."""

    name: str
    algorithm: str
    env_id: str
    total_timesteps: int
    seed: int


DEFAULT_CONFIG_PATH = Path("configs/base.json")


def load_config(config_path: str | Path = DEFAULT_CONFIG_PATH) -> ExperimentConfig:
    """Load and validate a json config into a dataclass."""

    path = Path(config_path)
    raw: dict[str, Any] = json.loads(path.read_text())

    return ExperimentConfig(
        name=raw.get("name", "baseline"),
        algorithm=raw.get("algorithm", "PPO"),
        env_id=raw.get("env_id", "CartPole-v1"),
        total_timesteps=int(raw.get("total_timesteps", 100_000)),
        seed=int(raw.get("seed", 42)),
    )
