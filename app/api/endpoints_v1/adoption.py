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
    # This line is added to debug the pet_to_adopt variable
    Logger.info(pet_to_adopt)
    # Check if pet exists
    if not pet_to_adopt:
        return {
            "status": "false",
            "message": f"Pet with ID {pet_id} not found"}
    # Check if pet is already adopted
    if pet_to_adopt.status == Status.adopted or pet_to_adopt.status == Status.inactive or pet_to_adopt.status == Status.deleted or pet_to_adopt.status == Status.pending:
        return {
            "status": "false",
            "message": f"Pet with ID {pet_id} already {pet_to_adopt.status.value}"}
    
    pet_to_adopt.status = Status.pending
    db.commit()
    Logger.success(f"Pet with ID {pet_id} is now pending for adoption")
    return {
        "status": "true",
        "message": f"Pet with ID {pet_id} is now pending for adoption"
    }
    
