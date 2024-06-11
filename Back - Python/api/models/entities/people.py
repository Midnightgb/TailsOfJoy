from sqlalchemy import Column, String, BigInteger, TIMESTAMP
from api.models.base_class import Base

class People(Base):
    __tablename__ = 'people'

    person_id = Column(String(255), primary_key=True)
    identification = Column(BigInteger, nullable=False)
    first_name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
