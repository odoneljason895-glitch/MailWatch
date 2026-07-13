"""
MailWatch notification manager.
"""

from mailwatch.notifications.email import EmailNotifier


class NotificationManager:
    def __init__(self):
        self.email = EmailNotifier()

    def notify(self, recipient, subject, message):
        return self.email.send(
            recipient,
            subject,
            message,
        )