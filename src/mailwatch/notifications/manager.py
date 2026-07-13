from mailwatch.notifications.email import EmailNotifier
from mailwatch.core.logger import get_logger


class NotificationManager:
    def __init__(self):
        self.email = EmailNotifier()
        self.logger = get_logger("NotificationManager")
        self.sent = []

    def notify(self, recipient, subject, message):
        result = self.email.send(
            recipient,
            subject,
            message,
        )

        self.sent.append(result)

        self.logger.info(
            f"Notification sent to {recipient}"
        )

        return result

    def history(self):
        return self.sent