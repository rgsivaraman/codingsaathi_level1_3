# User Authentication System

This document describes the user authentication system implemented for the AI Agent Marketplace backend.

## Features

- **User Registration**: Sign up with email and password
- **User Login**: JWT-based authentication with access tokens
- **Password Security**: Bcrypt hashing for secure password storage
- **Profile Management**: Get and update user profiles
- **Protected Routes**: JWT token verification for protected endpoints
- **Role-based Access**: Support for regular users and superusers

## API Endpoints

### Authentication Routes (`/api/auth`)

#### POST `/api/auth/signup`
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "is_active": true
}
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false,
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

#### POST `/api/auth/login`
Authenticate user and receive JWT access token.

**Request Body (form-data):**
```
username: user@example.com
password: password123
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### GET `/api/auth/me`
Get current user profile (requires authentication).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false
}
```

#### PUT `/api/auth/me`
Update current user profile (requires authentication).

**Request Body:**
```json
{
  "full_name": "Jane Doe",
  "email": "newemail@example.com"
}
```

#### POST `/api/auth/logout`
Logout user (client-side token removal).

### Protected Routes (`/api/protected`)

#### GET `/api/protected/user-profile`
Example protected route for authenticated users.

#### GET `/api/protected/admin-only`
Example protected route for superusers only.

## Usage Examples

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/api/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "full_name": "Test User"
  }'
```

### 2. Login and get token
```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123"
```

### 3. Access protected route
```bash
curl -X GET "http://localhost:8000/api/auth/me" \
  -H "Authorization: Bearer <your_access_token>"
```

## Implementation Details

### Database Models

#### User Model (`app/models/user.py`)
```python
class User(BaseModel):
    email: str (unique, indexed)
    hashed_password: str
    full_name: str (optional)
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
```

### Authentication Flow

1. **Registration**: User provides email and password
2. **Password Hashing**: Password is hashed using bcrypt
3. **Database Storage**: User record created with hashed password
4. **Login**: User credentials verified against database
5. **JWT Generation**: Access token created with user email as subject
6. **Token Verification**: Protected routes verify JWT signature and extract user

### Security Features

- **Password Hashing**: Uses bcrypt with automatic salt generation
- **JWT Tokens**: HS256 algorithm with configurable secret key
- **Token Expiration**: Default 30 minutes (configurable)
- **CORS Support**: Configurable origins for frontend integration
- **Input Validation**: Pydantic schemas for request/response validation

### Dependencies

The authentication system uses the following key packages:
- `python-jose[cryptography]` - JWT token handling
- `passlib[bcrypt]` - Password hashing
- `python-multipart` - Form data support for login
- `email-validator` - Email validation in Pydantic schemas

## Configuration

Add these environment variables to your `.env` file:

```bash
# Security
SECRET_KEY=your-very-secure-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Integration with Existing Models

The User model is integrated with the existing Agent model through a foreign key relationship:
- Each Agent can have an `owner_id` pointing to a User
- Users can own multiple agents
- This enables user-specific agent management in the future

## Error Handling

The system includes comprehensive error handling:
- **400 Bad Request**: Invalid input, email already registered
- **401 Unauthorized**: Invalid credentials, missing/expired token
- **403 Forbidden**: Insufficient permissions for admin routes
- **404 Not Found**: User not found

## Next Steps

To extend the authentication system:
1. Add password reset functionality
2. Implement email verification
3. Add role-based permissions for agents
4. Create user activity logging
5. Add rate limiting for auth endpoints