# Tech Stack

## Definitive Technology Selection

This is the **single source of truth** for all technology choices in the Trackball video analysis system. All development must use these exact versions.

| Category | Technology | Version | Purpose | Rationale |
|----------|------------|---------|---------|-----------|
| **Frontend Language** | TypeScript | ^5.0.0 | Type-safe frontend development | Essential for large codebase maintainability and AI agent code generation |
| **Frontend Framework** | React | ^18.2.0 | UI component library | Large ecosystem, excellent video player integration, TypeScript support |
| **UI Component Library** | Material-UI (MUI) | ^5.14.0 | Professional UI components | Comprehensive component library with video controls, themes |
| **State Management** | Zustand | ^4.4.0 | Lightweight state management | Simple API, perfect for video player state and user preferences |
| **Backend Language** | Python | ^3.11.0 | Video processing and AI | Required for OpenCV, PyTorch, and video processing libraries |
| **Backend Framework** | FastAPI | ^0.104.0 | High-performance async API | Best Python async performance, automatic OpenAPI docs |
| **API Style** | REST + WebSocket | OpenAPI 3.0 | Hybrid API approach | REST for CRUD operations, WebSocket for real-time processing updates |
| **Database** | PostgreSQL | ^15.0 | Primary data storage | JSON support for metadata, excellent performance for time-series data |
| **Cache** | Redis | ^7.2.0 | Session and processing cache | Fast session storage and video processing status caching |
| **File Storage** | AWS S3 | Latest | Video file storage | Industry standard for large video files, CDN integration |
| **Authentication** | NextAuth.js | ^4.24.0 | User authentication | Comprehensive auth solution with multiple providers |
| **Frontend Testing** | Vitest + RTL | ^1.0.0 | Component and unit testing | Faster than Jest, excellent TypeScript support |
| **Backend Testing** | pytest + FastAPI TestClient | ^7.4.0 | API and service testing | Standard Python testing, excellent async support |
| **E2E Testing** | Playwright | ^1.40.0 | End-to-end testing | Best video player testing support, cross-browser |
| **Build Tool** | Vite | ^5.0.0 | Frontend build system | Fastest development server, excellent TypeScript support |
| **Bundler** | Rollup (via Vite) | ^4.0.0 | Production bundling | Optimal bundle splitting for video components |
| **IaC Tool** | AWS CDK | ^2.100.0 | Infrastructure as Code | Type-safe infrastructure, excellent AWS integration |
| **CI/CD** | GitHub Actions | Latest | Continuous integration | Native GitHub integration, excellent container support |
| **Monitoring** | AWS CloudWatch + Sentry | Latest | Application monitoring | AWS native monitoring + error tracking |
| **Logging** | Python logging + CloudWatch | Latest | Centralized logging | Structured logging for video processing pipeline |
| **CSS Framework** | Tailwind CSS | ^3.3.0 | Utility-first styling | Rapid UI development, excellent customization |

## Video Processing Specific Stack

| Category | Technology | Version | Purpose | Rationale |
|----------|------------|---------|---------|-----------|
| **Video Processing** | OpenCV | ^4.8.0 | Computer vision library | Industry standard for video processing and camera calibration |
| **Video Encoding** | FFmpeg | ^6.0 | Video transcoding | Most comprehensive video processing toolkit |
| **AI/ML Framework** | PyTorch | ^2.1.0 | Deep learning models | Best ecosystem for YOLO and tracking models |
| **Object Detection** | YOLOv8 (Ultralytics) | ^8.0.0 | Ball and player detection | State-of-the-art real-time object detection |
| **Object Tracking** | DeepSORT | Latest | Multi-object tracking | Proven tracking algorithm for sports analysis |
| **GPU Acceleration** | CUDA | ^12.0 | GPU processing | Required for real-time 4K video processing |
| **Video Streaming** | HLS.js | ^1.4.0 | Adaptive video streaming | Efficient 4K video delivery to browsers |

## Development Tools

| Category | Technology | Version | Purpose |
|----------|------------|---------|---------|
| **Code Formatting** | Prettier | ^3.0.0 | Code formatting |
| **Linting** | ESLint + Ruff | Latest | Code quality |
| **Type Checking** | TypeScript + mypy | Latest | Static analysis |
| **Git Hooks** | Husky | ^8.0.0 | Pre-commit validation |
| **Package Manager** | npm | ^10.0.0 | Dependency management |
| **Container Runtime** | Docker | ^24.0.0 | Containerization |
| **Orchestration** | Docker Compose | ^2.20.0 | Local development |

## Architecture Decisions

### Why FastAPI over Django?
- **Performance**: Async support crucial for video streaming
- **API-First**: Automatic OpenAPI documentation
- **Modern Python**: Better type hints and async patterns

### Why Zustand over Redux?
- **Simplicity**: Video player state is straightforward
- **Performance**: No unnecessary re-renders
- **TypeScript**: Excellent type inference

### Why PostgreSQL over MongoDB?
- **Structured Data**: Video metadata has clear relationships
- **JSON Support**: Flexible for tracking data storage
- **Performance**: Better for time-series analytics queries

### Why YOLOv8 over other models?
- **Speed**: Real-time performance on standard GPUs
- **Accuracy**: Best balance for sports object detection
- **Ecosystem**: Excellent Python integration