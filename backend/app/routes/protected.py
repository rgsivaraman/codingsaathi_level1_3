"""Protected routes that require authentication."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from app.utils.dependencies import get_current_active_user, get_current_superuser
from app.models.user import User

router = APIRouter(prefix="/protected", tags=["protected"])


@router.get("/user-profile")
async def user_profile(current_user: User = Depends(get_current_active_user)):
    """Example protected route for regular users."""
    return {
        "message": "This is a protected route",
        "user": {
            "id": current_user.id,
            "email": current_user.email,
            "full_name": current_user.full_name,
            "is_active": current_user.is_active,
        }
    }


@router.get("/admin-only")
async def admin_only(current_user: User = Depends(get_current_superuser)):
    """Example protected route for superusers only."""
    return {
        "message": "This is an admin-only route",
        "admin": {
            "id": current_user.id,
            "email": current_user.email,
            "full_name": current_user.full_name,
        }
    }