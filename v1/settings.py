import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings

CURRENT_DIRECTORY: Path = Path(__file__).resolve().parent
ROOT_DIR: Path = CURRENT_DIRECTORY.parent

load_dotenv(dotenv_path=ROOT_DIR.joinpath('.env'), override=True)


class Settings(BaseSettings):
    DEBUG: str = os.getenv('DEBUG')
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    FAVICON: Path = CURRENT_DIRECTORY.joinpath('static', 'favicon', 'justcode.ico')
    STATIC_PATH: Path = CURRENT_DIRECTORY.joinpath('static')
    TEMPLATES_PATH: Path = CURRENT_DIRECTORY.joinpath('templates')
    TEMPLATES: Jinja2Templates = Jinja2Templates(directory=TEMPLATES_PATH)


@lru_cache()
def get_settings():
    return Settings()
