from fastapi import APIRouter
from core.Logger import Logger
from core.database import get_database, server_status
from fastapi import Depends
from sqlalchemy.orm import Session
from api.v1.models.models import Pet, Status, User, Adoption

router = APIRouter()



@router.get("/list")
def get_available_pets(
    db: Session = Depends(get_database),
):
    if not server_status(db):
        return {
            "status": "false",
            "message": "Database server status: Database server is down. Please try again later."
        }
    Logger.success("Pet list retrieved")
    available_pets = db.query(Pet).all()
    return {"pets": available_pets}


@router.post("/adopt/{pet_id}/{user_id}")
def adopt_pet(pet_id: int, user_id: int, db: Session = Depends(get_database)):
    Logger.warning("Checking database server status")
    if not server_status(db):
        return {
            "status": "false",
            "message": "La base de datos no está disponible. Por favor intente más tarde"
        }
    try:
        Logger.info(f"Checking if pet with ID {pet_id} exists")
        pet_to_adopt = db.query(Pet).filter(Pet.pet_id == pet_id).first()
        # Check if pet exists
        if not pet_to_adopt:
            Logger.error(f"Pet with ID {pet_id} not found")
            return {
                "status": "false",
                "message": f"Mascota con ID {pet_id} no encontrada"}
        # This line is added to debug the pet_to_adopt variable
        Logger.debug(pet_to_adopt)
        # Check if pet is already adopted
        if pet_to_adopt.status != Status.active:
            return {
                "status": "false",
                "message": f"Mascota con ID {pet_id} actualmente se encuentra en estado {pet_to_adopt.status.value}"}
        Logger.info(f"Checking if user with ID {user_id} exists")
        user = db.query(User).filter(User.user_id == user_id).first()
        # Check if user exists
        if not user:
            Logger.error(f"User with ID {user_id} not found")
            return {
                "status": "false",
                "message": f"Usuario con ID {user_id} no encontrado"}
        # This line is added to debug the user variable
        Logger.debug(user)
        # Check if user is not active
        if user.status != Status.active:
            return {
                "status": "false",
                "message": f"Usuario con ID {user_id} actualmente se encuentra en estado {user.status.value}"}
        #Check if user has phone number or email
        if not user.phone_number:
            return {
                "status": "false",
                "message": f"Usuario con ID {user_id} no tiene número de teléfono vinculado a su cuenta"}
        if not user.email:
            return {
                "status": "false",
                "message": f"Usuario con ID {user_id} no tiene correo electrónico vinculado a su cuenta"}
        new_adoption = Adoption(
            pet_id=pet_id, adopter_id=user_id, status=Status.pending)
        
        pet_to_adopt.status = Status.pending
        db.add(new_adoption)
        db.commit()
        db.refresh(pet_to_adopt)
        db.refresh(new_adoption)
        Logger.success(f"Pet with ID {pet_id} is now pending for adoption")
        return {
            "status": "true",
            "message": f"Mascota con ID {pet_id} ahora está pendiente para adopción por usuario {user.name} {user.last_name}"
        }
    except Exception as e:
        Logger.error(f"Error adopting pet with ID {pet_id}: {e}")
        return {
            "status": "false",
            "message": f"Error adoptando mascota con ID {pet_id}: {e}"
        }
    finally:
        Logger.warning("Closing database connection")
        db.close()
