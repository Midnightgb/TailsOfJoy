from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .Logger import Logger
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from core.config import get_settings


Logger.info("Database connection in progress...")
settings = get_settings()
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300,
    pool_size=5,
    max_overflow=0
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database() -> GeneratorExit:
    database = SessionLocal()
    try:
        Logger.success("Database connection successful")
        yield database
    finally:
        database.close()


def server_status(db):
    try:
        db.execute(text('SELECT 1'))
        Logger.success("Database server status: OK")
        return True
    except OperationalError:
        Logger.error("Database server status: ERROR")
        return False
