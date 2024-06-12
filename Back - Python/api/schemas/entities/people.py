from pydantic import BaseModel

class People(BaseModel):
    identification : int
    first_name : str
    surname : str
    address : str
    phone : int

class people_read(BaseModel):
    person_id: str