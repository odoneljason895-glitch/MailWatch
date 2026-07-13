from mailwatch.core.scheduler import Scheduler


def test_scheduler_runs_jobs():
    scheduler = Scheduler()

    scheduler.add_job(lambda: "done")

    result = scheduler.run_once()

    assert result == ["done"]