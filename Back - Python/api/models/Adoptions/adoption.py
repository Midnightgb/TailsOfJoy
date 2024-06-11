from sqlalchemy import Column, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base
from api.models.entities.user import User
from api.models.pets.pet import Pet

class Adoption(Base):
    __tablename__ = 'adoptions'

    adoption_id = Column(String(255), primary_key=True)
    temporary_owner_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    adopter_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    pet_id = Column(String(255), ForeignKey('pets.pet_id'), nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    temporary_owner = relationship('User', back_populates='adoptions')
    adopter = relationship('User', back_populates='adoptions')
    pet = relationship('Pet', back_populates='adoptions')