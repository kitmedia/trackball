# Multi-stage Dockerfile for FastAPI backend
FROM python:3.11-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create app user
RUN useradd --create-home --shell /bin/bash trackball

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Development stage
FROM base as development

# Install development dependencies
RUN pip install --no-cache-dir pytest pytest-asyncio pytest-cov black ruff mypy

# Copy source code
COPY . .

# Change ownership to app user
RUN chown -R trackball:trackball /app

# Switch to app user
USER trackball

# Expose port
EXPOSE 3333

# Command for development
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3333", "--reload"]

# Production stage
FROM base as production

# Copy source code
COPY . .

# Change ownership to app user
RUN chown -R trackball:trackball /app

# Switch to app user
USER trackball

# Expose port
EXPOSE 3333

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:3333/health || exit 1

# Command for production
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3333", "--workers", "4"]