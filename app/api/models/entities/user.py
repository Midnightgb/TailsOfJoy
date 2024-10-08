from sqlalchemy import Column, String, TIMESTAMP, Enum, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base
from api.models.entities.people import People
from api.models.entities.role import Role
from api.models.photos.user_photo import User_photo

class User(Base):
    __tablename__ = 'users'

    user_id = Column(String(255), primary_key=True)
    person_id = Column(String(255), ForeignKey('people.person_id'), nullable=False)
    id_role = Column(String(255), ForeignKey('roles.id_role'), nullable=False)
    id_user_photo = Column(String(255), ForeignKey('user_photos.id_user_photo'), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(Enum('ACTIVE', 'INACTIVE'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    person = relationship('People', back_populates='users')
    role = relationship('Role', back_populates='users')
    user_photo = relationship('User_photo', back_populates='users')