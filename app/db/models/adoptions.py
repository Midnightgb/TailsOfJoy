from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class Adoption(Base):
    __tablename__ = "adoptions"

    adoption_id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer, nullable=False)
    adopter_id = Column(Integer, nullable=False)
    adoption_date = Column(Date, nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    pet = relationship("Pet", back_populates="adoptions")
    adopter = relationship("User", back_populates="adoptions")