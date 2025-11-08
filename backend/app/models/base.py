"""Base model with common fields."""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime
from database import Base


class BaseModel(Base):
    """Abstract base model with common fields."""
    
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
