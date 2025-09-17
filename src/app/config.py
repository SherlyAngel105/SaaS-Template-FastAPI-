from typing import Optional

from src.app.utils.schemas_utils import AbstractSettings, BaseModel, EmailStr


class DBSettings(AbstractSettings):
    """Database Settings

    Args:
        AbstractSettings (_type_): inherits Core settings.
    """

    name: str = "saas_template"
    username: str = "postgres"
    password: str = "password"
    hostname: str = "localhost"
    port: int = 5432

    class Config:
        env_prefix = "DB_"
        extra = "ignore"


class AuthSettings(AbstractSettings):
    """Authentication Settings

    Args:
        AbstractSettings (_type_): inherits Core settings.
    """

    access_secret_key: str = "your_access_secret_key_here"
    refresh_secret_key: str = "your_refresh_secret_key_here"
    access_time_exp: int = 15
    refresh_time_exp: int = 10080
    algorithm: str = "HS256"
    frontend_url: str = "http://localhost:3000"

    class Config:
        env_prefix = ""
        extra = "ignore"


class MailSettings(AbstractSettings):
    """Mail Settings

    Args:
        AbstractSettings (_type_): inherits Core settings.
    """

    mail_username: str = "your_email@example.com"
    mail_password: str = "your_email_password"
    mail_from: EmailStr = "your_email@example.com"
    mail_port: int = 587
    mail_server: str = "smtp.gmail.com"
    mail_from_name: str = "SaaS Template"

    class Config:
        env_prefix = "MAIL_"
        extra = "ignore"


class TestSettings(AbstractSettings):
    should_test: Optional[bool] = False

    class Config:
        env_prefix = ""
        extra = "ignore"


db_settings = DBSettings()
auth_settings = AuthSettings()
mail_settings = MailSettings()
test_status = TestSettings()
