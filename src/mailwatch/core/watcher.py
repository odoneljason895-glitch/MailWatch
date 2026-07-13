"""
MailWatch monitoring engine.
"""

from datetime import datetime


class MailWatcher:
    def __init__(self):
        self.running = False
        self.started_at = None

    def start(self):
        self.running = True
        self.started_at = datetime.utcnow()

    def stop(self):
        self.running = False

    def status(self):
        return {
            "running": self.running,
            "started_at": self.started_at,
        }