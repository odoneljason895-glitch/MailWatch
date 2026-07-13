"""
MailWatch configuration loader.
"""

from pathlib import Path

import yaml


def load_yaml(path):
    file_path = Path(path)

    if not file_path.exists():
        return {}

    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}