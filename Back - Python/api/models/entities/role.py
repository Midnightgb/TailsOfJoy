from sqlalchemy import Column, String, TIMESTAMP
from api.models.base_class import Base

class Role(Base):
    __tablename__ = 'roles'

    id_role = Column(String(255), primary_key=True)
    name = Column(String(255), nullable=False)
    role_description = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')