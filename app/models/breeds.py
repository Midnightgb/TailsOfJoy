from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from models import *

Base = declarative_base()

class Breed(Base):
    __tablename__ = "breeds"

    breed_id = Column(Integer, primary_key=True, index=True)
    breed_name = Column(String(50), nullable=False)
    breed_description = Column(String(60), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())