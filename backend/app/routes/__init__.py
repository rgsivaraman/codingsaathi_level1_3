"""API routes package."""
from app.routes.auth import router as auth_router
from app.routes.health import router as health_router
from app.routes.protected import router as protected_router

__all__ = ["auth_router", "health_router", "protected_router"]
