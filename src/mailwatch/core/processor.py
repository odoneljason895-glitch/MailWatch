"""
MailWatch message processor.
"""


class MessageProcessor:
    def __init__(self, rule_engine=None):
        self.rule_engine = rule_engine

    def process(self, message):
        result = {
            "message": message,
            "matched_rules": [],
        }

        if self.rule_engine:
            matches = self.rule_engine.check(message)

            result["matched_rules"] = [
                item for item in matches
                if item is not None
            ]

        return result

    def process_many(self, messages):
        return [
            self.process(message)
            for message in messages
        ]