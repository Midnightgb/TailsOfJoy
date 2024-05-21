from sqlalchemy import Column, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from api.models.base_class import Base

class Interaction(Base):
    __tablename__ = 'interactions'

    id_interaction = Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    post_id = Column(String(255), ForeignKey('posts.post_id'), nullable=False)
    date = Column(Date, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')