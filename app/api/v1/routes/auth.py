from fastapi import APIRouter, Request, Form, Depends, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.core.database import get_database, serverStatus

router = APIRouter()


@router.post("/login", tags=["auth"])
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_database)):
    if serverStatus(db):
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
