from sqlalchemy import Column, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base

class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    pet_id = Column(String(255), ForeignKey('pets.pet_id'), nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
