from mailwatch.accounts.manager import AccountManager
from mailwatch.accounts.models import MailAccount
from mailwatch.core.watcher import MailWatcher
from mailwatch.core.processor import MessageProcessor
from mailwatch.rules.engine import RuleEngine


def main():
    watcher = MailWatcher()

    manager = AccountManager()
    manager.add(
        MailAccount(
            name="Demo",
            email="demo@example.com",
            server="imap.example.com",
            username="demo@example.com",
        )
    )

    rules = RuleEngine()
    rules.add_rule(lambda message: "contains hello" if "hello" in message.lower() else None)

    processor = MessageProcessor(rules)

    watcher.start()

    print("MailWatch started")
    print(watcher.status())
    print(manager.all())
    print(processor.process("Hello MailWatch"))


if __name__ == "__main__":
    main()