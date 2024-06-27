from pydantic import BaseModel

class Role(BaseModel):
    name: str
    role_description: str

class Role_read(BaseModel):
    id_role: str