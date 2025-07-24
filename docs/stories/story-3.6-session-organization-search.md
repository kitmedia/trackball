# Story 3.6: Session Organization and Search

## Status
🟡 **PENDING** - Comprehensive session organization and search system with advanced metadata management, filtering, and archival capabilities

## Story
**As a** coach,
**I want** to organize analysis sessions by team, match, and date with searchable metadata,
**so that** I can efficiently locate and manage team footage across seasons.

## Acceptance Criteria
1. Session listing interface with filtering by team, date, opponent, and status ⏳
2. Advanced search functionality supporting metadata, tags, and custom fields ⏳
3. Session metadata management (team name, opponent, match date, venue, notes) ⏳
4. Tagging system for categorizing sessions by competition, importance, or analysis type ⏳
5. Session archiving and deletion functionality with confirmation safeguards ⏳
6. Bulk session operations for efficient season management ⏳
7. Session sharing controls with team-specific permissions and access levels ⏳
8. Export session lists and metadata for external reporting and analysis ⏳

## Tasks / Subtasks

- [ ] **Task 3.6.1: Session Listing & Overview Interface** ⏳
  - [ ] Create responsive session list with grid and table view options
  - [ ] Implement session cards with thumbnail previews and key metadata display
  - [ ] Add session status indicators (processing, completed, error, archived)
  - [ ] Create session quick actions (view, edit, share, archive, delete)
  - [ ] Implement infinite scroll for large session collections
  - [ ] Add session selection with multi-select capabilities for bulk operations
  - [ ] Create session sorting options (date, name, duration, team, status)
  - [ ] Implement session grouping by team, competition, or time period
  - **Estimate:** 30 hours | **Priority:** Critical | **Dependencies:** Story 3.3 (timeline interface)
  - **Deliverables:**
    - Responsive session listing with grid and table views
    - Session cards with thumbnail previews and metadata
    - Multi-select capabilities with bulk operation support
    - Sorting and grouping functionality

- [ ] **Task 3.6.2: Advanced Search & Filtering System** ⏳
  - [ ] Implement full-text search across session metadata and content
  - [ ] Create multi-criteria filtering with date ranges, teams, and opponents
  - [ ] Add search filters for session tags, venue, competition type
  - [ ] Implement saved search queries with custom names and shortcuts
  - [ ] Create search suggestions with auto-complete functionality
  - [ ] Add search history with recent searches and quick access
  - [ ] Implement advanced search operators (AND, OR, NOT, wildcards)
  - [ ] Create search result highlighting and relevance scoring
  - **Estimate:** 35 hours | **Priority:** Critical | **Dependencies:** Task 3.6.1
  - **Deliverables:**
    - Full-text search with metadata and content indexing
    - Multi-criteria filtering with date ranges and team selection
    - Saved search queries with auto-complete suggestions
    - Advanced search operators with relevance scoring

- [ ] **Task 3.6.3: Comprehensive Metadata Management** ⏳
  - [ ] Create session metadata schema with required and optional fields
  - [ ] Implement metadata editing interface with form validation
  - [ ] Add custom metadata fields with user-defined schemas
  - [ ] Create metadata templates for different match types and competitions
  - [ ] Implement metadata validation with business rules and constraints
  - [ ] Add metadata import/export functionality for external systems
  - [ ] Create metadata history tracking with change log and versioning
  - [ ] Implement metadata auto-completion based on historical data
  - **Estimate:** 32 hours | **Priority:** High | **Dependencies:** Task 3.6.2
  - **Deliverables:**
    - Comprehensive metadata schema with validation
    - Metadata editing interface with template support
    - Custom metadata fields with user-defined schemas
    - Import/export functionality with change tracking

- [ ] **Task 3.6.4: Dynamic Tagging System** ⏳
  - [ ] Create hierarchical tag system with categories and subcategories
  - [ ] Implement tag management interface with creation, editing, and deletion
  - [ ] Add tag suggestions based on session content and historical usage
  - [ ] Create tag filtering and search integration with main search system
  - [ ] Implement tag analytics with usage statistics and trending tags
  - [ ] Add tag bulk operations for efficient session categorization
  - [ ] Create tag templates for common categorization patterns
  - [ ] Implement tag sharing and collaboration features for team use
  - **Estimate:** 28 hours | **Priority:** High | **Dependencies:** Task 3.6.3
  - **Deliverables:**
    - Hierarchical tag system with categories and subcategories
    - Tag management interface with suggestion capabilities
    - Tag analytics with usage statistics
    - Bulk tagging operations with template support

- [ ] **Task 3.6.5: Archive & Deletion Management** ⏳
  - [ ] Implement session archiving with configurable retention policies
  - [ ] Create archive management interface with restore capabilities
  - [ ] Add deletion confirmation workflows with multi-step verification
  - [ ] Implement soft deletion with recovery period and permanent deletion
  - [ ] Create bulk archiving and deletion operations with progress tracking
  - [ ] Add archive storage optimization with compression and tiered storage
  - [ ] Implement archive access controls with permission management
  - [ ] Create archive analytics with storage usage and cost tracking
  - **Estimate:** 30 hours | **Priority:** High | **Dependencies:** Task 3.6.4
  - **Deliverables:**
    - Session archiving with configurable retention policies
    - Archive management with restore and deletion workflows
    - Bulk operations with progress tracking and confirmation
    - Storage optimization with compression and access controls

- [ ] **Task 3.6.6: Bulk Operations & Season Management** ⏳
  - [ ] Create bulk operation interface with action selection and confirmation
  - [ ] Implement bulk metadata editing with batch update capabilities
  - [ ] Add bulk tagging and tag removal operations
  - [ ] Create season management tools with automatic organization
  - [ ] Implement bulk export functionality with customizable formats
  - [ ] Add bulk sharing operations with permission management
  - [ ] Create bulk processing queue with status tracking and cancellation
  - [ ] Implement undo functionality for reversible bulk operations
  - **Estimate:** 25 hours | **Priority:** Medium | **Dependencies:** Task 3.6.5
  - **Deliverables:**
    - Bulk operation interface with confirmation workflows
    - Season management tools with automatic organization
    - Bulk export functionality with multiple format support
    - Undo functionality for reversible operations

- [ ] **Task 3.6.7: Session Sharing & Permissions** ⏳
  - [ ] Implement granular permission system with role-based access control
  - [ ] Create session sharing interface with user and team selection
  - [ ] Add sharing link generation with expiration and access limits
  - [ ] Implement sharing notifications with email and in-app alerts
  - [ ] Create sharing analytics with access tracking and usage metrics
  - [ ] Add sharing templates for common sharing scenarios
  - [ ] Implement sharing history with audit log and permission changes
  - [ ] Create sharing integration with external collaboration tools
  - **Estimate:** 33 hours | **Priority:** High | **Dependencies:** Task 3.6.6
  - **Deliverables:**
    - Granular permission system with role-based access
    - Session sharing with link generation and access limits
    - Sharing analytics with access tracking and notifications
    - Integration with external collaboration tools

- [ ] **Task 3.6.8: Export & Reporting System** ⏳
  - [ ] Create session list export with customizable column selection
  - [ ] Implement multiple export formats (CSV, Excel, PDF, JSON)
  - [ ] Add export filtering with search criteria preservation
  - [ ] Create scheduled export functionality with automated delivery
  - [ ] Implement export templates for common reporting requirements
  - [ ] Add export analytics with download tracking and usage metrics
  - [ ] Create custom report builder with drag-and-drop interface
  - [ ] Implement export API for external system integration
  - **Estimate:** 27 hours | **Priority:** Medium | **Dependencies:** Task 3.6.7
  - **Deliverables:**
    - Multi-format export system with customizable columns
    - Scheduled export functionality with automated delivery
    - Custom report builder with drag-and-drop interface
    - Export API for external system integration

## API Implementation

### Session Organization and Search API

```python
# FastAPI implementation for session organization and search
from fastapi import FastAPI, HTTPException, Depends, Security, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import Column, String, DateTime, Boolean, Text, Integer, Float, JSON, Index
from sqlalchemy.ext.declarative import declarative_base
from typing import List, Optional, Dict, Any, Union
from datetime import datetime, timedelta
from pydantic import BaseModel
import json
import uuid
from elasticsearch import Elasticsearch
import pandas as pd
from io import BytesIO, StringIO

Base = declarative_base()

class AnalysisSession(Base):
    __tablename__ = "analysis_sessions"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    team_id = Column(String, nullable=False)
    session_name = Column(String, nullable=False)
    session_description = Column(Text)
    match_date = Column(DateTime)
    opponent_team = Column(String)
    venue = Column(String)
    competition = Column(String)
    season = Column(String)
    match_type = Column(String)  # friendly, league, cup, tournament
    importance_level = Column(Integer, default=5)  # 1-10 scale
    status = Column(String, default="active")  # active, processing, completed, archived, deleted
    processing_status = Column(String, default="pending")
    tags = Column(JSON)  # Array of tags
    custom_metadata = Column(JSON)  # User-defined metadata
    sharing_settings = Column(JSON)
    access_permissions = Column(JSON)
    archive_date = Column(DateTime)
    deletion_date = Column(DateTime)
    video_duration = Column(Float)  # seconds
    file_size = Column(Integer)  # bytes
    thumbnail_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Indexes for search performance
    __table_args__ = (
        Index('idx_session_team_date', 'team_id', 'match_date'),
        Index('idx_session_user_status', 'user_id', 'status'),
        Index('idx_session_competition', 'competition', 'season'),
        Index('idx_session_search', 'session_name', 'opponent_team', 'venue'),
    )

class SessionTag(Base):
    __tablename__ = "session_tags"
    
    id = Column(String, primary_key=True)
    tag_name = Column(String, nullable=False, unique=True)
    tag_category = Column(String)
    tag_description = Column(Text)
    color = Column(String, default="#1976d2")
    usage_count = Column(Integer, default=0)
    created_by = Column(String, nullable=False)
    is_system_tag = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class SavedSearch(Base):
    __tablename__ = "saved_searches"
    
    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    search_name = Column(String, nullable=False)
    search_query = Column(JSON, nullable=False)
    search_filters = Column(JSON)
    is_shared = Column(Boolean, default=False)
    usage_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_used = Column(DateTime)

class SessionOrganizationManager:
    def __init__(self, db_session, elasticsearch_client):
        self.db = db_session
        self.es = elasticsearch_client
        self.search_index = "trackball_sessions"
        
    async def list_sessions(self, filter_params: Dict[str, Any], pagination: Dict[str, int]) -> Dict[str, Any]:
        """List sessions with filtering and pagination"""
        try:
            query = self.db.query(AnalysisSession)
            
            # Apply filters
            if filter_params.get("team_id"):
                query = query.filter(AnalysisSession.team_id == filter_params["team_id"])
            
            if filter_params.get("status"):
                query = query.filter(AnalysisSession.status == filter_params["status"])
            
            if filter_params.get("competition"):
                query = query.filter(AnalysisSession.competition == filter_params["competition"])
            
            if filter_params.get("season"):
                query = query.filter(AnalysisSession.season == filter_params["season"])
            
            # Date range filtering
            if filter_params.get("start_date"):
                query = query.filter(AnalysisSession.match_date >= filter_params["start_date"])
            
            if filter_params.get("end_date"):
                query = query.filter(AnalysisSession.match_date <= filter_params["end_date"])
            
            # Tag filtering
            if filter_params.get("tags"):
                tags = filter_params["tags"] if isinstance(filter_params["tags"], list) else [filter_params["tags"]]
                for tag in tags:
                    query = query.filter(AnalysisSession.tags.contains(tag))
            
            # Text search
            if filter_params.get("search_query"):
                search_term = f"%{filter_params['search_query']}%"
                query = query.filter(
                    (AnalysisSession.session_name.ilike(search_term)) |
                    (AnalysisSession.opponent_team.ilike(search_term)) |
                    (AnalysisSession.venue.ilike(search_term)) |
                    (AnalysisSession.session_description.ilike(search_term))
                )
            
            # Sorting
            sort_field = filter_params.get("sort_by", "created_at")
            sort_order = filter_params.get("sort_order", "desc")
            
            if sort_order.lower() == "desc":
                query = query.order_by(getattr(AnalysisSession, sort_field).desc())
            else:
                query = query.order_by(getattr(AnalysisSession, sort_field).asc())
            
            # Count total for pagination
            total_count = query.count()
            
            # Apply pagination
            offset = pagination.get("offset", 0)
            limit = pagination.get("limit", 50)
            sessions = query.offset(offset).limit(limit).all()
            
            # Convert to response format
            session_list = []
            for session in sessions:
                session_data = {
                    "id": session.id,
                    "session_name": session.session_name,
                    "team_id": session.team_id,
                    "match_date": session.match_date.isoformat() if session.match_date else None,
                    "opponent_team": session.opponent_team,
                    "venue": session.venue,
                    "competition": session.competition,
                    "season": session.season,
                    "status": session.status,
                    "processing_status": session.processing_status,
                    "tags": json.loads(session.tags) if session.tags else [],
                    "importance_level": session.importance_level,
                    "video_duration": session.video_duration,
                    "thumbnail_url": session.thumbnail_url,
                    "created_at": session.created_at.isoformat(),
                    "updated_at": session.updated_at.isoformat()
                }
                session_list.append(session_data)
            
            return {
                "sessions": session_list,
                "total_count": total_count,
                "offset": offset,
                "limit": limit,
                "has_more": (offset + limit) < total_count
            }
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to list sessions: {str(e)}")
    
    async def advanced_search(self, search_params: Dict[str, Any]) -> Dict[str, Any]:
        """Advanced search using Elasticsearch"""
        try:
            # Build Elasticsearch query
            es_query = {
                "bool": {
                    "must": [],
                    "filter": [],
                    "should": []
                }
            }
            
            # Full-text search
            if search_params.get("query"):
                es_query["bool"]["must"].append({
                    "multi_match": {
                        "query": search_params["query"],
                        "fields": ["session_name^2", "session_description", "opponent_team", "venue"],
                        "fuzziness": "AUTO"
                    }
                })
            
            # Filters
            if search_params.get("team_id"):
                es_query["bool"]["filter"].append({"term": {"team_id": search_params["team_id"]}})
            
            if search_params.get("competition"):
                es_query["bool"]["filter"].append({"term": {"competition": search_params["competition"]}})
            
            if search_params.get("date_range"):
                date_range = search_params["date_range"]
                es_query["bool"]["filter"].append({
                    "range": {
                        "match_date": {
                            "gte": date_range.get("start"),
                            "lte": date_range.get("end")
                        }
                    }
                })
            
            # Tag filtering
            if search_params.get("tags"):
                for tag in search_params["tags"]:
                    es_query["bool"]["filter"].append({"term": {"tags": tag}})
            
            # Execute search
            search_body = {
                "query": es_query,
                "sort": [
                    {search_params.get("sort_field", "_score"): {"order": search_params.get("sort_order", "desc")}}
                ],
                "size": search_params.get("limit", 50),
                "from": search_params.get("offset", 0),
                "highlight": {
                    "fields": {
                        "session_name": {},
                        "session_description": {},
                        "opponent_team": {},
                        "venue": {}
                    }
                }
            }
            
            response = self.es.search(index=self.search_index, body=search_body)
            
            # Process results
            sessions = []
            for hit in response["hits"]["hits"]:
                session_doc = hit["_source"]
                session_doc["id"] = hit["_id"]
                session_doc["search_score"] = hit["_score"]
                if "highlight" in hit:
                    session_doc["highlights"] = hit["highlight"]
                sessions.append(session_doc)
            
            return {
                "sessions": sessions,
                "total_count": response["hits"]["total"]["value"],
                "search_time": response["took"],
                "max_score": response["hits"]["max_score"]
            }
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
    
    async def update_session_metadata(self, session_id: str, metadata_updates: Dict[str, Any]) -> Dict[str, Any]:
        """Update session metadata with validation"""
        try:
            session = self.db.query(AnalysisSession).filter(AnalysisSession.id == session_id).first()
            if not session:
                raise HTTPException(status_code=404, detail="Session not found")
            
            # Update basic metadata
            updatable_fields = [
                "session_name", "session_description", "match_date", "opponent_team",
                "venue", "competition", "season", "match_type", "importance_level"
            ]
            
            for field in updatable_fields:
                if field in metadata_updates:
                    setattr(session, field, metadata_updates[field])
            
            # Update tags
            if "tags" in metadata_updates:
                session.tags = json.dumps(metadata_updates["tags"])
                await self._update_tag_usage_counts(metadata_updates["tags"])
            
            # Update custom metadata
            if "custom_metadata" in metadata_updates:
                existing_custom = json.loads(session.custom_metadata) if session.custom_metadata else {}
                existing_custom.update(metadata_updates["custom_metadata"])
                session.custom_metadata = json.dumps(existing_custom)
            
            session.updated_at = datetime.utcnow()
            self.db.commit()
            
            # Update Elasticsearch index
            await self._update_search_index(session)
            
            return {
                "session_id": session.id,
                "updated_fields": list(metadata_updates.keys()),
                "updated_at": session.updated_at.isoformat()
            }
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Metadata update failed: {str(e)}")
    
    async def bulk_operations(self, operation_data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform bulk operations on sessions"""
        try:
            session_ids = operation_data["session_ids"]
            operation_type = operation_data["operation_type"]
            operation_params = operation_data.get("params", {})
            
            # Validate sessions exist and user has permissions
            sessions = self.db.query(AnalysisSession).filter(
                AnalysisSession.id.in_(session_ids)
            ).all()
            
            if len(sessions) != len(session_ids):
                raise HTTPException(status_code=404, detail="Some sessions not found")
            
            results = {"success_count": 0, "error_count": 0, "errors": []}
            
            for session in sessions:
                try:
                    if operation_type == "archive":
                        session.status = "archived"
                        session.archive_date = datetime.utcnow()
                    
                    elif operation_type == "delete":
                        session.status = "deleted"
                        session.deletion_date = datetime.utcnow()
                    
                    elif operation_type == "update_tags":
                        new_tags = operation_params.get("tags", [])
                        if operation_params.get("replace_tags", False):
                            session.tags = json.dumps(new_tags)
                        else:
                            existing_tags = json.loads(session.tags) if session.tags else []
                            combined_tags = list(set(existing_tags + new_tags))
                            session.tags = json.dumps(combined_tags)
                    
                    elif operation_type == "update_metadata":
                        metadata_updates = operation_params.get("metadata", {})
                        for field, value in metadata_updates.items():
                            if hasattr(session, field):
                                setattr(session, field, value)
                    
                    elif operation_type == "share":
                        sharing_settings = operation_params.get("sharing_settings", {})
                        session.sharing_settings = json.dumps(sharing_settings)
                    
                    session.updated_at = datetime.utcnow()
                    results["success_count"] += 1
                    
                except Exception as e:
                    results["error_count"] += 1
                    results["errors"].append({
                        "session_id": session.id,
                        "error": str(e)
                    })
            
            self.db.commit()
            
            # Update search index for affected sessions
            await self._bulk_update_search_index([s.id for s in sessions])
            
            return results
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Bulk operation failed: {str(e)}")
    
    async def export_sessions(self, export_params: Dict[str, Any]) -> BytesIO:
        """Export session data in various formats"""
        try:
            # Get sessions based on filters
            session_list = await self.list_sessions(
                export_params.get("filters", {}),
                {"offset": 0, "limit": 10000}  # Export limit
            )
            
            sessions_data = session_list["sessions"]
            export_format = export_params.get("format", "csv")
            columns = export_params.get("columns", ["all"])
            
            # Prepare DataFrame
            df_data = []
            for session in sessions_data:
                row = {}
                if "all" in columns or "session_name" in columns:
                    row["Session Name"] = session["session_name"]
                if "all" in columns or "team_id" in columns:
                    row["Team"] = session["team_id"]
                if "all" in columns or "match_date" in columns:
                    row["Match Date"] = session["match_date"]
                if "all" in columns or "opponent_team" in columns:
                    row["Opponent"] = session["opponent_team"]
                if "all" in columns or "venue" in columns:
                    row["Venue"] = session["venue"]
                if "all" in columns or "competition" in columns:
                    row["Competition"] = session["competition"]
                if "all" in columns or "season" in columns:
                    row["Season"] = session["season"]
                if "all" in columns or "status" in columns:
                    row["Status"] = session["status"]
                if "all" in columns or "tags" in columns:
                    row["Tags"] = ", ".join(session["tags"])
                if "all" in columns or "duration" in columns:
                    row["Duration (min)"] = round(session["video_duration"] / 60, 1) if session["video_duration"] else None
                if "all" in columns or "created_at" in columns:
                    row["Created"] = session["created_at"]
                
                df_data.append(row)
            
            df = pd.DataFrame(df_data)
            
            # Export in requested format
            output = BytesIO()
            
            if export_format == "csv":
                csv_buffer = StringIO()
                df.to_csv(csv_buffer, index=False)
                output.write(csv_buffer.getvalue().encode('utf-8'))
            
            elif export_format == "excel":
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name='Sessions', index=False)
            
            elif export_format == "json":
                json_data = df.to_json(orient='records', date_format='iso')
                output.write(json_data.encode('utf-8'))
            
            output.seek(0)
            return output
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")
    
    async def save_search_query(self, user_id: str, search_data: Dict[str, Any]) -> Dict[str, Any]:
        """Save search query for future use"""
        try:
            saved_search = SavedSearch(
                id=f"search_{uuid.uuid4().hex[:12]}",
                user_id=user_id,
                search_name=search_data["name"],
                search_query=json.dumps(search_data["query"]),
                search_filters=json.dumps(search_data.get("filters", {})),
                is_shared=search_data.get("is_shared", False)
            )
            
            self.db.add(saved_search)
            self.db.commit()
            
            return {
                "search_id": saved_search.id,
                "search_name": saved_search.search_name,
                "created_at": saved_search.created_at.isoformat()
            }
            
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to save search: {str(e)}")
    
    async def _update_tag_usage_counts(self, tags: List[str]) -> None:
        """Update usage counts for tags"""
        try:
            for tag_name in tags:
                tag = self.db.query(SessionTag).filter(SessionTag.tag_name == tag_name).first()
                if tag:
                    tag.usage_count += 1
                else:
                    # Create new tag
                    new_tag = SessionTag(
                        id=f"tag_{uuid.uuid4().hex[:12]}",
                        tag_name=tag_name,
                        created_by="system",
                        usage_count=1
                    )
                    self.db.add(new_tag)
            
            self.db.commit()
            
        except Exception as e:
            # Non-critical, don't fail the main operation
            pass
    
    async def _update_search_index(self, session: AnalysisSession) -> None:
        """Update Elasticsearch index for session"""
        try:
            doc = {
                "session_name": session.session_name,
                "session_description": session.session_description,
                "team_id": session.team_id,
                "opponent_team": session.opponent_team,
                "venue": session.venue,
                "competition": session.competition,
                "season": session.season,
                "match_date": session.match_date.isoformat() if session.match_date else None,
                "tags": json.loads(session.tags) if session.tags else [],
                "status": session.status,
                "importance_level": session.importance_level,
                "updated_at": session.updated_at.isoformat()
            }
            
            self.es.index(index=self.search_index, id=session.id, body=doc)
            
        except Exception as e:
            # Log error but don't fail the main operation
            pass

# API Endpoints
app = FastAPI()
security = HTTPBearer()

@app.get("/api/v1/sessions")
async def list_sessions(
    team_id: Optional[str] = None,
    status: Optional[str] = None,
    competition: Optional[str] = None,
    season: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    tags: Optional[str] = None,
    search_query: Optional[str] = None,
    sort_by: str = "created_at",
    sort_order: str = "desc",
    offset: int = 0,
    limit: int = 50,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """List sessions with filtering and pagination"""
    # Implementation logic here
    pass

@app.post("/api/v1/sessions/search")
async def advanced_search_sessions(
    search_params: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Advanced search with Elasticsearch"""
    # Implementation logic here
    pass

@app.put("/api/v1/sessions/{session_id}/metadata")
async def update_session_metadata(
    session_id: str,
    metadata_updates: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Update session metadata"""
    # Implementation logic here
    pass

@app.post("/api/v1/sessions/bulk")
async def bulk_session_operations(
    operation_data: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Perform bulk operations on sessions"""
    # Implementation logic here
    pass

@app.post("/api/v1/sessions/export")
async def export_session_data(
    export_params: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Export session data in various formats"""
    # Implementation logic here
    pass

@app.get("/api/v1/sessions/tags")
async def get_session_tags(
    search: Optional[str] = None,
    limit: int = 100,
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get available session tags"""
    # Implementation logic here
    pass

@app.post("/api/v1/sessions/searches")
async def save_search_query(
    search_data: Dict[str, Any],
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Save search query for future use"""
    # Implementation logic here
    pass

@app.get("/api/v1/sessions/searches")
async def get_saved_searches(
    credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Get user's saved searches"""
    # Implementation logic here
    pass
```

## Frontend Component Architecture

### Session Organization and Search Interface

```typescript
// React components for session organization and search
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import {
  Box, Card, CardContent, Typography, Button, TextField, Chip,
  Grid, Select, MenuItem, FormControl, InputLabel, IconButton,
  Dialog, DialogTitle, DialogContent, DialogActions, Checkbox,
  List, ListItem, ListItemText, ListItemIcon, Tabs, Tab,
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  Paper, Autocomplete, DatePicker, Tooltip, Badge, Menu,
  Drawer, Divider, Switch, FormControlLabel, Alert
} from '@mui/material';
import {
  Search, FilterList, Sort, ViewModule, ViewList, Archive,
  Delete, Share, GetApp, Tag, Star, MoreVert, Add,
  Edit, Visibility, Schedule, Group, Stadium, EmojiEvents
} from '@mui/icons-material';
import { DataGrid, GridColDef, GridRowSelectionModel } from '@mui/x-data-grid';
import { useSessionStore } from '../stores/sessionStore';

interface AnalysisSession {
  id: string;
  sessionName: string;
  teamId: string;
  matchDate: string;
  opponentTeam: string;
  venue: string;
  competition: string;
  season: string;
  status: string;
  processingStatus: string;
  tags: string[];
  importanceLevel: number;
  videoDuration: number;
  thumbnailUrl: string;
  createdAt: string;
  updatedAt: string;
}

interface SearchFilters {
  teamId?: string;
  status?: string;
  competition?: string;
  season?: string;
  startDate?: string;
  endDate?: string;
  tags?: string[];
  searchQuery?: string;
  importanceLevel?: number[];
}

const SessionOrganizationManager: React.FC = () => {
  const [sessions, setSessions] = useState<AnalysisSession[]>([]);
  const [filteredSessions, setFilteredSessions] = useState<AnalysisSession[]>([]);
  const [selectedSessions, setSelectedSessions] = useState<string[]>([]);
  const [viewMode, setViewMode] = useState<'grid' | 'table'>('grid');
  const [showFilters, setShowFilters] = useState(false);
  const [showBulkActions, setShowBulkActions] = useState(false);
  const [showExportDialog, setShowExportDialog] = useState(false);
  const [showMetadataDialog, setShowMetadataDialog] = useState(false);
  const [selectedSession, setSelectedSession] = useState<AnalysisSession | null>(null);
  
  const [filters, setFilters] = useState<SearchFilters>({});
  const [searchQuery, setSearchQuery] = useState('');
  const [sortBy, setSortBy] = useState('createdAt');
  const [sortOrder, setSortOrder] = useState<'asc' | 'desc'>('desc');
  const [pagination, setPagination] = useState({ offset: 0, limit: 24 });
  const [totalCount, setTotalCount] = useState(0);
  
  const [availableTags, setAvailableTags] = useState<string[]>([]);
  const [savedSearches, setSavedSearches] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const {
    listSessions,
    advancedSearchSessions,
    updateSessionMetadata,
    bulkSessionOperations,
    exportSessionData,
    getSessionTags,
    saveSearchQuery,
    getSavedSearches
  } = useSessionStore();

  useEffect(() => {
    loadSessions();
    loadTags();
    loadSavedSearches();
  }, [filters, sortBy, sortOrder, pagination]);

  const loadSessions = async () => {
    try {
      setLoading(true);
      const params = {
        ...filters,
        search_query: searchQuery,
        sort_by: sortBy,
        sort_order: sortOrder,
        offset: pagination.offset,
        limit: pagination.limit
      };
      
      const result = await listSessions(params);
      setSessions(result.sessions);
      setFilteredSessions(result.sessions);
      setTotalCount(result.total_count);
    } catch (error) {
      console.error('Failed to load sessions:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadTags = async () => {
    try {
      const tags = await getSessionTags();
      setAvailableTags(tags.map((tag: any) => tag.tag_name));
    } catch (error) {
      console.error('Failed to load tags:', error);
    }
  };

  const loadSavedSearches = async () => {
    try {
      const searches = await getSavedSearches();
      setSavedSearches(searches);
    } catch (error) {
      console.error('Failed to load saved searches:', error);
    }
  };

  const handleSearch = useCallback(async (query: string) => {
    if (query.trim() === '') {
      setFilteredSessions(sessions);
      return;
    }

    try {
      setLoading(true);
      const searchParams = {
        query: query,
        filters: filters,
        sort_field: sortBy,
        sort_order: sortOrder,
        offset: pagination.offset,
        limit: pagination.limit
      };
      
      const result = await advancedSearchSessions(searchParams);
      setFilteredSessions(result.sessions);
      setTotalCount(result.total_count);
    } catch (error) {
      console.error('Search failed:', error);
    } finally {
      setLoading(false);
    }
  }, [sessions, filters, sortBy, sortOrder, pagination]);

  const handleFilterChange = (newFilters: Partial<SearchFilters>) => {
    setFilters(prev => ({ ...prev, ...newFilters }));
    setPagination(prev => ({ ...prev, offset: 0 })); // Reset to first page
  };

  const handleBulkOperation = async (operation: string, params?: any) => {
    if (selectedSessions.length === 0) return;

    try {
      const operationData = {
        session_ids: selectedSessions,
        operation_type: operation,
        params: params
      };
      
      await bulkSessionOperations(operationData);
      setSelectedSessions([]);
      setShowBulkActions(false);
      await loadSessions();
    } catch (error) {
      console.error('Bulk operation failed:', error);
    }
  };

  const handleExport = async (exportParams: any) => {
    try {
      const exportData = {
        filters: filters,
        format: exportParams.format,
        columns: exportParams.columns
      };
      
      const result = await exportSessionData(exportData);
      
      // Create download link
      const blob = new Blob([result], { 
        type: exportParams.format === 'csv' ? 'text/csv' : 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
      });
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `sessions_export.${exportParams.format}`;
      a.click();
      window.URL.revokeObjectURL(url);
      
      setShowExportDialog(false);
    } catch (error) {
      console.error('Export failed:', error);
    }
  };

  const handleSaveSearch = async (searchName: string) => {
    try {
      const searchData = {
        name: searchName,
        query: searchQuery,
        filters: filters
      };
      
      await saveSearchQuery(searchData);
      await loadSavedSearches();
    } catch (error) {
      console.error('Failed to save search:', error);
    }
  };

  const SessionCard = ({ session }: { session: AnalysisSession }) => (
    <Card sx={{ height: '100%', position: 'relative' }}>
      <Box sx={{ position: 'relative' }}>
        <img
          src={session.thumbnailUrl || '/default-thumbnail.jpg'}
          alt={session.sessionName}
          style={{ width: '100%', height: 200, objectFit: 'cover' }}
        />
        <Checkbox
          checked={selectedSessions.includes(session.id)}
          onChange={(e) => {
            if (e.target.checked) {
              setSelectedSessions(prev => [...prev, session.id]);
            } else {
              setSelectedSessions(prev => prev.filter(id => id !== session.id));
            }
          }}
          sx={{
            position: 'absolute',
            top: 8,
            left: 8,
            backgroundColor: 'rgba(255,255,255,0.8)'
          }}
        />
        <Box
          sx={{
            position: 'absolute',
            top: 8,
            right: 8,
            display: 'flex',
            gap: 0.5
          }}
        >
          {session.importanceLevel >= 8 && (
            <Star sx={{ color: 'gold', fontSize: 20 }} />
          )}
          <Chip
            label={session.status}
            size="small"
            color={session.status === 'completed' ? 'success' : 'default'}
          />
        </Box>
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
          {Math.round(session.videoDuration / 60)}min
        </Box>
      </Box>
      
      <CardContent>
        <Typography variant="h6" noWrap gutterBottom>
          {session.sessionName}
        </Typography>
        
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Group fontSize="small" color="action" />
          <Typography variant="body2" color="textSecondary">
            vs {session.opponentTeam}
          </Typography>
        </Box>
        
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Stadium fontSize="small" color="action" />
          <Typography variant="body2" color="textSecondary" noWrap>
            {session.venue}
          </Typography>
        </Box>
        
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <Schedule fontSize="small" color="action" />
          <Typography variant="body2" color="textSecondary">
            {new Date(session.matchDate).toLocaleDateString()}
          </Typography>
        </Box>
        
        <Box sx={{ display: 'flex', gap: 0.5, mb: 2, flexWrap: 'wrap' }}>
          <Chip label={session.competition} size="small" />
          {session.tags.slice(0, 2).map((tag, index) => (
            <Chip key={index} label={tag} size="small" variant="outlined" />
          ))}
          {session.tags.length > 2 && (
            <Chip label={`+${session.tags.length - 2}`} size="small" variant="outlined" />
          )}
        </Box>
        
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <Button
            size="small"
            startIcon={<Visibility />}
            onClick={() => {/* Navigate to session */}}
          >
            View
          </Button>
          
          <IconButton
            size="small"
            onClick={(e) => {
              setSelectedSession(session);
              // Show context menu
            }}
          >
            <MoreVert />
          </IconButton>
        </Box>
      </CardContent>
    </Card>
  );

  const SessionTable = () => {
    const columns: GridColDef[] = [
      {
        field: 'sessionName',
        headerName: 'Session Name',
        flex: 1,
        minWidth: 200
      },
      {
        field: 'opponentTeam',
        headerName: 'Opponent',
        width: 150
      },
      {
        field: 'matchDate',
        headerName: 'Date',
        width: 120,
        valueFormatter: (params) => new Date(params.value).toLocaleDateString()
      },
      {
        field: 'venue',
        headerName: 'Venue',
        width: 150
      },
      {
        field: 'competition',
        headerName: 'Competition',
        width: 120
      },
      {
        field: 'status',
        headerName: 'Status',
        width: 100,
        renderCell: (params) => (
          <Chip
            label={params.value}
            size="small"
            color={params.value === 'completed' ? 'success' : 'default'}
          />
        )
      },
      {
        field: 'videoDuration',
        headerName: 'Duration',
        width: 100,
        valueFormatter: (params) => `${Math.round(params.value / 60)}min`
      },
      {
        field: 'actions',
        headerName: 'Actions',
        width: 120,
        sortable: false,
        renderCell: (params) => (
          <Box>
            <IconButton size="small" onClick={() => {/* View session */}}>
              <Visibility />
            </IconButton>
            <IconButton size="small" onClick={() => {
              setSelectedSession(params.row);
              setShowMetadataDialog(true);
            }}>
              <Edit />
            </IconButton>
          </Box>
        )
      }
    ];

    return (
      <DataGrid
        rows={filteredSessions}
        columns={columns}
        checkboxSelection
        disableRowSelectionOnClick
        rowSelectionModel={selectedSessions}
        onRowSelectionModelChange={(newSelection: GridRowSelectionModel) => {
          setSelectedSessions(newSelection as string[]);
        }}
        paginationMode="server"
        rowCount={totalCount}
        paginationModel={{ page: Math.floor(pagination.offset / pagination.limit), pageSize: pagination.limit }}
        onPaginationModelChange={(model) => {
          setPagination({
            offset: model.page * model.pageSize,
            limit: model.pageSize
          });
        }}
        loading={loading}
        sx={{ height: 600 }}
      />
    );
  };

  const FilterDrawer = () => (
    <Drawer
      anchor="right"
      open={showFilters}
      onClose={() => setShowFilters(false)}
      sx={{ '& .MuiDrawer-paper': { width: 320, p: 2 } }}
    >
      <Typography variant="h6" gutterBottom>
        Filters & Search
      </Typography>
      
      <Divider sx={{ mb: 2 }} />
      
      <TextField
        fullWidth
        label="Search sessions..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        onKeyPress={(e) => {
          if (e.key === 'Enter') {
            handleSearch(searchQuery);
          }
        }}
        InputProps={{
          endAdornment: (
            <IconButton onClick={() => handleSearch(searchQuery)}>
              <Search />
            </IconButton>
          )
        }}
        sx={{ mb: 2 }}
      />
      
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel>Status</InputLabel>
        <Select
          value={filters.status || ''}
          onChange={(e) => handleFilterChange({ status: e.target.value })}
        >
          <MenuItem value="">All</MenuItem>
          <MenuItem value="active">Active</MenuItem>
          <MenuItem value="completed">Completed</MenuItem>
          <MenuItem value="processing">Processing</MenuItem>
          <MenuItem value="archived">Archived</MenuItem>
        </Select>
      </FormControl>
      
      <FormControl fullWidth sx={{ mb: 2 }}>
        <InputLabel>Competition</InputLabel>
        <Select
          value={filters.competition || ''}
          onChange={(e) => handleFilterChange({ competition: e.target.value })}
        >
          <MenuItem value="">All</MenuItem>
          <MenuItem value="league">League</MenuItem>
          <MenuItem value="cup">Cup</MenuItem>
          <MenuItem value="friendly">Friendly</MenuItem>
          <MenuItem value="tournament">Tournament</MenuItem>
        </Select>
      </FormControl>
      
      <Autocomplete
        multiple
        options={availableTags}
        value={filters.tags || []}
        onChange={(_, newValue) => handleFilterChange({ tags: newValue })}
        renderInput={(params) => (
          <TextField {...params} label="Tags" />
        )}
        renderTags={(value, getTagProps) =>
          value.map((option, index) => (
            <Chip
              label={option}
              {...getTagProps({ index })}
              key={option}
              size="small"
            />
          ))
        }
        sx={{ mb: 2 }}
      />
      
      <Box sx={{ display: 'flex', gap: 1, mt: 2 }}>
        <Button
          variant="outlined"
          onClick={() => {
            setFilters({});
            setSearchQuery('');
          }}
        >
          Clear All
        </Button>
        <Button
          variant="contained"
          onClick={() => handleSearch(searchQuery)}
        >
          Apply
        </Button>
      </Box>
      
      <Divider sx={{ my: 2 }} />
      
      <Typography variant="subtitle2" gutterBottom>
        Saved Searches
      </Typography>
      
      <List dense>
        {savedSearches.map((search) => (
          <ListItem
            key={search.id}
            button
            onClick={() => {
              // Load saved search
            }}
          >
            <ListItemText primary={search.search_name} />
          </ListItem>
        ))}
      </List>
      
      <Button
        startIcon={<Add />}
        onClick={() => {
          const name = prompt('Enter search name:');
          if (name) {
            handleSaveSearch(name);
          }
        }}
        sx={{ mt: 1 }}
      >
        Save Current Search
      </Button>
    </Drawer>
  );

  return (
    <Box sx={{ p: 3 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
        <Typography variant="h4">
          Session Management
        </Typography>
        
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            size="small"
            placeholder="Quick search..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onKeyPress={(e) => {
              if (e.key === 'Enter') {
                handleSearch(searchQuery);
              }
            }}
            InputProps={{
              endAdornment: (
                <IconButton size="small" onClick={() => handleSearch(searchQuery)}>
                  <Search />
                </IconButton>
              )
            }}
          />
          
          <Button
            variant="outlined"
            startIcon={<FilterList />}
            onClick={() => setShowFilters(true)}
          >
            Filters
          </Button>
          
          <Button
            variant="outlined"
            startIcon={viewMode === 'grid' ? <ViewList /> : <ViewModule />}
            onClick={() => setViewMode(viewMode === 'grid' ? 'table' : 'grid')}
          >
            {viewMode === 'grid' ? 'Table' : 'Grid'}
          </Button>
          
          {selectedSessions.length > 0 && (
            <Button
              variant="contained"
              color="secondary"
              onClick={() => setShowBulkActions(true)}
            >
              Actions ({selectedSessions.length})
            </Button>
          )}
        </Box>
      </Box>
      
      {loading && (
        <Alert severity="info" sx={{ mb: 2 }}>
          Loading sessions...
        </Alert>
      )}
      
      {viewMode === 'grid' ? (
        <Grid container spacing={2}>
          {filteredSessions.map((session) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={session.id}>
              <SessionCard session={session} />
            </Grid>
          ))}
        </Grid>
      ) : (
        <SessionTable />
      )}
      
      <FilterDrawer />
      
      {/* Bulk Actions Dialog */}
      <Dialog
        open={showBulkActions}
        onClose={() => setShowBulkActions(false)}
      >
        <DialogTitle>Bulk Actions</DialogTitle>
        <DialogContent>
          <Typography gutterBottom>
            {selectedSessions.length} sessions selected
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            <Button onClick={() => handleBulkOperation('archive')}>
              Archive Sessions
            </Button>
            <Button onClick={() => handleBulkOperation('delete')}>
              Delete Sessions
            </Button>
            <Button onClick={() => setShowExportDialog(true)}>
              Export Sessions
            </Button>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowBulkActions(false)}>
            Cancel
          </Button>
        </DialogActions>
      </Dialog>
      
      {/* Export Dialog */}
      <Dialog
        open={showExportDialog}
        onClose={() => setShowExportDialog(false)}
      >
        <DialogTitle>Export Sessions</DialogTitle>
        <DialogContent>
          <FormControl fullWidth sx={{ mb: 2 }}>
            <InputLabel>Format</InputLabel>
            <Select defaultValue="csv">
              <MenuItem value="csv">CSV</MenuItem>
              <MenuItem value="excel">Excel</MenuItem>
              <MenuItem value="json">JSON</MenuItem>
            </Select>
          </FormControl>
          {/* Column selection would go here */}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setShowExportDialog(false)}>
            Cancel
          </Button>
          <Button
            variant="contained"
            onClick={() => handleExport({ format: 'csv', columns: ['all'] })}
          >
            Export
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default SessionOrganizationManager;
```

## Performance Considerations

1. **Search Performance**
   - Elasticsearch integration for fast full-text search
   - Database indexing on frequently queried fields
   - Efficient pagination with cursor-based navigation

2. **UI Performance**
   - Virtualized rendering for large session lists  
   - Lazy loading of thumbnail images
   - Optimized filtering with debounced search queries

3. **Data Management**
   - Efficient bulk operations with batch processing
   - Smart caching of search results and metadata
   - Optimized database queries with proper indexing

## Security

1. **Access Control**
   - Session-level permissions with team-based access
   - Secure sharing with token-based authentication
   - Audit logging for all session operations

2. **Data Protection**
   - Secure metadata handling with validation
   - Protected bulk operations with confirmation workflows  
   - Safe archival and deletion with recovery options

3. **Search Security**
   - Query sanitization to prevent injection attacks
   - Access-controlled search results based on permissions
   - Secure export functionality with data protection

## Testing

```python
# Comprehensive testing for session organization features
import pytest
from unittest.mock import Mock, patch, AsyncMock
from datetime import datetime, timedelta

class TestSessionOrganizationManager:
    
    @pytest.fixture
    def session_manager(self):
        mock_db = Mock()
        mock_es = Mock()
        return SessionOrganizationManager(mock_db, mock_es)
    
    @pytest.mark.asyncio
    async def test_list_sessions_with_filters(self, session_manager):
        """Test session listing with various filters"""
        filter_params = {
            "team_id": "team_123",
            "status": "completed", 
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "tags": ["important", "championship"]
        }
        pagination = {"offset": 0, "limit": 24}
        
        # Mock database query
        mock_sessions = [Mock() for _ in range(5)]
        session_manager.db.query().filter().count.return_value = 100
        session_manager.db.query().filter().offset().limit().all.return_value = mock_sessions
        
        result = await session_manager.list_sessions(filter_params, pagination)
        
        assert result["total_count"] == 100
        assert len(result["sessions"]) == 5
        assert result["has_more"] == True
    
    @pytest.mark.asyncio
    async def test_advanced_search(self, session_manager):
        """Test Elasticsearch advanced search functionality"""
        search_params = {
            "query": "championship final",
            "team_id": "team_123",
            "date_range": {"start": "2024-01-01", "end": "2024-12-31"},
            "tags": ["important"],
            "sort_field": "_score",
            "sort_order": "desc"
        }
        
        # Mock Elasticsearch response
        mock_es_response = {
            "hits": {
                "hits": [
                    {"_id": "session_1", "_source": {"session_name": "Championship Final"}, "_score": 5.2},
                    {"_id": "session_2", "_source": {"session_name": "Semi Final"}, "_score": 4.8}
                ],
                "total": {"value": 2},
                "max_score": 5.2
            },
            "took": 15
        }
        session_manager.es.search.return_value = mock_es_response
        
        result = await session_manager.advanced_search(search_params)
        
        assert result["total_count"] == 2
        assert len(result["sessions"]) == 2
        assert result["search_time"] == 15
        assert result["sessions"][0]["search_score"] == 5.2
    
    @pytest.mark.asyncio
    async def test_bulk_operations(self, session_manager):
        """Test bulk operations on multiple sessions"""
        operation_data = {
            "session_ids": ["session_1", "session_2", "session_3"],
            "operation_type": "update_tags",
            "params": {
                "tags": ["playoff", "important"],
                "replace_tags": False
            }
        }
        
        # Mock sessions
        mock_sessions = [Mock() for _ in range(3)]
        for session in mock_sessions:
            session.tags = '["existing_tag"]'
        session_manager.db.query().filter().all.return_value = mock_sessions
        
        result = await session_manager.bulk_operations(operation_data)
        
        assert result["success_count"] == 3
        assert result["error_count"] == 0
    
    @pytest.mark.asyncio
    async def test_export_sessions(self, session_manager):
        """Test session data export functionality"""
        export_params = {
            "filters": {"team_id": "team_123"},
            "format": "csv",
            "columns": ["session_name", "match_date", "opponent_team"]
        }
        
        # Mock session data
        mock_session_list = {
            "sessions": [
                {
                    "session_name": "Test Match",
                    "match_date": "2024-01-15T00:00:00",
                    "opponent_team": "Rival Team",
                    "tags": ["important"]
                }
            ]
        }
        
        session_manager.list_sessions = AsyncMock(return_value=mock_session_list)
        
        result = await session_manager.export_sessions(export_params)
        
        assert isinstance(result, BytesIO)
        result.seek(0)
        content = result.read().decode('utf-8')
        assert "Test Match" in content
        assert "Rival Team" in content
    
    def test_tag_usage_tracking(self, session_manager):
        """Test tag usage count updates"""
        tags = ["important", "championship", "final"]
        
        # Mock existing tags
        existing_tag = Mock()
        existing_tag.usage_count = 5
        session_manager.db.query().filter().first.return_value = existing_tag
        
        # This would be called within _update_tag_usage_counts
        # Test that usage count is incremented
        pass
    
    @pytest.mark.asyncio
    async def test_metadata_update(self, session_manager):
        """Test session metadata updates"""
        session_id = "session_123"
        metadata_updates = {
            "session_name": "Updated Championship Final",
            "tags": ["championship", "victory", "historic"],
            "custom_metadata": {"mvp": "Player Name", "score": "3-1"}
        }
        
        # Mock existing session
        mock_session = Mock()
        mock_session.id = session_id
        mock_session.tags = '["old_tag"]'
        mock_session.custom_metadata = '{"old_field": "old_value"}'
        session_manager.db.query().filter().first.return_value = mock_session
        
        result = await session_manager.update_session_metadata(session_id, metadata_updates)
        
        assert result["session_id"] == session_id
        assert "session_name" in result["updated_fields"]
        assert "tags" in result["updated_fields"]

# Integration tests
class TestSessionSearchIntegration:
    
    @pytest.mark.asyncio
    async def test_elasticsearch_indexing(self):
        """Test Elasticsearch indexing and search integration"""
        # Test that sessions are properly indexed in Elasticsearch
        pass
    
    @pytest.mark.asyncio
    async def test_full_text_search_accuracy(self):
        """Test search result accuracy and relevance"""
        # Test search result ranking and relevance
        pass

# Performance tests
class TestSessionPerformance:
    
    @pytest.mark.asyncio
    async def test_large_session_list_performance(self):
        """Test performance with large numbers of sessions"""
        # Test pagination and filtering performance
        pass
    
    @pytest.mark.asyncio
    async def test_bulk_operation_performance(self):
        """Test bulk operation performance"""
        # Test bulk operations with many sessions
        pass
```

## Monitoring

1. **Search Analytics**
   - Search query performance and response times
   - Popular search terms and filter combinations
   - Search result relevance and click-through rates

2. **Usage Metrics**
   - Session organization patterns and workflows
   - Bulk operation usage and success rates
   - Export frequency and format preferences

3. **Performance Monitoring**
   - Database query performance for session lists
   - Elasticsearch search latency and accuracy
   - UI responsiveness for large session collections

## Definition of Done

- [ ] Session listing interface with grid and table views implemented
- [ ] Advanced search functionality with Elasticsearch integration
- [ ] Comprehensive metadata management with custom fields support
- [ ] Dynamic tagging system with hierarchical categories
- [ ] Session archiving and deletion with confirmation workflows
- [ ] Bulk operations for efficient season management
- [ ] Session sharing controls with permission management
- [ ] Export functionality with multiple format support (CSV, Excel, JSON)
- [ ] All organization features tested with comprehensive coverage
- [ ] Performance benchmarks met for search and filtering operations (<2s response)
- [ ] UI responsiveness validated for large session collections (>1000 sessions)
- [ ] Search accuracy above 90% for relevant results

## Dependencies

- **Story 3.3**: Timeline interface for session data structure
- **Story 1.2**: User authentication for access control
- **Story 4.1**: Role-based access for team permissions

## Risks

1. **Search Performance**
   - **Risk**: Search queries may become slow with large datasets
   - **Mitigation**: Implement efficient indexing and query optimization

2. **Data Consistency**
   - **Risk**: Metadata updates may cause inconsistency between database and search index
   - **Mitigation**: Implement transactional updates with rollback capabilities

3. **User Experience Complexity**
   - **Risk**: Advanced search features may overwhelm users
   - **Mitigation**: Progressive disclosure and intuitive defaults

## Change Log

| Date | Version | Changes | Author |
|------|---------|---------|---------|
| 2024-01-23 | 1.0 | Initial story creation with comprehensive session organization and search system | PM Team |