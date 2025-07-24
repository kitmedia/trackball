# Story 3.5: Real-time Processing Status Updates

## Status
🟡 **PENDING** - Real-time processing status updates via WebSocket connections with comprehensive progress tracking and notification system

## Story
**As a** coach,
**I want** real-time processing status updates via WebSocket connections,
**so that** I know when analysis is complete and can plan my review workflow.

## Acceptance Criteria
1. WebSocket connection for real-time processing progress updates ⏳
2. Processing status screen with pipeline visualization and progress bars ⏳
3. Estimated completion time calculation and display ⏳
4. Queue position visibility when multiple sessions are processing ⏳
5. Error notification system with detailed error messages and recovery options ⏳
6. Processing completion notifications with email and in-app alerts ⏳
7. Background processing support allowing continued platform use ⏳
8. Processing history and status log for troubleshooting and optimization ⏳

## Tasks / Subtasks

- [ ] **Task 3.5.1: WebSocket Infrastructure & Connection Management** ⏳
  - [ ] Implement WebSocket server with Socket.IO for real-time communication
  - [ ] Create connection management with automatic reconnection and heartbeat monitoring
  - [ ] Add authentication and authorization for WebSocket connections
  - [ ] Implement connection pooling with user session management
  - [ ] Create message routing system for targeted status updates
  - [ ] Add connection health monitoring with automatic failover
  - [ ] Implement rate limiting to prevent connection abuse
  - [ ] Create WebSocket middleware for logging and monitoring
  - **Estimate:** 35 hours | **Priority:** Critical | **Dependencies:** Story 1.2 (user authentication)
  - **Deliverables:**
    - WebSocket server with Socket.IO implementation
    - Connection management with automatic reconnection
    - Authentication and session management system
    - Message routing and health monitoring capabilities

- [ ] **Task 3.5.2: Processing Pipeline Visualization** ⏳
  - [ ] Create interactive pipeline visualization with stage progress indicators
  - [ ] Implement real-time progress bars for each processing stage
  - [ ] Add pipeline stage descriptions with estimated duration for each step
  - [ ] Create visual feedback for current processing stage with animated indicators
  - [ ] Implement error state visualization with detailed error information
  - [ ] Add processing stage dependencies with prerequisite status display
  - [ ] Create mobile-responsive pipeline visualization for tablet access
  - [ ] Implement pipeline history with previous processing run comparisons
  - **Estimate:** 32 hours | **Priority:** Critical | **Dependencies:** Task 3.5.1
  - **Deliverables:**
    - Interactive pipeline visualization with stage indicators
    - Real-time progress bars with animated feedback
    - Error state visualization with detailed information
    - Mobile-responsive design for cross-device access

- [ ] **Task 3.5.3: Completion Time Estimation & Prediction** ⏳
  - [ ] Implement machine learning model for processing time prediction
  - [ ] Create historical data analysis for accurate time estimation
  - [ ] Add dynamic estimation updates based on current system load
  - [ ] Implement confidence intervals for time estimates with uncertainty display
  - [ ] Create estimation accuracy tracking with continuous model improvement
  - [ ] Add queue position impact on completion time calculations
  - [ ] Implement resource availability consideration in time estimates
  - [ ] Create estimation API for integration with other system components
  - **Estimate:** 38 hours | **Priority:** High | **Dependencies:** Task 3.5.2
  - **Deliverables:**
    - ML-based processing time prediction model
    - Dynamic estimation with system load consideration
    - Confidence intervals with uncertainty quantification
    - Estimation accuracy tracking and model improvement

- [ ] **Task 3.5.4: Queue Management & Position Tracking** ⏳
  - [ ] Implement processing queue with priority-based ordering
  - [ ] Create queue position tracking with real-time updates
  - [ ] Add queue visualization with position and estimated wait time
  - [ ] Implement queue analytics with average wait times and throughput metrics
  - [ ] Create queue management API for external integrations
  - [ ] Add queue optimization algorithms for efficient resource utilization
  - [ ] Implement queue notifications with position change alerts
  - [ ] Create queue history and analytics dashboard for system optimization
  - **Estimate:** 30 hours | **Priority:** High | **Dependencies:** Task 3.5.3
  - **Deliverables:**
    - Priority-based processing queue system
    - Real-time queue position tracking with visualization
    - Queue analytics with performance metrics
    - Optimization algorithms for efficient processing

- [ ] **Task 3.5.5: Error Handling & Recovery System** ⏳
  - [ ] Create comprehensive error classification system with recovery suggestions
  - [ ] Implement automatic retry mechanisms with exponential backoff
  - [ ] Add error notification system with detailed diagnostic information
  - [ ] Create user-friendly error messages with actionable recovery steps
  - [ ] Implement error logging and tracking for system monitoring
  - [ ] Add error escalation procedures with support team notification
  - [ ] Create error analytics dashboard for identifying common issues
  - [ ] Implement self-healing capabilities for transient errors
  - **Estimate:** 33 hours | **Priority:** Critical | **Dependencies:** Task 3.5.4
  - **Deliverables:**
    - Comprehensive error classification and handling system
    - Automatic retry mechanisms with intelligent backoff
    - User-friendly error notifications with recovery guidance
    - Error analytics and self-healing capabilities

- [ ] **Task 3.5.6: Multi-Channel Notification System** ⏳
  - [ ] Implement in-app notifications with toast messages and status updates
  - [ ] Create email notification system with customizable templates
  - [ ] Add SMS notifications for critical processing updates
  - [ ] Implement push notifications for mobile app integration
  - [ ] Create notification preferences management with granular control
  - [ ] Add notification history and delivery tracking
  - [ ] Implement notification batching to prevent spam
  - [ ] Create notification analytics with engagement metrics
  - **Estimate:** 28 hours | **Priority:** High | **Dependencies:** Task 3.5.5
  - **Deliverables:**
    - Multi-channel notification system (in-app, email, SMS, push)
    - Customizable notification templates and preferences
    - Notification history and delivery tracking
    - Analytics with engagement metrics

- [ ] **Task 3.5.7: Background Processing Architecture** ⏳
  - [ ] Implement background job queue with Redis and Celery
  - [ ] Create service worker architecture for non-blocking processing
  - [ ] Add background task monitoring with health checks
  - [ ] Implement graceful background task cancellation
  - [ ] Create background processing analytics with performance metrics
  - [ ] Add resource management for background processing optimization
  - [ ] Implement background task scaling based on demand
  - [ ] Create background processing API for external integrations
  - **Estimate:** 36 hours | **Priority:** Critical | **Dependencies:** Task 3.5.6
  - **Deliverables:**
    - Background job queue with Redis and Celery
    - Service worker architecture for non-blocking operations
    - Background task monitoring and health checks
    - Resource management and auto-scaling capabilities

- [ ] **Task 3.5.8: Processing History & Analytics** ⏳
  - [ ] Create comprehensive processing history with detailed logs
  - [ ] Implement processing analytics dashboard with performance metrics
  - [ ] Add processing time trends and system performance tracking
  - [ ] Create processing success/failure rate monitoring
  - [ ] Implement processing bottleneck identification and optimization suggestions
  - [ ] Add comparative analysis between different processing runs
  - [ ] Create processing history export functionality for external analysis
  - [ ] Implement processing history search and filtering capabilities
  - **Estimate:** 25 hours | **Priority:** Medium | **Dependencies:** Task 3.5.7
  - **Deliverables:**
    - Comprehensive processing history with detailed analytics
    - Performance metrics dashboard with trend analysis
    - Bottleneck identification and optimization suggestions
    - Export functionality for external analysis

## API Implementation

### Real-time Processing Status API

```python
# FastAPI and Socket.IO implementation for real-time processing updates
from fastapi import FastAPI, HTTPException, Depends, Security, BackgroundTasks
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import socketio
from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional, Dict, Any, Callable
from datetime import datetime, timedelta
import asyncio
import redis
import json
import uuid
import logging
from celery import Celery
from sklearn.linear_model import LinearRegression
import numpy as np

Base = declarative_base()

class ProcessingJob(Base):
    __tablename__ = "processing_jobs"
    
    id = Column(String, primary_key=True)
    session_id = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
    job_type = Column(String, nullable=False)  # video_processing, ai_analysis, export
    status = Column(String, default="queued")  # queued, processing, completed, failed, cancelled
    progress_percentage = Column(Float, default=0.0)
    current_stage = Column(String)
    total_stages = Column(Integer, default=1)
    current_stage_progress = Column(Float, default=0.0)
    estimated_completion = Column(DateTime)
    actual_completion = Column(DateTime)
    processing_time = Column(Float)  # seconds
    queue_position = Column(Integer)
    priority = Column(Integer, default=5)  # 1-10, lower is higher priority
    error_message = Column(Text)
    error_code = Column(String)
    retry_count = Column(Integer, default=0)
    max_retries = Column(Integer, default=3)
    metadata = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    started_at = Column(DateTime)

class ProcessingStage(Base):
    __tablename__ = "processing_stages"
    
    id = Column(String, primary_key=True)
    job_id = Column(String, nullable=False)
    stage_name = Column(String, nullable=False)
    stage_order = Column(Integer, nullable=False)
    status = Column(String, default="pending")  # pending, processing, completed, failed
    progress_percentage = Column(Float, default=0.0)
    estimated_duration = Column(Float)  # seconds
    actual_duration = Column(Float)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    error_message = Column(Text)
    stage_data = Column(JSON)

class NotificationPreferences(Base):
    __tablename__ = "notification_preferences"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    email_enabled = Column(Boolean, default=True)
    sms_enabled = Column(Boolean, default=False)
    push_enabled = Column(Boolean, default=True)
    in_app_enabled = Column(Boolean, default=True)
    notification_types = Column(JSON)  # Array of notification types
    quiet_hours_start = Column(String)  # HH:MM format
    quiet_hours_end = Column(String)    # HH:MM format
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Initialize Socket.IO server
sio = socketio.AsyncServer(cors_allowed_origins="*", async_mode='asgi')

# Initialize Celery for background processing
celery_app = Celery('processing_status', broker='redis://localhost:6379')

class ProcessingStatusManager:
    def __init__(self, db_session, redis_client):
        self.db = db_session
        self.redis = redis_client
        self.logger = logging.getLogger(__name__)
        self.time_predictor = self._initialize_time_predictor()
        
    def _initialize_time_predictor(self):
        """Initialize ML model for processing time prediction"""
        return LinearRegression()
    
    async def create_processing_job(self, job_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new processing job with initial status"""
        try:
            job = ProcessingJob(
                id=f"job_{uuid.uuid4().hex[:12]}",
                session_id=job_data["session_id"],
                user_id=job_data["user_id"],
                job_type=job_data["job_type"],
                priority=job_data.get("priority", 5),
                metadata=json.dumps(job_data.get("metadata", {}))
            )
            
            self.db.add(job)
            
            # Create processing stages
            stages = self._get_processing_stages(job_data["job_type"])
            for i, stage_name in enumerate(stages):
                stage = ProcessingStage(
                    id=f"stage_{uuid.uuid4().hex[:12]}",
                    job_id=job.id,
                    stage_name=stage_name,
                    stage_order=i + 1,
                    estimated_duration=self._estimate_stage_duration(stage_name, job_data)
                )
                self.db.add(stage)
            
            job.total_stages = len(stages)
            
            # Calculate queue position and estimated completion
            queue_position = await self._calculate_queue_position(job.priority)
            job.queue_position = queue_position
            job.estimated_completion = await self._predict_completion_time(job)
            
            self.db.commit()
            
            # Add to Redis queue
            await self._add_to_processing_queue(job)
            
            # Send initial status update
            await self._send_status_update(job)
            
            return {
                "job_id": job.id,
                "status": job.status,
                "queue_position": job.queue_position,
                "estimated_completion": job.estimated_completion.isoformat(),
                "total_stages": job.total_stages
            }
            
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Failed to create processing job: {str(e)}")
            raise HTTPException(status_code=500, detail="Job creation failed")
    
    async def update_job_progress(self, job_id: str, progress_data: Dict[str, Any]) -> None:
        """Update processing job progress and notify clients"""
        try:
            job = self.db.query(ProcessingJob).filter(ProcessingJob.id == job_id).first()
            if not job:
                raise HTTPException(status_code=404, detail="Job not found")
            
            # Update job progress
            job.progress_percentage = progress_data.get("progress_percentage", job.progress_percentage)
            job.current_stage = progress_data.get("current_stage", job.current_stage)
            job.current_stage_progress = progress_data.get("stage_progress", job.current_stage_progress)
            job.status = progress_data.get("status", job.status)
            
            # Update stage progress if provided
            if progress_data.get("stage_progress") is not None:
                await self._update_stage_progress(job_id, job.current_stage, progress_data)
            
            # Recalculate estimated completion
            if job.status == "processing":
                job.estimated_completion = await self._predict_completion_time(job)
            
            job.updated_at = datetime.utcnow()
            
            # Handle completion
            if job.status == "completed":
                job.actual_completion = datetime.utcnow()
                job.processing_time = (job.actual_completion - job.started_at).total_seconds()
                await self._handle_job_completion(job)
            
            # Handle errors
            elif job.status == "failed":
                await self._handle_job_error(job, progress_data.get("error_message"))
            
            self.db.commit()
            
            # Send real-time update
            await self._send_status_update(job)
            
        except Exception as e:
            self.db.rollback()
            self.logger.error(f"Failed to update job progress: {str(e)}")
    
    async def _send_status_update(self, job: ProcessingJob) -> None:
        """Send real-time status update via WebSocket"""
        try:
            # Get current stage details
            current_stage_details = None
            if job.current_stage:
                current_stage_details = self.db.query(ProcessingStage).filter(
                    ProcessingStage.job_id == job.id,
                    ProcessingStage.stage_name == job.current_stage
                ).first()
            
            status_data = {
                "job_id": job.id,
                "session_id": job.session_id,
                "status": job.status,
                "progress_percentage": job.progress_percentage,
                "current_stage": job.current_stage,
                "current_stage_progress": job.current_stage_progress,
                "total_stages": job.total_stages,
                "queue_position": job.queue_position,
                "estimated_completion": job.estimated_completion.isoformat() if job.estimated_completion else None,
                "error_message": job.error_message,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            if current_stage_details:
                status_data["stage_details"] = {
                    "name": current_stage_details.stage_name,
                    "order": current_stage_details.stage_order,
                    "estimated_duration": current_stage_details.estimated_duration,
                    "status": current_stage_details.status
                }
            
            # Send to user's room
            await sio.emit('processing_update', status_data, room=f"user_{job.user_id}")
            
            # Send to session room for team members
            await sio.emit('session_processing_update', status_data, room=f"session_{job.session_id}")
            
        except Exception as e:
            self.logger.error(f"Failed to send status update: {str(e)}")
    
    async def _predict_completion_time(self, job: ProcessingJob) -> datetime:
        """Predict job completion time using ML model"""
        try:
            # Get historical data for similar jobs
            historical_jobs = self.db.query(ProcessingJob).filter(
                ProcessingJob.job_type == job.job_type,
                ProcessingJob.status == "completed",
                ProcessingJob.processing_time.isnot(None)
            ).limit(100).all()
            
            if len(historical_jobs) < 5:
                # Fallback to simple estimation if not enough data
                return datetime.utcnow() + timedelta(minutes=15)
            
            # Prepare features for prediction
            features = []
            processing_times = []
            
            for hist_job in historical_jobs:
                metadata = json.loads(hist_job.metadata) if hist_job.metadata else {}
                features.append([
                    metadata.get("video_duration", 0),
                    metadata.get("video_size_mb", 0),
                    metadata.get("resolution_factor", 1.0),
                    hist_job.priority
                ])
                processing_times.append(hist_job.processing_time)
            
            # Train model and predict
            self.time_predictor.fit(features, processing_times)
            
            current_metadata = json.loads(job.metadata) if job.metadata else {}
            current_features = [[
                current_metadata.get("video_duration", 0),
                current_metadata.get("video_size_mb", 0),
                current_metadata.get("resolution_factor", 1.0),
                job.priority
            ]]
            
            predicted_time = self.time_predictor.predict(current_features)[0]
            
            # Add current progress consideration
            remaining_progress = (100 - job.progress_percentage) / 100
            adjusted_time = predicted_time * remaining_progress
            
            # Add queue wait time
            queue_wait_time = await self._estimate_queue_wait_time(job.queue_position)
            
            return datetime.utcnow() + timedelta(seconds=adjusted_time + queue_wait_time)
            
        except Exception as e:
            self.logger.error(f"Failed to predict completion time: {str(e)}")
            return datetime.utcnow() + timedelta(minutes=15)
    
    async def _handle_job_completion(self, job: ProcessingJob) -> None:
        """Handle job completion with notifications"""
        try:
            # Send completion notification
            await self._send_completion_notification(job)
            
            # Update processing time analytics
            await self._update_processing_analytics(job)
            
            # Clean up temporary resources
            await self._cleanup_job_resources(job)
            
        except Exception as e:
            self.logger.error(f"Failed to handle job completion: {str(e)}")
    
    async def _handle_job_error(self, job: ProcessingJob, error_message: str) -> None:
        """Handle job errors with retry logic"""
        try:
            job.error_message = error_message
            job.retry_count += 1
            
            if job.retry_count <= job.max_retries:
                # Schedule retry
                job.status = "queued"
                job.progress_percentage = 0.0
                job.current_stage = None
                await self._add_to_processing_queue(job)
                
                self.logger.info(f"Retrying job {job.id}, attempt {job.retry_count}")
            else:
                # Max retries exceeded, send error notification
                await self._send_error_notification(job)
                
        except Exception as e:
            self.logger.error(f"Failed to handle job error: {str(e)}")
    
    async def _send_completion_notification(self, job: ProcessingJob) -> None:
        """Send completion notification through multiple channels"""
        try:
            # Get user notification preferences
            preferences = self.db.query(NotificationPreferences).filter(
                NotificationPreferences.user_id == job.user_id
            ).first()
            
            if not preferences:
                return
            
            notification_data = {
                "job_id": job.id,
                "session_id": job.session_id,
                "job_type": job.job_type,
                "processing_time": job.processing_time
            }
            
            # Send in-app notification
            if preferences.in_app_enabled:
                await sio.emit('processing_completed', notification_data, room=f"user_{job.user_id}")
            
            # Send email notification
            if preferences.email_enabled:
                await self._send_email_notification(job, "completion")
            
            # Send push notification
            if preferences.push_enabled:
                await self._send_push_notification(job, "completion")
                
        except Exception as e:
            self.logger.error(f"Failed to send completion notification: {str(e)}")
    
    def _get_processing_stages(self, job_type: str) -> List[str]:
        """Get processing stages based on job type"""
        stage_mapping = {
            "video_processing": [
                "video_upload_validation",
                "video_synchronization", 
                "ai_object_detection",
                "player_tracking",
                "event_detection",
                "analysis_generation",
                "result_finalization"
            ],
            "ai_analysis": [
                "data_preparation",
                "model_inference",
                "result_processing",
                "visualization_generation"
            ],
            "export": [
                "data_compilation",
                "format_conversion",
                "quality_optimization",
                "file_generation"
            ]
        }
        
        return stage_mapping.get(job_type, ["processing"])
    
    def _estimate_stage_duration(self, stage_name: str, job_data: Dict[str, Any]) -> float:
        """Estimate duration for a specific stage"""
        # Base durations in seconds
        base_durations = {
            "video_upload_validation": 30,
            "video_synchronization": 120,
            "ai_object_detection": 300,
            "player_tracking": 240,
            "event_detection": 180,
            "analysis_generation": 90,
            "result_finalization": 60
        }
        
        base_duration = base_durations.get(stage_name, 60)
        
        # Adjust based on video characteristics
        metadata = job_data.get("metadata", {})
        duration_factor = metadata.get("video_duration", 60) / 60  # Normalize to minutes
        size_factor = metadata.get("video_size_mb", 100) / 100     # Normalize to 100MB
        
        return base_duration * (1 + duration_factor * 0.5) * (1 + size_factor * 0.3)

# Socket.IO event handlers
@sio.event
async def connect(sid, environ, auth):
    """Handle WebSocket connection"""
    try:
        # Authenticate user
        user_id = auth.get('user_id') if auth else None
        if not user_id:
            await sio.disconnect(sid)
            return
        
        # Join user room
        await sio.enter_room(sid, f"user_{user_id}")
        
        # Send connection confirmation
        await sio.emit('connected', {'status': 'success'}, room=sid)
        
    except Exception as e:
        logging.error(f"Connection error: {str(e)}")
        await sio.disconnect(sid)

@sio.event
async def disconnect(sid):
    """Handle WebSocket disconnection"""
    logging.info(f"Client {sid} disconnected")

@sio.event
async def join_session(sid, data):
    """Join session room for team updates"""
    try:
        session_id = data.get('session_id')
        if session_id:
            await sio.enter_room(sid, f"session_{session_id}")
            await sio.emit('joined_session', {'session_id': session_id}, room=sid)
    except Exception as e:
        logging.error(f"Failed to join session: {str(e)}")

# Background processing tasks
@celery_app.task
def process_video_analysis(job_id: str):
    """Background task for video analysis processing"""
    # Implementation would go here
    pass

@celery_app.task
def cleanup_completed_jobs():
    """Periodic cleanup of old completed jobs"""
    # Implementation would go here
    pass

# API Endpoints
app = FastAPI()
security = HTTPBearer()

@app.post("/api/v1/processing/jobs")
async def create_processing_job(
    job_data: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Create new processing job with real-time tracking"""
    # Implementation logic here
    pass

@app.get("/api/v1/processing/jobs/{job_id}/status")
async def get_job_status(
    job_id: str,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get current processing job status"""
    # Implementation logic here
    pass

@app.get("/api/v1/processing/queue")
async def get_processing_queue(
    user_id: Optional[str] = None,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get current processing queue status"""
    # Implementation logic here
    pass

@app.post("/api/v1/processing/jobs/{job_id}/cancel")
async def cancel_processing_job(
    job_id: str,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Cancel processing job"""
    # Implementation logic here
    pass

@app.get("/api/v1/processing/history")
async def get_processing_history(
    user_id: Optional[str] = None,
    limit: int = 50,
    offset: int = 0,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get processing history and analytics"""
    # Implementation logic here
    pass

# Mount Socket.IO app
socket_app = socketio.ASGIApp(sio, app)
```

## Frontend Component Architecture

### Real-time Processing Status Interface

```typescript
// React components for real-time processing status
import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  Box, Card, CardContent, Typography, LinearProgress, Button,
  Dialog, DialogTitle, DialogContent, DialogActions, Grid,
  Chip, Alert, List, ListItem, ListItemText, ListItemIcon,
  Stepper, Step, StepLabel, StepContent, IconButton, Tooltip,
  CircularProgress, Badge, Snackbar
} from '@mui/material';
import {
  PlayArrow, Pause, Stop, CheckCircle, Error, Warning,
  Schedule, Queue, Refresh, Cancel, Visibility,
  Timeline, Analytics, Notifications
} from '@mui/icons-material';
import { io, Socket } from 'socket.io-client';
import { useProcessingStore } from '../stores/processingStore';

interface ProcessingJob {
  id: string;
  sessionId: string;
  jobType: string;
  status: 'queued' | 'processing' | 'completed' | 'failed' | 'cancelled';
  progressPercentage: number;
  currentStage: string;
  currentStageProgress: number;
  totalStages: number;
  queuePosition: number;
  estimatedCompletion: string;
  errorMessage?: string;
  createdAt: string;
  stageDetails?: {
    name: string;
    order: number;
    estimatedDuration: number;
    status: string;
  };
}

interface ProcessingStage {
  id: string;
  stageName: string;
  stageOrder: number;
  status: string;
  progressPercentage: number;
  estimatedDuration: number;
  actualDuration?: number;
}

const ProcessingStatusManager: React.FC = () => {
  const [currentJobs, setCurrentJobs] = useState<ProcessingJob[]>([]);
  const [jobHistory, setJobHistory] = useState<ProcessingJob[]>([]);
  const [selectedJob, setSelectedJob] = useState<ProcessingJob | null>(null);
  const [showJobDetails, setShowJobDetails] = useState(false);
  const [queueInfo, setQueueInfo] = useState({
    totalJobs: 0,
    averageWaitTime: 0,
    systemLoad: 0
  });
  const [notifications, setNotifications] = useState<any[]>([]);
  const [showNotification, setShowNotification] = useState(false);
  
  const socketRef = useRef<Socket | null>(null);
  const {
    createProcessingJob,
    getProcessingQueue,
    getProcessingHistory,
    cancelProcessingJob
  } = useProcessingStore();

  useEffect(() => {
    initializeWebSocket();
    loadInitialData();
    
    return () => {
      if (socketRef.current) {
        socketRef.current.disconnect();
      }
    };
  }, []);

  const initializeWebSocket = () => {
    const token = localStorage.getItem('auth_token');
    
    socketRef.current = io(process.env.REACT_APP_WEBSOCKET_URL || 'ws://localhost:8000', {
      auth: {
        user_id: 'current_user_id' // Get from auth context
      },
      transports: ['websocket']
    });

    socketRef.current.on('connected', (data) => {
      console.log('WebSocket connected:', data);
    });

    socketRef.current.on('processing_update', (data: ProcessingJob) => {
      handleProcessingUpdate(data);
    });

    socketRef.current.on('processing_completed', (data) => {
      handleProcessingCompleted(data);
    });

    socketRef.current.on('processing_failed', (data) => {
      handleProcessingFailed(data);
    });

    socketRef.current.on('queue_update', (data) => {
      setQueueInfo(data);
    });

    socketRef.current.on('disconnect', () => {
      console.log('WebSocket disconnected');
      // Attempt reconnection logic
      setTimeout(() => {
        socketRef.current?.connect();
      }, 5000);
    });
  };

  const loadInitialData = async () => {
    try {
      const [queueData, historyData] = await Promise.all([
        getProcessingQueue(),
        getProcessingHistory({ limit: 20 })
      ]);
      
      setCurrentJobs(queueData.jobs || []);
      setQueueInfo(queueData.queueInfo || {});
      setJobHistory(historyData || []);
    } catch (error) {
      console.error('Failed to load initial data:', error);
    }
  };

  const handleProcessingUpdate = (jobData: ProcessingJob) => {
    setCurrentJobs(prev => {
      const existingIndex = prev.findIndex(job => job.id === jobData.id);
      if (existingIndex >= 0) {
        const updated = [...prev];
        updated[existingIndex] = jobData;
        return updated;
      } else {
        return [...prev, jobData];
      }
    });

    // Update selected job if it's being viewed
    if (selectedJob?.id === jobData.id) {
      setSelectedJob(jobData);
    }
  };

  const handleProcessingCompleted = (data: any) => {
    // Move job from current to history
    setCurrentJobs(prev => prev.filter(job => job.id !== data.job_id));
    
    // Add to history
    const completedJob = currentJobs.find(job => job.id === data.job_id);
    if (completedJob) {
      setJobHistory(prev => [{ ...completedJob, status: 'completed' }, ...prev]);
    }

    // Show notification
    setNotifications(prev => [...prev, {
      id: Date.now(),
      type: 'success',
      message: `Processing completed for ${data.job_type}`,
      jobId: data.job_id
    }]);
    setShowNotification(true);
  };

  const handleProcessingFailed = (data: any) => {
    // Show error notification
    setNotifications(prev => [...prev, {
      id: Date.now(),
      type: 'error',
      message: `Processing failed: ${data.error_message}`,
      jobId: data.job_id
    }]);
    setShowNotification(true);
  };

  const handleCancelJob = async (jobId: string) => {
    try {
      await cancelProcessingJob(jobId);
      // Job will be removed via WebSocket update
    } catch (error) {
      console.error('Failed to cancel job:', error);
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed': return 'success';
      case 'processing': return 'primary';
      case 'failed': return 'error';
      case 'cancelled': return 'default';
      default: return 'info';
    }
  };

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed': return <CheckCircle color="success" />;
      case 'processing': return <PlayArrow color="primary" />;
      case 'failed': return <Error color="error" />;
      case 'cancelled': return <Stop color="action" />;
      default: return <Schedule color="info" />;
    }
  };

  const formatTimeRemaining = (estimatedCompletion: string) => {
    const now = new Date();
    const completion = new Date(estimatedCompletion);
    const diff = Math.max(0, completion.getTime() - now.getTime());
    const minutes = Math.floor(diff / 60000);
    const seconds = Math.floor((diff % 60000) / 1000);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  const ProcessingJobCard = ({ job }: { job: ProcessingJob }) => (
    <Card sx={{ mb: 2 }}>
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
          <Box>
            <Typography variant="h6" gutterBottom>
              {job.jobType.replace('_', ' ').toUpperCase()}
            </Typography>
            <Typography variant="body2" color="textSecondary">
              Session: {job.sessionId}
            </Typography>
          </Box>
          
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Chip
              label={job.status}
              color={getStatusColor(job.status) as any}
              icon={getStatusIcon(job.status)}
              size="small"
            />
            {job.status === 'queued' && (
              <Badge badgeContent={job.queuePosition} color="primary">
                <Queue />
              </Badge>
            )}
          </Box>
        </Box>

        {/* Progress Section */}
        {job.status === 'processing' && (
          <Box sx={{ mb: 2 }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
              <Typography variant="body2">
                Stage: {job.currentStage?.replace('_', ' ')} ({job.stageDetails?.order || 0}/{job.totalStages})
              </Typography>
              <Typography variant="body2">
                {Math.round(job.progressPercentage)}%
              </Typography>
            </Box>
            
            <LinearProgress
              variant="determinate"
              value={job.progressPercentage}
              sx={{ height: 8, borderRadius: 4, mb: 1 }}
            />
            
            <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
              <Typography variant="caption" color="textSecondary">
                Current Stage: {Math.round(job.currentStageProgress)}%
              </Typography>
              <Typography variant="caption" color="textSecondary">
                ETA: {formatTimeRemaining(job.estimatedCompletion)}
              </Typography>
            </Box>
          </Box>
        )}

        {/* Queue Information */}
        {job.status === 'queued' && (
          <Alert severity="info" sx={{ mb: 2 }}>
            <Typography variant="body2">
              Position {job.queuePosition} in queue • Estimated wait: {formatTimeRemaining(job.estimatedCompletion)}
            </Typography>
          </Alert>
        )}

        {/* Error Information */}
        {job.status === 'failed' && job.errorMessage && (
          <Alert severity="error" sx={{ mb: 2 }}>
            <Typography variant="body2">
              {job.errorMessage}
            </Typography>
          </Alert>
        )}

        {/* Action Buttons */}
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 1 }}>
          <IconButton
            size="small"
            onClick={() => {
              setSelectedJob(job);
              setShowJobDetails(true);
            }}
          >
            <Visibility />
          </IconButton>
          
          {(job.status === 'queued' || job.status === 'processing') && (
            <IconButton
              size="small"
              color="error"
              onClick={() => handleCancelJob(job.id)}
            >
              <Cancel />
            </IconButton>
          )}
        </Box>
      </CardContent>
    </Card>
  );

  const ProcessingPipeline = ({ job }: { job: ProcessingJob }) => (
    <Box sx={{ mt: 2 }}>
      <Typography variant="h6" gutterBottom>
        Processing Pipeline
      </Typography>
      
      <Stepper orientation="vertical" activeStep={job.stageDetails?.order || 0}>
        {/* This would be populated with actual stages */}
        {Array.from({ length: job.totalStages }, (_, index) => (
          <Step key={index}>
            <StepLabel>
              Stage {index + 1}
            </StepLabel>
            <StepContent>
              <LinearProgress
                variant="determinate"
                value={index === (job.stageDetails?.order || 0) - 1 ? job.currentStageProgress : 
                       index < (job.stageDetails?.order || 0) - 1 ? 100 : 0}
              />
            </StepContent>
          </Step>
        ))}
      </Stepper>
    </Box>
  );

  const QueueOverview = () => (
    <Card sx={{ mb: 3 }}>
      <CardContent>
        <Typography variant="h6" gutterBottom>
          Queue Overview
        </Typography>
        
        <Grid container spacing={3}>
          <Grid item xs={12} md={4}>
            <Box sx={{ textAlign: 'center' }}>
              <CircularProgress
                variant="determinate"
                value={Math.max(0, 100 - queueInfo.systemLoad)}
                size={60}
                thickness={4}
              />
              <Typography variant="h6" sx={{ mt: 1 }}>
                {queueInfo.totalJobs}
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Jobs in Queue
              </Typography>
            </Box>
          </Grid>
          
          <Grid item xs={12} md={4}>
            <Box sx={{ textAlign: 'center' }}>
              <Schedule sx={{ fontSize: 40, color: 'primary.main', mb: 1 }} />
              <Typography variant="h6">
                {Math.round(queueInfo.averageWaitTime / 60)}m
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Avg Wait Time
              </Typography>
            </Box>
          </Grid>
          
          <Grid item xs={12} md={4}>
            <Box sx={{ textAlign: 'center' }}>
              <Analytics sx={{ fontSize: 40, color: 'success.main', mb: 1 }} />
              <Typography variant="h6">
                {Math.round(queueInfo.systemLoad)}%
              </Typography>
              <Typography variant="body2" color="textSecondary">
                System Load
              </Typography>
            </Box>
          </Grid>
        </Grid>
      </CardContent>
    </Card>
  );

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Processing Status
      </Typography>
      
      <QueueOverview />
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Typography variant="h6" gutterBottom>
            Current Jobs
          </Typography>
          
          {currentJobs.length === 0 ? (
            <Alert severity="info">
              No active processing jobs
            </Alert>
          ) : (
            currentJobs.map(job => (
              <ProcessingJobCard key={job.id} job={job} />
            ))
          )}
        </Grid>
        
        <Grid item xs={12} md={4}>
          <Typography variant="h6" gutterBottom>
            Recent History
          </Typography>
          
          <List>
            {jobHistory.slice(0, 10).map(job => (
              <ListItem key={job.id}>
                <ListItemIcon>
                  {getStatusIcon(job.status)}
                </ListItemIcon>
                <ListItemText
                  primary={job.jobType.replace('_', ' ')}
                  secondary={new Date(job.createdAt).toLocaleString()}
                />
              </ListItem>
            ))}
          </List>
        </Grid>
      </Grid>

      {/* Job Details Dialog */}
      <Dialog
        open={showJobDetails}
        onClose={() => setShowJobDetails(false)}
        maxWidth="md"
        fullWidth
      >
        <DialogTitle>
          Processing Job Details
        </DialogTitle>
        <DialogContent>
          {selectedJob && (
            <Box>
              <ProcessingJobCard job={selectedJob} />
              <ProcessingPipeline job={selectedJob} />
            </Box>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowJobDetails(false)}>
            Close
          </Button>
        </DialogActions>
      </Dialog>

      {/* Notifications */}
      <Snackbar
        open={showNotification}
        autoHideDuration={6000}
        onClose={() => setShowNotification(false)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      >
        <Alert
          onClose={() => setShowNotification(false)}
          severity={notifications[notifications.length - 1]?.type || 'info'}
        >
          {notifications[notifications.length - 1]?.message}
        </Alert>
      </Snackbar>
    </Box>
  );
};

export default ProcessingStatusManager;
```

## Performance Considerations

1. **WebSocket Optimization**
   - Connection pooling with efficient resource management
   - Message batching to reduce network overhead
   - Intelligent reconnection with exponential backoff

2. **Real-time Updates**
   - Optimized status update frequency based on processing stage
   - Efficient data serialization for minimal payload size
   - Smart client-side caching to reduce server requests

3. **Queue Management**
   - Priority-based processing with resource optimization
   - Predictive analytics for accurate completion estimates
   - Load balancing across processing resources

## Security

1. **WebSocket Security**
   - Token-based authentication for all connections
   - Rate limiting to prevent connection abuse
   - Secure message validation and sanitization

2. **Data Protection**
   - Encrypted status information transmission
   - Access control for processing job visibility
   - Audit logging for all status operations

3. **Error Handling**
   - Secure error message sanitization
   - Safe retry mechanisms with backoff limits
   - Protected diagnostic information access

## Testing

```python
# Comprehensive testing for processing status features
import pytest
from unittest.mock import Mock, patch, AsyncMock
import asyncio
from datetime import datetime, timedelta

class TestProcessingStatusManager:
    
    @pytest.fixture
    def status_manager(self):
        mock_db = Mock()
        mock_redis = Mock()
        return ProcessingStatusManager(mock_db, mock_redis)
    
    @pytest.mark.asyncio
    async def test_create_processing_job(self, status_manager):
        """Test processing job creation with status tracking"""
        job_data = {
            "session_id": "session_123",
            "user_id": "user_456",
            "job_type": "video_processing",
            "priority": 3,
            "metadata": {"video_duration": 5400, "video_size_mb": 250}
        }
        
        result = await status_manager.create_processing_job(job_data)
        
        assert "job_id" in result
        assert result["status"] == "queued"
        assert result["queue_position"] > 0
        assert result["total_stages"] == 7  # video_processing stages
    
    @pytest.mark.asyncio
    async def test_job_progress_updates(self, status_manager):
        """Test real-time job progress updates"""
        job_id = "job_123"
        progress_data = {
            "progress_percentage": 45.5,
            "current_stage": "ai_object_detection",
            "stage_progress": 75.0,
            "status": "processing"
        }
        
        # Mock existing job
        mock_job = Mock()
        mock_job.id = job_id
        mock_job.status = "processing"
        mock_job.current_stage = "video_synchronization"
        status_manager.db.query().filter().first.return_value = mock_job
        
        await status_manager.update_job_progress(job_id, progress_data)
        
        assert mock_job.progress_percentage == 45.5
        assert mock_job.current_stage == "ai_object_detection"
        assert mock_job.current_stage_progress == 75.0
    
    @pytest.mark.asyncio
    async def test_completion_time_prediction(self, status_manager):
        """Test ML-based completion time prediction"""
        mock_job = Mock()
        mock_job.job_type = "video_processing"
        mock_job.metadata = '{"video_duration": 3600, "video_size_mb": 150}'
        mock_job.priority = 5
        mock_job.progress_percentage = 25.0
        mock_job.queue_position = 2
        
        predicted_time = await status_manager._predict_completion_time(mock_job)
        
        assert isinstance(predicted_time, datetime)
        assert predicted_time > datetime.utcnow()
    
    def test_processing_stages_configuration(self, status_manager):
        """Test processing stage configuration for different job types"""
        video_stages = status_manager._get_processing_stages("video_processing")
        ai_stages = status_manager._get_processing_stages("ai_analysis")
        export_stages = status_manager._get_processing_stages("export")
        
        assert len(video_stages) == 7
        assert "ai_object_detection" in video_stages
        assert len(ai_stages) == 4
        assert len(export_stages) == 4
    
    def test_stage_duration_estimation(self, status_manager):
        """Test stage duration estimation with video characteristics"""
        job_data = {
            "metadata": {
                "video_duration": 7200,  # 2 hours
                "video_size_mb": 500     # 500MB
            }
        }
        
        duration = status_manager._estimate_stage_duration("ai_object_detection", job_data)
        
        assert duration > 300  # Base duration
        assert isinstance(duration, float)

# WebSocket integration tests
class TestWebSocketIntegration:
    
    @pytest.mark.asyncio
    async def test_websocket_connection_auth(self):
        """Test WebSocket connection with authentication"""
        # Test WebSocket authentication flow
        pass
    
    @pytest.mark.asyncio
    async def test_real_time_status_updates(self):
        """Test real-time status update delivery"""
        # Test WebSocket message delivery
        pass
    
    @pytest.mark.asyncio
    async def test_connection_recovery(self):
        """Test WebSocket connection recovery after failure"""
        # Test reconnection and state recovery
        pass

# Performance tests
class TestProcessingPerformance:
    
    @pytest.mark.asyncio
    async def test_high_volume_status_updates(self):
        """Test performance with high volume of status updates"""
        # Test with many concurrent jobs
        pass
    
    @pytest.mark.asyncio
    async def test_websocket_scalability(self):
        """Test WebSocket performance with many connections"""
        # Test connection scaling
        pass
```

## Monitoring

1. **Processing Analytics**
   - Job completion rates and average processing times
   - Queue efficiency and resource utilization metrics
   - Error rates and retry success patterns

2. **WebSocket Performance**
   - Connection count and message throughput
   - Message delivery latency and success rates
   - Reconnection frequency and success rates

3. **User Experience**
   - Status update responsiveness and accuracy
   - Notification delivery rates and engagement
   - Processing prediction accuracy metrics

## Definition of Done

- [ ] WebSocket infrastructure implemented with Socket.IO and connection management
- [ ] Processing pipeline visualization with real-time progress indicators
- [ ] ML-based completion time estimation with confidence intervals
- [ ] Queue management with position tracking and analytics
- [ ] Comprehensive error handling with retry mechanisms and recovery
- [ ] Multi-channel notification system (in-app, email, SMS, push)
- [ ] Background processing architecture with Celery and Redis
- [ ] Processing history and analytics with trend analysis
- [ ] All status features tested with comprehensive coverage
- [ ] Performance benchmarks met for real-time updates (<100ms latency)
- [ ] WebSocket scalability validated for concurrent connections
- [ ] Processing prediction accuracy above 85% for completion times

## Dependencies

- **Story 1.2**: User authentication for WebSocket connections
- **Story 2.5**: Processing pipeline for status stage definitions
- **Story 1.4**: Video storage infrastructure for job data

## Risks

1. **WebSocket Scalability**
   - **Risk**: High concurrent connections may overwhelm server
   - **Mitigation**: Implement connection pooling and load balancing

2. **Prediction Accuracy**
   - **Risk**: Completion time predictions may be inaccurate initially
   - **Mitigation**: Continuous model training with historical data

3. **Real-time Performance**
   - **Risk**: Status updates may lag during high system load
   - **Mitigation**: Implement message queuing and priority handling

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|---------|
| 2024-01-23 | 1.0 | Initial story creation with comprehensive real-time processing status system | PM Team |