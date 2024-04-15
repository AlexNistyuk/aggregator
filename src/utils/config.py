import os
from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = os.path.join(BASE_DIR.parent.parent, ".env")


class Settings(BaseSettings):
    bot_token: SecretStr
    data_filename: str

    @property
    def data_file(self):
        return os.path.join(BASE_DIR.parent.parent, self.data_filename)

    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="allow")


@lru_cache
def get_settings():
    return Settings()
