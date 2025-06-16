import yaml

from mockserve.config import MockConfig


class ConfigLoader:
    """handle loading of mocked config"""

    @staticmethod
    def load(filepath: str) -> MockConfig:
        """load mocked config"""
        with open(filepath, "r") as config_file:
            config_dict = yaml.safe_load(config_file)
        return MockConfig(**config_dict)
