"""
MailWatch application container.
"""

from mailwatch.accounts.loader import load_accounts
from mailwatch.core.watcher import MailWatcher
from mailwatch.core.processor import MessageProcessor
from mailwatch.core.imap_client import IMAPClient
from mailwatch.core.scheduler import Scheduler
from mailwatch.rules.engine import RuleEngine
from mailwatch.rules.loader import load_rules
from mailwatch.notifications import NotificationManager


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

        self.notifications = NotificationManager()

        self.watcher = MailWatcher()

        self.scheduler = Scheduler()
        self.scheduler.add_job(self.poll)

    def start(self):
        self.watcher.start()

        for client in self.clients:
            client.connect()

    def poll(self):
        messages = []

        for client in self.clients:
            messages.extend(client.fetch_messages())

        results = self.processor.process_many(messages)

        for result in results:
            if result["matched_rules"]:
                self.notifications.notify(
                    result["message"].recipient,
                    "MailWatch Alert",
                    str(result),
                )

        return results

    def status(self):
        return {
            "watcher": self.watcher.status(),
            "accounts": self.accounts,
            "clients": len(self.clients),
            "scheduler_jobs": len(self.scheduler.jobs),
        }