"""
MailWatch IMAP client placeholder.
"""

from mailwatch.core.message import MailMessage


class IMAPClient:
    def __init__(self, account):
        self.account = account
        self.connected = False

    def connect(self):
        self.connected = True
        return True

    def disconnect(self):
        self.connected = False
        return True

    def fetch_messages(self):
        if not self.connected:
            return []

        return [
            MailMessage.create(
                message_id="demo-001",
                subject="MailWatch test message",
                sender="sender@example.com",
                recipient=self.account.email if hasattr(self.account, "email") else "unknown",
                body="Hello MailWatch",
            )
        ]