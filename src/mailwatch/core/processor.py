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
            result["matched_rules"] = self.rule_engine.check(message)

        return result