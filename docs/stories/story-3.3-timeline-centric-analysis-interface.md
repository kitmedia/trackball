# Story 3.3: Timeline-Centric Analysis Interface

## Status
🟡 **PENDING** - Master timeline interface with event markers, annotations, and comprehensive analysis navigation

## Story
**As a** coach,
**I want** all analysis interactions centered around a master timeline,
**so that** I can efficiently navigate through footage and access analysis tools.

## Acceptance Criteria
1. Master timeline interface with event markers and analysis annotations ⏳
2. Automatic event detection markers (goals, shots, passes, tackles) on timeline ⏳
3. Custom annotation creation with drag-and-drop timeline positioning ⏳
4. Zoom-in/zoom-out timeline controls for different granularity levels ⏳
5. Multi-layer timeline showing different data types (events, formations, statistics) ⏳
6. Timeline search and filtering by event type, player, or time period ⏳
7. Contextual right-click menus for quick clip creation and annotation tools ⏳
8. Timeline state preservation and sharing capabilities between team members ⏳

## Tasks / Subtasks

- [ ] **Task 3.3.1: Master Timeline Interface Architecture** ⏳
  - [ ] Design scalable timeline architecture with virtualized rendering for long videos
  - [ ] Implement timeline canvas with efficient drawing and interaction handling
  - [ ] Create timeline synchronization with video player and overlay systems
  - [ ] Add timeline responsive design for different screen sizes and orientations
  - [ ] Implement timeline keyboard navigation with professional editing shortcuts
  - [ ] Create timeline accessibility features with screen reader and keyboard support
  - [ ] Add timeline performance optimization with smooth scrolling and zooming
  - [ ] Implement timeline state management with undo/redo functionality
  - [ ] Create timeline customization with user preference settings
  - [ ] Add timeline integration with video player controls and overlays
  - [ ] Implement timeline error handling with graceful fallback rendering
  - [ ] Create timeline analytics with usage tracking and interaction metrics
  - [ ] Add timeline testing framework with automated interaction validation
  - [ ] Implement timeline documentation with user guides and examples
  - [ ] Create timeline localization support for international users
  - **Estimate:** 24 hours | **Priority:** Critical | **Dependencies:** Story 3.1 (video player)
  - **Deliverables:**
    - Scalable timeline architecture with virtualized rendering
    - Comprehensive synchronization with video player and overlays
    - Professional keyboard navigation and accessibility support
    - Performance optimization with smooth interactions
    - Complete state management and customization system

- [ ] **Task 3.3.2: Automatic Event Detection & Timeline Markers** ⏳
  - [ ] Integrate AI event detection results with timeline visualization
  - [ ] Create dynamic event marker rendering with different types and styles
  - [ ] Implement event marker clustering for dense event periods
  - [ ] Add event marker confidence visualization with color coding
  - [ ] Create event marker interaction with hover details and click navigation
  - [ ] Implement event marker filtering with type-based visibility controls
  - [ ] Add event marker search functionality with text and metadata queries
  - [ ] Create event marker validation with ground truth comparison
  - [ ] Implement event marker editing with manual correction capabilities
  - [ ] Add event marker statistics with frequency and distribution analysis
  - [ ] Create event marker export with detailed metadata and timestamps
  - [ ] Implement event marker synchronization across multiple timeline layers
  - [ ] Add event marker performance optimization for large datasets
  - [ ] Create event marker customization with user-defined types and styles
  - [ ] Implement event marker analytics with accuracy tracking and improvement
  - **Estimate:** 20 hours | **Priority:** Critical | **Dependencies:** Story 2.6 (event detection)
  - **Deliverables:**
    - AI event detection integration with timeline visualization
    - Dynamic marker rendering with clustering and confidence display
    - Comprehensive interaction and filtering capabilities
    - Event validation and manual correction tools
    - Performance optimization for large event datasets

- [ ] **Task 3.3.3: Custom Annotation System & Drag-Drop Interface** ⏳
  - [ ] Create intuitive annotation creation interface with drag-and-drop positioning
  - [ ] Implement rich text annotation editor with formatting and media support
  - [ ] Add annotation types (text, drawing, voice, video clips, tactical diagrams)
  - [ ] Create annotation timeline positioning with precise timestamp control
  - [ ] Implement annotation visualization with different display modes
  - [ ] Add annotation collaboration features with team sharing and comments
  - [ ] Create annotation search functionality with content and metadata queries
  - [ ] Implement annotation templates for common tactical analysis scenarios
  - [ ] Add annotation export capabilities with multiple format support
  - [ ] Create annotation validation with content quality assessment
  - [ ] Implement annotation versioning with change tracking and history
  - [ ] Add annotation integration with AI analysis for automated suggestions
  - [ ] Create annotation performance optimization for large annotation datasets
  - [ ] Implement annotation security with access control and permissions
  - [ ] Add annotation analytics with usage patterns and effectiveness tracking
  - **Estimate:** 22 hours | **Priority:** High | **Dependencies:** Task 3.3.2
  - **Deliverables:**
    - Comprehensive annotation creation and editing system
    - Drag-and-drop interface with precise timeline positioning
    - Multiple annotation types with rich content support
    - Collaboration features with team sharing and commenting
    - Performance optimization and security implementation

- [ ] **Task 3.3.4: Multi-level Timeline Zoom & Granularity Control** ⏳
  - [ ] Implement smooth timeline zooming with different granularity levels (seconds, minutes, periods)
  - [ ] Create intelligent zoom presets for common analysis scenarios
  - [ ] Add zoom state persistence with user preference management
  - [ ] Implement zoom synchronization across multiple timeline layers
  - [ ] Create zoom performance optimization with efficient rendering at all scales
  - [ ] Add zoom accessibility features with keyboard navigation and screen reader support
  - [ ] Implement zoom animation with smooth transitions and momentum scrolling
  - [ ] Create zoom indicators with current scale display and navigation breadcrumbs
  - [ ] Add zoom integration with video player seeking and overlay rendering
  - [ ] Implement zoom testing with automated validation at different scales
  - [ ] Create zoom customization with user-defined scales and preferences
  - [ ] Add zoom analytics with usage patterns and preferred scales tracking
  - [ ] Implement zoom performance monitoring with render time and memory usage
  - [ ] Create zoom documentation with user guides and best practices
  - [ ] Add zoom integration with timeline search and filtering functionality
  - **Estimate:** 16 hours | **Priority:** High | **Dependencies:** Task 3.3.3
  - **Deliverables:**
    - Smooth multi-level timeline zooming with intelligent presets
    - Comprehensive zoom state management and synchronization
    - Performance optimization with efficient rendering at all scales
    - Accessibility features and smooth animation support
    - Integration with video player and search functionality

- [ ] **Task 3.3.5: Multi-layer Timeline Data Visualization** ⏳
  - [ ] Create layered timeline architecture with independent data streams
  - [ ] Implement event layer with game events and user annotations
  - [ ] Add formation layer with tactical shape evolution over time
  - [ ] Create statistics layer with performance metrics and trends
  - [ ] Implement player tracking layer with movement and positioning data
  - [ ] Add layer visibility controls with toggle and opacity management
  - [ ] Create layer synchronization with consistent timeline alignment
  - [ ] Implement layer interaction with cross-layer data correlation
  - [ ] Add layer customization with user-defined layer types and styling
  - [ ] Create layer performance optimization with efficient rendering pipeline
  - [ ] Implement layer export capabilities with selective data inclusion
  - [ ] Add layer analytics with usage patterns and interaction tracking
  - [ ] Create layer validation with data consistency checking
  - [ ] Implement layer testing framework with automated data verification
  - [ ] Add layer documentation with configuration guides and examples
  - **Estimate:** 26 hours | **Priority:** High | **Dependencies:** Task 3.3.4
  - **Deliverables:**
    - Multi-layer timeline architecture with independent data streams
    - Comprehensive layer management with visibility and interaction controls
    - Performance optimization with efficient multi-layer rendering
    - Cross-layer data correlation and synchronization
    - Complete customization and export capabilities

- [ ] **Task 3.3.6: Advanced Timeline Search & Filtering System** ⏳
  - [ ] Implement comprehensive search functionality with text, metadata, and temporal queries
  - [ ] Create advanced filtering interface with multiple criteria and logical operators
  - [ ] Add search result highlighting with context preservation on timeline
  - [ ] Implement search history management with saved queries and favorites
  - [ ] Create real-time search with instant results and progressive filtering
  - [ ] Add search integration with AI analysis for intelligent query suggestions
  - [ ] Implement search performance optimization with indexing and caching
  - [ ] Create search accessibility features with keyboard navigation and screen reader support
  - [ ] Add search analytics with query patterns and result effectiveness tracking
  - [ ] Implement search export capabilities with filtered timeline data
  - [ ] Create search validation with query syntax checking and error handling
  - [ ] Add search customization with user-defined filters and search presets
  - [ ] Implement search integration with annotation and event detection systems
  - [ ] Create search documentation with query syntax guides and examples
  - [ ] Add search testing framework with automated query and result validation
  - **Estimate:** 18 hours | **Priority:** Medium | **Dependencies:** Task 3.3.5
  - **Deliverables:**
    - Comprehensive search system with advanced filtering capabilities
    - Real-time search with intelligent suggestions and result highlighting
    - Performance optimization with indexing and caching
    - Integration with AI analysis and annotation systems
    - Complete analytics and customization features

- [ ] **Task 3.3.7: Contextual Menus & Quick Action Tools** ⏳
  - [ ] Create contextual right-click menus with timeline-specific actions
  - [ ] Implement quick clip creation with drag-select timeline range
  - [ ] Add instant annotation creation with context-aware templates
  - [ ] Create bookmark and marker creation tools with one-click actions
  - [ ] Implement navigation shortcuts with jump-to-event and seek controls
  - [ ] Add sharing tools with timeline position and context preservation
  - [ ] Create analysis shortcuts with direct access to statistical views
  - [ ] Implement export tools with timeline range and layer selection
  - [ ] Add collaboration tools with team member notification and sharing
  - [ ] Create customization tools with timeline appearance and behavior settings
  - [ ] Implement validation tools with data quality checking and error reporting
  - [ ] Add integration tools with external systems and workflow connections
  - [ ] Create accessibility tools with alternative interaction methods
  - [ ] Implement performance tools with rendering optimization and debugging
  - [ ] Add analytics integration with action tracking and usage optimization
  - **Estimate:** 14 hours | **Priority:** Medium | **Dependencies:** Task 3.3.6
  - **Deliverables:**
    - Comprehensive contextual menu system with timeline-specific actions
    - Quick action tools for clip creation, annotation, and navigation
    - Integration with sharing, collaboration, and export functionality
    - Customization tools with appearance and behavior settings
    - Performance and analytics integration for optimization

- [ ] **Task 3.3.8: Timeline State Management & Team Sharing** ⏳
  - [ ] Implement comprehensive timeline state serialization and persistence
  - [ ] Create timeline sharing functionality with team member access control
  - [ ] Add collaborative timeline editing with real-time synchronization
  - [ ] Implement timeline versioning with change tracking and rollback capabilities
  - [ ] Create timeline conflict resolution with merge and override options
  - [ ] Add timeline backup and recovery with automatic and manual saves
  - [ ] Implement timeline access control with role-based permissions
  - [ ] Create timeline audit logging with detailed change history
  - [ ] Add timeline integration with team management and notification systems
  - [ ] Implement timeline performance optimization for collaborative scenarios
  - [ ] Create timeline security with encryption and access validation
  - [ ] Add timeline analytics with collaboration patterns and effectiveness tracking
  - [ ] Implement timeline testing with multi-user scenario validation
  - [ ] Create timeline documentation with sharing workflows and best practices
  - [ ] Add timeline integration with external collaboration platforms
  - **Estimate:** 20 hours | **Priority:** Medium | **Dependencies:** Task 3.3.7
  - **Deliverables:**
    - Complete timeline state management with persistence and versioning
    - Team sharing functionality with real-time collaboration
    - Access control and security implementation
    - Conflict resolution and change tracking system
    - Integration with team management and external platforms

## API Implementation ⏳

### Timeline & Analysis Endpoints (16 endpoints)
- [ ] **GET /timeline/sessions/{session_id}/events** - Get timeline events and markers
  - Request: time_range, event_types, confidence_threshold, layer_filter
  - Response: events_data, markers, annotations, metadata
  - Features: Multi-layer data, filtering, confidence scoring

- [ ] **POST /timeline/sessions/{session_id}/annotations** - Create timeline annotation
  - Request: timestamp, annotation_type, content, position, styling
  - Response: annotation_id, creation_status, collaboration_info
  - Features: Rich content, collaborative editing, template support

- [ ] **PUT /timeline/annotations/{annotation_id}** - Update timeline annotation
  - Request: content_updates, position_changes, styling_updates
  - Response: update_status, version_info, conflict_resolution
  - Features: Version control, conflict handling, change tracking

- [ ] **DELETE /timeline/annotations/{annotation_id}** - Delete timeline annotation
  - Response: deletion_status, backup_info, audit_log
  - Features: Soft deletion, backup preservation, audit trail

- [ ] **GET /timeline/sessions/{session_id}/layers** - Get timeline layer configuration
  - Response: layer_config, visibility_settings, data_sources, customization
  - Features: Multi-layer management, customization, data integration

- [ ] **POST /timeline/sessions/{session_id}/layers** - Configure timeline layers
  - Request: layer_settings, visibility_options, data_sources, styling
  - Response: config_id, applied_settings, validation_results
  - Features: Custom layers, data source integration, validation

- [ ] **GET /timeline/search** - Search timeline content
  - Request: query, session_id, search_filters, time_range, result_limit
  - Response: search_results, highlighted_segments, faceted_filters
  - Features: Advanced search, filtering, result highlighting

- [ ] **POST /timeline/bookmarks** - Create timeline bookmark
  - Request: session_id, timestamp, bookmark_name, description, tags
  - Response: bookmark_id, creation_status, sharing_options
  - Features: Named bookmarks, tagging, team sharing

- [ ] **GET /timeline/bookmarks/{session_id}** - Get session bookmarks
  - Response: bookmarks_list, timestamps, metadata, sharing_status
  - Features: Bookmark management, filtering, collaboration

- [ ] **POST /timeline/clips/create** - Create clip from timeline selection
  - Request: session_id, start_time, end_time, layers_included, export_options
  - Response: clip_job_id, processing_status, estimated_completion
  - Features: Multi-layer clips, custom export, processing queue

- [ ] **GET /timeline/state/{session_id}** - Get timeline state
  - Response: timeline_config, zoom_level, position, layer_visibility, annotations
  - Features: Complete state retrieval, user preferences

- [ ] **POST /timeline/state/{session_id}** - Save timeline state
  - Request: timeline_config, zoom_level, position, layer_settings, annotations
  - Response: save_status, version_info, sharing_options
  - Features: State persistence, versioning, team sharing

- [ ] **POST /timeline/share** - Share timeline configuration
  - Request: session_id, timeline_state, recipients, permissions, message
  - Response: share_id, access_url, notification_status
  - Features: Team sharing, access control, notifications

- [ ] **GET /timeline/analytics/{session_id}** - Get timeline usage analytics
  - Response: usage_statistics, interaction_patterns, performance_metrics
  - Features: Usage tracking, optimization insights, user behavior

- [ ] **POST /timeline/export** - Export timeline data
  - Request: session_id, export_format, time_range, layers, annotations
  - Response: export_job_id, processing_status, download_info
  - Features: Multiple formats, selective export, batch processing

- [ ] **GET /timeline/templates** - Get annotation and analysis templates
  - Response: template_list, categories, usage_statistics, customization_options
  - Features: Template management, categorization, user customization

## Frontend Component Architecture ⏳

### Timeline Components
```typescript
// Core timeline interfaces
interface TimelineProps {
  sessionId: string;
  duration: number;
  events: TimelineEvent[];
  annotations: TimelineAnnotation[];
  onTimeChange?: (timestamp: number) => void;
  onEventSelect?: (event: TimelineEvent) => void;
}

// Main timeline components
export const MasterTimeline: React.FC<TimelineProps>
export const TimelineLayer: React.FC<TimelineLayerProps>
export const EventMarker: React.FC<EventMarkerProps>
export const AnnotationMarker: React.FC<AnnotationMarkerProps>
export const TimelineRuler: React.FC<TimelineRulerProps>

// Navigation and control components
export const TimelineNavigator: React.FC<NavigatorProps>
export const TimelineZoomControls: React.FC<ZoomControlsProps>
export const LayerVisibilityPanel: React.FC<LayerPanelProps>
export const TimelineSearchBar: React.FC<SearchBarProps>

// Interaction components
export const ContextualMenu: React.FC<ContextMenuProps>
export const AnnotationEditor: React.FC<AnnotationEditorProps>
export const ClipCreationTool: React.FC<ClipCreationProps>
export const BookmarkManager: React.FC<BookmarkManagerProps>

// Analysis components
export const FormationTimeline: React.FC<FormationTimelineProps>
export const StatisticsTimeline: React.FC<StatisticsTimelineProps>
export const PlayerTrackingTimeline: React.FC<PlayerTimelineProps>
```

### Timeline State Management
```typescript
interface TimelineState {
  // Timeline configuration
  currentTime: number;
  duration: number;
  zoomLevel: number;
  viewportStart: number;
  viewportEnd: number;
  
  // Layer management
  layers: TimelineLayer[];
  layerVisibility: Record<string, boolean>;
  layerOpacity: Record<string, number>;
  activeLayer: string | null;
  
  // Data state
  events: TimelineEvent[];
  annotations: TimelineAnnotation[];
  bookmarks: TimelineBookmark[];
  searchResults: SearchResult[];
  
  // Interaction state
  selectedEvents: string[];
  selectedAnnotations: string[];
  hoveredElement: TimelineElement | null;
  selectionRange: TimeRange | null;
  
  // UI state
  showRuler: boolean;
  showGrid: boolean;
  contextMenu: ContextMenuState | null;
  searchQuery: string;
  
  // Collaboration state
  collaborators: Collaborator[];
  sharedState: SharedTimelineState;
  conflictResolution: ConflictResolution[];
  
  // Actions
  setCurrentTime: (time: number) => void;
  setZoomLevel: (level: number, center?: number) => void;
  toggleLayerVisibility: (layerId: string) => void;
  createAnnotation: (annotation: CreateAnnotationRequest) => void;
  selectEvents: (eventIds: string[]) => void;
  createClip: (range: TimeRange) => void;
  search: (query: string) => void;
  
  // Collaboration actions
  shareTimeline: (recipients: string[]) => void;
  resolveConflict: (conflictId: string, resolution: Resolution) => void;
  syncWithTeam: () => void;
}
```

## Timeline Implementation ⏳

### Master Timeline Component
```typescript
// Master Timeline with Multi-layer Support
import React, { useRef, useEffect, useState, useCallback } from 'react';
import { TimelineState, TimelineProps, TimelineEvent, TimelineLayer } from './types';

export const MasterTimeline: React.FC<TimelineProps> = ({
  sessionId,
  duration,
  events,
  annotations,
  onTimeChange,
  onEventSelect
}) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const [timelineState, setTimelineState] = useState<TimelineState>({
    currentTime: 0,
    duration,
    zoomLevel: 1,
    viewportStart: 0,
    viewportEnd: duration,
    layers: [
      { id: 'events', name: 'Events', type: 'events', visible: true, height: 60 },
      { id: 'annotations', name: 'Annotations', type: 'annotations', visible: true, height: 40 },
      { id: 'formations', name: 'Formations', type: 'formations', visible: true, height: 80 },
      { id: 'statistics', name: 'Statistics', type: 'statistics', visible: false, height: 100 }
    ],
    layerVisibility: {
      events: true,
      annotations: true,
      formations: true,
      statistics: false
    },
    events,
    annotations,
    bookmarks: [],
    searchResults: [],
    selectedEvents: [],
    selectedAnnotations: [],
    hoveredElement: null,
    selectionRange: null,
    showRuler: true,
    showGrid: true,
    contextMenu: null,
    searchQuery: '',
    collaborators: [],
    sharedState: {},
    conflictResolution: []
  });

  // Timeline rendering with virtualized content
  const renderTimeline = useCallback((ctx: CanvasRenderingContext2D, width: number, height: number) => {
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Calculate viewport and zoom parameters
    const pixelsPerSecond = (width * timelineState.zoomLevel) / duration;
    const viewportStartTime = timelineState.viewportStart;
    const viewportEndTime = timelineState.viewportEnd;
    
    // Render timeline background and grid
    renderTimelineBackground(ctx, width, height, pixelsPerSecond, viewportStartTime);
    
    if (timelineState.showGrid) {
      renderTimelineGrid(ctx, width, height, pixelsPerSecond, viewportStartTime);
    }
    
    // Render timeline ruler
    if (timelineState.showRuler) {
      renderTimelineRuler(ctx, width, 30, pixelsPerSecond, viewportStartTime, viewportEndTime);
    }
    
    // Render layers
    let currentY = timelineState.showRuler ? 30 : 0;
    timelineState.layers.forEach(layer => {
      if (timelineState.layerVisibility[layer.id]) {
        renderTimelineLayer(
          ctx,
          layer,
          0,
          currentY,
          width,
          layer.height,
          pixelsPerSecond,
          viewportStartTime,
          viewportEndTime
        );
        currentY += layer.height;
      }
    });
    
    // Render current time indicator
    renderCurrentTimeIndicator(
      ctx,
      timelineState.currentTime,
      pixelsPerSecond,
      viewportStartTime,
      height
    );
    
    // Render selection range
    if (timelineState.selectionRange) {
      renderSelectionRange(
        ctx,
        timelineState.selectionRange,
        pixelsPerSecond,
        viewportStartTime,
        height
      );
    }
  }, [timelineState, duration]);

  // Layer rendering with event and annotation support
  const renderTimelineLayer = (
    ctx: CanvasRenderingContext2D,
    layer: TimelineLayer,
    x: number,
    y: number,
    width: number,
    height: number,
    pixelsPerSecond: number,
    viewportStart: number,
    viewportEnd: number
  ) => {
    // Layer background
    ctx.fillStyle = layer.type === 'events' ? '#f8f9fa' : '#ffffff';
    ctx.fillRect(x, y, width, height);
    
    // Layer border
    ctx.strokeStyle = '#dee2e6';
    ctx.lineWidth = 1;
    ctx.strokeRect(x, y, width, height);
    
    // Layer label
    ctx.fillStyle = '#495057';
    ctx.font = '12px -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto';
    ctx.fillText(layer.name, x + 8, y + 16);
    
    switch (layer.type) {
      case 'events':
        renderEventMarkers(ctx, timelineState.events, x, y, width, height, pixelsPerSecond, viewportStart, viewportEnd);
        break;
      case 'annotations':
        renderAnnotationMarkers(ctx, timelineState.annotations, x, y, width, height, pixelsPerSecond, viewportStart, viewportEnd);
        break;
      case 'formations':
        renderFormationData(ctx, x, y, width, height, pixelsPerSecond, viewportStart, viewportEnd);
        break;
      case 'statistics':
        renderStatisticsData(ctx, x, y, width, height, pixelsPerSecond, viewportStart, viewportEnd);
        break;
    }
  };

  // Event marker rendering with clustering
  const renderEventMarkers = (
    ctx: CanvasRenderingContext2D,
    events: TimelineEvent[],
    x: number,
    y: number,
    width: number,
    height: number,
    pixelsPerSecond: number,
    viewportStart: number,
    viewportEnd: number
  ) => {
    // Filter events in viewport
    const visibleEvents = events.filter(event => 
      event.timestamp >= viewportStart && event.timestamp <= viewportEnd
    );
    
    // Cluster nearby events if zoom level is low
    const clusteredEvents = timelineState.zoomLevel < 0.1 
      ? clusterEvents(visibleEvents, pixelsPerSecond)
      : visibleEvents.map(event => ({ events: [event], timestamp: event.timestamp }));
    
    clusteredEvents.forEach(cluster => {
      const eventX = x + (cluster.timestamp - viewportStart) * pixelsPerSecond;
      
      if (cluster.events.length === 1) {
        // Single event marker
        const event = cluster.events[0];
        const markerColor = getEventColor(event.type);
        const isSelected = timelineState.selectedEvents.includes(event.id);
        const isHovered = timelineState.hoveredElement?.id === event.id;
        
        renderEventMarker(ctx, eventX, y + height / 2, markerColor, isSelected, isHovered, event.confidence);
      } else {
        // Clustered events marker
        renderClusteredEventMarker(ctx, eventX, y + height / 2, cluster.events.length);
      }
    });
  };

  // Individual event marker rendering
  const renderEventMarker = (
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    color: string,
    isSelected: boolean,
    isHovered: boolean,
    confidence: number = 1.0
  ) => {
    const radius = isHovered ? 8 : (isSelected ? 7 : 6);
    
    // Confidence ring
    if (confidence < 0.8) {
      ctx.beginPath();
      ctx.arc(x, y, radius + 3, 0, 2 * Math.PI);
      ctx.strokeStyle = `rgba(255, 193, 7, ${0.5 + (1 - confidence) * 0.5})`;
      ctx.lineWidth = 2;
      ctx.stroke();
    }
    
    // Main marker
    ctx.beginPath();
    ctx.arc(x, y, radius, 0, 2 * Math.PI);
    ctx.fillStyle = color;
    ctx.fill();
    
    // Selection indicator
    if (isSelected) {
      ctx.strokeStyle = '#007bff';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
    
    // Hover indicator
    if (isHovered) {
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1;
      ctx.stroke();
    }
  };

  // Zoom controls with smooth transitions
  const handleZoom = useCallback((delta: number, centerTime?: number) => {
    const newZoomLevel = Math.max(0.01, Math.min(100, timelineState.zoomLevel * (1 + delta)));
    const center = centerTime ?? (timelineState.viewportStart + timelineState.viewportEnd) / 2;
    
    // Calculate new viewport to keep center point stable
    const viewportDuration = (timelineState.viewportEnd - timelineState.viewportStart) / newZoomLevel * timelineState.zoomLevel;
    const newViewportStart = Math.max(0, center - viewportDuration / 2);
    const newViewportEnd = Math.min(duration, newViewportStart + viewportDuration);
    
    setTimelineState(prev => ({
      ...prev,
      zoomLevel: newZoomLevel,
      viewportStart: newViewportStart,
      viewportEnd: newViewportEnd
    }));
  }, [timelineState, duration]);

  // Mouse interaction handling
  const handleMouseMove = useCallback((event: React.MouseEvent) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    // Convert pixel position to timestamp
    const pixelsPerSecond = (canvas.width * timelineState.zoomLevel) / duration;
    const timestamp = timelineState.viewportStart + (x / pixelsPerSecond);
    
    // Hit testing for timeline elements
    const hoveredElement = performTimelineHitTest(x, y, timelineState);
    
    if (hoveredElement !== timelineState.hoveredElement) {
      setTimelineState(prev => ({ ...prev, hoveredElement }));
    }
  }, [timelineState, duration]);

  const handleMouseClick = useCallback((event: React.MouseEvent) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    // Convert pixel position to timestamp
    const pixelsPerSecond = (canvas.width * timelineState.zoomLevel) / duration;
    const timestamp = timelineState.viewportStart + (x / pixelsPerSecond);
    
    // Handle element selection
    const clickedElement = performTimelineHitTest(x, y, timelineState);
    
    if (clickedElement) {
      if (clickedElement.type === 'event') {
        const eventId = clickedElement.id;
        const isSelected = timelineState.selectedEvents.includes(eventId);
        
        if (event.ctrlKey || event.metaKey) {
          // Multi-select
          setTimelineState(prev => ({
            ...prev,
            selectedEvents: isSelected
              ? prev.selectedEvents.filter(id => id !== eventId)
              : [...prev.selectedEvents, eventId]
          }));
        } else {
          // Single select
          setTimelineState(prev => ({
            ...prev,
            selectedEvents: [eventId],
            selectedAnnotations: []
          }));
          
          const event = timelineState.events.find(e => e.id === eventId);
          if (event) {
            onEventSelect?.(event);
          }
        }
      }
    } else {
      // Timeline navigation
      setTimelineState(prev => ({ ...prev, currentTime: timestamp }));
      onTimeChange?.(timestamp);
    }
  }, [timelineState, duration, onTimeChange, onEventSelect]);

  // Context menu handling
  const handleContextMenu = useCallback((event: React.MouseEvent) => {
    event.preventDefault();
    
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const rect = canvas.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    const pixelsPerSecond = (canvas.width * timelineState.zoomLevel) / duration;
    const timestamp = timelineState.viewportStart + (x / pixelsPerSecond);
    
    const contextElement = performTimelineHitTest(x, y, timelineState);
    
    setTimelineState(prev => ({
      ...prev,
      contextMenu: {
        x: event.clientX,
        y: event.clientY,
        timestamp,
        element: contextElement,
        visible: true
      }
    }));
  }, [timelineState, duration]);

  // Keyboard shortcuts
  const handleKeyDown = useCallback((event: KeyboardEvent) => {
    if (event.target !== document.body) return;
    
    switch (event.code) {
      case 'Space':
        event.preventDefault();
        // Toggle play/pause (handled by parent)
        break;
        
      case 'ArrowLeft':
        event.preventDefault();
        if (event.shiftKey) {
          // Frame-by-frame
          const newTime = Math.max(0, timelineState.currentTime - 1/30);
          setTimelineState(prev => ({ ...prev, currentTime: newTime }));
          onTimeChange?.(newTime);
        } else {
          // 10 second jump
          const newTime = Math.max(0, timelineState.currentTime - 10);
          setTimelineState(prev => ({ ...prev, currentTime: newTime }));
          onTimeChange?.(newTime);
        }
        break;
        
      case 'ArrowRight':
        event.preventDefault();
        if (event.shiftKey) {
          // Frame-by-frame
          const newTime = Math.min(duration, timelineState.currentTime + 1/30);
          setTimelineState(prev => ({ ...prev, currentTime: newTime }));
          onTimeChange?.(newTime);
        } else {
          // 10 second jump
          const newTime = Math.min(duration, timelineState.currentTime + 10);
          setTimelineState(prev => ({ ...prev, currentTime: newTime }));
          onTimeChange?.(newTime);
        }
        break;
        
      case 'Equal':
      case 'NumpadAdd':
        event.preventDefault();
        handleZoom(0.2);
        break;
        
      case 'Minus':
      case 'NumpadSubtract':
        event.preventDefault();
        handleZoom(-0.2);
        break;
        
      case 'KeyA':
        if (event.ctrlKey || event.metaKey) {
          event.preventDefault();
          // Select all events
          setTimelineState(prev => ({
            ...prev,
            selectedEvents: prev.events.map(e => e.id)
          }));
        }
        break;
    }
  }, [timelineState, duration, onTimeChange, handleZoom]);

  // Canvas rendering loop
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    const render = () => {
      renderTimeline(ctx, canvas.width, canvas.height);
    };
    
    render();
  }, [renderTimeline]);

  // Event listeners
  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleKeyDown]);

  return (
    <div className="master-timeline">
      <div className="timeline-header">
        <TimelineZoomControls
          zoomLevel={timelineState.zoomLevel}
          onZoomChange={handleZoom}
        />
        <LayerVisibilityPanel
          layers={timelineState.layers}
          visibility={timelineState.layerVisibility}
          onVisibilityChange={(layerId, visible) => {
            setTimelineState(prev => ({
              ...prev,
              layerVisibility: { ...prev.layerVisibility, [layerId]: visible }
            }));
          }}
        />
        <TimelineSearchBar
          query={timelineState.searchQuery}
          onSearch={(query) => {
            setTimelineState(prev => ({ ...prev, searchQuery: query }));
            // Implement search functionality
          }}
        />
      </div>
      
      <div ref={scrollContainerRef} className="timeline-container">
        <canvas
          ref={canvasRef}
          className="timeline-canvas"
          width={1200}
          height={400}
          onMouseMove={handleMouseMove}
          onClick={handleMouseClick}
          onContextMenu={handleContextMenu}
          onWheel={(e) => {
            e.preventDefault();
            const delta = e.deltaY > 0 ? -0.1 : 0.1;
            handleZoom(delta, timelineState.currentTime);
          }}
        />
      </div>
      
      {timelineState.contextMenu?.visible && (
        <ContextualMenu
          x={timelineState.contextMenu.x}
          y={timelineState.contextMenu.y}
          timestamp={timelineState.contextMenu.timestamp}
          element={timelineState.contextMenu.element}
          onClose={() => {
            setTimelineState(prev => ({
              ...prev,
              contextMenu: { ...prev.contextMenu!, visible: false }
            }));
          }}
          onCreateClip={(range) => {
            // Handle clip creation
          }}
          onCreateAnnotation={(annotation) => {
            // Handle annotation creation
          }}
        />
      )}
    </div>
  );
};

// Utility functions
function clusterEvents(events: TimelineEvent[], pixelsPerSecond: number, minDistance = 20): EventCluster[] {
  // Implementation for clustering nearby events
  const clusters: EventCluster[] = [];
  // ... clustering logic
  return clusters;
}

function getEventColor(eventType: string): string {
  const colors = {
    goal: '#28a745',
    shot: '#ffc107',
    pass: '#17a2b8',
    tackle: '#dc3545',
    foul: '#fd7e14',
    card: '#e83e8c'
  };
  return colors[eventType] || '#6c757d';
}

function performTimelineHitTest(x: number, y: number, state: TimelineState): TimelineElement | null {
  // Implementation for hit testing timeline elements
  return null;
}

// Additional rendering functions would be implemented here...
function renderTimelineBackground(ctx: CanvasRenderingContext2D, width: number, height: number, pixelsPerSecond: number, viewportStart: number) {
  // Implementation for timeline background rendering
}

function renderTimelineGrid(ctx: CanvasRenderingContext2D, width: number, height: number, pixelsPerSecond: number, viewportStart: number) {
  // Implementation for timeline grid rendering
}

function renderTimelineRuler(ctx: CanvasRenderingContext2D, width: number, height: number, pixelsPerSecond: number, viewportStart: number, viewportEnd: number) {
  // Implementation for timeline ruler rendering
}
```

## Performance Optimization ⏳

### Timeline Rendering Performance
- [ ] **Virtualized Rendering**
  - Efficient viewport-based rendering with culling
  - Level-of-detail optimization for different zoom levels
  - Canvas optimization with efficient drawing operations
  - Memory management for large timeline datasets
  - Smooth scrolling and zooming with performance optimization

- [ ] **Data Processing Optimization**
  - Efficient timeline data structures with spatial indexing
  - Event clustering algorithms for dense timeline periods
  - Lazy loading for timeline layers and annotations
  - Caching strategies for frequently accessed timeline data
  - Background processing for complex timeline calculations

### User Interface Performance
- [ ] **Component Optimization**
  - React optimization with memoization and efficient re-rendering
  - State management optimization with selective updates
  - Event handling optimization with debouncing and throttling
  - Animation optimization with requestAnimationFrame
  - Accessibility performance with optimized screen reader support

## Security Implementation ⏳

### Timeline Data Security
- [ ] **Data Protection**
  - Secure timeline data transmission with encryption
  - Access control for sensitive timeline information
  - Data validation for timeline configurations and annotations
  - Audit logging for timeline access and modifications
  - Content integrity verification for timeline data

- [ ] **Collaboration Security**
  - Secure team sharing with access control
  - Real-time collaboration security with conflict resolution
  - Version control security with change tracking
  - User authentication and authorization for timeline access
  - Rate limiting for collaborative timeline operations

## Testing Strategy ⏳

### Timeline Functionality Testing
- [ ] **Functional Testing**
  - Cross-browser timeline rendering validation
  - Interactive feature testing (zoom, selection, navigation)
  - Multi-layer timeline synchronization testing
  - Search and filtering functionality validation
  - Annotation and bookmark creation testing

- [ ] **Performance Testing**
  - Timeline rendering performance with large datasets
  - Memory usage optimization with long timeline sessions
  - Smooth scrolling and zooming performance validation
  - Real-time collaboration performance testing
  - Cross-platform performance comparison

### User Experience Testing
- [ ] **Usability Testing**
  - Timeline navigation efficiency validation
  - Keyboard shortcut effectiveness testing
  - Accessibility compliance testing with assistive technologies
  - Mobile and tablet timeline interface optimization
  - Error handling and recovery user experience

## Monitoring and Analytics ⏳

### Timeline Usage Analytics
- [ ] **Usage Metrics**
  - Timeline interaction patterns and user engagement
  - Feature usage statistics (zoom, layers, search, annotations)
  - Performance metrics (render times, interaction responsiveness)
  - Collaboration effectiveness and team usage patterns
  - Cross-platform usage distribution and optimization

- [ ] **Performance Monitoring**
  - Real-time timeline rendering performance tracking
  - Memory usage and optimization monitoring
  - User experience metrics (interaction latency, smoothness)
  - Error rates and failure analysis by browser/device
  - Timeline data quality and accuracy monitoring

## Definition of Done ✅
**This story is complete when:**
- ✅ Master timeline interface renders smoothly with multi-layer support
- ✅ Automatic event detection markers display accurately with confidence indicators
- ✅ Custom annotation creation works intuitively with drag-and-drop positioning
- ✅ Timeline zoom controls provide smooth transitions between granularity levels
- ✅ Multi-layer timeline shows synchronized data types with visibility controls
- ✅ Timeline search and filtering delivers instant results with highlighting
- ✅ Contextual right-click menus provide quick access to analysis tools
- ✅ Timeline state preservation and team sharing works across sessions
- ✅ Cross-browser compatibility testing passes for all major browsers
- ✅ Performance benchmarks meet targets for large timeline datasets
- ✅ Accessibility compliance testing passes (WCAG 2.1 AA)
- ✅ All tests pass with >95% coverage and interaction validation

## Dependencies
- **Internal:** Story 3.1 (video player), Story 2.6 (event detection), Story 3.2 (AI overlays)
- **External:** Canvas 2D and WebGL support for timeline rendering
- **External:** High-quality event detection data from AI processing pipeline
- **External:** Real-time collaboration infrastructure for team sharing

## Risks & Mitigation
- **Risk:** Timeline rendering performance issues with large datasets affecting user experience
- **Mitigation:** Virtualized rendering, level-of-detail optimization, and efficient data structures
- **Risk:** Complex multi-layer synchronization causing timing issues
- **Mitigation:** Robust synchronization algorithms, comprehensive testing, and fallback mechanisms
- **Risk:** Real-time collaboration conflicts and merge complexity
- **Mitigation:** Conflict resolution algorithms, version control, and user feedback systems
- **Risk:** Cross-browser compatibility issues with advanced canvas features
- **Mitigation:** Progressive enhancement, feature detection, and comprehensive fallbacks

## Change Log
| Date | Version | Description | Author |
| :--- | :--- | :--- | :--- |
| 2025-01-23 | 1.0 | Initial story creation with comprehensive timeline interface system | Sarah (Product Owner) |
| 2025-01-23 | 1.1 | Added detailed multi-layer implementation and collaboration features | Sarah (Product Owner) |
| 2025-01-23 | 1.2 | Enhanced with performance optimization and accessibility features | Sarah (Product Owner) |