from mailwatch.core.app import MailWatchApp


def test_app_start():
    app = MailWatchApp("src/mailwatch/config/accounts.yml")

    app.start()

    status = app.status()

    assert status["watcher"]["running"] is True
    assert len(status["accounts"]) == 1