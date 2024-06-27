from pydantic import BaseModel

class Pet(BaseModel):
    status: str

class Pet_create(Pet):
    specie_id : str
    traits_id : str

class Pet_read(BaseModel):
    pet_id : str