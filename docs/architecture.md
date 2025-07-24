# Trackball Fullstack Architecture Document

## Introduction

This document outlines the complete fullstack architecture for Trackball, including backend systems, frontend implementation, and their integration. It serves as the single source of truth for AI-driven development, ensuring consistency across the entire technology stack.

This unified approach combines what would traditionally be separate backend and frontend architecture documents, streamlining the development process for modern fullstack applications where these concerns are increasingly intertwined.

### Starter Template or Existing Project

**N/A - Greenfield Project**

This is a new project built from the ground up to address the specific requirements of AI-powered sports video analysis. We will leverage modern fullstack development patterns optimized for video processing workflows and cloud-native deployment.

### Change Log
| Date | Version | Description | Author |
|------|---------|-------------|---------|
| 2025-01-22 | 1.0 | Initial fullstack architecture document | Winston (Architect) |

## High Level Architecture

### Technical Summary

Trackball employs a cloud-native microservices architecture with React frontend and Python FastAPI backend, deployed on AWS infrastructure optimized for GPU-intensive video processing. The system integrates dual 4K video streams through automated synchronization pipelines, processes them using YOLOv8 + DeepSORT AI models, and delivers analysis results through real-time WebSocket connections. AWS S3 with CloudFront CDN handles massive video storage and streaming requirements, while PostgreSQL manages session metadata and Redis orchestrates processing queues. This architecture achieves the critical sub-15 minute processing goal through parallel GPU processing and efficient cloud resource scaling.

### Platform and Infrastructure Choice

**Platform:** AWS (Amazon Web Services)  
**Key Services:** EC2 G4 instances for GPU processing, S3 for video storage, CloudFront CDN, RDS PostgreSQL, ElastiCache Redis, API Gateway, Lambda for auxiliary functions, Cognito for authentication  
**Deployment Host and Regions:** US-East-1 (primary) with US-West-2 (secondary) for coaching staff geographic distribution

### Repository Structure

**Structure:** Nx Monorepo  
**Monorepo Tool:** Nx with TypeScript project references  
**Package Organization:** Apps separated by deployment unit (web, api), packages for shared code (types, utilities, UI components)

### High Level Architecture Diagram

```mermaid
graph TB
    User[Coaching Staff] --> Web[React Web App]
    Web --> CDN[CloudFront CDN]
    Web --> Gateway[API Gateway]
    
    Gateway --> Auth[Cognito Auth]
    Gateway --> API[FastAPI Backend]
    Gateway --> WS[WebSocket Service]
    
    API --> DB[(PostgreSQL RDS)]
    API --> Cache[(Redis ElastiCache)]
    API --> Queue[Processing Queue]
    
    Queue --> GPU[EC2 G4 Processing]
    GPU --> AI[YOLOv8 + DeepSORT]
    GPU --> Video[FFmpeg Pipeline]
    
    API --> S3[S3 Video Storage]
    S3 --> CDN
    
    GPU --> S3
    DB --> Backup[RDS Backups]
    
    External[External APIs] --> Gateway
```

### Architectural Patterns

- **Cloud-Native Architecture:** Serverless and managed services where possible to minimize operational overhead - _Rationale:_ Allows team to focus on video analysis features rather than infrastructure management
- **Event-Driven Processing:** Asynchronous video processing with queue-based coordination - _Rationale:_ Enables scalable processing of multiple concurrent video analysis sessions
- **CQRS Pattern:** Separate read/write models for video metadata and analysis results - _Rationale:_ Optimizes database performance for time-series tracking data queries
- **Repository Pattern:** Abstract data access for session and user management - _Rationale:_ Enables testing and potential future database migration flexibility
- **BFF (Backend for Frontend):** API designed specifically for React frontend needs - _Rationale:_ Optimizes data fetching and reduces client-side complexity
- **Circuit Breaker Pattern:** Fault tolerance for external AI services and GPU processing - _Rationale:_ Ensures system stability when processing resources are constrained

## Tech Stack

| Category | Technology | Version | Purpose | Rationale |
|----------|------------|---------|---------|-----------|
| Frontend Language | TypeScript | 5.3+ | Type-safe React development | Provides compile-time error checking for video player interfaces and AI data structures |
| Frontend Framework | React | 18.2+ | Component-based UI framework | Mature ecosystem with video player libraries, excellent performance for timeline scrubbing |
| UI Component Library | Material-UI | 5.14+ | Professional design system | Provides accessible, professional components suitable for coaching workflows |
| State Management | Zustand | 4.4+ | Lightweight state management | Simple API perfect for video player state without Redux complexity |
| Backend Language | Python | 3.11+ | AI/ML ecosystem compatibility | Native integration with OpenCV, PyTorch, and video processing libraries |
| Backend Framework | FastAPI | 0.104+ | Modern async API framework | High performance async support essential for video processing coordination |
| API Style | REST with WebSocket | OpenAPI 3.0 | Standard API with real-time updates | REST for CRUD operations, WebSocket for processing progress updates |
| Database | PostgreSQL | 15+ | JSONB support for tracking data | Handles both relational team data and flexible AI analysis results |
| Cache | Redis | 7.2+ | Session and queue management | Essential for processing queue coordination and video player session state |
| File Storage | AWS S3 | - | Video file storage and CDN | Optimized for large video files with global CDN distribution |
| Authentication | AWS Cognito | - | OAuth 2.0 and user management | Enterprise-grade auth with role-based access control |
| Frontend Testing | Vitest + RTL | Latest | Unit and integration testing | Fast test runner optimized for TypeScript and React components |
| Backend Testing | pytest + TestClient | Latest | API and service testing | Comprehensive testing for FastAPI with async support |
| E2E Testing | Playwright | Latest | Full user journey validation | Cross-browser testing including video playback scenarios |
| Build Tool | Nx | 17+ | Monorepo build orchestration | Coordinates frontend/backend builds with shared dependencies |
| Bundler | Vite | 5+ | Fast frontend bundling | Optimized for React development with hot reload |
| IaC Tool | AWS CDK | 2.100+ | Infrastructure as code | Type-safe infrastructure definitions with AWS service integration |
| CI/CD | GitHub Actions | - | Automated testing and deployment | Native GitHub integration with AWS deployment workflows |
| Monitoring | DataDog | - | Application performance monitoring | Comprehensive monitoring for video processing performance |
| Logging | CloudWatch | - | Centralized logging | Native AWS logging with video processing pipeline observability |
| CSS Framework | Tailwind CSS | 3.3+ | Utility-first styling | Flexible styling system for custom video analysis interfaces |

## Data Models

### User

**Purpose:** Represents coaching staff and analysts with role-based access control for team video content

**Key Attributes:**
- id: UUID - Unique user identifier
- email: string - Authentication email address
- name: string - Display name for coaching staff
- role: UserRole - Coach, Analyst, or Viewer permissions
- teamId: UUID - Associated team for data access control

#### TypeScript Interface

```typescript
interface User {
  id: string;
  email: string;
  name: string;
  role: 'coach' | 'analyst' | 'viewer';
  teamId: string;
  createdAt: Date;
  lastLoginAt?: Date;
  preferences: UserPreferences;
}

interface UserPreferences {
  defaultVideoQuality: 'auto' | '1080p' | '4k';
  overlayDefaults: OverlaySettings;
  notificationSettings: NotificationSettings;
}
```

#### Relationships
- Belongs to one Team (many-to-one)
- Creates many AnalysisSessions (one-to-many)
- Creates many VideoClips (one-to-many)

### Team

**Purpose:** Organizational unit for grouping users and managing video analysis sessions with shared access permissions

#### TypeScript Interface

```typescript
interface Team {
  id: string;
  name: string;
  sport: 'soccer' | 'football' | 'basketball' | 'hockey';
  subscriptionTier: 'starter' | 'professional' | 'elite';
  storageQuota: number;
  processingQuota: number;
  createdAt: Date;
  settings: TeamSettings;
}
```

### AnalysisSession

**Purpose:** Represents a complete video analysis workflow from dual camera upload through AI processing to final results

#### TypeScript Interface

```typescript
interface AnalysisSession {
  id: string;
  teamId: string;
  createdById: string;
  status: 'uploading' | 'queued' | 'processing' | 'completed' | 'failed';
  metadata: SessionMetadata;
  processingStarted?: Date;
  processingCompleted?: Date;
  videoFiles: VideoFile[];
  aiResults?: AIAnalysisResults;
  createdAt: Date;
}

interface SessionMetadata {
  matchDate: Date;
  opponent: string;
  venue: string;
  notes?: string;
  tags: string[];
}
```

### AIAnalysisResults

**Purpose:** Stores comprehensive AI processing results including tracking data, event detection, and confidence metrics

#### TypeScript Interface

```typescript
interface AIAnalysisResults {
  sessionId: string;
  processingVersion: string;
  trackingData: TrackingData;
  detectedEvents: GameEvent[];
  confidenceMetrics: ConfidenceMetrics;
  panoramicVideoS3Key: string;
  processingDuration: number;
  createdAt: Date;
}

interface GameEvent {
  type: 'goal' | 'shot' | 'pass' | 'tackle' | 'offside';
  timestamp: number;
  confidence: number;
  boundingBox: BoundingBox;
  description: string;
}
```

## API Specification

### REST API Endpoints

```yaml
openapi: 3.0.0
info:
  title: Trackball Video Analysis API
  version: 1.0.0
  description: REST API for sports video analysis with AI-powered tracking and insights

paths:
  /sessions:
    get:
      summary: List analysis sessions for team
      responses:
        200:
          description: Session list retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/AnalysisSession'
    
    post:
      summary: Create new analysis session
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SessionCreate'
      responses:
        201:
          description: Session created successfully

  /sessions/{sessionId}/upload:
    post:
      summary: Upload video file for analysis session
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  type: string
                  format: binary
                cameraPosition:
                  type: string
                  enum: [A, B]

  /sessions/{sessionId}/process:
    post:
      summary: Initiate AI processing for uploaded videos
      responses:
        202:
          description: Processing queued successfully

  /sessions/{sessionId}/clips:
    get:
      summary: Get video clips for analysis session
    post:
      summary: Create new video clip
```

## Components

### Web Application Component

**Responsibility:** React-based frontend providing video analysis interface, real-time processing updates, and clip creation tools for coaching staff

**Key Interfaces:**
- REST API client for session and user management
- WebSocket connection for real-time processing updates
- S3 direct upload for large video files
- CDN streaming for 4K video playback

**Technology Stack:** React 18 + TypeScript, Material-UI components, Zustand state management, React Query for API caching

### API Gateway Component

**Responsibility:** Central API orchestration handling authentication, rate limiting, and routing to appropriate backend services

**Key Interfaces:**
- RESTful endpoints for client applications
- Cognito integration for JWT validation
- Lambda function invocation for auxiliary operations

**Technology Stack:** AWS API Gateway with custom authorizers, CloudWatch integration

### FastAPI Backend Component

**Responsibility:** Core business logic handling session management, video processing coordination, and data persistence operations

**Key Interfaces:**
- RESTful API endpoints for session CRUD operations
- WebSocket server for real-time client updates
- PostgreSQL database connections for data persistence
- Redis queue management for processing coordination

**Technology Stack:** FastAPI with async/await, SQLAlchemy ORM, Pydantic models, WebSocket support

### Video Processing Pipeline Component

**Responsibility:** GPU-intensive AI processing using YOLOv8 and DeepSORT for object detection, tracking, and video analysis

**Key Interfaces:**
- Redis queue consumer for processing jobs
- S3 direct access for video file retrieval and result storage
- FFmpeg integration for video manipulation
- AI model inference endpoints

**Technology Stack:** Python with OpenCV, PyTorch, YOLOv8, DeepSORT, FFmpeg, Docker containers

## Core Workflows

### Video Analysis Workflow

```mermaid
sequenceDiagram
    participant Coach
    participant WebApp
    participant API
    participant S3
    participant Queue
    participant GPU
    participant WebSocket
    
    Coach->>WebApp: Upload dual camera videos
    WebApp->>API: Create analysis session
    API->>S3: Generate pre-signed upload URLs
    WebApp->>S3: Direct upload video files
    WebApp->>API: Initiate processing
    API->>Queue: Add processing job
    API->>WebSocket: Send queued status
    WebSocket->>WebApp: Update UI with queue position
    
    Queue->>GPU: Start video processing
    GPU->>S3: Download video files
    GPU->>GPU: AI analysis (YOLOv8 + DeepSORT)
    GPU->>S3: Upload panoramic video and results
    GPU->>API: Processing completed callback
    API->>WebSocket: Send completed status
    WebSocket->>WebApp: Update UI with results
    
    Coach->>WebApp: Review analysis results
    WebApp->>S3: Stream processed video
```

## Database Schema

```sql
-- Users and Teams
CREATE TABLE teams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    sport VARCHAR(50) NOT NULL,
    subscription_tier VARCHAR(50) NOT NULL DEFAULT 'starter',
    storage_quota BIGINT NOT NULL DEFAULT 100000000000, -- 100GB
    processing_quota INTEGER NOT NULL DEFAULT 1000, -- minutes per month
    settings JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('coach', 'analyst', 'viewer')),
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    cognito_sub VARCHAR(255) UNIQUE NOT NULL,
    preferences JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login_at TIMESTAMP WITH TIME ZONE
);

-- Analysis Sessions
CREATE TABLE analysis_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    created_by_id UUID NOT NULL REFERENCES users(id),
    status VARCHAR(20) NOT NULL DEFAULT 'uploading' 
        CHECK (status IN ('uploading', 'queued', 'processing', 'completed', 'failed')),
    metadata JSONB NOT NULL,
    processing_started_at TIMESTAMP WITH TIME ZONE,
    processing_completed_at TIMESTAMP WITH TIME ZONE,
    processing_duration INTEGER, -- seconds
    error_message TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Video Files
CREATE TABLE video_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES analysis_sessions(id) ON DELETE CASCADE,
    camera_position CHAR(1) NOT NULL CHECK (camera_position IN ('A', 'B')),
    s3_key VARCHAR(1024) NOT NULL,
    original_filename VARCHAR(255),
    file_size BIGINT NOT NULL,
    duration INTEGER, -- seconds
    resolution VARCHAR(20), -- e.g., "3840x2160"
    frame_rate DECIMAL(5,2),
    codec VARCHAR(50),
    upload_status VARCHAR(20) DEFAULT 'pending'
        CHECK (upload_status IN ('pending', 'uploading', 'completed', 'failed')),
    uploaded_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- AI Analysis Results
CREATE TABLE ai_analysis_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES analysis_sessions(id) ON DELETE CASCADE,
    processing_version VARCHAR(50) NOT NULL,
    panoramic_video_s3_key VARCHAR(1024),
    tracking_data JSONB NOT NULL,
    detected_events JSONB NOT NULL,
    confidence_metrics JSONB NOT NULL,
    processing_metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Video Clips
CREATE TABLE video_clips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES analysis_sessions(id) ON DELETE CASCADE,
    created_by_id UUID NOT NULL REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    start_time INTEGER NOT NULL, -- seconds
    end_time INTEGER NOT NULL, -- seconds
    notes TEXT,
    s3_key VARCHAR(1024), -- generated clip file
    thumbnail_s3_key VARCHAR(1024),
    tags JSONB DEFAULT '[]',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Performance Indexes
CREATE INDEX idx_analysis_sessions_team_id ON analysis_sessions(team_id);
CREATE INDEX idx_analysis_sessions_status ON analysis_sessions(status);
CREATE INDEX idx_video_files_session_id ON video_files(session_id);
CREATE INDEX idx_video_clips_session_id ON video_clips(session_id);
```

## Frontend Architecture

### Component Architecture

#### Component Organization

```
apps/web/src/
├── components/
│   ├── ui/                    # Reusable UI components
│   │   ├── Button/
│   │   ├── Timeline/
│   │   └── VideoPlayer/
│   ├── features/              # Feature-specific components
│   │   ├── auth/
│   │   ├── sessions/
│   │   ├── video-analysis/
│   │   └── clips/
│   └── layout/               # Layout components
├── pages/                    # Route components
├── hooks/                    # Custom React hooks
├── services/                 # API client services
├── stores/                   # Zustand stores
└── types/                    # TypeScript type definitions
```

### State Management Architecture

```typescript
// stores/sessionStore.ts
interface SessionStore {
  sessions: AnalysisSession[];
  currentSession: AnalysisSession | null;
  processingStatus: Record<string, ProcessingStatus>;
  
  // Actions
  fetchSessions: () => Promise<void>;
  setCurrentSession: (session: AnalysisSession) => void;
  updateProcessingStatus: (sessionId: string, status: ProcessingStatus) => void;
  uploadVideos: (sessionId: string, files: File[]) => Promise<void>;
}
```

### Routing Architecture

```
/                           # Dashboard
/sessions                   # Session list
/sessions/:id              # Session detail/analysis
/sessions/:id/clips        # Clip management
/upload                    # Video upload wizard
/team                      # Team management
/profile                   # User profile
```

## Backend Architecture

### Service Architecture

#### Function Organization

```
apps/api/src/
├── routes/                   # FastAPI route handlers
│   ├── auth.py
│   ├── sessions.py
│   ├── videos.py
│   └── clips.py
├── services/                 # Business logic services
│   ├── session_service.py
│   ├── video_service.py
│   ├── processing_service.py
│   └── auth_service.py
├── models/                   # SQLAlchemy models
│   ├── user.py
│   ├── team.py
│   ├── session.py
│   └── video.py
├── schemas/                  # Pydantic schemas
├── core/                     # Core configuration
│   ├── config.py
│   ├── database.py
│   ├── redis.py
│   └── auth.py
└── main.py                   # FastAPI application
```

### Authentication and Authorization

#### Auth Flow

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant Cognito
    participant DB
    
    Client->>API: POST /auth/login
    API->>Cognito: Validate credentials
    Cognito->>API: JWT tokens
    API->>DB: Get/create user record
    DB->>API: User data with team info
    API->>Client: JWT + user profile
    
    Note over Client,API: Subsequent requests
    Client->>API: Request with Bearer token
    API->>Cognito: Validate JWT
    Cognito->>API: Token claims
    API->>API: Check permissions
    API->>Client: Authorized response
```

## Unified Project Structure

```plaintext
trackball/
├── .github/                    # CI/CD workflows
├── apps/                       # Application packages
│   ├── web/                    # React frontend application
│   │   ├── src/
│   │   │   ├── components/     # UI components
│   │   │   ├── pages/          # Page components/routes
│   │   │   ├── hooks/          # Custom React hooks
│   │   │   ├── services/       # API client services
│   │   │   ├── stores/         # Zustand state management
│   │   │   └── utils/          # Frontend utilities
│   │   ├── public/             # Static assets
│   │   └── tests/              # Frontend tests
│   └── api/                    # FastAPI backend application
│       ├── src/
│       │   ├── routes/         # API routes/controllers
│       │   ├── services/       # Business logic
│       │   ├── models/         # SQLAlchemy models
│       │   ├── schemas/        # Pydantic schemas
│       │   ├── core/           # Configuration
│       │   └── main.py         # FastAPI entry point
│       └── tests/              # Backend tests
├── packages/                   # Shared packages
│   ├── shared/                 # Shared types/utilities
│   │   ├── src/
│   │   │   ├── types/          # TypeScript interfaces
│   │   │   └── utils/          # Shared utilities
│   │   └── package.json
│   └── ui/                     # Shared UI components
├── infrastructure/             # AWS CDK infrastructure
│   ├── lib/
│   │   ├── compute-stack.ts
│   │   ├── storage-stack.ts
│   │   └── network-stack.ts
│   └── bin/infrastructure.ts
├── docs/                       # Documentation
│   ├── prd.md
│   ├── front-end-spec.md
│   └── architecture.md
├── .env.example                # Environment template
├── package.json                # Root package.json
├── nx.json                     # Nx configuration
└── README.md
```

## Development Workflow

### Local Development Setup

#### Prerequisites

```bash
# Install required tools
node --version  # >= 18.0.0
python --version  # >= 3.11
docker --version  # >= 20.10.0
aws --version  # Latest AWS CLI
```

#### Initial Setup

```bash
# Clone and setup
git clone https://github.com/organization/trackball.git
cd trackball

# Install dependencies
npm install
cd apps/api && poetry install && cd ../..

# Setup environment
cp .env.example .env.local
# Edit .env.local with development values

# Start services
docker-compose up -d postgres redis
cd apps/api && poetry run alembic upgrade head && cd ../..

# Start development
npm run dev
```

#### Development Commands

```bash
# Start all services
npm run dev

# Start individual services
npm run dev:web          # Frontend only
npm run dev:api          # Backend only

# Testing
npm run test             # All tests
npm run test:web         # Frontend tests
npm run test:api         # Backend tests
npm run test:e2e         # End-to-end tests

# Code quality
npm run lint            # Lint all code
npm run format          # Format all code
npm run typecheck       # TypeScript checking
```

### Environment Configuration

```bash
# Frontend (.env.local)
REACT_APP_API_BASE_URL=http://localhost:8000/api/v1
REACT_APP_WS_URL=ws://localhost:8000/ws
REACT_APP_COGNITO_USER_POOL_ID=us-east-1_example
REACT_APP_COGNITO_CLIENT_ID=example-client-id

# Backend (.env)
DATABASE_URL=postgresql://trackball:password@localhost:5432/trackball
REDIS_URL=redis://localhost:6379/0
AWS_REGION=us-east-1
S3_BUCKET_NAME=trackball-dev-videos
COGNITO_USER_POOL_ID=us-east-1_example
JWT_SECRET_KEY=development-secret-key
```

## Deployment Architecture

### Deployment Strategy

**Frontend Deployment:**
- **Platform:** Vercel with automatic deployments from main branch
- **Build Command:** `nx build web --prod`
- **Output Directory:** `dist/apps/web`
- **CDN/Edge:** Vercel Edge Network with global distribution

**Backend Deployment:**
- **Platform:** AWS ECS Fargate with Application Load Balancer
- **Build Command:** `docker build -f apps/api/Dockerfile .`
- **Deployment Method:** Blue/green deployments via AWS CodePipeline

### Environments

| Environment | Frontend URL | Backend URL | Purpose |
|-------------|-------------|-------------|---------|
| Development | http://localhost:3000 | http://localhost:8000 | Local development |
| Staging | https://staging.trackball.ai | https://api-staging.trackball.ai | Pre-production testing |
| Production | https://app.trackball.ai | https://api.trackball.ai | Live environment |

## Security and Performance

### Security Requirements

**Frontend Security:**
- CSP Headers: Strict CSP policy allowing only trusted domains
- XSS Prevention: Content sanitization, React's built-in XSS protection
- Secure Storage: JWT tokens in HTTP-only cookies

**Backend Security:**
- Input Validation: Pydantic model validation for all API inputs
- Rate Limiting: 100 requests/minute per user for API endpoints
- CORS Policy: Restricted to production and staging frontend domains

**Authentication Security:**
- Token Storage: JWT access tokens in HTTP-only cookies
- Session Management: 24-hour access token expiry, 30-day refresh token rotation
- Password Policy: Minimum 12 characters with complexity requirements

### Performance Optimization

**Frontend Performance:**
- Bundle Size Target: <500KB initial load, <2MB total
- Loading Strategy: Code splitting by route, lazy loading for video components
- Caching Strategy: React Query for API responses, Service Worker for thumbnails

**Backend Performance:**
- Response Time Target: <200ms for API endpoints, <2s for processing initiation
- Database Optimization: Connection pooling, query optimization, strategic indexing
- Caching Strategy: Redis for session state, CloudFront for video content

## Testing Strategy

### Testing Pyramid

```
                  E2E Tests
                 /        \
            Integration Tests  
               /            \
          Frontend Unit  Backend Unit
```

### Test Organization

#### Frontend Tests
```
apps/web/tests/
├── unit/                     # Component and hook tests
├── integration/              # Feature integration tests
└── __mocks__/               # Test mocks and fixtures
```

#### Backend Tests
```
apps/api/tests/
├── unit/                     # Service and model tests
├── integration/              # API endpoint tests
└── fixtures/                 # Test data and fixtures
```

#### E2E Tests
```
tests/e2e/
├── auth/                     # Authentication flows
├── video-upload/             # Video upload workflows
├── analysis/                 # Video analysis features
└── clips/                    # Clip creation and export
```

## Coding Standards

### Critical Fullstack Rules

- **Type Sharing:** Always define types in packages/shared and import from there
- **API Calls:** Never make direct HTTP calls - use the service layer
- **Environment Variables:** Access only through config objects, never process.env directly
- **Error Handling:** All API routes must use the standard error handler
- **State Updates:** Never mutate state directly - use proper state management patterns
- **Database Queries:** Always use the repository pattern
- **Video Processing:** All file operations must include proper error handling and cleanup
- **Authentication:** Always validate user permissions at the service layer
- **Testing:** Every service method must have unit tests with proper mocking

### Naming Conventions

| Element | Frontend | Backend | Example |
|---------|----------|---------|---------|
| Components | PascalCase | - | `VideoPlayer.tsx` |
| Hooks | camelCase with 'use' | - | `useVideoPlayer.ts` |
| API Routes | - | kebab-case | `/api/v1/analysis-sessions` |
| Database Tables | - | snake_case | `analysis_sessions` |

## Error Handling Strategy

### Error Response Format

```typescript
interface ApiError {
  error: {
    code: string;
    message: string;
    details?: Record<string, any>;
    timestamp: string;
    requestId: string;
  };
}
```

### Error Flow

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant Service
    participant DB
    
    Client->>API: Request with invalid data
    API->>API: Pydantic validation fails
    API->>Client: 422 Validation Error
    
    Client->>API: Valid request
    API->>Service: Call service method
    Service->>DB: Database operation
    DB->>Service: Connection error
    Service->>API: Raise ApiError
    API->>Client: Formatted error response
```

## Monitoring and Observability

### Monitoring Stack

- **Frontend Monitoring:** DataDog RUM for client-side performance and error tracking
- **Backend Monitoring:** DataDog APM for API performance and distributed tracing
- **Error Tracking:** DataDog error tracking with automatic alerting
- **Performance Monitoring:** Custom metrics for video processing pipeline performance

### Key Metrics

**Frontend Metrics:**
- Core Web Vitals (LCP, FID, CLS)
- JavaScript errors with stack traces
- API response times with endpoint-specific monitoring
- User interactions including video playback events

**Backend Metrics:**
- Request rate per endpoint with 95th percentile response times
- Error rate by endpoint and error type
- Database query performance with slow query identification
- Video processing pipeline metrics including queue depth

**Infrastructure Metrics:**
- EC2 GPU utilization and memory usage
- RDS connection pool usage and query performance
- S3 request metrics and transfer rates
- Redis memory usage and connection metrics

---

**Document Status**: Complete - Ready for development implementation

**Next Steps**:
1. Infrastructure deployment using AWS CDK
2. Development environment setup for team onboarding
3. Frontend component library development  
4. Backend service implementation with database schema
5. AI processing pipeline development and testing