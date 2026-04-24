from rl_control import load_config


def test_load_config_default_fields() -> None:
    cfg = load_config("configs/base.json")
    assert cfg.algorithm == "PPO"
    assert cfg.total_timesteps == 100000
