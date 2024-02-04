from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from core.Logger import Logger
from core.database import get_database, server_status
from api.v1.models.models import Pet, Status, User, Adoption, Species, Breed, Size
from api.utils.utils import handle_server_down
from typing import Optional
from fastapi.params import Query
from sqlalchemy.orm import Query as DBQuery

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
    responses={404: {"description": "Not found"}},
)


@router.get("/available", status_code=status.HTTP_200_OK)
def get_available_pets(
    offset: Optional[int] = Query(default=0, description="Number of results to skip"),
    limit: Optional[int] = Query(default=20, description="Number of results to return"),
    size: Optional[str] = Query(None, description="Size of pet"),
    specie: Optional[str] = Query(None, description="Specie of pet"),
    breed: Optional[str] = Query(None, description="Breed of pet"),
    db: Session = Depends(get_database),
):
    if not server_status(db):
        return handle_server_down()
    
    if offset < 0 or limit < 0:
        offset = 0
        limit = 20
    
    query: DBQuery = db.query(Pet).filter(Pet.status == Status.active)

    if size is not None:
        query = query.filter(Pet.size_id == size)

    if specie is not None:
        query = query.filter(Pet.species_id == specie)

    if breed is not None:
        query = query.filter(Pet.breed_id == breed)
    
    available_pets = query.offset(offset).limit(limit).all()

    if not available_pets:
        return {"message": "No hay mascotas disponibles en este momento", "status": "false"}

    for pet in available_pets:
        species_info = db.query(
            Species.specie_id,
            Species.specie_name,
            Species.specie_description
        ).filter(Species.specie_id == pet.species_id).first()

        species_data = {
            "specie_id": species_info.specie_id,
            "specie_name": species_info.specie_name,
            "specie_description": species_info.specie_description,
        }


        breed_info = db.query(
            Breed.breed_id,
            Breed.breed_name,
            Breed.breed_description
        ).filter(Breed.breed_id == pet.breed_id).first()

        breed_data = {
            "breed_id": breed_info.breed_id,
            "breed_name": breed_info.breed_name,
            "breed_description": breed_info.breed_description,
        }

        size_info = db.query(
            Size.size_id,
            Size.size_name
        ).filter(Size.size_id == pet.size_id).first()

        size_data = {
            "size_id": size_info.size_id,
            "size_name": size_info.size_name,
        }

        pet.species_id = species_data
        pet.size_id = size_data
        pet.breed_id = breed_data

    return {"pets": available_pets}


@router.get("/species", status_code=status.HTTP_200_OK)
def get_species(
    db: Session = Depends(get_database),
):
    if not server_status(db):
        return handle_server_down()
    species = db.query(Species).all()
    return {"species": species}


@router.get("/breeds", status_code=status.HTTP_200_OK)
def get_breeds(
    db: Session = Depends(get_database),
):
    if not server_status(db):
        return handle_server_down()
    breeds = db.query(Breed).all()
    return {"breeds": breeds}


@router.post("/adopt/{pet_id}/{user_id}")
def adopt_pet(pet_id: int, user_id: int, db: Session = Depends(get_database)):
    Logger.warning("Checking database server status")
    if not server_status(db):
        return handle_server_down()
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
        # Check if user has phone number or email
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
