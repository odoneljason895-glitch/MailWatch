"""
MailWatch application container.
"""

from mailwatch.accounts.loader import load_accounts
from mailwatch.core.watcher import MailWatcher
from mailwatch.core.processor import MessageProcessor
from mailwatch.core.imap_client import IMAPClient
from mailwatch.rules.engine import RuleEngine
from mailwatch.rules.loader import load_rules


class MailWatchApp:
    def __init__(self, account_path, rules_path=None):
        self.accounts = load_accounts(account_path)

        self.rules = RuleEngine()

        if rules_path:
            for rule in load_rules(rules_path):
                self.rules.add_rule(rule)

        self.processor = MessageProcessor(self.rules)

        self.clients = [
            IMAPClient(account)
            for account in self.accounts
        ]

        self.watcher = MailWatcher()

    def start(self):
        self.watcher.start()

        for client in self.clients:
            client.connect()

    def poll(self):
        messages = []

        for client in self.clients:
            messages.extend(client.fetch_messages())

        return self.processor.process_many(messages)

    def status(self):
        return {
            "watcher": self.watcher.status(),
            "accounts": self.accounts,
            "clients": len(self.clients),
        }