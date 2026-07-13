from datetime import UTC, datetime

from mailwatch.core.logger import get_logger


class MailWatcher:
    def __init__(self):
        self.running = False
        self.started_at = None
        self.logger = get_logger("MailWatcher")

    def start(self):
        self.running = True
        self.started_at = datetime.now(UTC)
        self.logger.info("Watcher started")

    def stop(self):
        self.running = False
        self.logger.info("Watcher stopped")

    def status(self):
        return {
            "running": self.running,
            "started_at": self.started_at,
        }