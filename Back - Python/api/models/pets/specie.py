from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base
from api.models.pets.breed import Breed

class Specie(Base):
    __tablename__ = 'species'

    specie_id = Column(String(255), primary_key=True)
    breed_id = Column(String(255), ForeignKey('breeds.breed_id'), nullable=False)
    name = Column(String(255))
    specie_description = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    
    breed = relationship('Breed', back_populates='species')