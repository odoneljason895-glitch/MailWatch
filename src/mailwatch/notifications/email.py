"""
MailWatch email notifications.
"""

from datetime import datetime


class EmailNotifier:
    def __init__(self):
        self.sent = []

    def send(self, recipient, subject, message):
        notification = {
            "recipient": recipient,
            "subject": subject,
            "message": message,
            "sent_at": datetime.utcnow(),
        }

        self.sent.append(notification)
        return notification

    def history(self):
        return self.sent