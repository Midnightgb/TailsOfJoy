from pydantic import BaseModel

class Specie(BaseModel):
    name : str
    specie_description : str 

class Specie_create(Specie):
    breed_id : str

class Specie_read(BaseModel):
    specie_id : str
