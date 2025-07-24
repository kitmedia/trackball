# Trackball AI Sports Analysis Platform

Professional video analysis for semi-professional teams using AI-powered object detection and tracking.

## Architecture

- **Frontend**: React 18 + TypeScript + Material-UI + Zustand
- **Backend**: Python FastAPI + PostgreSQL + Redis
- **AI/ML**: YOLOv8 + DeepSORT + OpenCV
- **Infrastructure**: AWS with CDK + Docker + Nx Monorepo

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.11+
- Docker & Docker Compose
- AWS CLI (for deployment)

### Development Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development environment**:
   ```bash
   npm run start
   ```

3. **Run with Docker**:
   ```bash
   npm run docker:dev
   ```

### Available Scripts

- `npm run start` - Start frontend and backend concurrently
- `npm run build` - Build all applications
- `npm run test` - Run all tests
- `npm run lint` - Lint all code
- `npm run format` - Format code with Prettier
- `npm run docker:dev` - Start development environment with Docker
- `npm run infra:deploy` - Deploy to AWS

## Project Structure

```
trackball/
├── apps/
│   ├── web/                    # React frontend
│   ├── api/                    # FastAPI backend
│   ├── video-processor/        # Video processing service
│   ├── ai-tracker/             # AI tracking service
│   └── export-service/         # Export and analytics service
├── libs/
│   ├── shared-types/           # Shared TypeScript/Python types
│   ├── ui-components/          # React component library
│   ├── api-client/             # Frontend API client
│   ├── video-utils/            # Video processing utilities
│   ├── ai-models/              # ML models and utilities
│   └── database/               # Database models and migrations
├── tools/                      # Build and development tools
├── infrastructure/             # Infrastructure as Code
├── docs/                       # Documentation
└── .github/                    # CI/CD workflows
```

## Technology Stack

### Frontend
- **React 18.2.0** - Modern UI framework
- **TypeScript 5.0+** - Type safety
- **Material-UI 5.14+** - Component library
- **Zustand 4.4+** - State management
- **Vite 5.0+** - Build tool

### Backend
- **Python 3.11+** - Core language
- **FastAPI 0.104+** - Async API framework
- **PostgreSQL 15+** - Primary database
- **Redis 7.2+** - Caching and sessions
- **SQLAlchemy** - ORM

### AI/ML
- **YOLOv8** - Object detection
- **DeepSORT** - Multi-object tracking
- **OpenCV 4.8+** - Computer vision
- **PyTorch 2.1+** - ML framework

### Infrastructure
- **AWS** - Cloud platform
- **Docker** - Containerization
- **Nx** - Monorepo tools
- **GitHub Actions** - CI/CD

## Development

### Frontend Development

```bash
# Start frontend only
nx serve web

# Build frontend
nx build web

# Test frontend
nx test web

# Lint frontend
nx lint web
```

### Backend Development

```bash
# Start backend only
nx serve api

# Build backend
nx build api

# Test backend
nx test api

# Database migrations
npm run db:migrate
```

### Testing

- **Unit Tests**: Jest/Vitest + React Testing Library + pytest
- **Integration Tests**: FastAPI TestClient + Database fixtures
- **E2E Tests**: Playwright
- **Coverage**: >80% required

## Deployment

### Development
```bash
npm run infra:deploy
```

### Production
CI/CD pipeline handles production deployments via GitHub Actions.

## Documentation

- [Architecture Documentation](./docs/architecture.md)
- [API Documentation](./docs/api-specification.md)
- [Frontend Components](./docs/front-end-spec.md)
- [Development Guidelines](./docs/development.md)

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines and coding standards.

## License

MIT License - see [LICENSE](./LICENSE) for details.