"""
MailWatch application container.
"""

from mailwatch.accounts.loader import load_accounts
from mailwatch.core.watcher import MailWatcher
from mailwatch.core.processor import MessageProcessor
from mailwatch.rules.engine import RuleEngine


class MailWatchApp:
    def __init__(self, config_path):
        self.accounts = load_accounts(config_path)

        self.rules = RuleEngine()
        self.processor = MessageProcessor(self.rules)

        self.watcher = MailWatcher()

    def start(self):
        self.watcher.start()

    def status(self):
        return {
            "watcher": self.watcher.status(),
            "accounts": self.accounts,
        }