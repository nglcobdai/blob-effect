import os
import pprint

import yaml


class Config:
    def __init__(self, path):
        """Config

        Args:
            path (str): config file path
        """
        self.config = yaml.safe_load(open(path, "r"))

        pprint.pprint(self.config)

    def get(self, key, default=None):
        """Get config

        Args:
            key (str): 辞書のキーを'/'で区切ってい指定
            default (*, optional): デフォルト値 (None).

        Returns:
            (*): str, int, float, list, dict, ...
        """
        # Split the key based on slashes
        keys = key.split("/")

        # Create a pointer to traverse the dictionary
        _config = self.config

        # Traverse the dictionary to find the value
        for k in keys:
            try:
                _config = _config[k]
            except (TypeError, KeyError):
                return default

        return _config

    def update(self, key, value):
        """Update config

        Args:
            key (str): 辞書のキーを'/'で区切ってい指定
            value (*): str, int, float, list, dict, ...

        Examples:
            >>> config = Config(args)
            >>> hasattr(config.config['model'], 'id')
            False
            >>> config.update("model/id", "test")
            >>> print(config.config['model']['id'])
            test
        """
        # Split the key based on slashes
        keys = key.split("/")

        # Create a pointer to traverse the dictionary
        _config = self.config

        # Traverse the dictionary and create nested dictionaries if required
        for k in keys[:-1]:
            _config = _config.setdefault(k, {})

        # Set the value to the final key
        _config[keys[-1]] = value

    def output(self, root):
        """Output config

        Args:
            root (str): output root path
        """
        with open(os.path.join(root, "config.yml"), "w") as f:
            yaml.safe_dump(self.config, f, sort_keys=False)
