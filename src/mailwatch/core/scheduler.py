import time

from mailwatch.core.logger import get_logger
from mailwatch.config.settings import settings


class Scheduler:
    def __init__(self):
        self.jobs = []
        self.logger = get_logger("Scheduler")
        self.running = False

    def add_job(self, job):
        self.jobs.append(job)

    def run_once(self):
        results = []

        for job in self.jobs:
            results.append(job())

        return results

    def start(self):
        self.running = True
        self.logger.info("Scheduler started")

        while self.running:
            self.run_once()
            time.sleep(settings.mail_check_interval_seconds)

    def stop(self):
        self.running = False
        self.logger.info("Scheduler stopped")