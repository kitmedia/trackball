"""
Health check endpoints for monitoring and load balancer integration.

Provides endpoints to check the health of the application, database,
cache, and external services.
"""

import asyncio
import logging
import time
from typing import Dict, Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from ..config.settings import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()

settings = get_settings()


class HealthStatus(BaseModel):
    """Health check response model."""
    status: str
    timestamp: float
    environment: str
    version: str
    checks: Dict[str, Any]


class ComponentHealth(BaseModel):
    """Individual component health model."""
    status: str
    response_time_ms: float
    details: Dict[str, Any] = {}


async def check_database() -> ComponentHealth:
    """Check database connectivity and performance."""
    start_time = time.time()
    
    try:
        # Mock database check for now
        # TODO: Implement actual database connection check
        await asyncio.sleep(0.01)  # Simulate database query
        
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="healthy",
            response_time_ms=response_time,
            details={
                "connection": "active",
                "pool_size": 10,
                "active_connections": 2,
            }
        )
    except Exception as e:
        logger.error(f"Database health check failed: {e}")
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="unhealthy",
            response_time_ms=response_time,
            details={
                "error": str(e),
                "connection": "failed",
            }
        )


async def check_redis() -> ComponentHealth:
    """Check Redis connectivity and performance."""
    start_time = time.time()
    
    try:
        # Mock Redis check for now
        # TODO: Implement actual Redis connection check
        await asyncio.sleep(0.005)  # Simulate Redis ping
        
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="healthy",
            response_time_ms=response_time,
            details={
                "connection": "active",
                "memory_usage": "50MB",
                "connected_clients": 5,
            }
        )
    except Exception as e:
        logger.error(f"Redis health check failed: {e}")
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="unhealthy",
            response_time_ms=response_time,
            details={
                "error": str(e),
                "connection": "failed",
            }
        )


async def check_storage() -> ComponentHealth:
    """Check S3 storage connectivity and quota status."""
    start_time = time.time()
    
    try:
        # Mock S3 check for now
        # TODO: Implement actual S3 connectivity check
        await asyncio.sleep(0.02)  # Simulate S3 API call
        
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="healthy",
            response_time_ms=response_time,
            details={
                "bucket_accessible": True,
                "storage_used_gb": 150.5,
                "quota_limit_gb": 1000,
                "quota_usage_percent": 15.05,
            }
        )
    except Exception as e:
        logger.error(f"Storage health check failed: {e}")
        response_time = (time.time() - start_time) * 1000
        
        return ComponentHealth(
            status="unhealthy",
            response_time_ms=response_time,
            details={
                "error": str(e),
                "bucket_accessible": False,
            }
        )


@router.get("/", response_model=HealthStatus)
async def health_check() -> HealthStatus:
    """
    Overall application health status.
    
    Returns comprehensive health information including database,
    cache, storage, and application status.
    """
    start_time = time.time()
    
    try:
        # Run all health checks concurrently
        db_health, redis_health, storage_health = await asyncio.gather(
            check_database(),
            check_redis(),
            check_storage(),
            return_exceptions=True
        )
        
        # Determine overall status
        all_checks = [db_health, redis_health, storage_health]
        overall_status = "healthy"
        
        for check in all_checks:
            if isinstance(check, Exception) or check.status != "healthy":
                overall_status = "degraded"
                break
        
        total_time = (time.time() - start_time) * 1000
        
        return HealthStatus(
            status=overall_status,
            timestamp=time.time(),
            environment=settings.environment,
            version="1.0.0",
            checks={
                "database": db_health.dict() if not isinstance(db_health, Exception) else {"status": "error", "error": str(db_health)},
                "redis": redis_health.dict() if not isinstance(redis_health, Exception) else {"status": "error", "error": str(redis_health)},
                "storage": storage_health.dict() if not isinstance(storage_health, Exception) else {"status": "error", "error": str(storage_health)},
                "response_time_ms": total_time,
            }
        )
        
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Health check failed"
        )


@router.get("/db", response_model=ComponentHealth)
async def database_health() -> ComponentHealth:
    """Database connectivity and performance check."""
    return await check_database()


@router.get("/redis", response_model=ComponentHealth)
async def redis_health() -> ComponentHealth:
    """Redis cache connectivity and performance check."""
    return await check_redis()


@router.get("/storage", response_model=ComponentHealth)
async def storage_health() -> ComponentHealth:
    """S3 storage connectivity and quota status check."""
    return await check_storage()


@router.get("/ready")
async def readiness_check() -> Dict[str, str]:
    """
    Kubernetes/container readiness probe.
    
    Returns 200 OK when the application is ready to serve traffic.
    """
    return {"status": "ready"}


@router.get("/live")
async def liveness_check() -> Dict[str, str]:
    """
    Kubernetes/container liveness probe.
    
    Returns 200 OK when the application is alive and responding.
    """
    return {"status": "alive"}