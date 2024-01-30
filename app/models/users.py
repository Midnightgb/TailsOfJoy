from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from enum import Enum as PyEnum

Base = declarative_base()

class Role(PyEnum):
    basic = "basic"
    admin = "admin"

class Status(PyEnum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(40), nullable=False)
    birth_day = Column(Date, nullable=False)
    phone_number = Column(String(30), nullable=False)
    address = Column(String(100), nullable=False)
    country = Column(String(60), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(Role), nullable=False, default=Role.basic)
    status = Column(Enum(Status), nullable=False, default=Status.active)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())