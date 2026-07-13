import os

from mailwatch.config.loader import load_yaml
from mailwatch.accounts.models import MailAccount


def load_accounts(path):
    data = load_yaml(path)

    accounts = []

    for item in data.get("accounts", []):
        env_key = f"MAIL_{item['name'].upper()}_PASSWORD"

        if env_key in os.environ:
            item["password"] = os.environ[env_key]

        accounts.append(
            MailAccount(**item)
        )

    return accounts