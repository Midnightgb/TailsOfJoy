from pydantic import BaseModel

class User_photo(BaseModel):
    photo_url : str

class User_photo_read(BaseModel):
    id_user_photo : str
