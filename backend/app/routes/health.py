"""Health check and status endpoints."""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy", "message": "API is running"}


@router.get("/health/db")
async def database_health(db: Session = Depends(get_db)) -> dict:
    """Database health check endpoint."""
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "message": "Database connection is working"}
    except Exception as e:
        return {"status": "unhealthy", "message": f"Database error: {str(e)}"}
