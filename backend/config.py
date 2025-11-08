import os
from typing import Optional


class Settings:
    """Application settings and configuration management."""
    
    # Database configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./app.db"
    )
    
    # API settings
    API_TITLE: str = "AI Agent Marketplace Backend"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "Backend API for AI Agent Marketplace"
    
    # CORS settings
    CORS_ORIGINS: list[str] = [
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:3000",
    ]
    
    # Application settings
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Security settings
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY",
        "your-secret-key-change-in-production"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    @property
    def sqlalchemy_database_url(self) -> str:
        """Return the SQLAlchemy database URL."""
        return self.DATABASE_URL


settings = Settings()
