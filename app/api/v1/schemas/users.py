from pydantic import BaseModel
from typing import List
from datetime import datetime, date
from enum import Enum


class RoleEnum(str, Enum):
    basic = "basic"
    admin = "admin"


class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    deleted = "deleted"
    pending = "pending"
    adopted = "adopted"
    rejected = "rejected"


class UserBase(BaseModel):
    name: str
    last_name: str
    birth_day: date
    phone_number: str
    address: str
    country: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    role: RoleEnum
    status: StatusEnum
    created_at: datetime
    updated_at: datetime
    pets: List["Pet"] = []
    adoptions: List["Adoption"] = []

    class Config:
        orm_mode = True


class PetBase(BaseModel):
    registered_by: int
    status: StatusEnum
    species_id: int
    breed_id: int
    name: str
    size_id: int
    weight: int
    age: int
    color: str
    description: str
    photo_url: str


class PetCreate(PetBase):
    pass


class Pet(PetBase):
    pet_id: int
    created_at: datetime
    updated_at: datetime
    temp_owner: User
    adoptions: List["Adoption"] = []
    species: "Species"
    breed: "Breed"
    size: "Size"

    class Config:
        orm_mode = True


class SpeciesBase(BaseModel):
    specie_name: str
    specie_description: str


class SpeciesCreate(SpeciesBase):
    pass


class Species(SpeciesBase):
    specie_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class SizeBase(BaseModel):
    size_name: str


class SizeCreate(SizeBase):
    pass


class Size(SizeBase):
    size_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class BreedBase(BaseModel):
    breed_name: str
    breed_description: str


class BreedCreate(BreedBase):
    pass


class Breed(BreedBase):
    breed_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class AdoptionBase(BaseModel):
    pet_id: int
    adopter_id: int
    status: StatusEnum
    adoption_date: date


class AdoptionCreate(AdoptionBase):
    pass


class Adoption(AdoptionBase):
    adoption_id: int
    created_at: datetime
    updated_at: datetime
    pet: Pet
    adopter: User

    class Config:
        orm_mode = True
