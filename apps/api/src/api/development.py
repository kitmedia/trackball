"""
Development-only endpoints for testing and debugging.

These endpoints are only available when DEBUG=True and provide
utilities for development, testing, and troubleshooting.
"""

import logging
import platform
import time
from typing import Dict, Any, List

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..config.settings import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()

settings = get_settings()


class SystemInfo(BaseModel):
    """System information model."""
    python_version: str
    platform: str
    architecture: str
    environment: str
    debug_mode: bool
    uptime_seconds: float


class ConfigInfo(BaseModel):
    """Configuration information model."""
    environment: str
    debug: bool
    database_configured: bool
    redis_configured: bool
    aws_configured: bool
    gpu_enabled: bool
    log_level: str


class MetricsInfo(BaseModel):
    """Development metrics model."""
    total_requests: int
    avg_response_time_ms: float
    error_rate_percent: float
    active_connections: int
    memory_usage_mb: float


# Mock data for development
start_time = time.time()
mock_metrics = {
    "total_requests": 0,
    "response_times": [],
    "errors": 0,
}


@router.get("/info", response_model=SystemInfo)
async def get_system_info() -> SystemInfo:
    """
    Get system and environment information.
    
    Returns detailed information about the running system,
    Python environment, and application configuration.
    """
    current_time = time.time()
    uptime = current_time - start_time
    
    return SystemInfo(
        python_version=platform.python_version(),
        platform=platform.platform(),
        architecture=platform.architecture()[0],
        environment=settings.environment,
        debug_mode=settings.debug,
        uptime_seconds=uptime,
    )


@router.get("/config", response_model=ConfigInfo)
async def get_config_info() -> ConfigInfo:
    """
    Get application configuration information.
    
    Returns sanitized configuration information useful for debugging.
    Note: Sensitive values are not exposed.
    """
    return ConfigInfo(
        environment=settings.environment,
        debug=settings.debug,
        database_configured=bool(settings.database_url),
        redis_configured=bool(settings.redis_url),
        aws_configured=bool(settings.aws_region and settings.s3_bucket_video),
        gpu_enabled=settings.gpu_enabled,
        log_level=settings.log_level,
    )


@router.get("/metrics", response_model=MetricsInfo)
async def get_metrics() -> MetricsInfo:
    """
    Get development metrics and performance information.
    
    Returns basic metrics about application performance and usage.
    Useful for development monitoring and debugging.
    """
    # Update mock metrics
    mock_metrics["total_requests"] += 1
    mock_metrics["response_times"].append(50.0)  # Mock 50ms response time
    
    # Calculate averages
    avg_response_time = (
        sum(mock_metrics["response_times"]) / len(mock_metrics["response_times"])
        if mock_metrics["response_times"] else 0.0
    )
    
    error_rate = (
        (mock_metrics["errors"] / mock_metrics["total_requests"]) * 100
        if mock_metrics["total_requests"] > 0 else 0.0
    )
    
    return MetricsInfo(
        total_requests=mock_metrics["total_requests"],
        avg_response_time_ms=avg_response_time,
        error_rate_percent=error_rate,
        active_connections=5,  # Mock value
        memory_usage_mb=128.5,  # Mock value
    )


@router.post("/seed")
async def seed_database() -> Dict[str, str]:
    """
    Seed database with development data.
    
    Creates sample users, teams, sessions, and video data
    for development and testing purposes.
    """
    try:
        # Mock database seeding
        # TODO: Implement actual database seeding with sample data
        
        logger.info("Seeding database with development data...")
        
        # Simulate seeding process
        await asyncio.sleep(0.1)
        
        logger.info("Database seeded successfully")
        
        return {
            "message": "Database seeded successfully",
            "users_created": "5",
            "teams_created": "2",
            "sessions_created": "10",
            "video_files_created": "20",
        }
        
    except Exception as e:
        logger.error(f"Database seeding failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database seeding failed: {str(e)}"
        )


@router.delete("/reset")
async def reset_environment() -> Dict[str, str]:
    """
    Reset development environment.
    
    Clears all development data, resets metrics,
    and returns the environment to a clean state.
    """
    try:
        # Mock environment reset
        # TODO: Implement actual environment reset
        
        logger.warning("Resetting development environment...")
        
        # Reset mock metrics
        global mock_metrics
        mock_metrics = {
            "total_requests": 0,
            "response_times": [],
            "errors": 0,
        }
        
        logger.warning("Development environment reset completed")
        
        return {
            "message": "Development environment reset successfully",
            "warning": "All development data has been cleared",
        }
        
    except Exception as e:
        logger.error(f"Environment reset failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Environment reset failed: {str(e)}"
        )


@router.get("/logs")
async def get_recent_logs() -> Dict[str, List[str]]:
    """
    Get recent application logs for debugging.
    
    Returns the most recent log entries for troubleshooting
    and development purposes.
    """
    try:
        # Mock log retrieval
        # TODO: Implement actual log file reading
        
        mock_logs = [
            "2024-01-23 10:00:00 - INFO - Application started",
            "2024-01-23 10:01:15 - INFO - User demo@trackball.com logged in",
            "2024-01-23 10:02:30 - INFO - Health check passed",
            "2024-01-23 10:03:45 - DEBUG - Database query executed in 25ms",
            "2024-01-23 10:05:00 - INFO - Video processing job queued",
        ]
        
        return {
            "logs": mock_logs,
            "total_entries": len(mock_logs),
            "last_updated": "2024-01-23T10:05:00Z",
        }
        
    except Exception as e:
        logger.error(f"Log retrieval failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Log retrieval failed: {str(e)}"
        )


@router.get("/ping")
async def ping() -> Dict[str, str]:
    """
    Simple ping endpoint for connectivity testing.
    
    Returns a basic response to verify the API is responding.
    """
    return {
        "message": "pong",
        "timestamp": str(time.time()),
        "environment": settings.environment,
    }