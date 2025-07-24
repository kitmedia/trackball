# Story 3.4: Clip Creation and Management

## Status
🟡 **PENDING** - Comprehensive clip creation and management system with frame-accurate editing, metadata management, and export capabilities

## Story
**As a** coach,
**I want** to create and export video clips with user-defined start/end points,
**so that** I can share specific moments and build tactical presentations.

## Acceptance Criteria
1. Intuitive clip creation interface with timeline selection and preview ⏳
2. Clip trimming controls with frame-accurate start/end point adjustment ⏳
3. Multiple export formats (MP4, MOV) with quality and resolution options ⏳
4. Clip metadata management (title, description, tags, category) ⏳
5. Clip library interface with grid view, search, and filtering capabilities ⏳
6. Batch clip export functionality with progress tracking ⏳
7. Clip sharing capabilities with team members and external stakeholders ⏳
8. Integration with tracking overlays and annotations in exported clips ⏳

## Tasks / Subtasks

- [ ] **Task 3.4.1: Clip Creation Interface Development** ⏳
  - [ ] Implement timeline-based clip selection with drag handles for start/end points
  - [ ] Create real-time clip preview with playback controls and duration display
  - [ ] Add visual feedback for selection boundaries with overlay highlights
  - [ ] Implement keyboard shortcuts for precise clip boundary adjustment
  - [ ] Create clip creation modal with metadata input fields and preview
  - [ ] Add validation for minimum/maximum clip duration limits
  - [ ] Implement undo/redo functionality for clip creation operations
  - [ ] Create quick clip creation from event markers and annotations
  - **Estimate:** 32 hours | **Priority:** Critical | **Dependencies:** Story 3.3 (timeline interface)
  - **Deliverables:**
    - Timeline-based clip selection interface with drag controls
    - Real-time preview with accurate duration display
    - Clip creation modal with metadata input capabilities
    - Keyboard shortcut support for precise editing

- [ ] **Task 3.4.2: Frame-Accurate Trimming Controls** ⏳
  - [ ] Implement frame-by-frame navigation with arrow key controls
  - [ ] Create precise trimming interface with frame number display
  - [ ] Add zoom controls for timeline precision editing
  - [ ] Implement snap-to-frame functionality for exact positioning
  - [ ] Create visual frame boundaries with thumbnail previews
  - [ ] Add trim preview with before/after comparison view
  - [ ] Implement batch trimming for multiple clips simultaneously
  - [ ] Create trimming history with rollback capabilities
  - **Estimate:** 28 hours | **Priority:** Critical | **Dependencies:** Task 3.4.1
  - **Deliverables:**
    - Frame-accurate trimming with arrow key navigation
    - Zoom controls for precision timeline editing
    - Snap-to-frame functionality with visual feedback
    - Batch trimming capabilities with progress tracking

- [ ] **Task 3.4.3: Multi-Format Export System** ⏳
  - [ ] Implement MP4 export with H.264/H.265 codec options
  - [ ] Create MOV export with ProRes codec for professional workflows
  - [ ] Add WebM export for web-optimized sharing and streaming
  - [ ] Implement resolution options (720p, 1080p, 4K) with aspect ratio preservation
  - [ ] Create quality presets (low, medium, high, ultra) with bitrate optimization
  - [ ] Add custom export settings with advanced codec parameter control
  - [ ] Implement export queue management with priority scheduling
  - [ ] Create export progress tracking with estimated completion times
  - **Estimate:** 35 hours | **Priority:** Critical | **Dependencies:** Task 3.4.2
  - **Deliverables:**
    - Multi-format export (MP4, MOV, WebM) with codec options
    - Resolution and quality preset system
    - Export queue management with progress tracking
    - Custom export settings for advanced users

- [ ] **Task 3.4.4: Clip Metadata Management System** ⏳
  - [ ] Create comprehensive metadata schema with title, description, and tags
  - [ ] Implement category system with predefined and custom categories
  - [ ] Add automatic metadata extraction from video content and AI analysis
  - [ ] Create batch metadata editing for multiple clips simultaneously
  - [ ] Implement metadata templates for consistent clip organization
  - [ ] Add metadata validation with required field enforcement
  - [ ] Create metadata export/import functionality for external systems
  - [ ] Implement metadata search with full-text search capabilities
  - **Estimate:** 30 hours | **Priority:** High | **Dependencies:** Task 3.4.3
  - **Deliverables:**
    - Comprehensive metadata schema with validation
    - Category system with custom category support
    - Batch metadata editing capabilities
    - Metadata templates and search functionality

- [ ] **Task 3.4.5: Clip Library Interface** ⏳
  - [ ] Create responsive grid view with thumbnail previews and hover playback
  - [ ] Implement list view with detailed metadata and sorting options
  - [ ] Add advanced filtering by date, category, tags, duration, and resolution
  - [ ] Create full-text search across clip metadata and content
  - [ ] Implement sorting options (date, duration, name, size, quality)
  - [ ] Add bulk selection with multi-select operations and actions
  - [ ] Create folder organization system with drag-and-drop management
  - [ ] Implement clip preview modal with playback and quick editing
  - **Estimate:** 33 hours | **Priority:** High | **Dependencies:** Task 3.4.4
  - **Deliverables:**
    - Responsive grid and list view interfaces
    - Advanced filtering and search capabilities
    - Bulk selection with multi-select operations
    - Folder organization with drag-and-drop support

- [ ] **Task 3.4.6: Batch Export Processing** ⏳
  - [ ] Implement queue-based batch export with priority management
  - [ ] Create export job scheduling with optimal resource utilization
  - [ ] Add parallel processing support for multiple simultaneous exports
  - [ ] Implement export progress tracking with individual job status
  - [ ] Create export notification system with completion alerts
  - [ ] Add export history with job details and download links
  - [ ] Implement export retry mechanism for failed jobs
  - [ ] Create export analytics with processing time and success metrics
  - **Estimate:** 25 hours | **Priority:** High | **Dependencies:** Task 3.4.5
  - **Deliverables:**
    - Queue-based batch export system
    - Parallel processing with resource optimization
    - Export progress tracking and notification system
    - Export history and retry mechanisms

- [ ] **Task 3.4.7: Clip Sharing System** ⏳
  - [ ] Implement secure clip sharing with permission-based access control
  - [ ] Create shareable links with expiration dates and view limits
  - [ ] Add team member sharing with role-based access permissions
  - [ ] Implement external stakeholder sharing with guest access
  - [ ] Create sharing analytics with view tracking and engagement metrics
  - [ ] Add sharing notification system with email and in-app alerts
  - [ ] Implement sharing history with audit log and access tracking
  - [ ] Create sharing templates for common distribution scenarios
  - **Estimate:** 28 hours | **Priority:** High | **Dependencies:** Task 3.4.6
  - **Deliverables:**
    - Secure sharing with permission-based access control
    - Shareable links with expiration and view limits
    - Team and external stakeholder sharing capabilities
    - Sharing analytics and notification system

- [ ] **Task 3.4.8: AI Overlay Integration** ⏳
  - [ ] Implement AI tracking overlay preservation in exported clips
  - [ ] Create overlay customization options for export presentation
  - [ ] Add annotation inclusion with customizable visibility settings
  - [ ] Implement overlay rendering optimization for export performance
  - [ ] Create overlay template system for consistent presentation styles
  - [ ] Add overlay animation controls for dynamic presentation effects
  - [ ] Implement overlay export settings with quality and format options
  - [ ] Create overlay preview system for export verification
  - **Estimate:** 30 hours | **Priority:** Medium | **Dependencies:** Task 3.4.7
  - **Deliverables:**
    - AI overlay preservation in exported clips
    - Overlay customization and template system
    - Annotation inclusion with visibility controls
    - Overlay animation and presentation effects

## API Implementation

### Clip Management API

```python
# FastAPI implementation for clip creation and management
from fastapi import FastAPI, HTTPException, Depends, Security, UploadFile, File
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from pydantic import BaseModel
import asyncio
import boto3
import ffmpeg
import json
import uuid

Base = declarative_base()

class VideoClip(Base):
    __tablename__ = "video_clips"
    
    id = Column(String, primary_key=True)
    session_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    tags = Column(JSON)
    category = Column(String)
    start_time = Column(Float, nullable=False)  # seconds
    end_time = Column(Float, nullable=False)    # seconds
    duration = Column(Float, nullable=False)    # seconds
    source_video_path = Column(String, nullable=False)
    output_video_path = Column(String)
    export_status = Column(String, default="pending")  # pending, processing, completed, failed
    export_format = Column(String, default="mp4")
    export_quality = Column(String, default="high")
    export_resolution = Column(String, default="1080p")
    file_size = Column(Integer)  # bytes
    thumbnail_path = Column(String)
    metadata = Column(JSON)
    sharing_settings = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ClipExportJob(Base):
    __tablename__ = "clip_export_jobs"
    
    id = Column(String, primary_key=True)
    clip_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    export_format = Column(String, nullable=False)
    export_quality = Column(String, nullable=False)
    export_resolution = Column(String, nullable=False)
    status = Column(String, default="queued")  # queued, processing, completed, failed
    progress_percentage = Column(Float, default=0.0)
    estimated_completion = Column(DateTime)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    error_message = Column(Text)
    output_path = Column(String)
    file_size = Column(Integer)
    processing_time = Column(Float)  # seconds
    created_at = Column(DateTime, default=datetime.utcnow)

class ClipManager:
    def __init__(self, db_session, s3_client):
        self.db = db_session
        self.s3 = s3_client
        self.export_queue = asyncio.Queue()
        
    async def create_clip(self, clip_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new video clip with metadata"""
        try:
            # Validate clip boundaries
            if clip_data["end_time"] <= clip_data["start_time"]:
                raise HTTPException(status_code=400, detail="End time must be after start time")
            
            duration = clip_data["end_time"] - clip_data["start_time"]
            if duration < 1.0:  # Minimum 1 second
                raise HTTPException(status_code=400, detail="Clip must be at least 1 second long")
            
            # Create clip record
            clip = VideoClip(
                id=f"clip_{uuid.uuid4().hex[:12]}",
                session_id=clip_data["session_id"],
                user_id=clip_data["user_id"],
                title=clip_data["title"],
                description=clip_data.get("description"),
                tags=json.dumps(clip_data.get("tags", [])),
                category=clip_data.get("category"),
                start_time=float(clip_data["start_time"]),
                end_time=float(clip_data["end_time"]),
                duration=duration,
                source_video_path=clip_data["source_video_path"],
                export_format=clip_data.get("format", "mp4"),
                export_quality=clip_data.get("quality", "high"),
                export_resolution=clip_data.get("resolution", "1080p"),
                metadata=json.dumps(clip_data.get("metadata", {})),
                sharing_settings=json.dumps(clip_data.get("sharing_settings", {"public": False}))
            )
            
            self.db.add(clip)
            
            # Generate thumbnail
            thumbnail_path = await self.generate_clip_thumbnail(clip)
            clip.thumbnail_path = thumbnail_path
            
            # Queue for export if requested
            if clip_data.get("auto_export", True):
                export_job = await self.queue_clip_export(clip)
                
            self.db.commit()
            
            return {
                "clip_id": clip.id,
                "title": clip.title,
                "duration": clip.duration,
                "thumbnail_url": f"/api/v1/clips/{clip.id}/thumbnail",
                "export_status": clip.export_status,
                "created_at": clip.created_at.isoformat()
            }
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Clip creation failed: {str(e)}")
    
    async def trim_clip(self, clip_id: str, trim_data: Dict[str, Any]) -> Dict[str, Any]:
        """Trim existing clip with frame-accurate precision"""
        try:
            clip = self.db.query(VideoClip).filter(VideoClip.id == clip_id).first()
            if not clip:
                raise HTTPException(status_code=404, detail="Clip not found")
            
            new_start = float(trim_data["start_time"])
            new_end = float(trim_data["end_time"])
            
            # Validate new boundaries
            if new_end <= new_start:
                raise HTTPException(status_code=400, detail="End time must be after start time")
            
            if new_start < clip.start_time or new_end > clip.end_time:
                raise HTTPException(status_code=400, detail="New boundaries exceed original clip")
            
            # Update clip boundaries
            clip.start_time = new_start
            clip.end_time = new_end
            clip.duration = new_end - new_start
            clip.export_status = "pending"
            clip.updated_at = datetime.utcnow()
            
            # Regenerate thumbnail
            clip.thumbnail_path = await self.generate_clip_thumbnail(clip)
            
            # Queue for re-export
            export_job = await self.queue_clip_export(clip)
            
            self.db.commit()
            
            return {
                "clip_id": clip.id,
                "new_duration": clip.duration,
                "export_job_id": export_job["job_id"],
                "status": "trim_successful"
            }
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Clip trimming failed: {str(e)}")
    
    async def export_clip(self, clip_id: str, export_settings: Dict[str, Any]) -> Dict[str, Any]:
        """Export clip with specified format and quality settings"""
        try:
            clip = self.db.query(VideoClip).filter(VideoClip.id == clip_id).first()
            if not clip:
                raise HTTPException(status_code=404, detail="Clip not found")
            
            # Create export job
            export_job = ClipExportJob(
                id=f"export_{uuid.uuid4().hex[:12]}",
                clip_id=clip.id,
                user_id=clip.user_id,
                export_format=export_settings.get("format", "mp4"),
                export_quality=export_settings.get("quality", "high"),
                export_resolution=export_settings.get("resolution", "1080p")
            )
            
            # Calculate estimated completion time
            export_job.estimated_completion = datetime.utcnow() + timedelta(
                minutes=self.estimate_export_time(clip.duration, export_settings)
            )
            
            self.db.add(export_job)
            self.db.commit()
            
            # Add to export queue
            await self.export_queue.put({
                "job_id": export_job.id,
                "clip_id": clip.id,
                "settings": export_settings
            })
            
            return {
                "export_job_id": export_job.id,
                "estimated_completion": export_job.estimated_completion.isoformat(),
                "queue_position": self.export_queue.qsize(),
                "status": "queued"
            }
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")
    
    async def process_export_queue(self):
        """Background worker to process export queue"""
        while True:
            try:
                # Get next job from queue
                job_data = await self.export_queue.get()
                
                # Get job and clip from database
                job = self.db.query(ClipExportJob).filter(
                    ClipExportJob.id == job_data["job_id"]
                ).first()
                
                clip = self.db.query(VideoClip).filter(
                    VideoClip.id == job_data["clip_id"]
                ).first()
                
                if not job or not clip:
                    continue
                
                # Update job status
                job.status = "processing"
                job.started_at = datetime.utcnow()
                self.db.commit()
                
                # Process export using FFmpeg
                output_path = await self.process_video_export(clip, job_data["settings"])
                
                # Update job completion
                job.status = "completed"
                job.completed_at = datetime.utcnow()
                job.output_path = output_path
                job.processing_time = (job.completed_at - job.started_at).total_seconds()
                job.progress_percentage = 100.0
                
                # Update clip status
                clip.export_status = "completed"
                clip.output_video_path = output_path
                
                self.db.commit()
                
            except Exception as e:
                # Handle export failure
                if 'job' in locals():
                    job.status = "failed" 
                    job.error_message = str(e)
                    job.completed_at = datetime.utcnow()
                    self.db.commit()
    
    async def generate_clip_thumbnail(self, clip: VideoClip) -> str:
        """Generate thumbnail for clip at midpoint"""
        try:
            thumbnail_time = clip.start_time + (clip.duration / 2)
            thumbnail_path = f"thumbnails/{clip.id}_thumb.jpg"
            
            # Use FFmpeg to extract frame
            (
                ffmpeg
                .input(clip.source_video_path, ss=thumbnail_time)
                .output(thumbnail_path, vframes=1, format='image2', vcodec='mjpeg')
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )
            
            # Upload to S3
            await self.upload_to_s3(thumbnail_path, f"thumbnails/{clip.id}_thumb.jpg")
            
            return thumbnail_path
            
        except Exception as e:
            return None
    
    async def process_video_export(self, clip: VideoClip, settings: Dict[str, Any]) -> str:
        """Process video export using FFmpeg"""
        try:
            output_path = f"exports/{clip.id}_{settings['format']}.{settings['format']}"
            
            input_stream = ffmpeg.input(clip.source_video_path, ss=clip.start_time, t=clip.duration)
            
            # Configure output based on settings
            output_args = {
                'format': settings['format'],
                'vcodec': 'libx264' if settings['format'] == 'mp4' else 'libx265',
                'acodec': 'aac',
                'strict': 'experimental'
            }
            
            # Quality settings
            if settings['quality'] == 'low':
                output_args['crf'] = 28
            elif settings['quality'] == 'medium':
                output_args['crf'] = 23
            elif settings['quality'] == 'high':
                output_args['crf'] = 18
            else:  # ultra
                output_args['crf'] = 15
            
            # Resolution settings
            if settings['resolution'] == '720p':
                output_args['s'] = '1280x720'
            elif settings['resolution'] == '1080p':
                output_args['s'] = '1920x1080'
            elif settings['resolution'] == '4K':
                output_args['s'] = '3840x2160'
            
            output_stream = ffmpeg.output(input_stream, output_path, **output_args)
            ffmpeg.run(output_stream, overwrite_output=True)
            
            # Upload to S3
            await self.upload_to_s3(output_path, f"clips/{clip.id}/{output_path}")
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Video export processing failed: {str(e)}")
    
    def estimate_export_time(self, duration: float, settings: Dict[str, Any]) -> int:
        """Estimate export processing time in minutes"""
        base_time = duration / 60  # 1:1 ratio as baseline
        
        # Adjust for quality
        quality_multiplier = {
            'low': 0.5,
            'medium': 1.0,
            'high': 1.5,
            'ultra': 2.0
        }.get(settings.get('quality', 'high'), 1.0)
        
        # Adjust for resolution
        resolution_multiplier = {
            '720p': 0.7,
            '1080p': 1.0,
            '4K': 2.5
        }.get(settings.get('resolution', '1080p'), 1.0)
        
        return max(1, int(base_time * quality_multiplier * resolution_multiplier))

# API Endpoints
app = FastAPI()
security = HTTPBearer()

@app.post("/api/v1/clips")
async def create_clip(
    clip_data: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Create new video clip"""
    # Implementation logic here
    pass

@app.put("/api/v1/clips/{clip_id}/trim")
async def trim_clip(
    clip_id: str,
    trim_data: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Trim existing clip with frame-accurate precision"""
    # Implementation logic here
    pass

@app.post("/api/v1/clips/{clip_id}/export")
async def export_clip(
    clip_id: str,
    export_settings: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Export clip with specified settings"""
    # Implementation logic here
    pass

@app.get("/api/v1/clips")
async def list_clips(
    session_id: Optional[str] = None,
    category: Optional[str] = None,
    tags: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """List clips with filtering and pagination"""
    # Implementation logic here
    pass

@app.get("/api/v1/clips/{clip_id}")
async def get_clip(
    clip_id: str,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get clip details and metadata"""
    # Implementation logic here
    pass

@app.delete("/api/v1/clips/{clip_id}")
async def delete_clip(
    clip_id: str,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Delete clip and associated files"""
    # Implementation logic here
    pass
```

## Frontend Component Architecture

### Clip Creation and Management Interface

```typescript
// React components for clip creation and management
import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  Box, Card, CardContent, Typography, Button, TextField, Chip,
  Dialog, DialogTitle, DialogContent, DialogActions, Grid,
  Select, MenuItem, FormControl, InputLabel, Slider, IconButton,
  List, ListItem, ListItemText, ListItemIcon, Tabs, Tab,
  LinearProgress, Alert, Tooltip, Badge, Menu, MenuList, MenuItem as MenuItemComponent
} from '@mui/material';
import {
  PlayArrow, Pause, Stop, ContentCut, GetApp, Share,
  Delete, Edit, Visibility, FilterList, Search,
  VideoLibrary, Schedule, CheckCircle, Error
} from '@mui/icons-material';
import { useClipStore } from '../stores/clipStore';

interface VideoClip {
  id: string;
  title: string;
  description?: string;
  tags: string[];
  category?: string;
  startTime: number;
  endTime: number;
  duration: number;
  exportStatus: 'pending' | 'processing' | 'completed' | 'failed';
  thumbnailUrl: string;
  createdAt: string;
}

interface ClipCreationData {
  title: string;
  description: string;
  tags: string[];
  category: string;
  startTime: number;
  endTime: number;
  format: string;
  quality: string;
  resolution: string;
}

const ClipCreationManager: React.FC = () => {
  const [activeTab, setActiveTab] = useState(0);
  const [clips, setClips] = useState<VideoClip[]>([]);
  const [showCreateDialog, setShowCreateDialog] = useState(false);
  const [showExportDialog, setShowExportDialog] = useState(false);
  const [selectedClip, setSelectedClip] = useState<VideoClip | null>(null);
  const [clipCreationData, setClipCreationData] = useState<ClipCreationData>({
    title: '',
    description: '',
    tags: [],
    category: '',
    startTime: 0,
    endTime: 0,
    format: 'mp4',
    quality: 'high',
    resolution: '1080p'
  });
  const [isCreating, setIsCreating] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCategory, setFilterCategory] = useState('');
  const [previewTime, setPreviewTime] = useState(0);
  
  const videoRef = useRef<HTMLVideoElement>(null);
  const timelineRef = useRef<HTMLDivElement>(null);
  
  const {
    createClip,
    trimClip,
    exportClip,
    getClips,
    deleteClip,
    shareClip
  } = useClipStore();

  useEffect(() => {
    loadClips();
  }, []);

  const loadClips = async () => {
    try {
      const clipsData = await getClips({
        category: filterCategory || undefined,
        search: searchTerm || undefined
      });
      setClips(clipsData);
    } catch (error) {
      console.error('Failed to load clips:', error);
    }
  };

  const handleCreateClip = async () => {
    try {
      setIsCreating(true);
      await createClip(clipCreationData);
      setShowCreateDialog(false);
      await loadClips();
      resetClipCreationData();
    } catch (error) {
      console.error('Failed to create clip:', error);
    } finally {
      setIsCreating(false);
    }
  };

  const handleTrimClip = async (clipId: string, newStartTime: number, newEndTime: number) => {
    try {
      await trimClip(clipId, {
        start_time: newStartTime,
        end_time: newEndTime
      });
      await loadClips();
    } catch (error) {
      console.error('Failed to trim clip:', error);
    }
  };

  const handleExportClip = async (clipId: string, exportSettings: any) => {
    try {
      await exportClip(clipId, exportSettings);
      setShowExportDialog(false);
      await loadClips();
    } catch (error) {
      console.error('Failed to export clip:', error);
    }
  };

  const resetClipCreationData = () => {
    setClipCreationData({
      title: '',
      description: '',
      tags: [],
      category: '',
      startTime: 0,
      endTime: 0,
      format: 'mp4',
      quality: 'high',
      resolution: '1080p'
    });
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const ClipCreationInterface = () => (
    <Card>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Create New Clip
        </Typography>
        
        <Grid container spacing={3}>
          <Grid item xs={12} md={8}>
            <Box sx={{ position: 'relative', mb: 2 }}>
              <video
                ref={videoRef}
                style={{ width: '100%', height: 'auto' }}
                controls
                onTimeUpdate={(e) => setPreviewTime(e.currentTarget.currentTime)}
              />
              
              {/* Timeline Selection Overlay */}
              <Box
                ref={timelineRef}
                sx={{
                  position: 'absolute',
                  bottom: 40,
                  left: 0,
                  right: 0,
                  height: 20,
                  backgroundColor: 'rgba(0,0,0,0.5)',
                  cursor: 'crosshair'
                }}
              >
                {/* Selection handles and preview */}
                <Box
                  sx={{
                    position: 'absolute',
                    left: `${(clipCreationData.startTime / (videoRef.current?.duration || 1)) * 100}%`,
                    width: `${((clipCreationData.endTime - clipCreationData.startTime) / (videoRef.current?.duration || 1)) * 100}%`,
                    height: '100%',
                    backgroundColor: 'primary.main',
                    opacity: 0.7
                  }}
                />
              </Box>
            </Box>
            
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <TextField
                  label="Start Time (seconds)"
                  type="number"
                  value={clipCreationData.startTime}
                  onChange={(e) => setClipCreationData({
                    ...clipCreationData,
                    startTime: parseFloat(e.target.value) || 0
                  })}
                  fullWidth
                  inputProps={{ min: 0, step: 0.1 }}
                />
              </Grid>
              <Grid item xs={6}>
                <TextField
                  label="End Time (seconds)"
                  type="number"
                  value={clipCreationData.endTime}
                  onChange={(e) => setClipCreationData({
                    ...clipCreationData,
                    endTime: parseFloat(e.target.value) || 0
                  })}
                  fullWidth
                  inputProps={{ min: 0, step: 0.1 }}
                />
              </Grid>
            </Grid>
          </Grid>
          
          <Grid item xs={12} md={4}>
            <TextField
              label="Clip Title"
              value={clipCreationData.title}
              onChange={(e) => setClipCreationData({
                ...clipCreationData,
                title: e.target.value
              })}
              fullWidth
              margin="normal"
              required
            />
            
            <TextField
              label="Description"
              value={clipCreationData.description}
              onChange={(e) => setClipCreationData({
                ...clipCreationData,
                description: e.target.value
              })}
              fullWidth
              multiline
              rows={3}
              margin="normal"
            />
            
            <FormControl fullWidth margin="normal">
              <InputLabel>Category</InputLabel>
              <Select
                value={clipCreationData.category}
                onChange={(e) => setClipCreationData({
                  ...clipCreationData,
                  category: e.target.value
                })}
              >
                <MenuItem value="goal">Goal</MenuItem>
                <MenuItem value="save">Save</MenuItem>
                <MenuItem value="tackle">Tackle</MenuItem>
                <MenuItem value="pass">Pass</MenuItem>
                <MenuItem value="formation">Formation</MenuItem>
                <MenuItem value="other">Other</MenuItem>
              </Select>
            </FormControl>
            
            <Box sx={{ mt: 2 }}>
              <Typography variant="subtitle2" gutterBottom>
                Export Settings
              </Typography>
              
              <FormControl fullWidth size="small" sx={{ mb: 1 }}>
                <InputLabel>Format</InputLabel>
                <Select
                  value={clipCreationData.format}
                  onChange={(e) => setClipCreationData({
                    ...clipCreationData,
                    format: e.target.value
                  })}
                >
                  <MenuItem value="mp4">MP4</MenuItem>
                  <MenuItem value="mov">MOV</MenuItem>
                  <MenuItem value="webm">WebM</MenuItem>
                </Select>
              </FormControl>
              
              <FormControl fullWidth size="small" sx={{ mb: 1 }}>
                <InputLabel>Quality</InputLabel>
                <Select
                  value={clipCreationData.quality}
                  onChange={(e) => setClipCreationData({
                    ...clipCreationData,
                    quality: e.target.value
                  })}
                >
                  <MenuItem value="low">Low</MenuItem>
                  <MenuItem value="medium">Medium</MenuItem>
                  <MenuItem value="high">High</MenuItem>
                  <MenuItem value="ultra">Ultra</MenuItem>
                </Select>
              </FormControl>
              
              <FormControl fullWidth size="small">
                <InputLabel>Resolution</InputLabel>
                <Select
                  value={clipCreationData.resolution}
                  onChange={(e) => setClipCreationData({
                    ...clipCreationData,
                    resolution: e.target.value
                  })}
                >
                  <MenuItem value="720p">720p</MenuItem>
                  <MenuItem value="1080p">1080p</MenuItem>
                  <MenuItem value="4K">4K</MenuItem>
                </Select>
              </FormControl>
            </Box>
          </Grid>
        </Grid>
        
        <Box sx={{ mt: 3, display: 'flex', justifyContent: 'flex-end', gap: 2 }}>
          <Button onClick={() => setShowCreateDialog(false)}>
            Cancel
          </Button>
          <Button
            variant="contained"
            onClick={handleCreateClip}
            disabled={isCreating || !clipCreationData.title}
            startIcon={isCreating ? <LinearProgress size={20} /> : <ContentCut />}
          >
            {isCreating ? 'Creating...' : 'Create Clip'}
          </Button>
        </Box>
      </CardContent>
    </Card>
  );

  const ClipLibrary = () => (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 3 }}>
        <Typography variant="h6">Clip Library</Typography>
        <Button
          variant="contained"
          startIcon={<ContentCut />}
          onClick={() => setShowCreateDialog(true)}
        >
          Create Clip
        </Button>
      </Box>
      
      <Box sx={{ display: 'flex', gap: 2, mb: 3 }}>
        <TextField
          placeholder="Search clips..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          size="small"
          InputProps={{
            startAdornment: <Search />
          }}
        />
        
        <FormControl size="small" sx={{ minWidth: 120 }}>
          <InputLabel>Category</InputLabel>
          <Select
            value={filterCategory}
            onChange={(e) => setFilterCategory(e.target.value)}
          >
            <MenuItem value="">All</MenuItem>
            <MenuItem value="goal">Goals</MenuItem>
            <MenuItem value="save">Saves</MenuItem>
            <MenuItem value="tackle">Tackles</MenuItem>
            <MenuItem value="pass">Passes</MenuItem>
            <MenuItem value="formation">Formations</MenuItem>
          </Select>
        </FormControl>
        
        <Button variant="outlined" onClick={loadClips}>
          Apply Filters
        </Button>
      </Box>
      
      <Grid container spacing={2}>
        {clips.map((clip) => (
          <Grid item xs={12} sm={6} md={4} key={clip.id}>
            <Card>
              <Box sx={{ position: 'relative' }}>
                <img
                  src={clip.thumbnailUrl}
                  alt={clip.title}
                  style={{ width: '100%', height: 200, objectFit: 'cover' }}
                />
                <Box
                  sx={{
                    position: 'absolute',
                    bottom: 8,
                    right: 8,
                    backgroundColor: 'rgba(0,0,0,0.7)',
                    color: 'white',
                    padding: '2px 6px',
                    borderRadius: 1,
                    fontSize: '0.75rem'
                  }}
                >
                  {formatTime(clip.duration)}
                </Box>
                <Box
                  sx={{
                    position: 'absolute',
                    top: 8,
                    right: 8
                  }}
                >
                  {clip.exportStatus === 'completed' && (
                    <CheckCircle color="success" fontSize="small" />
                  )}
                  {clip.exportStatus === 'processing' && (
                    <LinearProgress size={20} />
                  )}
                  {clip.exportStatus === 'failed' && (
                    <Error color="error" fontSize="small" />
                  )}
                </Box>
              </Box>
              
              <CardContent>
                <Typography variant="h6" noWrap>
                  {clip.title}
                </Typography>
                
                <Box sx={{ display: 'flex', gap: 1, mb: 1, flexWrap: 'wrap' }}>
                  {clip.category && (
                    <Chip label={clip.category} size="small" />
                  )}
                  {clip.tags.map((tag, index) => (
                    <Chip key={index} label={tag} size="small" variant="outlined" />
                  ))}
                </Box>
                
                <Typography variant="body2" color="textSecondary" gutterBottom>
                  Created: {new Date(clip.createdAt).toLocaleDateString()}
                </Typography>
                
                <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 2 }}>
                  <IconButton size="small" onClick={() => {/* Handle preview */}}>
                    <Visibility />
                  </IconButton>
                  <IconButton size="small" onClick={() => {/* Handle edit */}}>
                    <Edit />
                  </IconButton>
                  <IconButton size="small" onClick={() => {
                    setSelectedClip(clip);
                    setShowExportDialog(true);
                  }}>
                    <GetApp />
                  </IconButton>
                  <IconButton size="small" onClick={() => shareClip(clip.id)}>
                    <Share />
                  </IconButton>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Clip Creation & Management
      </Typography>
      
      <Tabs value={activeTab} onChange={(_, value) => setActiveTab(value)} sx={{ mb: 3 }}>
        <Tab label="Create Clip" />
        <Tab label="Clip Library" />
        <Tab label="Export Queue" />
      </Tabs>
      
      {activeTab === 0 && <ClipCreationInterface />}
      {activeTab === 1 && <ClipLibrary />}
      {activeTab === 2 && <div>Export Queue Management</div>}
      
      {/* Create Clip Dialog */}
      <Dialog
        open={showCreateDialog}
        onClose={() => setShowCreateDialog(false)}
        maxWidth="lg"
        fullWidth
      >
        <DialogTitle>Create New Clip</DialogTitle>
        <DialogContent>
          <ClipCreationInterface />
        </DialogContent>
      </Dialog>
      
      {/* Export Dialog */}
      <Dialog
        open={showExportDialog}
        onClose={() => setShowExportDialog(false)}
        maxWidth="sm"
        fullWidth
      >
        <DialogTitle>Export Clip</DialogTitle>
        <DialogContent>
          {selectedClip && (
            <Box sx={{ pt: 2 }}>
              <Typography variant="h6" gutterBottom>
                {selectedClip.title}
              </Typography>
              <Typography variant="body2" color="textSecondary" gutterBottom>
                Duration: {formatTime(selectedClip.duration)}
              </Typography>
              {/* Export settings form */}
            </Box>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowExportDialog(false)}>Cancel</Button>
          <Button variant="contained" onClick={() => {
            if (selectedClip) {
              handleExportClip(selectedClip.id, {
                format: 'mp4',
                quality: 'high',
                resolution: '1080p'
              });
            }
          }}>
            Export
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default ClipCreationManager;
```

## Performance Considerations

1. **Video Processing Performance**
   - FFmpeg optimization with hardware acceleration
   - Parallel processing for batch exports
   - Efficient thumbnail generation with caching

2. **UI Responsiveness**
   - Frame-accurate timeline scrubbing with smooth performance
   - Optimized clip preview with lazy loading
   - Efficient grid rendering for large clip libraries

3. **Storage Optimization**
   - Smart compression based on content analysis
   - Automatic cleanup of temporary processing files
   - S3 lifecycle policies for archived clips

## Security

1. **Access Control**
   - User-based clip access with ownership validation
   - Secure sharing with token-based authentication
   - Team-level permissions for clip management

2. **Content Protection**
   - Watermarking for exported clips
   - DRM protection for sensitive content
   - Audit logging for all clip operations

3. **Export Security**
   - Secure temporary file handling
   - Encrypted export queue processing
   - Safe cleanup of processing artifacts

## Testing

```python
# Comprehensive testing for clip management
import pytest
from unittest.mock import Mock, patch, AsyncMock
import tempfile
import os

class TestClipManager:
    
    @pytest.fixture
    def clip_manager(self):
        mock_db = Mock()
        mock_s3 = Mock()
        return ClipManager(mock_db, mock_s3)
    
    @pytest.mark.asyncio
    async def test_clip_creation(self, clip_manager):
        """Test basic clip creation functionality"""
        clip_data = {
            "session_id": "session_123",
            "user_id": "user_456", 
            "title": "Great Goal Sequence",
            "start_time": 120.5,
            "end_time": 135.2,
            "source_video_path": "/path/to/source.mp4",
            "category": "goal"
        }
        
        result = await clip_manager.create_clip(clip_data)
        
        assert "clip_id" in result
        assert result["duration"] == 14.7
        assert result["title"] == "Great Goal Sequence"
        assert result["export_status"] == "pending"
    
    @pytest.mark.asyncio
    async def test_clip_trimming(self, clip_manager):
        """Test frame-accurate clip trimming"""
        clip_id = "clip_123"
        trim_data = {
            "start_time": 125.0,
            "end_time": 130.0
        }
        
        # Mock existing clip
        mock_clip = Mock()
        mock_clip.start_time = 120.0
        mock_clip.end_time = 135.0
        clip_manager.db.query().filter().first.return_value = mock_clip
        
        result = await clip_manager.trim_clip(clip_id, trim_data)
        
        assert result["new_duration"] == 5.0
        assert result["status"] == "trim_successful"
        assert "export_job_id" in result
    
    @pytest.mark.asyncio
    async def test_export_processing(self, clip_manager):
        """Test video export with different settings"""
        clip_id = "clip_123"
        export_settings = {
            "format": "mp4",
            "quality": "high",
            "resolution": "1080p"
        }
        
        result = await clip_manager.export_clip(clip_id, export_settings)
        
        assert "export_job_id" in result
        assert result["status"] == "queued"
        assert "estimated_completion" in result
    
    def test_export_time_estimation(self, clip_manager):
        """Test export time estimation algorithm"""
        duration = 60.0  # 1 minute clip
        settings = {"quality": "high", "resolution": "1080p"}
        
        estimated_time = clip_manager.estimate_export_time(duration, settings)
        
        assert estimated_time > 0
        assert isinstance(estimated_time, int)
    
    @pytest.mark.asyncio 
    async def test_thumbnail_generation(self, clip_manager):
        """Test automatic thumbnail generation"""
        mock_clip = Mock()
        mock_clip.id = "clip_123"
        mock_clip.start_time = 120.0
        mock_clip.duration = 15.0
        mock_clip.source_video_path = "/path/to/source.mp4"
        
        with patch('ffmpeg.input') as mock_ffmpeg:
            thumbnail_path = await clip_manager.generate_clip_thumbnail(mock_clip)
            assert thumbnail_path is not None
            mock_ffmpeg.assert_called_once()
```

## Monitoring

1. **Processing Metrics**
   - Export queue length and processing times
   - Success/failure rates for different formats
   - Resource utilization during video processing

2. **User Engagement**
   - Clip creation and usage patterns
   - Popular export formats and settings
   - Sharing and collaboration metrics

3. **Performance Tracking**
   - Timeline scrubbing responsiveness
   - Thumbnail generation speed
   - Export completion times by settings

## Definition of Done

- [ ] Clip creation interface with timeline selection implemented
- [ ] Frame-accurate trimming controls with keyboard navigation
- [ ] Multi-format export system (MP4, MOV, WebM) with quality options
- [ ] Comprehensive metadata management with tags and categories
- [ ] Clip library with grid view, search, and filtering
- [ ] Batch export processing with queue management
- [ ] Secure sharing system with permission controls
- [ ] AI overlay integration in exported clips
- [ ] All clip features tested with comprehensive coverage
- [ ] Performance benchmarks met for video processing operations
- [ ] UI responsiveness validated for large clip libraries
- [ ] Export quality verified across all supported formats

## Dependencies

- **Story 3.3**: Timeline interface for clip selection
- **Story 3.2**: AI overlay system for overlay integration
- **Story 1.4**: Video storage infrastructure

## Risks

1. **Video Processing Performance**
   - **Risk**: Large video files may cause processing delays
   - **Mitigation**: Implement smart compression and parallel processing

2. **Storage Costs**
   - **Risk**: Clip exports may consume significant storage
   - **Mitigation**: Implement lifecycle policies and compression

3. **User Experience Complexity**
   - **Risk**: Advanced trimming features may overwhelm users
   - **Mitigation**: Progressive disclosure and intuitive defaults

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|---------|
| 2024-01-23 | 1.0 | Initial story creation with comprehensive clip management system | PM Team |