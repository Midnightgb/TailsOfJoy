from pydantic import BaseModel

class Specie(BaseModel):
    name : str
    species_description : str 

class Specie_create(Specie):
    breed_id : str

class Specie_read(BaseModel):
    species_id : str
