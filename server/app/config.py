import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "WinMes"
    )

    APP_VERSION = os.getenv(
        "APP_VERSION",
        "6.0.0"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "CHANGE_ME_IN_ENV"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            "30"
        )
    )

    REFRESH_TOKEN_EXPIRE_DAYS = int(
        os.getenv(
            "REFRESH_TOKEN_EXPIRE_DAYS",
            "30"
        )
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./winmes.db"
    )


settings = Settings()