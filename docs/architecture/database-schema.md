# Database Schema

## Overview

PostgreSQL database schema for the Trackball video analysis system. Designed for high-performance video metadata storage, user management, and AI tracking data.

## Core Tables

### Users and Authentication

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    role VARCHAR(50) NOT NULL DEFAULT 'analyst', -- admin, coach, analyst
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE
);

-- Teams table
CREATE TABLE teams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(200) NOT NULL,
    description TEXT,
    owner_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Team memberships
CREATE TABLE team_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL DEFAULT 'member', -- owner, admin, member
    joined_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(team_id, user_id)
);
```

### Video and Session Management

```sql
-- Matches/Games
CREATE TABLE matches (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    name VARCHAR(300) NOT NULL,
    opponent VARCHAR(200),
    match_date DATE,
    venue VARCHAR(200),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Recording sessions
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    match_id UUID REFERENCES matches(id) ON DELETE SET NULL,
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    name VARCHAR(300) NOT NULL,
    duration_seconds INTEGER,
    camera_count INTEGER DEFAULT 2,
    recording_start TIMESTAMP WITH TIME ZONE,
    recording_end TIMESTAMP WITH TIME ZONE,
    status VARCHAR(50) DEFAULT 'recording', -- recording, processing, completed, failed
    created_by UUID NOT NULL REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Raw video files from cameras
CREATE TABLE video_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    camera_number INTEGER NOT NULL, -- 1 or 2
    file_path VARCHAR(500) NOT NULL, -- S3 key
    file_size_bytes BIGINT,
    duration_seconds DECIMAL(10,3),
    resolution VARCHAR(20), -- "3840x2160"
    fps DECIMAL(5,2),
    codec VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(session_id, camera_number)
);
```

### Video Processing Pipeline

```sql
-- Processing jobs
CREATE TABLE processing_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    job_type VARCHAR(50) NOT NULL, -- sync, stitch, tracking, export
    status VARCHAR(50) DEFAULT 'pending', -- pending, running, completed, failed
    progress DECIMAL(5,2) DEFAULT 0, -- percentage 0-100
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    error_message TEXT,
    config JSONB, -- job-specific configuration
    result JSONB, -- job results and metadata
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Processed video outputs
CREATE TABLE processed_videos (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    video_type VARCHAR(50) NOT NULL, -- synchronized, stitched, individual
    file_path VARCHAR(500) NOT NULL, -- S3 key
    file_size_bytes BIGINT,
    duration_seconds DECIMAL(10,3),
    resolution VARCHAR(20),
    fps DECIMAL(5,2),
    processing_job_id UUID REFERENCES processing_jobs(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### AI Tracking and Analysis

```sql
-- AI tracking data
CREATE TABLE tracking_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    processed_video_id UUID NOT NULL REFERENCES processed_videos(id) ON DELETE CASCADE,
    ai_model_version VARCHAR(100),
    tracking_status VARCHAR(50) DEFAULT 'pending', -- pending, processing, completed, failed
    total_frames INTEGER,
    processed_frames INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    completed_at TIMESTAMP WITH TIME ZONE
);

-- Object detections per frame
CREATE TABLE detections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tracking_session_id UUID NOT NULL REFERENCES tracking_sessions(id) ON DELETE CASCADE,
    frame_number INTEGER NOT NULL,
    timestamp_seconds DECIMAL(10,3) NOT NULL,
    object_type VARCHAR(50) NOT NULL, -- ball, player, referee
    confidence DECIMAL(5,4) NOT NULL, -- 0-1
    bbox_x INTEGER NOT NULL, -- bounding box coordinates
    bbox_y INTEGER NOT NULL,
    bbox_width INTEGER NOT NULL,
    bbox_height INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Object tracks (connected detections)
CREATE TABLE tracks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tracking_session_id UUID NOT NULL REFERENCES tracking_sessions(id) ON DELETE CASCADE,
    object_type VARCHAR(50) NOT NULL,
    track_id INTEGER NOT NULL, -- unique within session
    start_frame INTEGER NOT NULL,
    end_frame INTEGER NOT NULL,
    start_time DECIMAL(10,3) NOT NULL,
    end_time DECIMAL(10,3) NOT NULL,
    trajectory JSONB, -- array of {frame, x, y, confidence}
    metadata JSONB, -- additional tracking info
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(tracking_session_id, object_type, track_id)
);

-- Game events detected by AI
CREATE TABLE game_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tracking_session_id UUID NOT NULL REFERENCES tracking_sessions(id) ON DELETE CASCADE,
    event_type VARCHAR(50) NOT NULL, -- goal, pass, shot, tackle
    timestamp_seconds DECIMAL(10,3) NOT NULL,
    frame_number INTEGER NOT NULL,
    confidence DECIMAL(5,4) NOT NULL,
    participants JSONB, -- track IDs involved in event
    metadata JSONB, -- event-specific data
    verified BOOLEAN DEFAULT false, -- manually verified by user
    created_by UUID REFERENCES users(id), -- user who verified
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### User Content and Annotations

```sql
-- Video clips created by users
CREATE TABLE clips (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    processed_video_id UUID NOT NULL REFERENCES processed_videos(id) ON DELETE CASCADE,
    created_by UUID NOT NULL REFERENCES users(id),
    name VARCHAR(300) NOT NULL,
    description TEXT,
    start_time DECIMAL(10,3) NOT NULL,
    end_time DECIMAL(10,3) NOT NULL,
    tags VARCHAR(500), -- comma-separated tags
    is_public BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- User annotations on videos
CREATE TABLE annotations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    clip_id UUID REFERENCES clips(id) ON DELETE CASCADE, -- null if on full video
    created_by UUID NOT NULL REFERENCES users(id),
    timestamp_seconds DECIMAL(10,3) NOT NULL,
    annotation_type VARCHAR(50) NOT NULL, -- text, drawing, measurement
    content JSONB NOT NULL, -- annotation data
    position JSONB, -- x,y coordinates if applicable
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### Licensing and Usage

```sql
-- License tiers
CREATE TABLE license_tiers (
    id VARCHAR(50) PRIMARY KEY, -- starter, pro, premium
    name VARCHAR(100) NOT NULL,
    max_teams INTEGER,
    max_storage_gb INTEGER,
    max_users_per_team INTEGER,
    features JSONB, -- array of enabled features
    price_monthly DECIMAL(8,2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Team licenses
CREATE TABLE team_licenses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    team_id UUID NOT NULL REFERENCES teams(id) ON DELETE CASCADE,
    tier_id VARCHAR(50) NOT NULL REFERENCES license_tiers(id),
    starts_at TIMESTAMP WITH TIME ZONE NOT NULL,
    expires_at TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT true,
    usage_limits JSONB, -- current usage tracking
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

## Indexes for Performance

```sql
-- User and team lookups
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_team_members_team_id ON team_members(team_id);
CREATE INDEX idx_team_members_user_id ON team_members(user_id);

-- Video and session queries
CREATE INDEX idx_sessions_team_id ON sessions(team_id);
CREATE INDEX idx_sessions_match_id ON sessions(match_id);
CREATE INDEX idx_sessions_created_at ON sessions(created_at DESC);
CREATE INDEX idx_video_files_session_id ON video_files(session_id);

-- Processing pipeline
CREATE INDEX idx_processing_jobs_session_id ON processing_jobs(session_id);
CREATE INDEX idx_processing_jobs_status ON processing_jobs(status, created_at);
CREATE INDEX idx_processed_videos_session_id ON processed_videos(session_id);

-- AI tracking performance
CREATE INDEX idx_tracking_sessions_session_id ON tracking_sessions(session_id);
CREATE INDEX idx_detections_tracking_session ON detections(tracking_session_id, frame_number);
CREATE INDEX idx_detections_timestamp ON detections(timestamp_seconds);
CREATE INDEX idx_tracks_session_type ON tracks(tracking_session_id, object_type);
CREATE INDEX idx_game_events_session_time ON game_events(tracking_session_id, timestamp_seconds);

-- User content
CREATE INDEX idx_clips_session_id ON clips(session_id);
CREATE INDEX idx_clips_created_by ON clips(created_by);
CREATE INDEX idx_annotations_session_id ON annotations(session_id);
CREATE INDEX idx_annotations_timestamp ON annotations(timestamp_seconds);

-- Licensing
CREATE INDEX idx_team_licenses_team_id ON team_licenses(team_id);
CREATE INDEX idx_team_licenses_active ON team_licenses(is_active, expires_at);
```

## Data Relationships

### Key Relationships
- **Teams** own **Sessions** and **Matches**
- **Sessions** contain **Video Files** and generate **Processed Videos**
- **Processing Jobs** transform raw videos into processed outputs
- **Tracking Sessions** analyze **Processed Videos** to generate **Detections** and **Tracks**
- **Game Events** are extracted from **Tracking Sessions**
- **Users** create **Clips** and **Annotations** on **Sessions**
- **Team Licenses** control feature access and usage limits

### Data Flow
1. **Raw Video** → Video Files (S3 storage + metadata)
2. **Processing** → Processed Videos (synchronized, stitched)
3. **AI Analysis** → Detections → Tracks → Game Events
4. **User Interaction** → Clips + Annotations
5. **Export** → Generated content for external use

## Performance Considerations

### Time-Series Optimization
- **Detections** table partitioned by `tracking_session_id` for large datasets
- **Trajectory data** stored as JSONB for flexible querying
- **Composite indexes** on time-based queries

### Storage Efficiency
- **File paths** point to S3, not database BLOBs
- **JSONB** for flexible metadata without schema changes
- **UUIDs** for distributed system compatibility

### Scaling Strategy
- **Read replicas** for analytics queries
- **Connection pooling** for high concurrent access
- **Materialized views** for complex reporting queries