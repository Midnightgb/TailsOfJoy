from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from models import *




Base = declarative_base()

class Status(PyEnum):
    pending = "pending"
    active = "active"
    adopted = "adopted"
    inactive = "inactive"
    deleted = "deleted"


class Pet(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    registered_by = Column(Integer, ForeignKey(
        'users.user_id'), nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.active)
    species_id = Column(Integer(), ForeignKey(
        'species.species_id'), nullable=False)
    breed_id = Column(Integer(), ForeignKey('breeds.breed_id'), nullable=False)
    name = Column(String(20), nullable=False)
    size_id = Column(Integer(), ForeignKey('sizes.size_id'), nullable=False)
    weight = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    color = Column(String(30), nullable=False)
    description = Column(String(160))
    photo_url = Column(String(200), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Pet(pet_id={self.pet_id}, name={self.name}, status={self.status}, species_id={self.species_id}, breed_id={self.breed_id}, size_id={self.size_id}, weight={self.weight}, age={self.age}, color={self.color}, description={self.description}, photo_url={self.photo_url}, created_at={self.created_at}, updated_at={self.updated_at})>"
