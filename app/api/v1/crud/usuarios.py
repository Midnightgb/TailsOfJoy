from sqlalchemy.orm import Session
from models.models import User
from schemas.users import UserCreate

def create_user(db: Session, user_create: UserCreate) -> User:
    # Crea una instancia del modelo User con los datos proporcionados
    new_user = User(
        name=user_create.name,
        last_name=user_create.last_name,
        birth_day=user_create.birth_day,
        phone_number=user_create.phone_number,
        address=user_create.address,
        country=user_create.country,
        email=user_create.email,
        password=user_create.password,
        role=user_create.role,
        status=user_create.status
    )

    # Agrega el nuevo usuario a la sesión de la base de datos y realiza la confirmación
    db.add(new_user)
    db.commit()

    # Refresca el objeto User para obtener los valores actualizados de la base de datos
    db.refresh(new_user)

    return new_user
