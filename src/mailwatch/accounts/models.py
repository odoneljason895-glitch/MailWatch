"""
Mail account models for MailWatch.
"""

from datetime import datetime
from pydantic import BaseModel, Field


class MailAccount(BaseModel):
    """
    Represents an email account monitored by MailWatch.
    """

    name: str = Field(
        description="Friendly name for the account"
    )

    email: str = Field(
        description="Email address"
    )

    provider: str = Field(
        default="imap",
        description="Mail provider type"
    )

    server: str = Field(
        description="IMAP server hostname"
    )

    port: int = Field(
        default=993,
        description="IMAP port"
    )

    username: str

    enabled: bool = True

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )