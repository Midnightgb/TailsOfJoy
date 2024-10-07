from pydantic import BaseModel, EmailStr

class User_base(BaseModel):
    email : EmailStr
    password : str

class User_create(User_base):
    person_id : str
    id_role : str
    id_user_photo : str
    status : str

class User_read(BaseModel):
    user_id : str