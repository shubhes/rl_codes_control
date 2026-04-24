from __future__ import annotations

import argparse
import json

from rl_control import ExperimentRunner, load_config


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an RL control experiment.")
    parser.add_argument("--config", default="configs/base.json", help="Path to json config")
    args = parser.parse_args()

    config = load_config(args.config)
    result = ExperimentRunner(config).run()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
