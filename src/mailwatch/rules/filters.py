"""
MailWatch rule filters.
"""


def contains_text(text):
    def rule(message):
        content = str(message).lower()

        if text.lower() in content:
            return f"contains: {text}"

        return None

    return rule


def from_sender(sender):
    def rule(message):
        if hasattr(message, "sender"):
            if message.sender.lower() == sender.lower():
                return f"from: {sender}"

        return None

    return rule