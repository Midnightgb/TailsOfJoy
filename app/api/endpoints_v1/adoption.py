from fastapi import APIRouter
from logger.Logger import Logger
from db.database import *
from fastapi import Depends
from sqlalchemy.orm import Session
from models.pets import Pet, Status

router = APIRouter()


""" @router.get("/list")
def get_available_pets(
    db: Session = Depends(get_database),
):
    if not serverStatus(db):
        return {
            "status": "false",
            "message": "Database server status: Database server is down. Please try again later."
        }
    Logger.success("Pet list retrieved")
    available_pets = db.query(Pet).all()
    return {"pets": available_pets}
"""
@router.post("/adopt/{pet_id}")
def adopt_pet(pet_id: int, db: Session = Depends(get_database)):
    if not serverStatus(db):
        return {
            "status": "false",
            "message": "Database server is down. Please try again later."
        }
    Logger.success("Pet list retrieved")
    pet_to_adopt = db.query(Pet).filter(Pet.pet_id == pet_id).first()
    Logger.info(pet_to_adopt)
    if not pet_to_adopt:
        return {"message": f"Pet with ID {pet_id} not found"}
    #if pet_to_adopt.adopted:
        #return {"message": f"Pet with ID {pet_id} already adopted"}
    
    