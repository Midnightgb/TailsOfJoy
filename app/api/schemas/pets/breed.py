from pydantic import BaseModel

class Breed(BaseModel):
    name: str
    breed_description: str

class Breed_read(BaseModel):
    breed_id: str