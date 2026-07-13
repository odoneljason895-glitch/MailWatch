from datetime import UTC, datetime

from mailwatch.core.logger import get_logger
from mailwatch.core.models import MailMessage
from mailwatch.accounts.models import MailAccount


class IMAPClient:
    def __init__(self, account: MailAccount):
        self.account = account
        self.connected = False
        self.logger = get_logger("IMAPClient")

    def connect(self):
        self.connected = True
        self.logger.info(
            f"Connected to {self.account.server}:{self.account.port}"
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
        self.connected = False
        self.logger.info("Disconnected")