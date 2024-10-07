from datetime import date
from pydantic import BaseModel

class Adoption_base(BaseModel):
    date: date

class Adoption_create(Adoption_base):
    temporary_owner_id: str
    adopter_id: str
    pet_id: str

class Adoption_read(BaseModel):
    adoption_id: str
