from mailwatch.accounts.models import MailAccount
from mailwatch.core.imap_client import IMAPClient


def test_imap_client_fetch():
    account = MailAccount(
        name="Test",
        email="test@example.com",
        server="imap.example.com",
        username="test@example.com",
    )

    client = IMAPClient(account)

    client.connect()

    messages = client.fetch_messages()

    assert len(messages) == 1
    assert messages[0].subject == "MailWatch test message"