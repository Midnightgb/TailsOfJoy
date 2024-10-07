from sqlalchemy import Column, Integer, Date, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from core.database import Base
from enum import Enum as PyEnum


class Role(PyEnum):
    basic = "basic"
    admin = "admin"


class Status(PyEnum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"
    pending = "pending"
    adopted = "adopted"
    rejected = "rejected"


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

    pets = relationship("Pet", back_populates="temp_owner")
    adoptions = relationship("Adoption", back_populates="adopter")

class Pet(Base):
    __tablename__ = "pets"

    pet_id = Column(Integer, primary_key=True, index=True)
    registered_by = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.active)
    species_id = Column(Integer(), ForeignKey(
        'species.specie_id'), nullable=False)
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

    temp_owner = relationship("User", back_populates="pets")
    adoptions = relationship("Adoption", back_populates="pet")
    species = relationship("Species")
    breed = relationship("Breed")
    size = relationship("Size")

    def __repr__(self):
        return f"<Pet(pet_id={self.pet_id}, name={self.name}, status={self.status}, species_id={self.species_id}, breed_id={self.breed_id}, size_id={self.size_id}, weight={self.weight}, age={self.age}, color={self.color}, description={self.description}, photo_url={self.photo_url}, created_at={self.created_at}, updated_at={self.updated_at})>"


class Species(Base):
    __tablename__ = "species"

    species_id = Column(Integer, primary_key=True, index=True)
    species_name = Column(String(20), nullable=False)
    species_description = Column(String(60), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Species(species_id={self.species_id}, species_name={self.species_name}, species_description={self.species_description}, created_at={self.created_at}, updated_at={self.updated_at})>"


class Size(Base):
    __tablename__ = "sizes"

    size_id = Column(Integer, primary_key=True, index=True)
    size_name = Column(String(20), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())


class Breed(Base):
    __tablename__ = "breeds"

    breed_id = Column(Integer, primary_key=True, index=True)
    breed_name = Column(String(50), nullable=False)
    breed_description = Column(String(60), nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())


class Adoption(Base):
    __tablename__ = "adoptions"

    adoption_id = Column(Integer, primary_key=True, index=True)
    pet_id = Column(Integer(), ForeignKey('pets.pet_id'), nullable=False)
    adopter_id = Column(Integer(), ForeignKey('users.user_id'), nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.pending)
    adoption_date = Column(Date, nullable=False)
    created_at = Column(Date, server_default=func.now())
    updated_at = Column(Date, server_default=func.now(), onupdate=func.now())

    pet = relationship("Pet", back_populates="adoptions")
    adopter = relationship("User", back_populates="adoptions")


