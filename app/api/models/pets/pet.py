from sqlalchemy import Column, String, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base
from api.models.pets.pet_trait import Pet_trait
from api.models.pets.specie import Specie

class Pet(Base):
    __tablename__ = 'pets'

    pet_id = Column(String(255), primary_key=True)
    species_id = Column(String(255), ForeignKey('species.species_id'), nullable=False)
    traits_id = Column(String(255), ForeignKey('pet_traits.traits_id'), nullable=False)
    status = Column(Enum('ACTIVE', 'INACTIVE', 'DELETED', 'ADOPTED'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    species = relationship('Specie', back_populates='pets')
    pet_trait = relationship('Pet_trait', back_populates='pets')