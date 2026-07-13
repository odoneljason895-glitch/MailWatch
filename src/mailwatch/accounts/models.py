from datetime import UTC, datetime

from pydantic import BaseModel


class MailAccount(BaseModel):
    name: str
    email: str
    provider: str = "imap"
    server: str
    port: int = 993
    username: str
    password: str = ""
    enabled: bool = True
    created_at: datetime = datetime.now(UTC)