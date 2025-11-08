# Backend Setup Complete

This document provides an overview of the Python backend structure that has been set up for the AI Agent Marketplace.

## Overview

The backend is built with:
- **Framework**: FastAPI (modern, fast Python web framework)
- **ORM**: SQLAlchemy (SQL toolkit and Object-Relational Mapper)
- **Database**: SQLite (default), PostgreSQL, or MySQL supported
- **Server**: Uvicorn (ASGI server)

## Project Structure

```
backend/
├── app/                           # Main application package
│   ├── __init__.py
│   ├── models/                    # Database models
│   │   ├── __init__.py
│   │   ├── base.py               # BaseModel with common fields
│   │   └── agent.py              # Sample Agent model
│   ├── routes/                    # API endpoint routers
│   │   ├── __init__.py
│   │   └── health.py             # Health check endpoints
│   ├── services/                  # Business logic layer
│   │   ├── __init__.py
│   │   └── agent_service.py       # Agent CRUD service
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       └── helpers.py             # Helper functions
├── __init__.py
├── config.py                      # Configuration management
├── database.py                    # Database setup & session management
├── main.py                        # FastAPI application entry point
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variables template
└── README.md                      # Backend-specific documentation
```

## Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Set Up Environment

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env` with your configuration (optional for local development).

### 3. Run the Application

```bash
python main.py
```

Or with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:
- **API Server**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc

## API Endpoints

### Health Check
- `GET /api/health` - API health status
- `GET /api/health/db` - Database connection status

### Information
- `GET /` - API information and version

## Configuration

Configuration is managed through:

1. **Environment Variables** (`.env` file)
   - `DATABASE_URL`: Database connection string
   - `DEBUG`: Enable debug mode
   - `ENVIRONMENT`: Development/production environment
   - `SECRET_KEY`: Application secret key

2. **Settings Class** (`config.py`)
   - Centralized configuration management
   - Environment variable loading with defaults
   - CORS settings
   - API settings

## Database

### Supported Databases

- **SQLite** (default): `sqlite:///./app.db`
- **PostgreSQL**: `postgresql://user:password@localhost/dbname`
- **MySQL**: `mysql+pymysql://user:password@localhost/dbname`

### Database Initialization

Tables are automatically created when the application starts. The database schema is defined using SQLAlchemy models.

### Creating Migrations

For more complex database changes, use Alembic:

```bash
# Generate a migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head
```

## Adding Features

### Add a New Model

1. Create a new file in `app/models/`:

```python
from sqlalchemy import Column, String
from .base import BaseModel

class YourModel(BaseModel):
    __tablename__ = "your_table"
    name = Column(String(255), unique=True, index=True)
```

2. Import in `app/models/__init__.py`

### Add a New Route

1. Create a new file in `app/routes/`:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/endpoint")
async def your_endpoint():
    return {"message": "success"}
```

2. Import and include in `main.py`:

```python
from app.routes import your_router
app.include_router(your_router.router, prefix="/api", tags=["tag"])
```

### Add a New Service

1. Create a new file in `app/services/`:

```python
class YourService:
    @staticmethod
    def your_method(db):
        # Business logic
        pass
```

2. Use in route handlers with dependency injection

## Dependencies

Key dependencies in `requirements.txt`:

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **sqlalchemy**: ORM and database toolkit
- **pydantic**: Data validation
- **python-dotenv**: Environment variable management
- **alembic**: Database migrations
- **psycopg2-binary**: PostgreSQL adapter
- **pymysql**: MySQL adapter

## Development Notes

- The project uses Python 3.10+ type hints
- CORS is enabled for localhost on ports 8000 and 3000
- Database sessions are managed as dependencies
- All models inherit from `BaseModel` which provides `id`, `created_at`, `updated_at`

## Next Steps

1. Install dependencies: `pip install -r requirements.txt`
2. Start the development server: `python main.py`
3. Visit http://localhost:8000/docs to see interactive API documentation
4. Create additional models, routes, and services as needed

For more details, see `backend/README.md`
