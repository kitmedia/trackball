# Unified Project Structure

## Overview

Monorepo structure for Trackball video analysis system using Nx workspace. Organizes frontend, backend, video processing services, and shared libraries in a scalable, maintainable architecture.

## Root Structure

```
trackball/
├── .github/                    # CI/CD workflows and GitHub configs
│   └── workflows/
│       ├── ci.yml              # Continuous integration
│       ├── deploy-staging.yml  # Staging deployment
│       └── deploy-prod.yml     # Production deployment
├── .nx/                        # Nx cache and configuration
├── apps/                       # Application packages
│   ├── web/                    # React frontend application
│   ├── api/                    # FastAPI backend application
│   ├── video-processor/        # Video processing microservice
│   ├── ai-tracker/             # AI tracking microservice
│   └── export-service/         # Export and analytics service
├── libs/                       # Shared libraries
│   ├── shared-types/           # TypeScript/Python shared types
│   ├── ui-components/          # React component library
│   ├── api-client/             # Frontend API client
│   ├── video-utils/            # Video processing utilities
│   ├── ai-models/              # ML models and utilities
│   └── database/               # Database models and migrations
├── tools/                      # Build and development tools
│   ├── docker/                 # Docker configurations
│   ├── scripts/                # Build and deployment scripts
│   └── generators/             # Nx generators for consistency
├── infrastructure/             # Infrastructure as Code
│   ├── aws-cdk/                # AWS CDK definitions
│   ├── terraform/              # Alternative Terraform configs
│   └── k8s/                    # Kubernetes manifests
├── docs/                       # Documentation
│   ├── architecture/           # Technical documentation
│   ├── prd/                    # Product requirements
│   └── stories/                # Development stories
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore patterns
├── docker-compose.yml          # Local development environment
├── nx.json                     # Nx workspace configuration
├── package.json                # Root package.json with workspace deps
├── tsconfig.base.json          # Base TypeScript configuration
└── README.md                   # Project overview and setup
```

## Applications (`apps/`)

### Web Application (`apps/web/`)

React frontend with TypeScript, Material-UI, and video analysis tools.

```
apps/web/
├── src/
│   ├── app/                    # App routing and layout
│   │   ├── App.tsx
│   │   ├── App.test.tsx
│   │   └── layout/
│   │       ├── Layout.tsx
│   │       ├── Sidebar.tsx
│   │       └── Header.tsx
│   ├── pages/                  # Page components
│   │   ├── auth/
│   │   │   ├── LoginPage.tsx
│   │   │   └── RegisterPage.tsx
│   │   ├── dashboard/
│   │   │   └── DashboardPage.tsx
│   │   ├── sessions/
│   │   │   ├── SessionListPage.tsx
│   │   │   ├── SessionDetailPage.tsx
│   │   │   └── VideoPlayerPage.tsx
│   │   ├── teams/
│   │   │   ├── TeamListPage.tsx
│   │   │   └── TeamDetailPage.tsx
│   │   └── analysis/
│   │       ├── AnalysisPage.tsx
│   │       └── ExportPage.tsx
│   ├── components/             # Page-specific components
│   │   ├── video/
│   │   │   ├── VideoPlayer.tsx
│   │   │   ├── VideoControls.tsx
│   │   │   ├── VideoTimeline.tsx
│   │   │   └── VideoAnnotations.tsx
│   │   ├── tracking/
│   │   │   ├── TrackingOverlay.tsx
│   │   │   ├── TrackingPanel.tsx
│   │   │   └── EventsList.tsx
│   │   └── forms/
│   │       ├── SessionForm.tsx
│   │       ├── TeamForm.tsx
│   │       └── ClipForm.tsx
│   ├── hooks/                  # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useWebSocket.ts
│   │   ├── useVideoPlayer.ts
│   │   └── useLocalStorage.ts
│   ├── services/               # API service layer
│   │   ├── api.ts              # Base API configuration
│   │   ├── auth.service.ts
│   │   ├── sessions.service.ts
│   │   ├── teams.service.ts
│   │   └── tracking.service.ts
│   ├── store/                  # Zustand state management
│   │   ├── authStore.ts
│   │   ├── sessionStore.ts
│   │   ├── videoPlayerStore.ts
│   │   └── index.ts
│   ├── utils/                  # Frontend utilities
│   │   ├── formatters.ts
│   │   ├── validators.ts
│   │   ├── constants.ts
│   │   └── helpers.ts
│   ├── styles/                 # Global styles and themes
│   │   ├── globals.css
│   │   ├── theme.ts
│   │   └── components.css
│   └── types/                  # App-specific types
│       ├── video.types.ts
│       ├── tracking.types.ts
│       └── ui.types.ts
├── public/                     # Static assets
│   ├── index.html
│   ├── favicon.ico
│   └── assets/
│       ├── icons/
│       └── images/
├── tests/                      # Frontend tests
│   ├── components/
│   ├── hooks/
│   ├── services/
│   └── utils/
├── .env.local.example
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
└── package.json
```

### API Application (`apps/api/`)

FastAPI backend with PostgreSQL, authentication, and video processing orchestration.

```
apps/api/
├── src/
│   ├── main.py                 # FastAPI application entry
│   ├── config/                 # Configuration management
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   └── database.py
│   ├── api/                    # API routes and endpoints
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication endpoints
│   │   ├── users.py            # User management
│   │   ├── teams.py            # Team management
│   │   ├── sessions.py         # Video sessions
│   │   ├── processing.py       # Video processing control
│   │   ├── tracking.py         # AI tracking results
│   │   ├── clips.py            # Video clips management
│   │   ├── annotations.py      # User annotations
│   │   └── exports.py          # Data export endpoints
│   ├── core/                   # Core business logic
│   │   ├── __init__.py
│   │   ├── auth.py             # Authentication logic
│   │   ├── security.py         # Security utilities
│   │   ├── permissions.py      # Authorization logic
│   │   └── websockets.py       # WebSocket management
│   ├── services/               # Business services
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   ├── team_service.py
│   │   ├── session_service.py
│   │   ├── processing_service.py
│   │   ├── tracking_service.py
│   │   └── export_service.py
│   ├── models/                 # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── team.py
│   │   ├── session.py
│   │   ├── processing.py
│   │   ├── tracking.py
│   │   └── annotation.py
│   ├── schemas/                # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── team.py
│   │   ├── session.py
│   │   ├── tracking.py
│   │   └── response.py
│   ├── middleware/             # FastAPI middleware
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── cors.py
│   │   ├── rate_limit.py
│   │   └── logging.py
│   ├── utils/                  # Backend utilities
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   ├── validators.py
│   │   └── constants.py
│   └── migrations/             # Database migrations
│       ├── alembic.ini
│       ├── env.py
│       └── versions/
├── tests/                      # Backend tests
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_sessions.py
│   ├── test_processing.py
│   └── integration/
│       ├── test_api.py
│       └── test_websockets.py
├── .env.example
├── requirements.txt
├── Dockerfile
├── pyproject.toml
└── pytest.ini
```

### Video Processor Service (`apps/video-processor/`)

Microservice for video synchronization, stitching, and preprocessing.

```
apps/video-processor/
├── src/
│   ├── main.py                 # Service entry point
│   ├── config/
│   │   ├── settings.py
│   │   └── gpu_config.py
│   ├── processors/             # Video processing modules
│   │   ├── __init__.py
│   │   ├── ingestion.py        # Video ingestion and validation
│   │   ├── synchronizer.py     # Multi-camera synchronization
│   │   ├── calibration.py      # Camera calibration and correction
│   │   ├── stitcher.py         # Panoramic video stitching
│   │   └── encoder.py          # Video encoding and optimization
│   ├── models/
│   │   ├── video_file.py
│   │   ├── processing_job.py
│   │   └── calibration_data.py
│   ├── services/
│   │   ├── queue_service.py    # Job queue management
│   │   ├── storage_service.py  # S3 video storage
│   │   └── notification_service.py # Processing status updates
│   ├── utils/
│   │   ├── opencv_utils.py
│   │   ├── ffmpeg_utils.py
│   │   ├── gpu_utils.py
│   │   └── metrics.py
│   └── workers/                # Background workers
│       ├── sync_worker.py
│       ├── stitch_worker.py
│       └── calibration_worker.py
├── tests/
├── requirements.txt
├── Dockerfile.gpu
└── docker-compose.gpu.yml
```

### AI Tracker Service (`apps/ai-tracker/`)

Microservice for AI-powered object detection and tracking.

```
apps/ai-tracker/
├── src/
│   ├── main.py
│   ├── models/                 # ML models and inference
│   │   ├── __init__.py
│   │   ├── yolo_detector.py    # YOLO object detection
│   │   ├── deep_sort.py        # Multi-object tracking
│   │   ├── event_detector.py   # Game event detection
│   │   └── model_loader.py     # Model management
│   ├── processors/
│   │   ├── frame_processor.py  # Individual frame processing
│   │   ├── batch_processor.py  # Batch processing optimization
│   │   └── tracking_processor.py # Object tracking logic
│   ├── services/
│   │   ├── inference_service.py
│   │   ├── tracking_service.py
│   │   └── event_service.py
│   ├── utils/
│   │   ├── model_utils.py
│   │   ├── tracking_utils.py
│   │   ├── visualization.py
│   │   └── metrics.py
│   └── config/
│       ├── model_config.py
│       └── tracking_config.py
├── models/                     # Pre-trained model files
│   ├── yolov8n.pt
│   ├── yolov8s.pt
│   └── deep_sort_weights/
├── tests/
├── requirements.txt
└── Dockerfile.gpu
```

## Shared Libraries (`libs/`)

### Shared Types (`libs/shared-types/`)

TypeScript interfaces and Python classes shared across services.

```
libs/shared-types/
├── src/
│   ├── typescript/             # Frontend types
│   │   ├── api.types.ts
│   │   ├── user.types.ts
│   │   ├── session.types.ts
│   │   ├── tracking.types.ts
│   │   └── video.types.ts
│   ├── python/                 # Backend types
│   │   ├── __init__.py
│   │   ├── api_types.py
│   │   ├── user_types.py
│   │   ├── session_types.py
│   │   └── tracking_types.py
│   └── schemas/                # JSON schemas for validation
│       ├── session.schema.json
│       ├── tracking.schema.json
│       └── annotation.schema.json
├── package.json
└── pyproject.toml
```

### UI Components (`libs/ui-components/`)

Reusable React components with Storybook documentation.

```
libs/ui-components/
├── src/
│   ├── components/
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.stories.tsx
│   │   │   ├── Button.test.tsx
│   │   │   └── Button.module.css
│   │   ├── VideoPlayer/
│   │   │   ├── VideoPlayer.tsx
│   │   │   ├── VideoPlayer.stories.tsx
│   │   │   └── VideoPlayer.test.tsx
│   │   ├── DataTable/
│   │   ├── Modal/
│   │   ├── Forms/
│   │   │   ├── Input/
│   │   │   ├── Select/
│   │   │   └── DatePicker/
│   │   └── Charts/
│   │       ├── LineChart/
│   │       └── BarChart/
│   ├── hooks/
│   │   ├── useClickOutside.ts
│   │   ├── useDebounce.ts
│   │   └── useMediaQuery.ts
│   ├── utils/
│   │   ├── theme.ts
│   │   └── animations.ts
│   └── index.ts                # Library exports
├── .storybook/
│   ├── main.js
│   └── preview.js
├── package.json
└── tsconfig.json
```

## Development Tools (`tools/`)

### Docker Configurations (`tools/docker/`)

```
tools/docker/
├── development/
│   ├── docker-compose.yml      # Local development stack
│   ├── postgres/
│   │   └── init.sql
│   ├── redis/
│   │   └── redis.conf
│   └── nginx/
│       └── nginx.conf
├── production/
│   ├── web.Dockerfile          # Production frontend
│   ├── api.Dockerfile          # Production backend
│   ├── video-processor.Dockerfile
│   └── ai-tracker.Dockerfile
└── gpu/
    ├── cuda.Dockerfile         # GPU-enabled containers
    └── requirements-gpu.txt
```

### Scripts (`tools/scripts/`)

```
tools/scripts/
├── setup/
│   ├── install-dependencies.sh
│   ├── setup-database.sh
│   └── setup-gpu.sh
├── build/
│   ├── build-all.sh
│   ├── build-frontend.sh
│   ├── build-backend.sh
│   └── build-docker.sh
├── deploy/
│   ├── deploy-staging.sh
│   ├── deploy-production.sh
│   └── rollback.sh
├── database/
│   ├── migrate.sh
│   ├── seed.sh
│   └── backup.sh
└── maintenance/
    ├── cleanup-logs.sh
    ├── optimize-database.sh
    └── update-models.sh
```

## Infrastructure (`infrastructure/`)

### AWS CDK (`infrastructure/aws-cdk/`)

```
infrastructure/aws-cdk/
├── src/
│   ├── app.ts                  # CDK app entry point
│   ├── stacks/
│   │   ├── networking-stack.ts # VPC, subnets, security groups
│   │   ├── database-stack.ts   # RDS PostgreSQL + Redis
│   │   ├── storage-stack.ts    # S3 buckets for videos
│   │   ├── compute-stack.ts    # ECS/Fargate services
│   │   ├── gpu-stack.ts        # EC2 GPU instances
│   │   ├── api-gateway-stack.ts # API Gateway + ALB
│   │   └── monitoring-stack.ts # CloudWatch + logging
│   ├── constructs/
│   │   ├── video-processor-service.ts
│   │   ├── ai-tracker-service.ts
│   │   └── web-application.ts
│   └── config/
│       ├── dev.ts
│       ├── staging.ts
│       └── production.ts
├── cdk.json
├── package.json
└── tsconfig.json
```

## File Naming Conventions

### Frontend Files
- **Components**: PascalCase (e.g., `VideoPlayer.tsx`)
- **Hooks**: camelCase with `use` prefix (e.g., `useAuth.ts`)
- **Services**: camelCase with `.service.ts` suffix
- **Types**: camelCase with `.types.ts` suffix
- **Tests**: Same as component with `.test.tsx` extension
- **Stories**: Same as component with `.stories.tsx` extension

### Backend Files
- **Models**: snake_case (e.g., `user_model.py`)
- **Services**: snake_case with `_service.py` suffix
- **Routes**: snake_case matching endpoint (e.g., `auth.py`)
- **Tests**: `test_` prefix with snake_case
- **Migrations**: Alembic auto-generated naming

### Configuration Files
- **Environment**: `.env.example`, `.env.local`, `.env.production`
- **Docker**: `Dockerfile` (default), `Dockerfile.gpu`, `docker-compose.yml`
- **Package managers**: `package.json`, `requirements.txt`, `pyproject.toml`
- **Build tools**: `vite.config.ts`, `tsconfig.json`, `nx.json`

## Build and Development Commands

### Nx Workspace Commands
```bash
# Install dependencies
npm install

# Start all services for development
nx run-many --target=serve --all

# Build all applications
nx run-many --target=build --all

# Run all tests
nx run-many --target=test --all

# Lint all projects
nx run-many --target=lint --all
```

### Individual Service Commands
```bash
# Start frontend only
nx serve web

# Start backend only
nx serve api

# Start video processor
nx serve video-processor

# Build specific app
nx build web --prod

# Test specific lib
nx test ui-components
```

### Docker Development
```bash
# Start local development stack
docker-compose -f tools/docker/development/docker-compose.yml up

# Build production containers
docker-compose -f tools/docker/production/docker-compose.yml build

# GPU-enabled development
docker-compose -f tools/docker/gpu/docker-compose.yml up
```

This unified structure provides clear separation of concerns while maintaining consistency across the monorepo, enabling efficient development and deployment of the Trackball video analysis system.