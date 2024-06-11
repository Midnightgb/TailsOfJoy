from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base

class Pet_photo(Base):
    __tablename__ = 'pet_photos'

    id_pet_photo = Column(String(255), primary_key=True)
    pet_id = Column(String(255), ForeignKey('pets.pet_id'), nullable=False)
    photo_url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

