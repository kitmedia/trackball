# Story 2.6: Game Event Detection & Classification

## Status
🟡 **PENDING** - Advanced game event detection and classification system with machine learning models and confidence scoring

## Story
**As a** coach,
**I want** automated detection and classification of game events with confidence scoring,
**so that** key moments (goals, shots, passes, tackles) are automatically identified for review.

## Acceptance Criteria
1. Machine learning models for event classification (goals, shots, passes, tackles) ⏳
2. Confidence scoring system with configurable threshold settings ⏳
3. Temporal event marking with precise timestamp coordinates ⏳
4. Event metadata export including type, confidence, and video coordinates ⏳
5. Visual event markers in video player timeline interface ⏳
6. Custom event type configuration for different sports ⏳
7. Event detection accuracy validation and continuous model improvement ⏳
8. Integration with tracking data for enhanced event context ⏳

## Tasks / Subtasks

- [ ] **Task 2.6.1: Machine Learning Models for Event Classification** ⏳
  - [ ] Design and implement CNN-LSTM architecture for temporal event recognition
  - [ ] Create sports-specific event classification models for soccer, football, basketball
  - [ ] Implement transfer learning from general action recognition models to sports domain
  - [ ] Add ensemble methods combining multiple model predictions for improved accuracy
  - [ ] Create multi-modal event detection using visual, audio, and tracking data fusion
  - [ ] Implement attention mechanisms for focusing on relevant temporal sequences
  - [ ] Add data augmentation strategies for sports event training data
  - [ ] Create model optimization techniques including quantization and pruning
  - [ ] Implement active learning for continuous model improvement with user feedback
  - [ ] Add cross-validation and hyperparameter optimization for model training
  - [ ] Create model versioning and A/B testing framework for production deployment
  - [ ] Implement model interpretability features with attention visualization
  - [ ] Add model robustness testing with adversarial examples and edge cases
  - [ ] Create model benchmarking against industry standards and datasets
  - [ ] Implement model deployment optimization with TensorRT and ONNX support
  - **Estimate:** 26 hours | **Priority:** Critical | **Dependencies:** Story 2.3 (tracking data)
  - **Deliverables:**
    - CNN-LSTM event classification models for multiple sports
    - Transfer learning and ensemble methods implementation
    - Multi-modal event detection with data fusion
    - Model optimization and deployment framework
    - Comprehensive benchmarking and validation system

- [ ] **Task 2.6.2: Confidence Scoring & Threshold Management** ⏳
  - [ ] Implement calibrated confidence scoring with temperature scaling and Platt scaling
  - [ ] Create dynamic threshold adjustment based on event type and game context
  - [ ] Add uncertainty quantification using Monte Carlo dropout and ensemble variance
  - [ ] Implement confidence-based event filtering with precision-recall optimization
  - [ ] Create adaptive thresholding based on user feedback and historical accuracy
  - [ ] Add confidence visualization with probability distributions and uncertainty bars
  - [ ] Implement threshold tuning interface with interactive ROC curve analysis
  - [ ] Create confidence analytics with accuracy correlation and threshold optimization
  - [ ] Add multi-class confidence normalization for consistent scoring across event types
  - [ ] Implement confidence-based active learning for model improvement
  - [ ] Create confidence-aware event ranking for priority-based review
  - [ ] Add temporal confidence smoothing for consistent event detection
  - [ ] Implement confidence threshold validation with cross-validation techniques
  - [ ] Create confidence reporting with detailed statistics and trend analysis
  - [ ] Add confidence integration with user interface for intuitive threshold setting
  - **Estimate:** 18 hours | **Priority:** Critical | **Dependencies:** Task 2.6.1
  - **Deliverables:**
    - Calibrated confidence scoring system with uncertainty quantification
    - Dynamic threshold management with adaptive optimization
    - Interactive threshold tuning interface with ROC analysis
    - Comprehensive confidence analytics and reporting
    - Confidence-aware event filtering and ranking system

- [ ] **Task 2.6.3: Temporal Event Marking & Precise Timestamping** ⏳
  - [ ] Implement high-precision temporal event localization with sub-second accuracy
  - [ ] Create event boundary detection for determining event start and end times
  - [ ] Add temporal event clustering for grouping related actions into sequences
  - [ ] Implement event duration estimation with confidence intervals
  - [ ] Create temporal consistency validation across multiple camera views
  - [ ] Add event timeline generation with hierarchical event organization
  - [ ] Implement temporal event smoothing to reduce detection noise
  - [ ] Create event synchronization with video frame timestamps
  - [ ] Add temporal event search and filtering with advanced query capabilities
  - [ ] Implement event temporal relationships analysis (before, after, during)
  - [ ] Create event frequency analysis with temporal pattern recognition
  - [ ] Add temporal event visualization with interactive timeline displays
  - [ ] Implement event temporal validation with ground truth comparison
  - [ ] Create temporal event export with multiple timestamp format support
  - [ ] Add temporal event analytics with duration and frequency statistics
  - **Estimate:** 16 hours | **Priority:** High | **Dependencies:** Task 2.6.2
  - **Deliverables:**
    - High-precision temporal event localization system
    - Event boundary detection and duration estimation
    - Temporal consistency validation and synchronization
    - Interactive event timeline with hierarchical organization
    - Comprehensive temporal analytics and export capabilities

- [ ] **Task 2.6.4: Event Metadata Generation & Export System** ⏳
  - [ ] Create comprehensive event metadata schema with extensible structure
  - [ ] Implement event context enrichment using tracking and player data
  - [ ] Add spatial event localization with field/court coordinate mapping
  - [ ] Create event participant identification and role assignment
  - [ ] Implement event outcome prediction and success probability scoring
  - [ ] Add event metadata validation and quality assessment
  - [ ] Create multiple export formats (JSON, XML, CSV) with customizable schemas
  - [ ] Implement event metadata compression and optimization for large datasets
  - [ ] Add event metadata search and indexing with full-text search capabilities
  - [ ] Create event metadata visualization with statistical summaries and charts
  - [ ] Implement event metadata integration with third-party analysis tools
  - [ ] Add event metadata versioning with change tracking and history
  - [ ] Create event metadata backup and recovery with cloud synchronization
  - [ ] Implement event metadata security with access control and encryption
  - [ ] Add event metadata analytics with pattern recognition and insights
  - **Estimate:** 14 hours | **Priority:** High | **Dependencies:** Task 2.6.3
  - **Deliverables:**
    - Comprehensive event metadata schema and generation system
    - Context enrichment with tracking and player data integration
    - Multiple export formats with customizable schemas
    - Advanced search and indexing capabilities
    - Metadata analytics and visualization tools

- [ ] **Task 2.6.5: Visual Event Markers & Timeline Integration** ⏳
  - [ ] Create interactive event markers for video player timeline integration
  - [ ] Implement event marker customization with colors, icons, and labels
  - [ ] Add event marker clustering for dense event visualization
  - [ ] Create event marker filtering and search with advanced criteria
  - [ ] Implement event marker tooltips with detailed event information
  - [ ] Add event marker animation and transitions for enhanced user experience
  - [ ] Create event marker accessibility features with keyboard navigation
  - [ ] Implement event marker synchronization across multiple video views
  - [ ] Add event marker export for external video editing tools
  - [ ] Create event marker performance optimization for large event datasets
  - [ ] Implement event marker context menus with action shortcuts
  - [ ] Add event marker grouping with hierarchical organization
  - [ ] Create event marker comparison between different analysis sessions
  - [ ] Implement event marker collaboration features with sharing and comments
  - [ ] Add event marker analytics with usage tracking and optimization insights
  - **Estimate:** 12 hours | **Priority:** High | **Dependencies:** Task 2.6.4
  - **Deliverables:**
    - Interactive event markers for video player integration
    - Customizable marker appearance and behavior
    - Advanced filtering and search capabilities
    - Accessibility and collaboration features
    - Performance optimization for large datasets

- [ ] **Task 2.6.6: Custom Event Type Configuration** ⏳
  - [ ] Create sport-specific event taxonomy with customizable categories
  - [ ] Implement custom event type creation with user-defined parameters
  - [ ] Add event type inheritance and hierarchical organization
  - [ ] Create event type validation and consistency checking
  - [ ] Implement event type templates for quick configuration
  - [ ] Add event type sharing and collaboration across teams
  - [ ] Create event type analytics with usage statistics and optimization
  - [ ] Implement event type migration and versioning support
  - [ ] Add event type documentation with examples and best practices
  - [ ] Create event type testing and validation with sample data
  - [ ] Implement event type integration with existing model architectures
  - [ ] Add event type performance monitoring with accuracy tracking
  - [ ] Create event type backup and recovery with configuration preservation
  - [ ] Implement event type API with programmatic configuration management
  - [ ] Add event type optimization with automatic parameter tuning
  - **Estimate:** 10 hours | **Priority:** Medium | **Dependencies:** Task 2.6.5
  - **Deliverables:**
    - Sport-specific event taxonomy with customization capabilities
    - User-defined event type creation and management
    - Event type templates and sharing functionality
    - Comprehensive validation and testing framework
    - API integration for programmatic configuration

- [ ] **Task 2.6.7: Continuous Model Improvement & Validation** ⏳
  - [ ] Implement automated model retraining with new event data
  - [ ] Create model performance monitoring with accuracy and drift detection
  - [ ] Add user feedback integration for model improvement with active learning
  - [ ] Implement model validation framework with comprehensive test suites
  - [ ] Create model comparison and A/B testing for performance evaluation
  - [ ] Add model explainability features with attention maps and feature importance
  - [ ] Implement model robustness testing with adversarial examples
  - [ ] Create model optimization pipeline with hyperparameter search
  - [ ] Add model deployment automation with continuous integration
  - [ ] Implement model rollback and version management for production safety
  - [ ] Create model analytics with performance trends and improvement tracking
  - [ ] Add model documentation with training procedures and configuration
  - [ ] Implement model compliance monitoring with bias detection and fairness
  - [ ] Create model backup and disaster recovery procedures
  - [ ] Add model cost optimization with resource usage analysis
  - **Estimate:** 20 hours | **Priority:** Medium | **Dependencies:** Task 2.6.6
  - **Deliverables:**
    - Automated model retraining and improvement pipeline
    - Comprehensive performance monitoring and validation
    - User feedback integration with active learning
    - Model explainability and robustness testing
    - Production deployment and rollback capabilities

## API Implementation ⏳

### Game Event Detection & Classification Endpoints (20 endpoints)
- [ ] **POST /events/detection/sessions** - Initialize event detection session
  - Request: tracking_session_id, event_types, detection_config, confidence_thresholds
  - Response: detection_session_id, initialization_status, estimated_processing_time
  - Features: Custom event types, confidence configuration, processing optimization

- [ ] **GET /events/detection/sessions/{session_id}** - Get event detection status
  - Response: detection_status, progress_percentage, detected_events_count, quality_metrics
  - Features: Real-time updates, progress tracking, quality assessment

- [ ] **POST /events/detection/sessions/{session_id}/execute** - Execute event detection
  - Request: time_range, detection_sensitivity, context_integration, batch_size
  - Response: execution_status, processing_job_id, resource_allocation
  - Features: Range selection, sensitivity tuning, context integration

- [ ] **GET /events/detection/sessions/{session_id}/results** - Get detected events
  - Response: detected_events, confidence_scores, temporal_markers, event_metadata
  - Features: Comprehensive event data, filtering, pagination, export options

- [ ] **GET /events/detection/sessions/{session_id}/events/{event_id}** - Get event details
  - Response: event_details, context_data, confidence_breakdown, related_events
  - Features: Detailed event information, context enrichment, relationship analysis

- [ ] **POST /events/detection/sessions/{session_id}/validate** - Validate detection results
  - Response: validation_results, accuracy_metrics, quality_assessment, improvement_suggestions
  - Features: Quality validation, accuracy analysis, optimization recommendations

- [ ] **POST /events/models/train** - Train custom event detection model
  - Request: training_data, model_config, training_parameters, validation_settings
  - Response: training_job_id, training_status, estimated_completion
  - Features: Custom model training, hyperparameter optimization, validation

- [ ] **GET /events/models** - List available event detection models
  - Response: available_models, model_details, performance_metrics, compatibility
  - Features: Model discovery, performance comparison, version management

- [ ] **GET /events/models/{model_id}** - Get model details and performance
  - Response: model_info, performance_metrics, training_history, deployment_status
  - Features: Model information, performance analysis, deployment tracking

- [ ] **POST /events/models/{model_id}/deploy** - Deploy model for detection
  - Request: deployment_config, resource_allocation, rollout_strategy
  - Response: deployment_status, model_endpoints, health_checks
  - Features: Model deployment, resource management, health monitoring

- [ ] **POST /events/thresholds/optimize** - Optimize confidence thresholds
  - Request: validation_data, optimization_criteria, threshold_ranges
  - Response: optimal_thresholds, performance_improvements, tuning_results
  - Features: Threshold optimization, performance analysis, automated tuning

- [ ] **GET /events/types** - Get available event types and configurations
  - Response: event_types, type_definitions, sport_specific_configs, usage_statistics
  - Features: Event type discovery, configuration options, usage insights

- [ ] **POST /events/types** - Create custom event type
  - Request: event_type_definition, validation_rules, detection_parameters
  - Response: event_type_id, validation_results, integration_status
  - Features: Custom event creation, validation, integration testing

- [ ] **PUT /events/types/{type_id}** - Update event type configuration
  - Request: updated_definition, parameter_changes, validation_requirements
  - Response: update_status, validation_results, impact_analysis
  - Features: Configuration updates, validation, impact assessment

- [ ] **GET /events/timeline/{session_id}** - Get event timeline for video player
  - Response: timeline_events, marker_data, clustering_info, visualization_settings
  - Features: Timeline integration, marker customization, clustering optimization

- [ ] **POST /events/export** - Export event data
  - Request: session_ids, export_format, data_selection, anonymization_options
  - Response: export_status, download_urls, file_information, access_tokens
  - Features: Multiple formats, data selection, privacy options

- [ ] **POST /events/feedback** - Submit event detection feedback
  - Request: event_id, feedback_type, corrections, quality_rating
  - Response: feedback_status, model_improvement_impact, contribution_tracking
  - Features: Quality feedback loop, correction submission, active learning

- [ ] **GET /events/analytics** - Get event detection analytics
  - Response: detection_statistics, accuracy_trends, usage_patterns, optimization_insights
  - Security: Team-based analytics, performance insights, usage tracking

- [ ] **POST /events/batch-detect** - Submit batch event detection job
  - Request: session_ids, detection_config, priority, notification_settings
  - Response: batch_job_id, queue_position, resource_allocation, cost_estimate
  - Features: Batch processing, cost estimation, notification management

- [ ] **DELETE /events/detection/sessions/{session_id}** - Cancel or cleanup detection session
  - Response: cleanup_status, resource_release, data_retention_info
  - Security: Session ownership validation, graceful cleanup

## Database Schema Implementation ⏳

### Event Detection Sessions and Results
```sql
-- Event detection sessions
CREATE TABLE event_detection_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tracking_session_id UUID NOT NULL REFERENCES tracking_sessions(id) ON DELETE CASCADE,
    created_by_id UUID NOT NULL REFERENCES users(id),
    model_id UUID NOT NULL REFERENCES event_detection_models(id),
    status VARCHAR(20) NOT NULL DEFAULT 'initialized'
        CHECK (status IN ('initialized', 'queued', 'processing', 'completed', 'failed', 'cancelled')),
    detection_config JSONB NOT NULL DEFAULT '{}',
    confidence_thresholds JSONB NOT NULL DEFAULT '{}',
    event_types_enabled JSONB NOT NULL DEFAULT '[]',
    total_frames INTEGER DEFAULT 0,
    processed_frames INTEGER DEFAULT 0,
    detected_events INTEGER DEFAULT 0,
    detection_quality_score DECIMAL(5, 2) DEFAULT 0.00 CHECK (detection_quality_score BETWEEN 0.00 AND 100.00),
    precision_score DECIMAL(5, 2) DEFAULT 0.00,
    recall_score DECIMAL(5, 2) DEFAULT 0.00,
    f1_score DECIMAL(5, 2) DEFAULT 0.00,
    processing_started_at TIMESTAMP WITH TIME ZONE,
    processing_completed_at TIMESTAMP WITH TIME ZONE,
    processing_duration INTEGER, -- seconds
    gpu_instance_id VARCHAR(255),
    resource_usage JSONB DEFAULT '{}',
    error_details JSONB DEFAULT '{}',
    results_s3_key VARCHAR(1024),
    visualization_s3_key VARCHAR(1024),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    INDEX idx_event_detection_sessions_tracking_id (tracking_session_id),
    INDEX idx_event_detection_sessions_status (status),
    INDEX idx_event_detection_sessions_model_id (model_id),
    INDEX idx_event_detection_sessions_quality_score (detection_quality_score),
    INDEX idx_event_detection_sessions_created_at (created_at)
);

-- Event detection models registry
CREATE TABLE event_detection_models (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    model_type VARCHAR(50) NOT NULL DEFAULT 'cnn_lstm'
        CHECK (model_type IN ('cnn_lstm', 'transformer', 'resnet3d', 'slowfast', 'x3d')),
    version VARCHAR(50) NOT NULL,
    description TEXT,
    supported_sports JSONB NOT NULL DEFAULT '[]',
    supported_event_types JSONB NOT NULL DEFAULT '[]',
    model_weights_s3_key VARCHAR(1024) NOT NULL,
    model_config JSONB NOT NULL DEFAULT '{}',
    training_dataset_info JSONB DEFAULT '{}',
    performance_metrics JSONB DEFAULT '{}',
    calibration_info JSONB DEFAULT '{}', -- for confidence calibration
    deployment_status VARCHAR(20) DEFAULT 'inactive'
        CHECK (deployment_status IN ('inactive', 'active', 'deprecated', 'retired')),
    resource_requirements JSONB DEFAULT '{}',
    inference_time_ms DECIMAL(10, 2),
    accuracy_metrics JSONB DEFAULT '{}',
    created_by_id UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    UNIQUE(name, version),
    
    -- Indexes for performance
    INDEX idx_event_models_type (model_type),
    INDEX idx_event_models_status (deployment_status),
    INDEX idx_event_models_sports (supported_sports USING GIN),
    INDEX idx_event_models_event_types (supported_event_types USING GIN),
    INDEX idx_event_models_created_at (created_at)
);

-- Detected events with detailed information
CREATE TABLE detected_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    detection_session_id UUID NOT NULL REFERENCES event_detection_sessions(id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,
    event_subtype VARCHAR(100),
    start_timestamp DECIMAL(10, 3) NOT NULL,
    end_timestamp DECIMAL(10, 3) NOT NULL,
    duration_seconds DECIMAL(10, 3) NOT NULL,
    confidence DECIMAL(5, 2) NOT NULL CHECK (confidence BETWEEN 0.00 AND 1.00),
    spatial_location JSONB DEFAULT '{}', -- field coordinates, bounding boxes
    primary_participants JSONB DEFAULT '[]', -- player IDs involved in event
    secondary_participants JSONB DEFAULT '[]', -- other relevant players
    event_context JSONB DEFAULT '{}', -- game situation, score, time
    event_outcome VARCHAR(50), -- success, failure, neutral
    outcome_confidence DECIMAL(5, 2) DEFAULT 0.00,
    detection_method VARCHAR(50) NOT NULL, -- model_prediction, rule_based, hybrid
    model_version VARCHAR(50),
    validation_status VARCHAR(20) DEFAULT 'pending'
        CHECK (validation_status IN ('pending', 'validated', 'corrected', 'rejected')),
    human_validation BOOLEAN DEFAULT FALSE,
    validation_feedback JSONB DEFAULT '{}',
    related_events JSONB DEFAULT '[]', -- IDs of related events
    event_metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    INDEX idx_detected_events_session_id (detection_session_id),
    INDEX idx_detected_events_type (event_type),
    INDEX idx_detected_events_start_timestamp (start_timestamp),
    INDEX idx_detected_events_confidence (confidence),
    INDEX idx_detected_events_validation_status (validation_status),
    INDEX idx_detected_events_participants (primary_participants USING GIN)
);
```

### Event Types and Configuration
```sql
-- Custom event type definitions
CREATE TABLE event_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) UNIQUE NOT NULL,
    display_name VARCHAR(255) NOT NULL,
    description TEXT,
    sport VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL, -- offensive, defensive, neutral, administrative
    parent_type_id UUID REFERENCES event_types(id),
    is_custom BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    detection_parameters JSONB DEFAULT '{}',
    validation_rules JSONB DEFAULT '{}',
    visualization_config JSONB DEFAULT '{}', -- colors, icons, markers
    statistical_weight DECIMAL(5, 2) DEFAULT 1.00,
    created_by_id UUID REFERENCES users(id),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    INDEX idx_event_types_sport (sport),
    INDEX idx_event_types_category (category),
    INDEX idx_event_types_parent_type (parent_type_id),
    INDEX idx_event_types_active (is_active)
);

-- Event type usage and performance statistics
CREATE TABLE event_type_statistics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_type_id UUID NOT NULL REFERENCES event_types(id) ON DELETE CASCADE,
    date_bucket DATE NOT NULL,
    team_id UUID REFERENCES teams(id) ON DELETE SET NULL,
    detection_count INTEGER DEFAULT 0,
    true_positive_count INTEGER DEFAULT 0,
    false_positive_count INTEGER DEFAULT 0,
    false_negative_count INTEGER DEFAULT 0,
    precision_score DECIMAL(5, 2) DEFAULT 0.00,
    recall_score DECIMAL(5, 2) DEFAULT 0.00,
    f1_score DECIMAL(5, 2) DEFAULT 0.00,
    avg_confidence DECIMAL(5, 2) DEFAULT 0.00,
    user_validation_rate DECIMAL(5, 2) DEFAULT 0.00,
    model_improvements_applied INTEGER DEFAULT 0,
    usage_trend VARCHAR(20), -- increasing, stable, decreasing
    
    UNIQUE(event_type_id, date_bucket, team_id),
    
    -- Indexes for performance
    INDEX idx_event_stats_type_id (event_type_id),
    INDEX idx_event_stats_date (date_bucket),
    INDEX idx_event_stats_team_id (team_id),
    INDEX idx_event_stats_precision (precision_score)
);

-- Event detection feedback and validation
CREATE TABLE event_detection_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    detected_event_id UUID NOT NULL REFERENCES detected_events(id) ON DELETE CASCADE,
    submitted_by_id UUID NOT NULL REFERENCES users(id),
    feedback_type VARCHAR(50) NOT NULL CHECK (feedback_type IN ('true_positive', 'false_positive', 'false_negative', 'timing_correction', 'participant_correction', 'type_correction')),
    original_event_data JSONB DEFAULT '{}',
    corrected_event_data JSONB DEFAULT '{}',
    feedback_comments TEXT,
    confidence_assessment INTEGER CHECK (confidence_assessment BETWEEN 1 AND 5),
    improvement_priority VARCHAR(20) DEFAULT 'medium'
        CHECK (improvement_priority IN ('low', 'medium', 'high', 'critical')),
    model_improvement_status VARCHAR(20) DEFAULT 'pending'
        CHECK (model_improvement_status IN ('pending', 'reviewed', 'incorporated', 'rejected')),
    feedback_quality_score DECIMAL(5, 2) DEFAULT 0.00,
    reviewer_id UUID REFERENCES users(id),
    reviewed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    INDEX idx_event_feedback_event_id (detected_event_id),
    INDEX idx_event_feedback_type (feedback_type),
    INDEX idx_event_feedback_priority (improvement_priority),
    INDEX idx_event_feedback_status (model_improvement_status),
    INDEX idx_event_feedback_created_at (created_at)
);
```

### Model Training and Performance Tracking
```sql
-- Event detection model training jobs
CREATE TABLE event_model_training_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    initiated_by_id UUID NOT NULL REFERENCES users(id),
    job_name VARCHAR(255) NOT NULL,
    base_model_id UUID REFERENCES event_detection_models(id),
    training_dataset_s3_key VARCHAR(1024) NOT NULL,
    validation_dataset_s3_key VARCHAR(1024),
    event_types_trained JSONB NOT NULL DEFAULT '[]',
    training_config JSONB NOT NULL DEFAULT '{}',
    hyperparameters JSONB NOT NULL DEFAULT '{}',
    data_augmentation_config JSONB DEFAULT '{}',
    status VARCHAR(20) NOT NULL DEFAULT 'queued'
        CHECK (status IN ('queued', 'preparing', 'training', 'validating', 'completed', 'failed', 'cancelled')),
    training_progress DECIMAL(5, 2) DEFAULT 0.00 CHECK (training_progress BETWEEN 0.00 AND 100.00),
    current_epoch INTEGER DEFAULT 0,
    total_epochs INTEGER NOT NULL,
    best_accuracy DECIMAL(8, 4) DEFAULT 0.0000,
    best_f1_score DECIMAL(8, 4) DEFAULT 0.0000,
    training_loss DECIMAL(12, 6),
    validation_loss DECIMAL(12, 6),
    training_metrics JSONB DEFAULT '{}',
    validation_metrics JSONB DEFAULT '{}',
    early_stopping_triggered BOOLEAN DEFAULT FALSE,
    gpu_instance_ids JSONB DEFAULT '[]',
    resource_usage JSONB DEFAULT '{}',
    training_logs_s3_key VARCHAR(1024),
    model_checkpoint_s3_key VARCHAR(1024),
    final_model_s3_key VARCHAR(1024),
    training_duration INTEGER, -- seconds
    started_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    
    -- Indexes for performance
    INDEX idx_model_training_user_id (initiated_by_id),
    INDEX idx_model_training_status (status),
    INDEX idx_model_training_event_types (event_types_trained USING GIN),
    INDEX idx_model_training_created_at (created_at)
);

-- Confidence threshold optimization results
CREATE TABLE confidence_threshold_optimizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    model_id UUID NOT NULL REFERENCES event_detection_models(id) ON DELETE CASCADE,
    event_type VARCHAR(100) NOT NULL,
    optimization_method VARCHAR(50) NOT NULL CHECK (optimization_method IN ('roc_optimization', 'precision_recall_balance', 'f1_maximization', 'custom_metric')),
    validation_dataset_s3_key VARCHAR(1024) NOT NULL,
    original_threshold DECIMAL(5, 2) NOT NULL,
    optimized_threshold DECIMAL(5, 2) NOT NULL,
    performance_improvement JSONB NOT NULL DEFAULT '{}',
    optimization_metrics JSONB DEFAULT '{}',
    cross_validation_results JSONB DEFAULT '{}',
    threshold_sensitivity_analysis JSONB DEFAULT '{}',
    applied_to_production BOOLEAN DEFAULT FALSE,
    performance_validation JSONB DEFAULT '{}',
    rollback_threshold DECIMAL(5, 2),
    optimization_job_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    applied_at TIMESTAMP WITH TIME ZONE,
    
    -- Indexes for performance
    INDEX idx_threshold_opt_model_id (model_id),
    INDEX idx_threshold_opt_event_type (event_type),
    INDEX idx_threshold_opt_method (optimization_method),
    INDEX idx_threshold_opt_applied (applied_to_production)
);
```

## Machine Learning Implementation ⏳

### Advanced Event Detection Models
```python
# Event Detection and Classification System
import torch
import torch.nn as nn
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import cv2
from transformers import VideoMAEModel
import logging

@dataclass
class EventDetectionConfig:
    model_type: str = 'cnn_lstm'
    sequence_length: int = 16  # frames
    overlap_ratio: float = 0.5
    confidence_threshold: float = 0.7
    nms_threshold: float = 0.4
    batch_size: int = 8
    num_classes: int = 10  # number of event types

class CNNLSTMEventDetector(nn.Module):
    """CNN-LSTM architecture for temporal event detection"""
    
    def __init__(self, config: EventDetectionConfig):
        super().__init__()
        self.config = config
        
        # CNN backbone for spatial feature extraction
        self.backbone = self._create_backbone()
        
        # LSTM for temporal modeling
        self.lstm = nn.LSTM(
            input_size=2048,  # ResNet feature size
            hidden_size=512,
            num_layers=2,
            batch_first=True,
            dropout=0.2,
            bidirectional=True
        )
        
        # Attention mechanism
        self.attention = nn.MultiheadAttention(
            embed_dim=1024,  # bidirectional LSTM output
            num_heads=8,
            dropout=0.1
        )
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(1024, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, config.num_classes)
        )
        
        # Confidence estimation head
        self.confidence_head = nn.Sequential(
            nn.Linear(1024, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )
        
        # Temporal localization head
        self.localization_head = nn.Sequential(
            nn.Linear(1024, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 2),  # start and end frame offsets
            nn.Sigmoid()
        )
    
    def _create_backbone(self):
        """Create CNN backbone for feature extraction"""
        import torchvision.models as models
        
        # Use pre-trained ResNet-50
        backbone = models.resnet50(pretrained=True)
        
        # Remove final classification layer
        backbone = nn.Sequential(*list(backbone.children())[:-1])
        
        # Freeze early layers
        for param in backbone[:6].parameters():
            param.requires_grad = False
        
        return backbone
    
    def forward(self, x):
        """Forward pass through the network"""
        # x shape: (batch_size, sequence_length, channels, height, width)
        batch_size, seq_len, c, h, w = x.shape
        
        # Reshape for CNN processing
        x = x.view(batch_size * seq_len, c, h, w)
        
        # Extract spatial features
        spatial_features = self.backbone(x)  # (batch_size * seq_len, 2048, 1, 1)
        spatial_features = spatial_features.view(batch_size * seq_len, -1)
        
        # Reshape back to sequence
        spatial_features = spatial_features.view(batch_size, seq_len, -1)
        
        # LSTM for temporal modeling
        lstm_out, _ = self.lstm(spatial_features)  # (batch_size, seq_len, 1024)
        
        # Apply attention mechanism
        attended_features, attention_weights = self.attention(
            lstm_out, lstm_out, lstm_out
        )
        
        # Global average pooling over sequence dimension
        pooled_features = torch.mean(attended_features, dim=1)  # (batch_size, 1024)
        
        # Generate predictions
        event_logits = self.classifier(pooled_features)
        confidence_scores = self.confidence_head(pooled_features)
        temporal_offsets = self.localization_head(pooled_features)
        
        return {
            'event_logits': event_logits,
            'confidence_scores': confidence_scores,
            'temporal_offsets': temporal_offsets,
            'attention_weights': attention_weights,
            'features': pooled_features
        }

class SportsEventDetector:
    """High-level interface for sports event detection"""
    
    def __init__(self, config: EventDetectionConfig):
        self.config = config
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.logger = logging.getLogger(__name__)
        
        # Load model
        self.model = CNNLSTMEventDetector(config)
        self.model.to(self.device)
        
        # Event type mapping
        self.event_types = self._load_event_types()
        
        # Confidence calibration
        self.confidence_calibrator = ConfidenceCalibrator()
        
        # Post-processing
        self.post_processor = EventPostProcessor()
        
    async def detect_events(self, video_frames: List[np.ndarray],
                          tracking_data: Dict) -> List[DetectedEvent]:
        """Detect events in video sequence with tracking integration"""
        
        # Preprocess video frames
        preprocessed_frames = self._preprocess_frames(video_frames)
        
        # Create sliding windows
        windows = self._create_sliding_windows(preprocessed_frames)
        
        # Batch processing
        all_detections = []
        for batch in self._create_batches(windows):
            batch_detections = await self._process_batch(batch, tracking_data)
            all_detections.extend(batch_detections)
        
        # Post-process detections
        final_events = await self.post_processor.process_detections(
            all_detections, tracking_data
        )
        
        return final_events
    
    def _preprocess_frames(self, frames: List[np.ndarray]) -> torch.Tensor:
        """Preprocess video frames for model input"""
        processed_frames = []
        
        for frame in frames:
            # Resize to model input size
            resized = cv2.resize(frame, (224, 224))
            
            # Normalize
            normalized = resized.astype(np.float32) / 255.0
            normalized = (normalized - np.array([0.485, 0.456, 0.406])) / np.array([0.229, 0.224, 0.225])
            
            # Convert to tensor
            tensor = torch.from_numpy(normalized).permute(2, 0, 1)
            processed_frames.append(tensor)
        
        return torch.stack(processed_frames)
    
    def _create_sliding_windows(self, frames: torch.Tensor) -> List[torch.Tensor]:
        """Create overlapping sliding windows for temporal analysis"""
        windows = []
        step_size = int(self.config.sequence_length * (1 - self.config.overlap_ratio))
        
        for i in range(0, len(frames) - self.config.sequence_length + 1, step_size):
            window = frames[i:i + self.config.sequence_length]
            windows.append(window)
        
        return windows
    
    async def _process_batch(self, batch: List[torch.Tensor],
                           tracking_data: Dict) -> List[RawDetection]:
        """Process batch of video windows"""
        
        # Stack windows into batch tensor
        batch_tensor = torch.stack(batch).to(self.device)
        
        # Model inference
        with torch.no_grad():
            outputs = self.model(batch_tensor)
        
        # Extract predictions
        event_probs = torch.softmax(outputs['event_logits'], dim=1)
        confidence_scores = outputs['confidence_scores']
        temporal_offsets = outputs['temporal_offsets']
        attention_weights = outputs['attention_weights']
        
        # Convert to detections
        detections = []
        for i in range(len(batch)):
            for class_idx, prob in enumerate(event_probs[i]):
                if prob > self.config.confidence_threshold:
                    detection = RawDetection(
                        window_index=i,
                        event_type=self.event_types[class_idx],
                        probability=float(prob),
                        confidence=float(confidence_scores[i]),
                        temporal_offset=temporal_offsets[i],
                        attention_weights=attention_weights[i],
                        tracking_context=self._extract_tracking_context(
                            tracking_data, i
                        )
                    )
                    detections.append(detection)
        
        return detections

class ConfidenceCalibrator:
    """Calibrate model confidence scores for better reliability"""
    
    def __init__(self):
        self.temperature_scaling = TemperatureScaling()
        self.platt_scaling = PlattScaling()
        self.calibration_method = 'temperature_scaling'
        
    def calibrate_confidence(self, logits: torch.Tensor,
                           confidence_scores: torch.Tensor) -> torch.Tensor:
        """Apply confidence calibration to model outputs"""
        
        if self.calibration_method == 'temperature_scaling':
            calibrated_logits = self.temperature_scaling(logits)
            calibrated_probs = torch.softmax(calibrated_logits, dim=1)
            
            # Combine with confidence scores
            calibrated_confidence = calibrated_probs.max(dim=1)[0] * confidence_scores.squeeze()
            
        elif self.calibration_method == 'platt_scaling':
            calibrated_confidence = self.platt_scaling(
                logits.max(dim=1)[0], confidence_scores.squeeze()
            )
        
        return calibrated_confidence
    
    def fit_calibration(self, validation_logits: torch.Tensor,
                       validation_confidence: torch.Tensor,
                       true_labels: torch.Tensor):
        """Fit calibration parameters on validation data"""
        
        if self.calibration_method == 'temperature_scaling':
            self.temperature_scaling.fit(validation_logits, true_labels)
        elif self.calibration_method == 'platt_scaling':
            self.platt_scaling.fit(
                validation_logits.max(dim=1)[0],
                validation_confidence.squeeze(),
                true_labels
            )

class EventPostProcessor:
    """Post-process raw detections into final events"""
    
    def __init__(self):
        self.nms_processor = NonMaximumSuppression()
        self.temporal_smoother = TemporalSmoother()
        self.context_enricher = ContextEnricher()
        
    async def process_detections(self, raw_detections: List[RawDetection],
                               tracking_data: Dict) -> List[DetectedEvent]:
        """Process raw detections into final events"""
        
        # Group detections by event type
        grouped_detections = self._group_by_event_type(raw_detections)
        
        processed_events = []
        for event_type, detections in grouped_detections.items():
            # Apply non-maximum suppression
            nms_detections = self.nms_processor.apply(detections)
            
            # Temporal smoothing
            smoothed_detections = self.temporal_smoother.smooth(nms_detections)
            
            # Context enrichment
            enriched_events = await self.context_enricher.enrich(
                smoothed_detections, tracking_data
            )
            
            processed_events.extend(enriched_events)
        
        # Sort by timestamp
        processed_events.sort(key=lambda x: x.start_timestamp)
        
        return processed_events
    
    def _group_by_event_type(self, detections: List[RawDetection]) -> Dict:
        """Group detections by event type"""
        grouped = {}
        for detection in detections:
            event_type = detection.event_type
            if event_type not in grouped:
                grouped[event_type] = []
            grouped[event_type].append(detection)
        
        return grouped

class ContextEnricher:
    """Enrich events with contextual information from tracking data"""
    
    async def enrich(self, detections: List[RawDetection],
                   tracking_data: Dict) -> List[DetectedEvent]:
        """Enrich detections with tracking context"""
        
        enriched_events = []
        for detection in detections:
            # Extract relevant tracking information
            participants = self._identify_participants(detection, tracking_data)
            spatial_context = self._extract_spatial_context(detection, tracking_data)
            game_context = self._extract_game_context(detection, tracking_data)
            
            # Create enriched event
            event = DetectedEvent(
                event_type=detection.event_type,
                start_timestamp=detection.start_timestamp,
                end_timestamp=detection.end_timestamp,
                confidence=detection.confidence,
                spatial_location=spatial_context,
                primary_participants=participants['primary'],
                secondary_participants=participants['secondary'],
                event_context=game_context,
                detection_metadata={
                    'model_confidence': detection.confidence,
                    'attention_weights': detection.attention_weights,
                    'detection_method': 'cnn_lstm'
                }
            )
            
            enriched_events.append(event)
        
        return enriched_events
    
    def _identify_participants(self, detection: RawDetection,
                             tracking_data: Dict) -> Dict:
        """Identify players involved in the event"""
        
        # Find players near the event location and time
        event_time = detection.start_timestamp
        event_location = detection.spatial_location
        
        primary_participants = []
        secondary_participants = []
        
        for track_id, track_data in tracking_data.items():
            # Find track position at event time
            track_position = self._interpolate_track_position(
                track_data, event_time
            )
            
            if track_position:
                distance = self._calculate_distance(event_location, track_position)
                
                if distance < 2.0:  # Primary participant threshold (meters)
                    primary_participants.append(track_id)
                elif distance < 5.0:  # Secondary participant threshold
                    secondary_participants.append(track_id)
        
        return {
            'primary': primary_participants,
            'secondary': secondary_participants
        }
```

## Performance Optimization ⏳

### Model Optimization and Inference
- [ ] **Model Acceleration**
  - TensorRT optimization for GPU inference acceleration
  - Model quantization (INT8, FP16) for faster processing
  - ONNX conversion for cross-platform deployment
  - Dynamic batching for optimal GPU utilization
  - Model distillation for smaller, faster models

- [ ] **Memory Optimization**
  - Gradient checkpointing for training large sequences
  - Mixed precision training and inference
  - Memory-efficient attention mechanisms
  - Streaming inference for long video sequences
  - Model sharding for distributed processing

### Real-time Processing
- [ ] **Streaming Processing**
  - Online event detection with sliding windows
  - Incremental confidence updates
  - Real-time threshold adaptation
  - Low-latency model serving
  - Edge processing capabilities

## Security Implementation ⏳

### Event Detection Security
- [ ] **Data Protection**
  - Encrypted model weights and training data
  - Secure event detection result storage
  - Access control for event analytics
  - Privacy-compliant event metadata
  - Audit logging for all detection operations

- [ ] **Model Security**
  - Model integrity verification
  - Secure model deployment and updates
  - Protection against adversarial examples
  - Model explainability for transparency
  - Bias detection and mitigation

## Testing Strategy ⏳

### Event Detection Testing
- [ ] **Accuracy Testing**
  - Ground truth event dataset validation
  - Cross-sport model performance evaluation
  - Confidence calibration accuracy testing
  - Temporal localization precision validation
  - User feedback integration effectiveness

- [ ] **Performance Testing**
  - Real-time processing speed benchmarking
  - Memory usage optimization validation
  - Concurrent detection session handling
  - Model inference latency measurement
  - Batch processing efficiency testing

### Integration Testing
- [ ] **System Integration**
  - Integration with tracking data pipeline
  - Video player timeline marker integration
  - Export functionality with multiple formats
  - User feedback loop integration
  - Model retraining pipeline validation

## Monitoring and Analytics ⏳

### Event Detection Analytics
- [ ] **Accuracy Metrics**
  - Real-time detection accuracy monitoring
  - Per-event-type performance tracking
  - Confidence score distribution analysis
  - False positive/negative rate monitoring
  - User validation accuracy correlation

- [ ] **Operational Metrics**
  - Model inference speed and latency
  - GPU utilization during detection
  - Memory usage patterns and optimization
  - Detection throughput and capacity
  - Cost per detection analysis

## Definition of Done ✅
**This story is complete when:**
- ✅ Machine learning models achieve >85% accuracy across major sports event types
- ✅ Confidence scoring provides reliable quality assessment with calibrated probabilities
- ✅ Temporal event marking achieves <1 second accuracy for event timestamps
- ✅ Event metadata export includes comprehensive context and participant information
- ✅ Visual event markers integrate seamlessly with video player timeline
- ✅ Custom event types can be created and trained with reasonable accuracy
- ✅ Event detection accuracy validation shows continuous improvement over time
- ✅ Tracking data integration enhances event context and participant identification
- ✅ System processes 90-minute matches with event detection in <8 minutes
- ✅ All security requirements met with encrypted models and secure processing
- ✅ User feedback loop demonstrates measurable model improvement
- ✅ All tests pass with >95% coverage and accuracy validation

## Dependencies
- **Internal:** Story 2.3 (tracking data), Story 2.5 (processing pipeline)
- **External:** Deep learning frameworks (PyTorch, TensorFlow) with GPU support
- **External:** Sports event datasets for training and validation
- **External:** Computer vision libraries for video processing

## Risks & Mitigation
- **Risk:** Model accuracy degradation with diverse sports and conditions
- **Mitigation:** Comprehensive training data collection, transfer learning, and continuous improvement
- **Risk:** Confidence calibration issues affecting event reliability
- **Mitigation:** Multiple calibration methods, validation testing, and user feedback integration
- **Risk:** Real-time processing requirements affecting detection quality
- **Mitigation:** Model optimization, adaptive quality control, and efficient inference
- **Risk:** Custom event type creation complexity overwhelming users
- **Mitigation:** Intuitive interface design, template system, and comprehensive documentation

## Change Log
| Date | Version | Description | Author |
| :--- | :--- | :--- | :--- |
| 2025-01-23 | 1.0 | Initial story creation with comprehensive event detection system | Sarah (Product Owner) |
| 2025-01-23 | 1.1 | Added detailed ML implementation and confidence calibration | Sarah (Product Owner) |
| 2025-01-23 | 1.2 | Enhanced with performance optimization and security measures | Sarah (Product Owner) |