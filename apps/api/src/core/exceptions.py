"""
Custom exception classes for the Trackball API.

Provides typed exceptions for different error scenarios
with proper HTTP status codes and error messages.
"""

from typing import Any, Dict, Optional


class TrackballException(Exception):
    """Base exception class for all Trackball-specific errors."""
    
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class HTTPException(TrackballException):
    """HTTP exception with status code."""
    
    def __init__(
        self,
        status_code: int,
        detail: str,
        headers: Optional[Dict[str, str]] = None
    ):
        self.status_code = status_code
        self.detail = detail
        self.headers = headers or {}
        super().__init__(detail)


class AuthenticationError(TrackballException):
    """Raised when authentication fails."""
    pass


class AuthorizationError(TrackballException):
    """Raised when user lacks required permissions."""
    pass


class ValidationError(TrackballException):
    """Raised when data validation fails."""
    pass


class NotFoundError(TrackballException):
    """Raised when a resource is not found."""
    pass


class ConflictError(TrackballException):
    """Raised when there's a conflict with existing data."""
    pass


class ProcessingError(TrackballException):
    """Raised when video processing fails."""
    pass


class StorageError(TrackballException):
    """Raised when file storage operations fail."""
    pass


class DatabaseError(TrackballException):
    """Raised when database operations fail."""
    pass


class ExternalServiceError(TrackballException):
    """Raised when external service calls fail."""
    pass