from fastapi import APIRouter
from core.database import get_database, server_status
from fastapi import Depends
from sqlalchemy.orm import Session
from core.utils.utils import handle_server_down, handle_server_up

router = APIRouter(
    prefix="/api/v1",
    tags=["Test Connection"],
    responses={404: {"description": "Not found"}},
)


@router.get("/health_check")
async def health_check(db: Session = Depends(get_database)):
    if server_status(db):
        return handle_server_up()
    return handle_server_down()
