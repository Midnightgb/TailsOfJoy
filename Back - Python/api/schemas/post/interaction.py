from pydantic import BaseModel
from datetime import date

class Interaction(BaseModel):
    date : date

class Interaction_create(Interaction):
    user_id : str
    post_id : str

class Interaction_read(Interaction):
    id_interaction : str