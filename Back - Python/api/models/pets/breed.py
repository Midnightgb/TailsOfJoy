from sqlalchemy import Column, String, TIMESTAMP
from api.models.base_class import Base

class Breed(Base):
    __tablename__ = 'breeds'

    breed_id = Column(String(255), primary_key=True)
    name = Column(String(255))
    breed_description = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')