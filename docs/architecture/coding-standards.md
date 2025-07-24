# Coding Standards

## Overview

**CRITICAL RULES** for AI agents implementing the Trackball video analysis system. These standards prevent common mistakes and ensure consistency across the fullstack TypeScript/Python codebase.

## 🚨 Critical Fullstack Rules

- **Type Sharing**: Always define types in `libs/shared-types` and import from there. NEVER duplicate type definitions between frontend and backend.
- **API Calls**: Never make direct HTTP calls in components. ALWAYS use the service layer from `libs/api-client`.
- **Environment Variables**: Access only through config objects in `src/config/`, never use `process.env` or `os.environ` directly.
- **Error Handling**: All API routes must use the standard error handler middleware. All frontend API calls must use try-catch.
- **State Updates**: Never mutate state directly. Use Zustand actions for state updates, React setState for component state.
- **Database Access**: Always use the repository pattern. Never write raw SQL in service classes.
- **File Paths**: Use path utilities from shared libraries. Never hardcode file paths.
- **Async/Await**: Prefer async/await over Promises. Always handle rejections.

## 📁 File Organization Rules

### Frontend Components
```typescript
// ✅ GOOD: Proper component structure
export interface VideoPlayerProps {
  sessionId: string;
  autoplay?: boolean;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ sessionId, autoplay = false }) => {
  const { session } = useSession(sessionId);
  // Component logic
};

export default VideoPlayer;
```

```typescript
// ❌ BAD: No props interface, inline types
const VideoPlayer = ({ sessionId, autoplay }: { sessionId: string, autoplay?: boolean }) => {
  // Component logic
};
```

### Backend Services
```python
# ✅ GOOD: Proper service structure
from libs.shared_types.python import SessionTypes
from .repositories import SessionRepository

class SessionService:
    def __init__(self, session_repo: SessionRepository):
        self.session_repo = session_repo
    
    async def get_session(self, session_id: str) -> SessionTypes.SessionResponse:
        session = await self.session_repo.get_by_id(session_id)
        return SessionTypes.SessionResponse.from_orm(session)
```

```python
# ❌ BAD: Direct database access, no types
class SessionService:
    async def get_session(self, session_id):
        # Direct database query - violates repository pattern
        result = await database.fetch_one("SELECT * FROM sessions WHERE id = ?", session_id)
        return result
```

## 🎯 Naming Conventions

| Element | Frontend | Backend | Example |
|---------|----------|---------|---------|
| **Components** | PascalCase | - | `VideoPlayer.tsx` |
| **Hooks** | camelCase with 'use' | - | `useVideoPlayer.ts` |
| **Services** | camelCase + .service | snake_case + _service | `sessionService.ts` / `session_service.py` |
| **API Routes** | - | kebab-case | `/api/video-sessions` |
| **Database Tables** | - | snake_case | `video_sessions` |
| **Environment Variables** | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE | `VIDEO_STORAGE_BUCKET` |
| **Constants** | UPPER_SNAKE_CASE | UPPER_SNAKE_CASE | `MAX_VIDEO_SIZE_MB` |

## 🔧 TypeScript Standards

### Import Organization
```typescript
// ✅ GOOD: Organized imports
// External libraries
import React from 'react';
import { Box, Typography } from '@mui/material';

// Internal libraries
import { SessionTypes } from '@trackball/shared-types';
import { VideoPlayer } from '@trackball/ui-components';

// Relative imports
import { useVideoPlayer } from '../hooks/useVideoPlayer';
import { sessionService } from '../services/session.service';
```

### Type Definitions
```typescript
// ✅ GOOD: Explicit interfaces
interface VideoPlayerState {
  isPlaying: boolean;
  currentTime: number;
  duration: number;
  volume: number;
}

interface VideoPlayerActions {
  play: () => void;
  pause: () => void;
  seek: (time: number) => void;
  setVolume: (volume: number) => void;
}

// ✅ GOOD: Proper generic usage
interface ApiResponse<T> {
  data: T;
  status: 'success' | 'error';
  message?: string;
}
```

### Error Handling
```typescript
// ✅ GOOD: Comprehensive error handling
const sessionService = {
  async getSession(id: string): Promise<SessionResponse> {
    try {
      const response = await api.get(`/sessions/${id}`);
      return response.data;
    } catch (error) {
      if (error instanceof ApiError) {
        logger.error('API Error:', error.message);
        throw new SessionError(`Failed to fetch session: ${error.message}`);
      }
      logger.error('Unexpected error:', error);
      throw new SessionError('An unexpected error occurred');
    }
  }
};
```

## 🐍 Python Standards

### Service Layer Pattern
```python
# ✅ GOOD: Clean service architecture
from abc import ABC, abstractmethod
from typing import List, Optional
from libs.shared_types.python import SessionTypes

class SessionRepositoryInterface(ABC):
    @abstractmethod
    async def get_by_id(self, session_id: str) -> Optional[Session]:
        pass

class SessionService:
    def __init__(self, session_repo: SessionRepositoryInterface):
        self.session_repo = session_repo
    
    async def get_session(self, session_id: str) -> SessionTypes.SessionResponse:
        session = await self.session_repo.get_by_id(session_id)
        if not session:
            raise SessionNotFoundError(f"Session {session_id} not found")
        return SessionTypes.SessionResponse.from_orm(session)
```

### FastAPI Route Structure
```python
# ✅ GOOD: Proper FastAPI route
from fastapi import APIRouter, Depends, HTTPException
from libs.shared_types.python import SessionTypes

router = APIRouter(prefix="/sessions", tags=["sessions"])

@router.get("/{session_id}", response_model=SessionTypes.SessionResponse)
async def get_session(
    session_id: str,
    session_service: SessionService = Depends(get_session_service),
    current_user: User = Depends(get_current_user)
):
    """Get session by ID with proper error handling."""
    try:
        return await session_service.get_session(session_id)
    except SessionNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in get_session: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
```

### Database Model Standards
```python
# ✅ GOOD: SQLAlchemy model with proper relationships
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String(300), nullable=False)
    team_id = Column(String, ForeignKey("teams.id"), nullable=False)
    status = Column(String(50), default="recording", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    team = relationship("Team", back_populates="sessions")
    video_files = relationship("VideoFile", back_populates="session", cascade="all, delete")
    
    def __repr__(self):
        return f"<Session(id='{self.id}', name='{self.name}')>"
```

## 🧪 Testing Standards

### Frontend Testing
```typescript
// ✅ GOOD: Comprehensive component test
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { VideoPlayer } from './VideoPlayer';
import { SessionProvider } from '../contexts/SessionContext';

const mockSession = {
  id: '123',
  name: 'Test Session',
  status: 'completed'
};

describe('VideoPlayer', () => {
  const renderWithContext = (props = {}) => {
    return render(
      <SessionProvider>
        <VideoPlayer sessionId="123" {...props} />
      </SessionProvider>
    );
  };

  test('should display video player controls', async () => {
    renderWithContext();
    
    await waitFor(() => {
      expect(screen.getByRole('button', { name: /play/i })).toBeInTheDocument();
      expect(screen.getByRole('slider', { name: /volume/i })).toBeInTheDocument();
    });
  });

  test('should handle play/pause interaction', async () => {
    const mockPlay = jest.fn();
    renderWithContext({ onPlay: mockPlay });
    
    const playButton = screen.getByRole('button', { name: /play/i });
    fireEvent.click(playButton);
    
    await waitFor(() => {
      expect(mockPlay).toHaveBeenCalledTimes(1);
    });
  });
});
```

### Backend Testing
```python
# ✅ GOOD: Comprehensive service test
import pytest
from unittest.mock import AsyncMock, MagicMock
from services.session_service import SessionService
from models.session import Session
from exceptions import SessionNotFoundError

class TestSessionService:
    @pytest.fixture
    def mock_session_repo(self):
        return AsyncMock()
    
    @pytest.fixture
    def session_service(self, mock_session_repo):
        return SessionService(session_repo=mock_session_repo)
    
    @pytest.mark.asyncio
    async def test_get_session_success(self, session_service, mock_session_repo):
        # Arrange
        mock_session = Session(id="123", name="Test Session")
        mock_session_repo.get_by_id.return_value = mock_session
        
        # Act
        result = await session_service.get_session("123")
        
        # Assert
        assert result.id == "123"
        assert result.name == "Test Session"
        mock_session_repo.get_by_id.assert_called_once_with("123")
    
    @pytest.mark.asyncio
    async def test_get_session_not_found(self, session_service, mock_session_repo):
        # Arrange
        mock_session_repo.get_by_id.return_value = None
        
        # Act & Assert
        with pytest.raises(SessionNotFoundError, match="Session 123 not found"):
            await session_service.get_session("123")
```

## 🎨 Code Formatting

### Prettier Configuration (`.prettierrc`)
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

### ESLint Rules (`.eslintrc.js`)
```javascript
module.exports = {
  extends: [
    '@nx/eslint-plugin-nx/typescript',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended'
  ],
  rules: {
    '@typescript-eslint/explicit-function-return-type': 'error',
    '@typescript-eslint/no-unused-vars': 'error',
    '@typescript-eslint/no-explicit-any': 'error',
    'react-hooks/exhaustive-deps': 'error'
  }
};
```

### Python Formatting (Black + Ruff)
```toml
[tool.black]
line-length = 100
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # Exclude migrations
  migrations
)/
'''

[tool.ruff]
select = ["E", "W", "F", "I", "N", "B", "A", "S", "T", "D"]
ignore = ["D100", "D101", "D102", "D103", "D104", "D105"]
line-length = 100
target-version = "py311"
```

## 🔒 Security Standards

### Frontend Security
```typescript
// ✅ GOOD: Secure token storage
const authService = {
  storeTokens: (accessToken: string, refreshToken: string): void => {
    // Use httpOnly cookies for production, localStorage for development
    if (process.env.NODE_ENV === 'production') {
      // Tokens handled by httpOnly cookies set by backend
      return;
    }
    localStorage.setItem('accessToken', accessToken);
    localStorage.setItem('refreshToken', refreshToken);
  },
  
  // ✅ GOOD: Sanitize user input
  sanitizeInput: (input: string): string => {
    return DOMPurify.sanitize(input);
  }
};
```

### Backend Security
```python
# ✅ GOOD: Input validation and sanitization
from pydantic import BaseModel, validator
from fastapi import HTTPException

class SessionCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None
    
    @validator('name')
    def validate_name(cls, v):
        if not v or len(v.strip()) == 0:
            raise ValueError('Session name cannot be empty')
        if len(v) > 300:
            raise ValueError('Session name too long')
        return v.strip()
    
    @validator('description')
    def validate_description(cls, v):
        if v and len(v) > 1000:
            raise ValueError('Description too long')
        return v.strip() if v else v

# ✅ GOOD: Secure password hashing
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AuthService:
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
```

## 📊 Performance Standards

### Frontend Performance
```typescript
// ✅ GOOD: Optimized component rendering
import { memo, useMemo, useCallback } from 'react';

interface VideoListProps {
  sessions: Session[];
  onSessionSelect: (session: Session) => void;
}

const VideoList: React.FC<VideoListProps> = memo(({ sessions, onSessionSelect }) => {
  const sortedSessions = useMemo(() => {
    return sessions.sort((a, b) => 
      new Date(b.created_at).getTime() - new Date(a.created_at).getTime()
    );
  }, [sessions]);
  
  const handleSessionClick = useCallback((session: Session) => {
    onSessionSelect(session);
  }, [onSessionSelect]);
  
  return (
    <div>
      {sortedSessions.map(session => (
        <SessionCard 
          key={session.id} 
          session={session} 
          onClick={handleSessionClick}
        />
      ))}
    </div>
  );
});
```

### Backend Performance
```python
# ✅ GOOD: Efficient database queries
from sqlalchemy.orm import selectinload

class SessionRepository:
    async def get_sessions_with_video_files(self, team_id: str, limit: int = 20):
        """Efficient query with eager loading to prevent N+1 queries."""
        query = (
            select(Session)
            .options(selectinload(Session.video_files))
            .where(Session.team_id == team_id)
            .order_by(Session.created_at.desc())
            .limit(limit)
        )
        result = await self.db.execute(query)
        return result.scalars().all()
```

## 🚀 Pre-commit Hooks

### Husky Configuration (`.husky/pre-commit`)
```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# Run linting and formatting
npm run lint:fix
npm run format

# Run type checking
npm run type-check

# Run tests for changed files
npm run test:changed

# Python formatting and linting
ruff check --fix .
black .
mypy .

# Run Python tests
pytest -x
```

These coding standards ensure consistent, maintainable, and secure code across the entire Trackball fullstack application. All AI agents must follow these rules without exception.