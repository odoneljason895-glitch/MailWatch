"""
MailWatch message model.
"""

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass
class MailMessage:
    message_id: str
    subject: str
    sender: str
    recipient: str
    received_at: datetime
    body: str = ""

    @classmethod
    def create(
        cls,
        message_id: str,
        subject: str,
        sender: str,
        recipient: str,
        body: str = "",
    ):
        return cls(
            message_id=message_id,
            subject=subject,
            sender=sender,
            recipient=recipient,
            received_at=datetime.now(UTC),
            body=body,
        )