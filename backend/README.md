# AI Agent Marketplace Backend

FastAPI-based backend for the AI Agent Marketplace.

## Project Structure

```
backend/
├── app/
│   ├── models/          # SQLAlchemy ORM models
│   ├── routes/          # API endpoints/routers
│   ├── services/        # Business logic services
│   └── utils/           # Utility functions
├── config.py            # Configuration management
├── database.py          # Database setup and session management
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
└── .env.example         # Environment variables template
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment

Copy `.env.example` to `.env` and update the values:

```bash
cp .env.example .env
```

### 3. Run the Application

```bash
python main.py
```

Or with uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, view the interactive API documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database

The backend uses SQLAlchemy ORM with support for:
- SQLite (default for development)
- PostgreSQL
- MySQL

### Initialize Database

The database tables are automatically created when the application starts.

## API Endpoints

### Authentication

See [AUTHENTICATION.md](./AUTHENTICATION.md) for detailed authentication documentation.

- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - User login (JWT token)
- `GET /api/auth/me` - Get current user profile
- `PUT /api/auth/me` - Update user profile
- `POST /api/auth/logout` - User logout

### Protected Routes

- `GET /api/protected/user-profile` - Example protected route
- `GET /api/protected/admin-only` - Admin-only route

### Health Check

- `GET /api/health` - Health check endpoint
- `GET /api/health/db` - Database health check

### Root

- `GET /` - API information

## Development

### Create New Models

1. Add model class in `app/models/`
2. Inherit from `BaseModel` for standard fields (id, created_at, updated_at)
3. Models are automatically created in the database on app startup

### Create New Endpoints

1. Create router in `app/routes/`
2. Import and include in `main.py`

### Create New Services

1. Add service class in `app/services/`
2. Implement business logic methods
3. Use in route handlers

## Requirements

- Python 3.10+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic
