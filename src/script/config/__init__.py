import os
from .config import Config
from pathlib import Path


def load_config(file_name):
    """load config

    Args:
        file_name (str): config file name

    Returns:
        Dict[*]: config
    """
    root = Path(os.environ["ROOT_DIR"]) / "cfg" / file_name
    config_path = root.with_suffix(".yml")
    config = Config(config_path)
    return config
