# API Specification

## Overview

RESTful API specification for Trackball video analysis system built with FastAPI. Includes authentication, video processing, AI tracking, and user management endpoints.

**Base URL**: `https://api.trackball.com/v1`  
**Authentication**: JWT Bearer tokens  
**API Version**: v1.0.0

## Authentication Endpoints

### POST /auth/login
Login user and receive JWT token.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response (200):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "email": "user@example.com",
    "username": "analyst1",
    "role": "analyst"
  }
}
```

### POST /auth/refresh
Refresh access token using refresh token.

**Headers:** `Authorization: Bearer <refresh_token>`

**Response (200):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "expires_in": 3600
}
```

### POST /auth/logout
Logout and invalidate tokens.

**Headers:** `Authorization: Bearer <access_token>`

**Response (204):** No content

## User Management

### GET /users/me
Get current user profile.

**Headers:** `Authorization: Bearer <access_token>`

**Response (200):**
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "username": "analyst1",
  "first_name": "John",
  "last_name": "Doe",
  "role": "analyst",
  "teams": [
    {
      "id": "team-uuid",
      "name": "FC Barcelona",
      "role": "member"
    }
  ],
  "created_at": "2024-01-15T10:30:00Z"
}
```

### PUT /users/me
Update current user profile.

**Request Body:**
```json
{
  "first_name": "John",
  "last_name": "Smith",
  "username": "newusername"
}
```

## Team Management

### GET /teams
List user's teams.

**Response (200):**
```json
{
  "teams": [
    {
      "id": "team-uuid",
      "name": "FC Barcelona",
      "description": "First team analysis",
      "role": "admin",
      "member_count": 5,
      "session_count": 12,
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1
}
```

### POST /teams
Create new team.

**Request Body:**
```json
{
  "name": "Real Madrid",
  "description": "Analysis team for Real Madrid"
}
```

### GET /teams/{team_id}/members
List team members.

**Response (200):**
```json
{
  "members": [
    {
      "id": "user-uuid",
      "username": "coach1",
      "email": "coach@team.com",
      "role": "admin",
      "joined_at": "2024-01-01T00:00:00Z"
    }
  ],
  "total": 1
}
```

## Video Session Management

### GET /teams/{team_id}/sessions
List video sessions for a team.

**Query Parameters:**
- `limit` (optional): Number of results (default: 20, max: 100)
- `offset` (optional): Offset for pagination (default: 0)
- `status` (optional): Filter by status (`recording`, `processing`, `completed`, `failed`)
- `match_id` (optional): Filter by match ID

**Response (200):**
```json
{
  "sessions": [
    {
      "id": "session-uuid",
      "name": "Training Session - Jan 15",
      "match": {
        "id": "match-uuid",
        "name": "vs Real Madrid",
        "match_date": "2024-01-15"
      },
      "status": "completed",
      "duration_seconds": 5400,
      "camera_count": 2,
      "recording_start": "2024-01-15T14:00:00Z",
      "recording_end": "2024-01-15T15:30:00Z",
      "created_by": "user-uuid",
      "created_at": "2024-01-15T14:00:00Z",
      "processing_progress": 100
    }
  ],
  "total": 15,
  "has_next": true
}
```

### POST /teams/{team_id}/sessions
Create new video session.

**Request Body:**
```json
{
  "name": "Training Session - Jan 20",
  "match_id": "match-uuid-optional",
  "camera_count": 2,
  "recording_start": "2024-01-20T14:00:00Z"
}
```

### GET /sessions/{session_id}
Get session details.

**Response (200):**
```json
{
  "id": "session-uuid",
  "name": "Training Session - Jan 15",
  "team_id": "team-uuid",
  "match": {
    "id": "match-uuid",
    "name": "vs Real Madrid",
    "opponent": "Real Madrid",
    "match_date": "2024-01-15",
    "venue": "Camp Nou"
  },
  "status": "completed",
  "duration_seconds": 5400,
  "camera_count": 2,
  "recording_start": "2024-01-15T14:00:00Z",
  "recording_end": "2024-01-15T15:30:00Z",
  "video_files": [
    {
      "id": "video-file-uuid",
      "camera_number": 1,
      "file_path": "sessions/session-uuid/camera1.mp4",
      "file_size_bytes": 2147483648,
      "duration_seconds": 5400,
      "resolution": "3840x2160",
      "fps": 30.0,
      "codec": "h264"
    },
    {
      "id": "video-file-uuid-2",
      "camera_number": 2,
      "file_path": "sessions/session-uuid/camera2.mp4",
      "file_size_bytes": 2147483648,
      "duration_seconds": 5400,
      "resolution": "3840x2160",
      "fps": 30.0,
      "codec": "h264"
    }
  ],
  "processed_videos": [
    {
      "id": "processed-video-uuid",
      "video_type": "synchronized",
      "file_path": "sessions/session-uuid/synchronized.mp4",
      "file_size_bytes": 1073741824,
      "resolution": "3840x2160",
      "fps": 30.0
    }
  ],
  "created_by": "user-uuid",
  "created_at": "2024-01-15T14:00:00Z"
}
```

## Video Processing

### POST /sessions/{session_id}/process
Start video processing pipeline.

**Request Body:**
```json
{
  "pipeline": ["sync", "stitch", "tracking"],
  "options": {
    "sync_method": "timestamp", // timestamp, visual_patterns
    "stitch_quality": "high",   // low, medium, high
    "ai_model": "yolov8n"       // yolov8n, yolov8s, yolov8m
  }
}
```

**Response (202):**
```json
{
  "job_id": "job-uuid",
  "status": "pending",
  "estimated_duration_minutes": 12
}
```

### GET /sessions/{session_id}/processing-status
Get processing status for session.

**Response (200):**
```json
{
  "session_id": "session-uuid",
  "overall_status": "processing",
  "overall_progress": 45.5,
  "jobs": [
    {
      "id": "job-uuid-1",
      "job_type": "sync",
      "status": "completed",
      "progress": 100.0,
      "started_at": "2024-01-15T15:35:00Z",
      "completed_at": "2024-01-15T15:37:00Z"
    },
    {
      "id": "job-uuid-2",
      "job_type": "stitch",
      "status": "running",
      "progress": 67.3,
      "started_at": "2024-01-15T15:37:00Z",
      "estimated_completion": "2024-01-15T15:42:00Z"
    },
    {
      "id": "job-uuid-3",
      "job_type": "tracking",
      "status": "pending",
      "progress": 0.0
    }
  ]
}
```

## AI Tracking and Analysis

### GET /sessions/{session_id}/tracking
Get AI tracking results.

**Query Parameters:**
- `object_type` (optional): Filter by type (`ball`, `player`, `referee`)
- `start_time` (optional): Start time in seconds
- `end_time` (optional): End time in seconds
- `confidence_min` (optional): Minimum confidence threshold (0-1)

**Response (200):**
```json
{
  "session_id": "session-uuid",
  "tracking_session_id": "tracking-uuid",
  "ai_model_version": "yolov8n-1.0",
  "total_frames": 162000,
  "processed_frames": 162000,
  "tracks": [
    {
      "id": "track-uuid",
      "object_type": "ball",
      "track_id": 1,
      "start_frame": 100,
      "end_frame": 5000,
      "start_time": 3.33,
      "end_time": 166.67,
      "trajectory": [
        {
          "frame": 100,
          "timestamp": 3.33,
          "x": 1920,
          "y": 1080,
          "confidence": 0.95
        }
      ],
      "metadata": {
        "avg_confidence": 0.87,
        "track_length": 4900
      }
    }
  ],
  "events": [
    {
      "id": "event-uuid",
      "event_type": "goal",
      "timestamp_seconds": 1245.5,
      "frame_number": 37365,
      "confidence": 0.92,
      "participants": [1, 5, 8], // track IDs
      "metadata": {
        "goal_location": {"x": 3700, "y": 1000},
        "shot_origin": {"x": 2800, "y": 1200}
      },
      "verified": false
    }
  ]
}
```

### POST /sessions/{session_id}/events/{event_id}/verify
Manually verify AI-detected event.

**Request Body:**
```json
{
  "verified": true,
  "notes": "Confirmed goal at 20:45"
}
```

## Video Clips and Annotations

### GET /sessions/{session_id}/clips
List video clips for session.

**Response (200):**
```json
{
  "clips": [
    {
      "id": "clip-uuid",
      "name": "Goal Sequence",
      "description": "Build-up play leading to goal",
      "start_time": 1240.0,
      "end_time": 1250.0,
      "duration": 10.0,
      "tags": "goal,attack,buildup",
      "created_by": "user-uuid",
      "created_at": "2024-01-15T16:30:00Z",
      "thumbnail_url": "https://cdn.trackball.com/clips/clip-uuid/thumbnail.jpg"
    }
  ]
}
```

### POST /sessions/{session_id}/clips
Create new video clip.

**Request Body:**
```json
{
  "name": "Tactical Play",
  "description": "Interesting tactical movement",
  "start_time": 1800.5,
  "end_time": 1815.2,
  "tags": "tactics,midfield,pressing"
}
```

### GET /sessions/{session_id}/annotations
Get annotations for session.

**Query Parameters:**
- `start_time` (optional): Filter annotations after timestamp
- `end_time` (optional): Filter annotations before timestamp
- `type` (optional): Filter by annotation type

**Response (200):**
```json
{
  "annotations": [
    {
      "id": "annotation-uuid",
      "timestamp_seconds": 1245.0,
      "annotation_type": "text",
      "content": {
        "text": "Excellent through ball by player #10",
        "color": "#ff0000"
      },
      "position": {"x": 2800, "y": 1200},
      "created_by": "user-uuid",
      "created_at": "2024-01-15T16:25:00Z"
    },
    {
      "id": "annotation-uuid-2",
      "timestamp_seconds": 1247.5,
      "annotation_type": "drawing",
      "content": {
        "type": "arrow",
        "start": {"x": 2800, "y": 1200},
        "end": {"x": 3200, "y": 800},
        "color": "#00ff00",
        "width": 3
      },
      "created_by": "user-uuid",
      "created_at": "2024-01-15T16:26:00Z"
    }
  ]
}
```

## Export and Analytics

### POST /sessions/{session_id}/export
Export session data and clips.

**Request Body:**
```json
{
  "export_type": "full", // full, clips_only, data_only
  "format": "zip",       // zip, json, csv
  "include": {
    "raw_video": false,
    "processed_video": true,
    "clips": true,
    "tracking_data": true,
    "annotations": true,
    "events": true
  },
  "filters": {
    "start_time": 0,
    "end_time": 5400,
    "event_types": ["goal", "shot"]
  }
}
```

**Response (202):**
```json
{
  "export_id": "export-uuid",
  "status": "pending",
  "estimated_size_mb": 2048,
  "estimated_duration_minutes": 5
}
```

### GET /exports/{export_id}
Get export status and download link.

**Response (200):**
```json
{
  "id": "export-uuid",
  "status": "completed",
  "progress": 100.0,
  "file_size_bytes": 2147483648,
  "download_url": "https://exports.trackball.com/exports/export-uuid/download",
  "expires_at": "2024-01-22T16:00:00Z",
  "created_at": "2024-01-15T16:45:00Z",
  "completed_at": "2024-01-15T16:50:00Z"
}
```

## WebSocket Events

### Connection
Connect to WebSocket for real-time updates.

**URL:** `wss://api.trackball.com/v1/ws`  
**Authentication:** Include JWT token as query parameter: `?token=<access_token>`

### Event Types

#### Processing Updates
```json
{
  "event_type": "processing_update",
  "session_id": "session-uuid",
  "job_id": "job-uuid",
  "job_type": "tracking",
  "status": "running",
  "progress": 73.5,
  "estimated_completion": "2024-01-15T15:42:00Z"
}
```

#### Export Ready
```json
{
  "event_type": "export_ready",
  "export_id": "export-uuid",
  "download_url": "https://exports.trackball.com/exports/export-uuid/download",
  "file_size_bytes": 1073741824
}
```

#### New Event Detection
```json
{
  "event_type": "ai_event_detected",
  "session_id": "session-uuid",
  "event": {
    "id": "event-uuid",
    "event_type": "goal",
    "timestamp_seconds": 1245.5,
    "confidence": 0.92
  }
}
```

## Error Responses

All error responses follow this format:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request data is invalid",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    },
    "timestamp": "2024-01-15T16:30:00Z",
    "request_id": "req-12345"
  }
}
```

### Common Error Codes
- `UNAUTHORIZED` (401): Invalid or missing authentication
- `FORBIDDEN` (403): Insufficient permissions
- `NOT_FOUND` (404): Resource not found
- `VALIDATION_ERROR` (422): Invalid request data
- `RATE_LIMITED` (429): Too many requests
- `INTERNAL_ERROR` (500): Server error
- `SERVICE_UNAVAILABLE` (503): Processing service unavailable

## Rate Limits
- Authentication endpoints: 10 requests/minute
- Standard API endpoints: 100 requests/minute
- Video upload endpoints: 5 requests/minute
- Export endpoints: 3 requests/minute