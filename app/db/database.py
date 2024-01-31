from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from logger.Logger import Logger
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://root@localhost/tailsofjoy"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database():
    database = SessionLocal()
    try:
        Logger.success("Database connection successful")
        yield database
    finally:
        database.close()

def serverStatus(db):
    try:
        db.execute(text('SELECT 1'))
        Logger.success("Database server status: OK")
        return True
    except OperationalError:
        Logger.error("Database server status: ERROR")
        return False
    