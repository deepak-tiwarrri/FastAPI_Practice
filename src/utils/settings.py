from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parents[2] / '.env'),
        extra='ignore'
    )
    DB_CONNECTION: str
    SECRET_KEY: str
    ALGORITHM: str
    EXP: int


settings = Settings()  # type: ignore
