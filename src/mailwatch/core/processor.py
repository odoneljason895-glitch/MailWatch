from mailwatch.core.models import MailMessage


class MessageProcessor:
    def __init__(self, rules=None):
        self.rules = rules

    def process(self, message):
        if isinstance(message, dict):
            message = MailMessage(**message)

        matched = []

        if self.rules:
            matched = self.rules.check(message)

        return {
            "message": message,
            "matched_rules": matched,
        }

    def process_many(self, messages):
        return [
            self.process(message)
            for message in messages
        ]