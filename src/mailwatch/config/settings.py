from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "MailWatch"

    mail_check_interval_seconds: int = 60
    log_level: str = "INFO"
    enable_notifications: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()