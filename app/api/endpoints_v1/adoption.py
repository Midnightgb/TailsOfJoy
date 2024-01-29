from fastapi import APIRouter

router = APIRouter()


@router.get("/list")
def get_available_pets():
    available_pets = [
        {"id": 1, "name": "Milo", "species": "Dog"},
        {"id": 2, "name": "Whiskers", "species": "Cat"},
    ]
    return {"pets": available_pets}


@router.post("/adopt/{pet_id}")
def adopt_pet(pet_id: int):
    return {"message": f"Pet with ID {pet_id} adopted successfully"}
