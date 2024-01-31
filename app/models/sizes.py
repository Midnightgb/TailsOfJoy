from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from models import *


Base = declarative_base()

class Size(Base):
    __tablename__ = "sizes"

    size_id = Column(Integer, primary_key=True, index=True)
    size_name = Column(String(20), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())