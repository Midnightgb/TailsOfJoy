from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from schemas import UserCreate, User
from crud.usuarios import create_user
from db.database import get_database

app = FastAPI()

@app.post("/users/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_route(user_create: UserCreate, db: Session = Depends(get_database)):
    # Validar y crear el usuario en la base de datos
    new_user = create_user(db, user_create)
    return new_user
