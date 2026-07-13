"""
MailWatch notification manager.
"""

from mailwatch.notifications.email import EmailNotifier


class NotificationManager:
    def __init__(self):
        self.notifiers = [
            EmailNotifier()
        ]

    def notify(self, recipient, subject, message):
        results = []

        for notifier in self.notifiers:
            results.append(
                notifier.send(
                    recipient,
                    subject,
                    message,
                )
            )

        return results