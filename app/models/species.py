from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Species(Base):
    __tablename__ = "species"

    specie_id = Column(Integer, primary_key=True, index=True)
    specie_name = Column(String(20), nullable=False)
    specie_description = Column(String(60), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())