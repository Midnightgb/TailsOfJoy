from pydantic import BaseModel

class Pet_trait(BaseModel):
    name: str
    description: str

class Pet_trait_create(Pet_trait):
    color : str
    height : float
    weight : float
    age : int
    disabilities : str
    