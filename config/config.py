from pathlib import Path
from typing import Dict

import yaml


class Config:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path=config_path)

    def load_config(self, config_path: str) -> Dict:
        file = Path(config_path)
        if not file.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        try:
            config = yaml.safe_load(file.read_text())
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid config file: {config_path}") from e
        return config
    
    def get_item(self, key: str) -> str | None:
        return self.config.get(key, None)
