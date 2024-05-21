from sqlalchemy import Column, String, TIMESTAMP
from api.models.base_class import Base

class UserPhoto(Base):
    __tablename__ = 'user_photos'

    id_user_photo = Column(String(255), primary_key=True)
    photo_url = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

