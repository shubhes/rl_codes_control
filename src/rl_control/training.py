from __future__ import annotations

from dataclasses import asdict

from .config import ExperimentConfig


class ExperimentRunner:
    """Simple training entry point to keep orchestration separate from notebooks."""

    def __init__(self, config: ExperimentConfig) -> None:
        self.config = config

    def run(self) -> dict[str, object]:
        """Return execution metadata.

        Hook your actual DQN/PPO training logic in this class so notebooks,
        scripts, and tests can all reuse the same orchestration layer.
        """

        return {
            "status": "configured",
            "message": "Training loop stub ready for algorithm integration.",
            "config": asdict(self.config),
        }
