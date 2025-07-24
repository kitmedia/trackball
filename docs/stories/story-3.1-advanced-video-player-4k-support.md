# Story 3.1: Advanced Video Player with 4K Support

## Status
🟡 **PENDING** - Professional-grade video player with 4K support, advanced controls, and comprehensive analysis features

## Story
**As a** coach,
**I want** a video player interface supporting 4K playback with professional controls,
**so that** I can analyze high-quality footage with precise timeline scrubbing, zoom, and speed adjustment.

## Acceptance Criteria
1. 4K video playback at 30fps on standard web browsers (Chrome, Firefox, Safari) ⏳
2. Timeline scrubbing with frame-accurate positioning and thumbnail previews ⏳
3. Variable playback speed controls (0.25x to 4x) with smooth transitions ⏳
4. Zoom functionality with pan controls for detailed area analysis ⏳
5. Dual-camera view switching and side-by-side comparison modes ⏳
6. Panoramic view integration with seamless transition capabilities ⏳
7. Keyboard shortcuts for all video controls (space, arrow keys, etc.) ⏳
8. Responsive design supporting desktop and tablet viewing experiences ⏳

## Tasks / Subtasks

- [ ] **Task 3.1.1: 4K Video Playback Infrastructure** ⏳
  - [ ] Implement HTML5 video player with MSE (Media Source Extensions) support for 4K streaming
  - [ ] Create adaptive bitrate streaming with automatic quality adjustment based on bandwidth
  - [ ] Add video decoder optimization for H.264/H.265 codecs with hardware acceleration
  - [ ] Implement progressive video loading with intelligent buffering strategies
  - [ ] Create cross-browser compatibility layer with WebKit, Blink, and Gecko support
  - [ ] Add GPU-accelerated video rendering with WebGL integration where available
  - [ ] Implement video performance monitoring with frame drop detection and recovery
  - [ ] Create video format support validation with fallback options
  - [ ] Add video quality assessment with automatic degradation for poor connections
  - [ ] Implement video caching strategies with service worker integration
  - [ ] Create video preloading system with predictive content loading
  - [ ] Add video error handling with comprehensive recovery mechanisms
  - [ ] Implement video analytics with playback performance metrics
  - [ ] Create video security features with DRM integration where required
  - [ ] Add video accessibility features with screen reader and keyboard support
  - **Estimate:** 26 hours | **Priority:** Critical | **Dependencies:** Story 2.4 (panoramic video), Story 1.4 (CDN)
  - **Deliverables:**
    - 4K-capable HTML5 video player with MSE support
    - Adaptive bitrate streaming with quality optimization
    - Cross-browser compatibility and hardware acceleration
    - Comprehensive error handling and recovery mechanisms
    - Performance monitoring and analytics integration

- [ ] **Task 3.1.2: Timeline Scrubbing & Frame-Accurate Navigation** ⏳
  - [ ] Create custom timeline component with precise frame-level positioning
  - [ ] Implement thumbnail preview generation with intelligent keyframe extraction
  - [ ] Add timeline zooming with multiple granularity levels (seconds, minutes, match periods)
  - [ ] Create smooth scrubbing with momentum-based navigation and elastic boundaries
  - [ ] Implement timeline markers with customizable event indicators and labels
  - [ ] Add timeline selection tools with range selection and multi-point marking
  - [ ] Create timeline synchronization across multiple video views
  - [ ] Implement timeline keyboard navigation with professional editing shortcuts
  - [ ] Add timeline accessibility with screen reader support and high contrast modes
  - [ ] Create timeline performance optimization with virtualization for long videos
  - [ ] Implement timeline state management with position persistence and sharing
  - [ ] Add timeline export capabilities with timestamp and marker data
  - [ ] Create timeline customization with user preferences and layout options
  - [ ] Implement timeline integration with video player controls and overlays
  - [ ] Add timeline analytics with usage patterns and interaction tracking
  - **Estimate:** 22 hours | **Priority:** Critical | **Dependencies:** Task 3.1.1
  - **Deliverables:**
    - Custom timeline component with frame-accurate positioning
    - Thumbnail preview system with keyframe extraction
    - Multi-level timeline zooming and navigation
    - Comprehensive keyboard shortcuts and accessibility
    - Timeline state management and persistence

- [ ] **Task 3.1.3: Variable Playback Speed Controls** ⏳
  - [ ] Implement smooth playback speed adjustment from 0.25x to 4x with fine-grain control
  - [ ] Create speed control UI with slider, buttons, and preset speed options
  - [ ] Add audio pitch correction for speed changes to maintain natural sound
  - [ ] Implement speed ramping with smooth acceleration and deceleration
  - [ ] Create frame-by-frame stepping with forward and backward navigation
  - [ ] Add speed presets for common analysis speeds (0.5x, 1x, 2x) with quick access
  - [ ] Implement speed synchronization across multiple video views
  - [ ] Create speed-aware timeline updates with dynamic time display
  - [ ] Add speed control keyboard shortcuts with professional video editing standards
  - [ ] Implement speed control accessibility with clear audio feedback
  - [ ] Create speed control customization with user-defined presets
  - [ ] Add speed control analytics with usage pattern tracking
  - [ ] Implement speed control integration with clip creation and export
  - [ ] Create speed control visualization with current speed indicators
  - [ ] Add speed control optimization with smooth performance at all speeds
  - **Estimate:** 16 hours | **Priority:** High | **Dependencies:** Task 3.1.2
  - **Deliverables:**
    - Variable speed playback with smooth transitions
    - Comprehensive speed control UI with presets
    - Audio pitch correction and frame-by-frame stepping
    - Speed synchronization across multiple views
    - Professional keyboard shortcuts and accessibility

- [ ] **Task 3.1.4: Zoom & Pan Functionality** ⏳
  - [ ] Create digital zoom with up to 8x magnification maintaining video quality
  - [ ] Implement smooth pan controls with mouse, touch, and keyboard navigation
  - [ ] Add zoom-to-fit and zoom-to-fill automatic scaling options
  - [ ] Create zoom region selection with click-to-zoom and rectangle selection
  - [ ] Implement zoom state persistence with position and level memory
  - [ ] Add zoom synchronization across dual-camera views
  - [ ] Create zoom performance optimization with efficient canvas rendering
  - [ ] Implement zoom accessibility with screen reader announcements
  - [ ] Add zoom indicators with current level display and navigation help
  - [ ] Create zoom presets for common analysis scenarios (player focus, ball tracking)
  - [ ] Implement zoom integration with timeline and playback controls
  - [ ] Add zoom export capabilities with cropped video generation
  - [ ] Create zoom analytics with usage patterns and preferred zoom levels
  - [ ] Implement zoom keyboard shortcuts with industry-standard bindings
  - [ ] Add zoom touch gestures for tablet and mobile interfaces
  - **Estimate:** 18 hours | **Priority:** High | **Dependencies:** Task 3.1.3
  - **Deliverables:**
    - Digital zoom with up to 8x magnification
    - Comprehensive pan controls with multiple input methods
    - Zoom state persistence and synchronization
    - Performance-optimized canvas rendering
    - Professional zoom shortcuts and accessibility

- [ ] **Task 3.1.5: Dual-Camera View Management** ⏳
  - [ ] Create seamless dual-camera view switching with synchronized playback
  - [ ] Implement side-by-side comparison mode with independent controls
  - [ ] Add picture-in-picture mode with resizable secondary video window
  - [ ] Create camera angle selection with labeled camera positions
  - [ ] Implement camera synchronization with automatic timing alignment
  - [ ] Add camera-specific controls with individual zoom and pan settings
  - [ ] Create camera switching animations with smooth transitions
  - [ ] Implement camera view presets for common analysis configurations
  - [ ] Add camera view state management with layout persistence
  - [ ] Create camera view export with multi-angle clip generation
  - [ ] Implement camera view keyboard shortcuts for quick switching
  - [ ] Add camera view accessibility with clear view indicators
  - [ ] Create camera view customization with user-defined layouts
  - [ ] Implement camera view analytics with usage preference tracking
  - [ ] Add camera view integration with AI overlays and timeline markers
  - **Estimate:** 20 hours | **Priority:** High | **Dependencies:** Task 3.1.4
  - **Deliverables:**
    - Seamless dual-camera view switching
    - Side-by-side and picture-in-picture modes
    - Camera synchronization and independent controls
    - Camera view presets and customization
    - Multi-angle export capabilities

- [ ] **Task 3.1.6: Panoramic View Integration** ⏳
  - [ ] Integrate panoramic video playback with seamless quality transitions
  - [ ] Create panoramic view controls with field-of-view adjustment
  - [ ] Implement panoramic-to-dual-camera view switching with position memory
  - [ ] Add panoramic zoom with intelligent region selection
  - [ ] Create panoramic view synchronization with timeline and overlays
  - [ ] Implement panoramic view export with customizable field-of-view
  - [ ] Add panoramic view performance optimization for large resolution videos
  - [ ] Create panoramic view accessibility with spatial navigation support
  - [ ] Implement panoramic view keyboard shortcuts for efficient navigation
  - [ ] Add panoramic view analytics with viewing pattern analysis
  - [ ] Create panoramic view customization with user preference settings
  - [ ] Implement panoramic view integration with AI tracking overlays
  - [ ] Add panoramic view quality assessment with automatic fallback
  - [ ] Create panoramic view state management with session persistence
  - [ ] Implement panoramic view testing with quality validation
  - **Estimate:** 14 hours | **Priority:** Medium | **Dependencies:** Task 3.1.5, Story 2.4 (panoramic stitching)
  - **Deliverables:**
    - Panoramic video playback integration
    - Field-of-view controls and view switching
    - Panoramic zoom and region selection
    - Performance optimization for large videos
    - Comprehensive keyboard shortcuts and accessibility

- [ ] **Task 3.1.7: Professional Keyboard Shortcuts & Accessibility** ⏳
  - [ ] Implement comprehensive keyboard shortcuts following video editing standards
  - [ ] Create customizable shortcut configuration with user-defined key bindings
  - [ ] Add keyboard shortcut help overlay with contextual command display
  - [ ] Implement accessibility compliance with WCAG 2.1 AA standards
  - [ ] Create screen reader support with descriptive video state announcements
  - [ ] Add high contrast mode support with customizable color themes
  - [ ] Implement focus management with clear visual indicators
  - [ ] Create keyboard navigation for all video player controls
  - [ ] Add voice command integration for hands-free operation
  - [ ] Implement keyboard shortcut conflicts resolution with priority management
  - [ ] Create keyboard shortcut documentation with interactive help system
  - [ ] Add keyboard shortcut analytics with usage pattern tracking
  - [ ] Implement keyboard shortcut testing with automated validation
  - [ ] Create keyboard shortcut export for team standardization
  - [ ] Add keyboard shortcut integration with external input devices
  - **Estimate:** 12 hours | **Priority:** Medium | **Dependencies:** Task 3.1.6
  - **Deliverables:**
    - Comprehensive keyboard shortcuts with customization
    - WCAG 2.1 AA accessibility compliance
    - Screen reader support and high contrast modes
    - Voice command integration and hands-free operation
    - Interactive help system and documentation

## API Implementation ⏳

### Video Player & Playback Endpoints (16 endpoints)
- [ ] **GET /player/sessions/{session_id}/stream** - Get video streaming URLs
  - Request: quality_preference, device_type, bandwidth_hint
  - Response: streaming_urls, quality_options, adaptive_manifest
  - Features: Adaptive streaming, device optimization, CDN integration

- [ ] **GET /player/sessions/{session_id}/thumbnails** - Get timeline thumbnails
  - Request: timeline_resolution, thumbnail_count, keyframe_preference
  - Response: thumbnail_urls, sprite_sheets, timing_metadata
  - Features: Intelligent keyframe selection, sprite optimization

- [ ] **POST /player/sessions/{session_id}/position** - Update playback position
  - Request: timestamp, camera_view, zoom_state, playback_speed
  - Response: position_update_status, synchronized_views, state_persistence
  - Features: Multi-view synchronization, state management

- [ ] **GET /player/sessions/{session_id}/position** - Get current playback state
  - Response: current_timestamp, camera_view, zoom_state, playback_speed, duration
  - Features: Complete state retrieval, cross-device synchronization

- [ ] **POST /player/sessions/{session_id}/bookmarks** - Create playback bookmark
  - Request: timestamp, bookmark_name, description, bookmark_type
  - Response: bookmark_id, creation_status, sharing_options
  - Features: Custom bookmarks, team sharing, categorization

- [ ] **GET /player/sessions/{session_id}/bookmarks** - Get session bookmarks
  - Response: bookmarks_list, timestamps, metadata, sharing_status
  - Features: Bookmark organization, filtering, team collaboration

- [ ] **POST /player/quality/adjust** - Adjust video quality
  - Request: session_id, target_quality, adaptation_mode, bandwidth_limit
  - Response: quality_adjustment_status, available_qualities, optimization_info
  - Features: Manual quality control, adaptive optimization

- [ ] **GET /player/performance** - Get playback performance metrics
  - Response: frame_rates, buffer_levels, dropped_frames, network_stats
  - Features: Real-time performance monitoring, optimization insights

- [ ] **POST /player/export/clip** - Export video clip
  - Request: session_id, start_time, end_time, quality, format, overlays_included
  - Response: export_job_id, processing_status, estimated_completion
  - Features: Custom clip creation, overlay inclusion, format options

- [ ] **GET /player/export/clips/{job_id}** - Get clip export status
  - Response: export_status, progress_percentage, download_url, file_info
  - Features: Export progress tracking, download management

- [ ] **POST /player/shortcuts/configure** - Configure keyboard shortcuts
  - Request: shortcut_mappings, user_preferences, device_type
  - Response: configuration_status, conflicts_resolved, validation_results
  - Features: Custom shortcut configuration, conflict resolution

- [ ] **GET /player/shortcuts** - Get available keyboard shortcuts
  - Response: available_shortcuts, current_mappings, help_documentation
  - Features: Shortcut discovery, help integration, documentation

- [ ] **POST /player/analytics/track** - Track player usage analytics
  - Request: interaction_type, timestamp, duration, feature_used
  - Response: tracking_status, analytics_acknowledgment
  - Features: Usage tracking, feature adoption, optimization insights

- [ ] **GET /player/settings** - Get player configuration settings
  - Response: player_config, user_preferences, accessibility_options, feature_flags
  - Features: Configuration management, preference persistence

- [ ] **POST /player/settings** - Update player configuration
  - Request: configuration_updates, preference_changes, accessibility_options
  - Response: update_status, configuration_validation, applied_changes
  - Features: Settings management, validation, team synchronization

- [ ] **GET /player/compatibility** - Check browser and device compatibility
  - Request: user_agent, device_capabilities, network_info
  - Response: compatibility_status, supported_features, optimization_recommendations
  - Features: Compatibility checking, feature detection, optimization

## Frontend Component Architecture ⏳

### Video Player Components
```typescript
// Core video player interfaces
interface VideoPlayerProps {
  sessionId: string;
  initialTimestamp?: number;
  autoplay?: boolean;
  quality?: VideoQuality;
  onPlaybackChange?: (state: PlaybackState) => void;
  onError?: (error: VideoPlayerError) => void;
}

// Main video player components
export const AdvancedVideoPlayer: React.FC<VideoPlayerProps>
export const VideoControls: React.FC<VideoControlsProps>
export const VideoTimeline: React.FC<VideoTimelineProps>
export const QualitySelector: React.FC<QualitySelectorProps>
export const SpeedControls: React.FC<SpeedControlsProps>
export const ZoomControls: React.FC<ZoomControlsProps>

// Multi-view components
export const DualCameraView: React.FC<DualCameraViewProps>
export const PanoramicView: React.FC<PanoramicViewProps>
export const ViewSwitcher: React.FC<ViewSwitcherProps>
export const CameraSelector: React.FC<CameraSelectorProps>

// Timeline components
export const TimelineMarkers: React.FC<TimelineMarkersProps>
export const ThumbnailPreview: React.FC<ThumbnailPreviewProps>
export const TimelineZoom: React.FC<TimelineZoomProps>
export const BookmarkManager: React.FC<BookmarkManagerProps>

// Control components
export const KeyboardShortcuts: React.FC<KeyboardShortcutsProps>
export const AccessibilityControls: React.FC<AccessibilityControlsProps>
export const PerformanceMonitor: React.FC<PerformanceMonitorProps>
```

### Video Player State Management
```typescript
interface VideoPlayerState {
  // Playback state
  currentTime: number;
  duration: number;
  isPlaying: boolean;
  playbackSpeed: number;
  volume: number;
  muted: boolean;
  
  // Quality state
  currentQuality: VideoQuality;
  availableQualities: VideoQuality[];
  adaptiveMode: boolean;
  bufferHealth: number;
  
  // View state
  currentView: ViewMode; // single, dual, panoramic
  activeCamera: CameraId;
  zoomLevel: number;
  panPosition: Position;
  
  // Timeline state
  timelineZoom: number;
  timelineRange: TimeRange;
  bookmarks: Bookmark[];
  markers: TimelineMarker[];
  
  // UI state
  controlsVisible: boolean;
  fullscreen: boolean;
  keyboardShortcuts: ShortcutMap;
  accessibilityMode: AccessibilitySettings;
  
  // Performance state
  performanceMetrics: PerformanceMetrics;
  networkStats: NetworkStats;
  
  // Actions
  play: () => void;
  pause: () => void;
  seek: (timestamp: number) => void;
  setPlaybackSpeed: (speed: number) => void;
  setQuality: (quality: VideoQuality) => void;
  toggleView: (viewMode: ViewMode) => void;
  switchCamera: (cameraId: CameraId) => void;
  zoom: (level: number, center?: Position) => void;
  createBookmark: (timestamp: number, name: string) => void;
  
  // Error handling
  errors: VideoPlayerError[];
  clearError: (errorId: string) => void;
}
```

## Video Player Implementation ⏳

### Advanced HTML5 Video Player
```typescript
// Advanced Video Player with 4K Support
import React, { useRef, useEffect, useState, useCallback } from 'react';
import { VideoPlayerState, VideoPlayerProps, PlaybackState } from './types';

export const AdvancedVideoPlayer: React.FC<VideoPlayerProps> = ({
  sessionId,
  initialTimestamp = 0,
  autoplay = false,
  quality = 'auto',
  onPlaybackChange,
  onError
}) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [playerState, setPlayerState] = useState<VideoPlayerState>({
    currentTime: initialTimestamp,
    duration: 0,
    isPlaying: false,
    playbackSpeed: 1,
    volume: 1,
    muted: false,
    currentQuality: quality,
    currentView: 'single',
    zoomLevel: 1,
    panPosition: { x: 0, y: 0 },
    controlsVisible: true,
    fullscreen: false
  });

  // Media Source Extensions setup for 4K streaming
  const setupMediaSource = useCallback(async () => {
    if (!videoRef.current || !('MediaSource' in window)) {
      console.warn('MediaSource not supported, falling back to standard video');
      return;
    }

    const mediaSource = new MediaSource();
    const videoElement = videoRef.current;
    
    videoElement.src = URL.createObjectURL(mediaSource);
    
    mediaSource.addEventListener('sourceopen', async () => {
      try {
        // Get streaming manifest
        const streamingUrls = await fetchStreamingUrls(sessionId, quality);
        
        // Create source buffers for video and audio
        const videoSourceBuffer = mediaSource.addSourceBuffer(
          'video/mp4; codecs="avc1.64002a"' // H.264 High Profile
        );
        const audioSourceBuffer = mediaSource.addSourceBuffer(
          'audio/mp4; codecs="mp4a.40.2"' // AAC
        );
        
        // Start streaming
        await startAdaptiveStreaming(
          streamingUrls,
          videoSourceBuffer,
          audioSourceBuffer
        );
        
      } catch (error) {
        console.error('Failed to setup adaptive streaming:', error);
        onError?.(new VideoPlayerError('streaming_setup_failed', error));
      }
    });
    
  }, [sessionId, quality, onError]);

  // Frame-accurate seeking
  const seekToFrame = useCallback((frameNumber: number) => {
    if (!videoRef.current) return;
    
    const video = videoRef.current;
    const frameRate = 30; // Assume 30fps, could be dynamic
    const targetTime = frameNumber / frameRate;
    
    // Use requestVideoFrameCallback for frame-accurate seeking if available
    if ('requestVideoFrameCallback' in video) {
      video.currentTime = targetTime;
      
      const seekToExactFrame = () => {
        video.requestVideoFrameCallback((now, metadata) => {
          const currentFrameNumber = Math.round(metadata.presentedFrames);
          if (currentFrameNumber !== frameNumber) {
            video.currentTime = frameNumber / frameRate;
            seekToExactFrame();
          }
        });
      };
      
      seekToExactFrame();
    } else {
      // Fallback to time-based seeking
      video.currentTime = targetTime;
    }
  }, []);

  // Variable speed playback with audio pitch correction
  const setPlaybackSpeed = useCallback((speed: number) => {
    if (!videoRef.current) return;
    
    const video = videoRef.current;
    video.playbackRate = speed;
    
    // Audio pitch correction using Web Audio API
    if (speed !== 1 && 'webkitAudioContext' in window) {
      try {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const source = audioContext.createMediaElementSource(video);
        const pitchShift = audioContext.createScriptProcessor(4096, 1, 1);
        
        pitchShift.onaudioprocess = (event) => {
          // Simple pitch correction algorithm
          const inputBuffer = event.inputBuffer.getChannelData(0);
          const outputBuffer = event.outputBuffer.getChannelData(0);
          
          for (let i = 0; i < inputBuffer.length; i++) {
            outputBuffer[i] = inputBuffer[Math.floor(i / speed)] || 0;
          }
        };
        
        source.connect(pitchShift);
        pitchShift.connect(audioContext.destination);
      } catch (error) {
        console.warn('Audio pitch correction not available:', error);
      }
    }
    
    setPlayerState(prev => ({ ...prev, playbackSpeed: speed }));
    onPlaybackChange?.({ ...playerState, playbackSpeed: speed });
  }, [playerState, onPlaybackChange]);

  // Digital zoom with canvas rendering
  const handleZoom = useCallback((zoomLevel: number, center?: Position) => {
    if (!videoRef.current || !canvasRef.current) return;
    
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    
    if (!ctx) return;
    
    // Set canvas size to match video
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    
    // Calculate zoom parameters
    const centerX = center?.x ?? canvas.width / 2;
    const centerY = center?.y ?? canvas.height / 2;
    
    const scaledWidth = canvas.width / zoomLevel;
    const scaledHeight = canvas.height / zoomLevel;
    
    const sourceX = Math.max(0, centerX - scaledWidth / 2);
    const sourceY = Math.max(0, centerY - scaledHeight / 2);
    
    // Clear canvas and draw zoomed video
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(
      video,
      sourceX, sourceY, scaledWidth, scaledHeight,
      0, 0, canvas.width, canvas.height
    );
    
    setPlayerState(prev => ({ ...prev, zoomLevel, panPosition: { x: sourceX, y: sourceY } }));
  }, []);

  // Keyboard shortcuts handler
  const handleKeyDown = useCallback((event: KeyboardEvent) => {
    const video = videoRef.current;
    if (!video) return;
    
    switch (event.code) {
      case 'Space':
        event.preventDefault();
        if (video.paused) {
          video.play();
        } else {
          video.pause();
        }
        break;
        
      case 'ArrowLeft':
        event.preventDefault();
        if (event.shiftKey) {
          // Frame-by-frame backward
          seekToFrame(Math.floor(video.currentTime * 30) - 1);
        } else {
          // 10 second backward
          video.currentTime = Math.max(0, video.currentTime - 10);
        }
        break;
        
      case 'ArrowRight':
        event.preventDefault();
        if (event.shiftKey) {
          // Frame-by-frame forward
          seekToFrame(Math.floor(video.currentTime * 30) + 1);
        } else {
          // 10 second forward
          video.currentTime = Math.min(video.duration, video.currentTime + 10);
        }
        break;
        
      case 'KeyJ':
        event.preventDefault();
        setPlaybackSpeed(Math.max(0.25, playerState.playbackSpeed - 0.25));
        break;
        
      case 'KeyK':
        event.preventDefault();
        video.paused ? video.play() : video.pause();
        break;
        
      case 'KeyL':
        event.preventDefault();
        setPlaybackSpeed(Math.min(4, playerState.playbackSpeed + 0.25));
        break;
        
      case 'KeyF':
        event.preventDefault();
        if (document.fullscreenElement) {
          document.exitFullscreen();
        } else {
          video.requestFullscreen();
        }
        break;
    }
  }, [playerState.playbackSpeed, seekToFrame, setPlaybackSpeed]);

  // Setup event listeners
  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    
    const handleTimeUpdate = () => {
      setPlayerState(prev => ({ ...prev, currentTime: video.currentTime }));
    };
    
    const handleDurationChange = () => {
      setPlayerState(prev => ({ ...prev, duration: video.duration }));
    };
    
    const handlePlay = () => {
      setPlayerState(prev => ({ ...prev, isPlaying: true }));
      onPlaybackChange?.({ ...playerState, isPlaying: true });
    };
    
    const handlePause = () => {
      setPlayerState(prev => ({ ...prev, isPlaying: false }));
      onPlaybackChange?.({ ...playerState, isPlaying: false });
    };
    
    const handleError = (event: Event) => {
      const error = new VideoPlayerError('playback_error', event);
      onError?.(error);
    };
    
    video.addEventListener('timeupdate', handleTimeUpdate);
    video.addEventListener('durationchange', handleDurationChange);
    video.addEventListener('play', handlePlay);
    video.addEventListener('pause', handlePause);
    video.addEventListener('error', handleError);
    
    document.addEventListener('keydown', handleKeyDown);
    
    return () => {
      video.removeEventListener('timeupdate', handleTimeUpdate);
      video.removeEventListener('durationchange', handleDurationChange);
      video.removeEventListener('play', handlePlay);
      video.removeEventListener('pause', handlePause);
      video.removeEventListener('error', handleError);
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleKeyDown, onPlaybackChange, onError, playerState]);

  // Initialize player
  useEffect(() => {
    setupMediaSource();
  }, [setupMediaSource]);

  return (
    <div className="advanced-video-player">
      <div className="video-container">
        <video
          ref={videoRef}
          className="video-element"
          preload="metadata"
          crossOrigin="anonymous"
          playsInline
          style={{ display: playerState.zoomLevel > 1 ? 'none' : 'block' }}
        />
        <canvas
          ref={canvasRef}
          className="zoom-canvas"
          style={{ display: playerState.zoomLevel > 1 ? 'block' : 'none' }}
        />
      </div>
      
      <VideoControls
        playerState={playerState}
        onPlayPause={() => videoRef.current?.paused ? videoRef.current.play() : videoRef.current?.pause()}
        onSeek={(time) => { if (videoRef.current) videoRef.current.currentTime = time; }}
        onSpeedChange={setPlaybackSpeed}
        onZoom={handleZoom}
      />
    </div>
  );
};

// Adaptive streaming implementation
async function startAdaptiveStreaming(
  streamingUrls: StreamingManifest,
  videoSourceBuffer: SourceBuffer,
  audioSourceBuffer: SourceBuffer
) {
  // Implementation of adaptive bitrate streaming
  // This would include quality switching logic based on bandwidth
}

// Utility functions
async function fetchStreamingUrls(sessionId: string, quality: string): Promise<StreamingManifest> {
  const response = await fetch(`/api/player/sessions/${sessionId}/stream?quality=${quality}`);
  return response.json();
}

class VideoPlayerError extends Error {
  constructor(public code: string, public originalError?: any) {
    super(`Video Player Error: ${code}`);
    this.name = 'VideoPlayerError';
  }
}
```

## Performance Optimization ⏳

### Video Playback Performance
- [ ] **Streaming Optimization**
  - Adaptive bitrate streaming with intelligent quality switching
  - Video preloading and intelligent buffering strategies
  - CDN optimization for global video delivery
  - Hardware-accelerated video decoding where available
  - Progressive video loading with quality adaptation

- [ ] **Rendering Performance**
  - GPU-accelerated video rendering with WebGL
  - Canvas optimization for zoom and pan operations
  - Efficient timeline rendering with virtualization
  - Smooth animations with requestAnimationFrame
  - Memory management for long video sessions

### User Interface Performance
- [ ] **Component Optimization**
  - Virtual scrolling for timeline and thumbnail components
  - Efficient re-rendering with React optimization techniques
  - State management optimization with selective updates
  - Event handling optimization with debouncing and throttling
  - Accessibility performance with optimized screen reader support

## Security Implementation ⏳

### Video Player Security
- [ ] **Content Protection**
  - Secure video streaming with encrypted connections
  - DRM integration for sensitive content protection
  - Watermarking support for copyright protection
  - Access control with session-based authentication
  - Content integrity verification with checksums

- [ ] **Interface Security**
  - XSS protection for video player interface
  - Content Security Policy implementation
  - Secure handling of user preferences and settings
  - Input validation for all player controls
  - Audit logging for video access and interactions

## Testing Strategy ⏳

### Video Player Testing
- [ ] **Functional Testing**
  - Cross-browser compatibility testing (Chrome, Firefox, Safari, Edge)
  - 4K video playback performance validation
  - Timeline scrubbing accuracy and responsiveness
  - Keyboard shortcuts and accessibility compliance
  - Multi-view synchronization and state management

- [ ] **Performance Testing**
  - Video playback performance with various resolutions
  - Memory usage optimization with long video sessions
  - Network bandwidth adaptation and quality switching
  - CPU and GPU utilization monitoring
  - Battery usage optimization for mobile devices

### User Experience Testing
- [ ] **Usability Testing**
  - User interaction flow validation with coaching workflows
  - Accessibility testing with screen readers and assistive technologies
  - Mobile and tablet interface optimization
  - Keyboard navigation and shortcut effectiveness
  - Error handling and recovery user experience

## Monitoring and Analytics ⏳

### Video Player Analytics
- [ ] **Usage Metrics**
  - Video playback statistics and engagement patterns
  - Feature usage tracking (zoom, speed control, views)
  - Performance metrics (load times, buffer health, errors)
  - User preference analysis (quality settings, shortcuts)
  - Cross-platform usage distribution and optimization

- [ ] **Performance Monitoring**
  - Real-time playback performance monitoring
  - Network condition impact on video quality
  - Error rates and failure analysis by browser/device
  - User experience metrics (time to first frame, seeking responsiveness)
  - Resource utilization and optimization opportunities

## Definition of Done ✅
**This story is complete when:**
- ✅ 4K video playback achieves 30fps performance on all major browsers
- ✅ Timeline scrubbing provides frame-accurate positioning with <100ms response
- ✅ Variable playback speed (0.25x to 4x) works smoothly with audio pitch correction
- ✅ Zoom functionality supports up to 8x magnification with smooth pan controls
- ✅ Dual-camera view switching maintains perfect synchronization
- ✅ Panoramic view integration provides seamless transition capabilities
- ✅ All keyboard shortcuts work according to professional video editing standards
- ✅ Responsive design provides optimal experience on desktop and tablet
- ✅ Video player passes accessibility compliance testing (WCAG 2.1 AA)
- ✅ Performance monitoring shows optimal resource utilization
- ✅ Cross-browser compatibility testing passes for all target browsers
- ✅ All tests pass with >95% coverage and performance validation

## Dependencies
- **Internal:** Story 2.4 (panoramic video), Story 1.4 (CDN infrastructure), Story 1.5 (basic video player)
- **External:** CDN configuration for 4K video streaming
- **External:** Browser support for Media Source Extensions and modern video APIs
- **External:** Hardware acceleration support for video decoding

## Risks & Mitigation
- **Risk:** 4K video performance issues on lower-end devices affecting user experience
- **Mitigation:** Adaptive quality control, device capability detection, and graceful degradation
- **Risk:** Cross-browser compatibility issues with advanced video features
- **Mitigation:** Progressive enhancement, feature detection, and comprehensive fallbacks
- **Risk:** Memory usage issues with long video sessions and zoom functionality
- **Mitigation:** Memory management optimization, efficient canvas rendering, and resource cleanup
- **Risk:** Accessibility compliance complexity affecting development timeline
- **Mitigation:** Accessibility-first design approach, automated testing, and expert consultation

## Change Log
| Date | Version | Description | Author |
| :--- | :--- | :--- | :--- |
| 2025-01-23 | 1.0 | Initial story creation with comprehensive 4K video player system | Sarah (Product Owner) |
| 2025-01-23 | 1.1 | Added detailed implementation and performance optimization | Sarah (Product Owner) |
| 2025-01-23 | 1.2 | Enhanced with accessibility features and cross-browser compatibility | Sarah (Product Owner) |