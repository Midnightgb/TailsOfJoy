from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
# Core dependencies
from core.database import get_database, server_status
from core.Logger import Logger
from core.utils.utils import handle_server_down
from core.security import create_access_token, verify_token
# API dependencies
#from api.v1.schemas.user import UserRead, UserCreate, Token
from api.crud.users import get_users, authenticate_user
from api.schemas.entities.user import User_read

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

@router.post("/login", response_model=dict)#change to Token when the schema is created
async def authenticate_and_provide_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_database)):
    if not server_status(db):
        return handle_server_down()
    # Authenticate the user and return the access token
    user = authenticate_user(form_data.username, form_data.password, db)
    if "status" in user and not user["status"]:
        Logger.error(user.get("message"))
        raise HTTPException(
            status_code=401, detail=f"{user.get("message")}", headers={"WWW-Authenticate": "Bearer"})
    user = user.get("user")
    access_token_expires = create_access_token(
        data={"sub": user.user_id, "role": user.id_role})
    return {"access_token": access_token_expires, "token_type": "bearer"}

@router.get("/", response_model=list[User_read])
async def get_all_users(db: Session = Depends(get_database)):
    if not server_status(db):
        return handle_server_down()
    return get_users(db)