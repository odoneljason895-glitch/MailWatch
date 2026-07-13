from datetime import datetime

from pydantic import BaseModel


class MailMessage(BaseModel):
    message_id: str
    subject: str
    sender: str
    recipient: str
    received_at: datetime
    body: str