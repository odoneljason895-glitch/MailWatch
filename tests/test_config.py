from mailwatch.config.settings import settings


def test_settings_loaded():
    assert settings.APP_NAME == "MailWatch"
    assert settings.log_level == "INFO"