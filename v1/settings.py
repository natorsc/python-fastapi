from functools import lru_cache
from pathlib import Path

from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings

CURRENT_DIRECTORY: Path = Path(__file__).resolve().parent
ROOT_DIR: Path = CURRENT_DIRECTORY.parent
ENV_FILE: str = str(ROOT_DIR.joinpath('.env'))


class Settings(BaseSettings):
    DEBUG: str = 'True'
    DATABASE_URL: str = 'sqlite:///dev.sqlite3'
    FAVICON: Path = CURRENT_DIRECTORY.joinpath(
        'static', 'favicon', 'justcode.ico'
    )
    STATIC_PATH: Path = CURRENT_DIRECTORY.joinpath('static')
    TEMPLATES_PATH: Path = CURRENT_DIRECTORY.joinpath('templates')
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory=TEMPLATES_PATH)

    class Config:
        env_file = ENV_FILE


@lru_cache()
def get_settings():
    return Settings()
