"""Authentication dependencies for FastAPI routes."""
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database import get_db
from app.utils.auth import verify_token, get_user_by_email
from app.models.user import User

# HTTP Bearer token scheme
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """Dependency to get current authenticated user."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Verify token and get email
    email = verify_token(credentials.credentials)
    if email is None:
        raise credentials_exception
    
    # Get user from database
    user = get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Dependency to get current active user."""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user


def get_current_superuser(
    current_user: User = Depends(get_current_user)
) -> User:
    """Dependency to get current superuser."""
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return current_user


def get_optional_current_user(
    db: Session = Depends(get_db)
) -> Optional[User]:
    """Optional dependency to get current user (doesn't raise exception if not authenticated)."""
    from fastapi import Request
    
    async def _get_optional_user(request: Request):
        authorization = request.headers.get("authorization")
        if not authorization:
            return None
        
        try:
            # Extract token from "Bearer <token>"
            scheme, _, token = authorization.partition(" ")
            if scheme.lower() != "bearer":
                return None
            
            email = verify_token(token)
            if email is None:
                return None
            
            user = get_user_by_email(db, email=email)
            if user is None or not user.is_active:
                return None
            
            return user
        except Exception:
            return None
    
    return _get_optional_user