"""
Rate limiting middleware for API protection.

Implements token bucket rate limiting to prevent abuse
and ensure fair usage of API resources.
"""

import logging
import time
from typing import Dict, Callable

from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

from ..config.settings import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting API requests."""
    
    def __init__(self, app, requests_per_minute: int = None, requests_per_hour: int = None):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute or settings.rate_limit_requests_per_minute
        self.requests_per_hour = requests_per_hour or settings.rate_limit_requests_per_hour
        
        # In-memory storage for rate limiting (use Redis in production)
        self.request_counts: Dict[str, Dict[str, any]] = {}
    
    def get_client_identifier(self, request: Request) -> str:
        """Get unique identifier for client (IP address)."""
        # Try to get real IP from headers (when behind proxy)
        forwarded_for = request.headers.get("X-Forwarded-For")
        if forwarded_for:
            return forwarded_for.split(",")[0].strip()
        
        real_ip = request.headers.get("X-Real-IP")
        if real_ip:
            return real_ip
        
        # Fallback to direct client IP
        return request.client.host if request.client else "unknown"
    
    def is_rate_limited(self, client_id: str) -> tuple[bool, Dict[str, any]]:
        """Check if client is rate limited and return current status."""
        current_time = time.time()
        
        # Initialize client data if not exists
        if client_id not in self.request_counts:
            self.request_counts[client_id] = {
                "minute_requests": [],
                "hour_requests": [],
                "last_request": current_time,
            }
        
        client_data = self.request_counts[client_id]
        
        # Clean old requests (older than 1 minute and 1 hour)
        minute_cutoff = current_time - 60
        hour_cutoff = current_time - 3600
        
        client_data["minute_requests"] = [
            req_time for req_time in client_data["minute_requests"]
            if req_time > minute_cutoff
        ]
        
        client_data["hour_requests"] = [
            req_time for req_time in client_data["hour_requests"]
            if req_time > hour_cutoff
        ]
        
        # Check rate limits
        minute_count = len(client_data["minute_requests"])
        hour_count = len(client_data["hour_requests"])
        
        # Return rate limit status
        rate_limit_info = {
            "requests_per_minute": minute_count,
            "requests_per_hour": hour_count,
            "limit_per_minute": self.requests_per_minute,
            "limit_per_hour": self.requests_per_hour,
            "reset_minute": int(minute_cutoff + 60),
            "reset_hour": int(hour_cutoff + 3600),
        }
        
        # Check if rate limited
        is_limited = (
            minute_count >= self.requests_per_minute or
            hour_count >= self.requests_per_hour
        )
        
        return is_limited, rate_limit_info
    
    def record_request(self, client_id: str) -> None:
        """Record a request for the client."""
        current_time = time.time()
        
        if client_id in self.request_counts:
            client_data = self.request_counts[client_id]
            client_data["minute_requests"].append(current_time)
            client_data["hour_requests"].append(current_time)
            client_data["last_request"] = current_time
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Process request with rate limiting."""
        # Skip rate limiting for health checks and development endpoints
        if request.url.path.startswith(("/health", "/dev")) and settings.debug:
            return await call_next(request)
        
        # Get client identifier
        client_id = self.get_client_identifier(request)
        
        # Check rate limit
        is_limited, rate_info = self.is_rate_limited(client_id)
        
        if is_limited:
            logger.warning(
                "Rate limit exceeded",
                extra={
                    "client_id": client_id,
                    "path": request.url.path,
                    "method": request.method,
                    "rate_info": rate_info,
                }
            )
            
            # Return rate limit error
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Please try again later.",
                headers={
                    "X-RateLimit-Limit-Minute": str(self.requests_per_minute),
                    "X-RateLimit-Limit-Hour": str(self.requests_per_hour),
                    "X-RateLimit-Remaining-Minute": str(
                        max(0, self.requests_per_minute - rate_info["requests_per_minute"])
                    ),
                    "X-RateLimit-Remaining-Hour": str(
                        max(0, self.requests_per_hour - rate_info["requests_per_hour"])
                    ),
                    "X-RateLimit-Reset-Minute": str(rate_info["reset_minute"]),
                    "X-RateLimit-Reset-Hour": str(rate_info["reset_hour"]),
                    "Retry-After": "60",  # Retry after 1 minute
                }
            )
        
        # Record the request
        self.record_request(client_id)
        
        # Process request
        response = await call_next(request)
        
        # Add rate limit headers to response
        response.headers.update({
            "X-RateLimit-Limit-Minute": str(self.requests_per_minute),
            "X-RateLimit-Limit-Hour": str(self.requests_per_hour),
            "X-RateLimit-Remaining-Minute": str(
                max(0, self.requests_per_minute - rate_info["requests_per_minute"] - 1)
            ),
            "X-RateLimit-Remaining-Hour": str(
                max(0, self.requests_per_hour - rate_info["requests_per_hour"] - 1)
            ),
        })
        
        return response