"""
MailWatch rule engine.
"""


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def check(self, message):
        results = []

        for rule in self.rules:
            results.append(rule(message))

        return results