from fastapi import APIRouter

router = APIRouter()

@router.get("/list")
def get_available_pets():
    # Lógica para obtener la lista de mascotas disponibles
    # Puedes reemplazar esto con la lógica real de tu aplicación
    available_pets = [
        {"id": 1, "name": "Milo", "species": "Dog"},
        {"id": 2, "name": "Whiskers", "species": "Cat"},
        # ... más mascotas
    ]
    return {"pets": available_pets}

@router.post("/adopt/{pet_id}")
def adopt_pet(pet_id: int):
    # Lógica para manejar la adopción de una mascota por su ID
    # Puedes reemplazar esto con la lógica real de tu aplicación
    return {"message": f"Pet with ID {pet_id} adopted successfully"}
