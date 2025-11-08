"""Agent model for the marketplace."""
from sqlalchemy import Column, String, Text, Float, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class Agent(BaseModel):
    """AI Agent model."""
    
    __tablename__ = "agents"
    
    name = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text)
    version = Column(String(50), default="1.0.0")
    author = Column(String(255))
    is_active = Column(Boolean, default=True, index=True)
    rating = Column(Float, default=0.0)
    download_count = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relationships
    owner = relationship("User", back_populates="agents")
    
    def __repr__(self) -> str:
        return f"<Agent(id={self.id}, name={self.name}, version={self.version})>"
