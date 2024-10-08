from pydantic import BaseModel

class Pet_photo(BaseModel):
    photo_url : str

class Pet_photo_create(Pet_photo):
    pet_id : str

class Pet_photo_read(BaseModel):
    id_pet_photo : str