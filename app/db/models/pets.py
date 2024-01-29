from sqlalchemy import Column, Integer, String, Enum, Date
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum

Base = declarative_base()

class Status(PyEnum):
    active = "active"
    adopted = "adopted"
    inactive = "inactive"
    deleted = "deleted"

class Pet(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    registered_by = Column(Integer, nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.active)
    species_id = Column(Integer, nullable=False)
    breed_id = Column(Integer, nullable=False)
    name = Column(String(20), nullable=False)
    size_id = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    color = Column(String(30), nullable=False)
    description = Column(String(160))
    photo_url = Column(String(200), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    owner = relationship("User", back_populates="pets")
    adoptions = relationship("Adoption", back_populates="pet")
    species = relationship("Species", back_populates="pets")
    breed = relationship("Breed", back_populates="pets")
    size = relationship("Size", back_populates="pets")