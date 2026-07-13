"""
MailWatch scheduler.
"""

import time


class Scheduler:
    def __init__(self, interval_seconds=60):
        self.interval_seconds = interval_seconds
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def run_once(self):
        results = []

        for job in self.jobs:
            results.append(job())

        return results

    def run(self, cycles=1):
        results = []

        for _ in range(cycles):
            results.extend(self.run_once())
            if cycles > 1:
                time.sleep(self.interval_seconds)

        return results