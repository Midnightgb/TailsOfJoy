import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings
from .Logger import Logger

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = "Tails of Joy API"
    PROJECT_VERSION: str = "0.0.1"
    PROJECT_DESCRIPTION: str = "API for Tails of Joy an application for pet adoption"
    
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DATABASE_URL: str = f"postgresql+psycopg2://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}" % quote_plus(
        DB_PASS)

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOKEN_EXPIRE_MINUTES = 30
    ALGORITHM: str = os.getenv("ALGORITHM")

def get_settings() -> Settings:
    return Settings()
