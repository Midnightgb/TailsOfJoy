import sys
from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.models.entities.user import User
#from api.schemas.entities.user import UserRead, UserCreate

from core.database import server_status
from core.Logger import Logger
from core.utils.utils import handle_server_down, generate_user_id
from core.security import get_hashed_password, verify_password

def get_users(db: Session):
    try:
        if not server_status(db):
            return handle_server_down()
        users = db.query(User).all()
        return users
    except Exception as e:
        Logger.error(f"Error getting users: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error al obtener los usuarios: {str(e)}")

def get_user_by_id(
        user_id: str,
        db: Session):
    try:
        if not server_status(db):
            return handle_server_down()
        user = db.query(User).filter(User.user_id == user_id).first()
        return user
    except Exception as e:
        Logger.error(f"Error getting user by id: {str(e)}", file=sys.stderr)
        raise HTTPException(
            status_code=500, detail=f"Error al obtener el usuario por id: {str(e)}")
        
def authenticate_user(
        email: str,
        password: str,
        db: Session):
    try:
        if not server_status(db):
            return handle_server_down()
        user = db.query(User).filter(User.email == email).first()
        if user:
            if verify_password(password, user.password):
                return {"status": True, "user": user}
            return {"status": False, "message": "Contraseña incorrecta."}
        return {"status": False, "message": "No se encontró el usuario con el email proporcionado."}
    except Exception as e:
        Logger.error(f"Error authenticating user: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error al autenticar el usuario: {str(e)}")
