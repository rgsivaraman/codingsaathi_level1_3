from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from config import settings

# Create database engine
engine = create_engine(
    settings.sqlalchemy_database_url,
    connect_args={"check_same_thread": False} if "sqlite" in settings.sqlalchemy_database_url else {},
    poolclass=StaticPool if "sqlite" in settings.sqlalchemy_database_url else None,
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()


def get_db():
    """Dependency for getting database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
