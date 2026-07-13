from mailwatch.accounts.models import MailAccount
from mailwatch.accounts.manager import AccountManager
from mailwatch.core.watcher import MailWatcher
from mailwatch.rules.engine import RuleEngine


def test_account_manager():
    manager = AccountManager()

    account = MailAccount(
        name="Test",
        email="test@example.com",
        server="imap.example.com",
        username="test@example.com",
    )

    manager.add(account)

    assert len(manager.all()) == 1


def test_watcher():
    watcher = MailWatcher()

    watcher.start()

    assert watcher.status()["running"] is True


def test_rules():
    engine = RuleEngine()

    engine.add_rule(lambda message: "match")

    assert engine.check("mail") == ["match"]