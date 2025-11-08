"""User service for authentication and account management."""
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.utils.auth import get_password_hash, get_user_by_email


def create_user(db: Session, user: UserCreate) -> User:
    """Create a new user."""
    # Check if user already exists
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user with hashed password
    hashed_password = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name,
        is_active=user.is_active,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    """Update user profile."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    # Check if email is being updated and if it's already taken
    if user_update.email and user_update.email != db_user.email:
        existing_user = get_user_by_email(db, email=user_update.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        db_user.email = user_update.email
    
    # Update other fields
    if user_update.full_name is not None:
        db_user.full_name = user_update.full_name
    
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_profile(db: Session, user_id: int) -> Optional[User]:
    """Get user profile by ID."""
    return db.query(User).filter(User.id == user_id).first()


def deactivate_user(db: Session, user_id: int) -> Optional[User]:
    """Deactivate user account."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return db_user