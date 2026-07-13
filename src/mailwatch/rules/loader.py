"""
MailWatch rule configuration loader.
"""

from mailwatch.config.loader import load_yaml
from .filters import contains_text


def load_rules(path):
    data = load_yaml(path)

    rules = []

    for rule in data.get("rules", []):
        if rule.get("type") == "contains":
            rules.append(
                contains_text(rule.get("value", ""))
            )

    return rules