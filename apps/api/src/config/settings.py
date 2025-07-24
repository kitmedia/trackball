"""
Application settings and configuration management.

Centralized configuration using Pydantic settings with environment variable support.
"""

from functools import lru_cache
from typing import List

from pydantic import Field, PostgresDsn, RedisDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # Application
    environment: str = Field(default="development", description="Environment name")
    debug: bool = Field(default=True, description="Debug mode")
    secret_key: str = Field(default="dev-secret-key", description="Secret key for JWT")
    
    # API Configuration
    api_base_url: str = Field(default="http://localhost:3333", description="API base URL")
    allowed_origins: List[str] = Field(
        default=["http://localhost:4200", "http://localhost:3000"],
        description="Allowed CORS origins"
    )
    allowed_hosts: List[str] = Field(
        default=["localhost", "127.0.0.1", "*.trackball.com"],
        description="Allowed host headers"
    )
    
    # Database
    database_url: PostgresDsn = Field(
        default="postgresql://trackball_dev:dev_password@localhost:5432/trackball_dev",
        description="PostgreSQL database URL"
    )
    
    # Redis
    redis_url: RedisDsn = Field(
        default="redis://localhost:6379/0",
        description="Redis URL for caching and sessions"
    )
    
    # Authentication
    jwt_secret_key: str = Field(default="dev-jwt-secret", description="JWT secret key")
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    jwt_access_token_expire_minutes: int = Field(default=15, description="Access token expiry")
    jwt_refresh_token_expire_days: int = Field(default=7, description="Refresh token expiry")
    
    # AWS Configuration
    aws_region: str = Field(default="us-east-1", description="AWS region")
    s3_bucket_video: str = Field(default="trackball-dev-videos", description="S3 bucket for videos")
    s3_bucket_thumbnails: str = Field(default="trackball-dev-thumbnails", description="S3 bucket for thumbnails")
    
    # Video Processing
    max_video_size_mb: int = Field(default=2048, description="Maximum video size in MB")
    processing_timeout_minutes: int = Field(default=30, description="Processing timeout")
    gpu_enabled: bool = Field(default=False, description="Enable GPU processing")
    
    # AI/ML Configuration
    yolo_model_path: str = Field(default="models/yolov8n.pt", description="YOLO model path")
    tracking_confidence_threshold: float = Field(default=0.5, description="Tracking confidence threshold")
    detection_confidence_threshold: float = Field(default=0.6, description="Detection confidence threshold")
    
    # Logging and Monitoring
    log_level: str = Field(default="INFO", description="Log level")
    sentry_dsn: str = Field(default="", description="Sentry DSN for error tracking")
    datadog_api_key: str = Field(default="", description="DataDog API key")
    
    # Rate Limiting
    rate_limit_requests_per_minute: int = Field(default=100, description="Rate limit per minute")
    rate_limit_requests_per_hour: int = Field(default=1000, description="Rate limit per hour")
    
    # Security
    password_min_length: int = Field(default=8, description="Minimum password length")
    session_timeout_minutes: int = Field(default=60, description="Session timeout")


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()