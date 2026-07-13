"""
MailWatch account manager.
"""

from .models import MailAccount


class AccountManager:
    def __init__(self):
        self.accounts = []

    def add(self, account: MailAccount):
        self.accounts.append(account)
        return account

    def remove(self, email: str):
        self.accounts = [
            account for account in self.accounts
            if account.email != email
        ]

    def all(self):
        return self.accounts