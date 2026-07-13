"""
MailWatch account configuration loader.
"""

from mailwatch.config.loader import load_yaml
from .models import MailAccount


def load_accounts(path):
    data = load_yaml(path)

    accounts = []

    for item in data.get("accounts", []):
        accounts.append(MailAccount(**item))

    return accounts
