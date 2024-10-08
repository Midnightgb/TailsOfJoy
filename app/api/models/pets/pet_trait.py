from sqlalchemy import Column, String, TIMESTAMP, Float, Integer
from api.models.base_class import Base

class Pet_trait(Base):
    __tablename__ = 'pet_traits'

    traits_id = Column(String(255), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    color = Column(String(255))
    height = Column(Float)
    weight = Column(Float)
    age = Column(Integer)
    disabilities = Column(String(255))
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')