"""
MailWatch configuration settings.

Loads environment variables and provides application configuration.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]

# Load .env file if present
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE)


class Settings:
    """
    Main application settings.
    """

    APP_NAME: str = "MailWatch"
    VERSION: str = "0.1.0"

    # Data storage
    DATA_DIR: Path = BASE_DIR / "data"

    # Mail account defaults
    MAIL_CHECK_INTERVAL_SECONDS: int = int(
        os.getenv("MAIL_CHECK_INTERVAL_SECONDS", "60")
    )

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Notification settings
    ENABLE_NOTIFICATIONS: bool = (
        os.getenv("ENABLE_NOTIFICATIONS", "false").lower() == "true"
    )


settings = Settings()