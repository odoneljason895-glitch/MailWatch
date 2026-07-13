from datetime import UTC, datetime

from imapclient import IMAPClient as Client

from mailwatch.accounts.models import MailAccount
from mailwatch.core.logger import get_logger
from mailwatch.core.models import MailMessage


class IMAPClient:
    def __init__(self, account: MailAccount):
        self.account = account
        self.connected = False
        self.client = None
        self.logger = get_logger("IMAPClient")

    def connect(self):
        if self.account.server == "imap.example.com" or not self.account.password:
            self.connected = True
            self.logger.info("Demo IMAP connection")
            return

        self.client = Client(
            self.account.server,
            port=self.account.port,
            ssl=True,
        )

        self.client.login(
            self.account.username,
            self.account.password,
        )

        self.connected = True

        self.logger.info(
            f"Connected to {self.account.email}"
        )

    def fetch_messages(self):
        if not self.connected:
            self.connect()

        return [
            MailMessage(
                message_id="demo-001",
                subject="MailWatch test message",
                sender="sender@example.com",
                recipient=self.account.email,
                received_at=datetime.now(UTC),
                body="Hello MailWatch",
            )
        ]

    def disconnect(self):
        if self.connected and self.client:
            self.client.logout()

        self.connected = False
        self.logger.info("Disconnected")