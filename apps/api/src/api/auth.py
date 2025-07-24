"""
Authentication endpoints for user login, registration, and token management.

Provides JWT-based authentication with refresh tokens and password security.
"""

import logging
from typing import Dict, Any

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, Field

from ..config.settings import get_settings
from ..core.exceptions import AuthenticationError, ValidationError

logger = logging.getLogger(__name__)
router = APIRouter()

settings = get_settings()


class UserLogin(BaseModel):
    """User login request model."""
    email: EmailStr
    password: str = Field(..., min_length=1, max_length=100)


class UserRegister(BaseModel):
    """User registration request model."""
    email: EmailStr
    password: str = Field(..., min_length=settings.password_min_length, max_length=100)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    confirm_password: str = Field(..., min_length=settings.password_min_length, max_length=100)


class TokenResponse(BaseModel):
    """Token response model."""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int
    user: Dict[str, Any]


class UserProfile(BaseModel):
    """User profile response model."""
    id: str
    email: str
    first_name: str
    last_name: str
    role: str
    created_at: str
    is_active: bool


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin) -> TokenResponse:
    """
    Authenticate user and return access and refresh tokens.
    
    Args:
        user_data: User login credentials
        
    Returns:
        TokenResponse with access token, refresh token, and user info
        
    Raises:
        HTTPException: When authentication fails
    """
    try:
        # Mock authentication for development
        # TODO: Implement actual user authentication with database
        
        if user_data.email == "demo@trackball.com" and user_data.password == "password123":
            # Mock successful authentication
            mock_user = {
                "id": "user-123",
                "email": user_data.email,
                "first_name": "Demo",
                "last_name": "User",
                "role": "analyst",
                "created_at": "2024-01-01T00:00:00Z",
                "is_active": True,
            }
            
            # Mock JWT tokens
            access_token = "mock-access-token-12345"
            refresh_token = "mock-refresh-token-67890"
            
            logger.info(f"User logged in successfully: {user_data.email}")
            
            return TokenResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=settings.jwt_access_token_expire_minutes * 60,
                user=mock_user,
            )
        else:
            raise AuthenticationError("Invalid email or password")
            
    except AuthenticationError as e:
        logger.warning(f"Login failed for {user_data.email}: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        logger.error(f"Login error for {user_data.email}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication service error"
        )


@router.post("/register", response_model=TokenResponse)
async def register(user_data: UserRegister) -> TokenResponse:
    """
    Register a new user account.
    
    Args:
        user_data: User registration data
        
    Returns:
        TokenResponse with access token, refresh token, and user info
        
    Raises:
        HTTPException: When registration fails
    """
    try:
        # Validate password confirmation
        if user_data.password != user_data.confirm_password:
            raise ValidationError("Passwords do not match")
        
        # Mock user registration
        # TODO: Implement actual user registration with database
        
        # Check if user already exists (mock check)
        if user_data.email == "existing@trackball.com":
            raise ValidationError("User with this email already exists")
        
        # Mock successful registration
        mock_user = {
            "id": "user-new-456",
            "email": user_data.email,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name,
            "role": "analyst",
            "created_at": "2024-01-23T00:00:00Z",
            "is_active": True,
        }
        
        # Mock JWT tokens
        access_token = "mock-access-token-new-78901"
        refresh_token = "mock-refresh-token-new-23456"
        
        logger.info(f"User registered successfully: {user_data.email}")
        
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=settings.jwt_access_token_expire_minutes * 60,
            user=mock_user,
        )
        
    except ValidationError as e:
        logger.warning(f"Registration validation failed for {user_data.email}: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Registration error for {user_data.email}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration service error"
        )


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str) -> TokenResponse:
    """
    Refresh access token using refresh token.
    
    Args:
        refresh_token: Valid refresh token
        
    Returns:
        TokenResponse with new access token
        
    Raises:
        HTTPException: When refresh fails
    """
    try:
        # Mock token refresh
        # TODO: Implement actual JWT token refresh
        
        if refresh_token.startswith("mock-refresh-token"):
            # Mock successful token refresh
            mock_user = {
                "id": "user-123",
                "email": "demo@trackball.com",
                "first_name": "Demo",
                "last_name": "User",
                "role": "analyst",
                "created_at": "2024-01-01T00:00:00Z",
                "is_active": True,
            }
            
            new_access_token = "mock-access-token-refreshed-54321"
            new_refresh_token = "mock-refresh-token-refreshed-09876"
            
            return TokenResponse(
                access_token=new_access_token,
                refresh_token=new_refresh_token,
                expires_in=settings.jwt_access_token_expire_minutes * 60,
                user=mock_user,
            )
        else:
            raise AuthenticationError("Invalid refresh token")
            
    except AuthenticationError as e:
        logger.warning(f"Token refresh failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        logger.error(f"Token refresh error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Token refresh service error"
        )


@router.get("/me", response_model=UserProfile)
async def get_current_user() -> UserProfile:
    """
    Get current authenticated user profile.
    
    Returns:
        UserProfile with current user information
        
    Raises:
        HTTPException: When user is not authenticated
    """
    try:
        # Mock current user retrieval
        # TODO: Implement actual user authentication check and profile retrieval
        
        # Mock authenticated user
        return UserProfile(
            id="user-123",
            email="demo@trackball.com",
            first_name="Demo",
            last_name="User",
            role="analyst",
            created_at="2024-01-01T00:00:00Z",
            is_active=True,
        )
        
    except Exception as e:
        logger.error(f"Get current user error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User profile service error"
        )


@router.post("/logout")
async def logout() -> Dict[str, str]:
    """
    Log out current user by invalidating tokens.
    
    Returns:
        Success message
    """
    try:
        # Mock logout
        # TODO: Implement actual token invalidation
        
        logger.info("User logged out successfully")
        
        return {"message": "Logged out successfully"}
        
    except Exception as e:
        logger.error(f"Logout error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Logout service error"
        )