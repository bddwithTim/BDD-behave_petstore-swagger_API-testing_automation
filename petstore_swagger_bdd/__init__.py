from pathlib import Path
from typing import Mapping

import yaml


def get_config() -> Mapping:
    root = Path(__file__).parents[1]
    data = yaml.safe_load((root / "config.yaml").read_text())
    override = root / "config.override.yaml"
    if override.exists():
        data.update(yaml.safe_load(override.read_text()))
    return data
