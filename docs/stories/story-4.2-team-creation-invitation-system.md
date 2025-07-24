# Story 4.2: Team Creation and Invitation System

## Status
🟡 **PENDING** - Comprehensive team creation and invitation system with role-based access and subscription management

## Story
**As a** coach,
**I want** team creation and invitation system for multiple users,
**so that** I can organize my coaching staff and provide access to our team's analysis content.

## Acceptance Criteria
1. Team creation workflow with basic team information (name, sport, settings) ⏳
2. Email-based invitation system with custom invitation messages ⏳
3. Invitation acceptance flow with account creation or existing account linking ⏳
4. Team member listing with role indicators and management controls ⏳
5. Team settings management including subscription tier and feature access ⏳
6. Member removal and deactivation capabilities with content preservation ⏳
7. Team transfer functionality for ownership changes ⏳
8. Integration with subscription billing and user limit enforcement ⏳

## Tasks / Subtasks

- [ ] **Task 4.2.1: Team Creation Workflow & Initial Setup** ⏳
  - [ ] Create team creation wizard with step-by-step setup process
  - [ ] Implement team information form with name, sport type, and description
  - [ ] Add team logo upload with image processing and storage
  - [ ] Create team settings configuration with default preferences
  - [ ] Implement sport-specific settings and analysis configurations
  - [ ] Add team URL/slug generation with availability checking
  - [ ] Create team validation rules with business logic enforcement
  - [ ] Implement team creation confirmation with email verification
  - [ ] Add team creation analytics with setup completion tracking
  - [ ] Create team import functionality for migrating existing teams
  - [ ] Implement team creation API with comprehensive validation
  - [ ] Add team creation rate limiting to prevent abuse
  - [ ] Create team creation documentation with best practices
  - [ ] Implement team creation testing with automated validation
  - [ ] Add team creation accessibility features for inclusive setup
  - **Estimate:** 20 hours | **Priority:** Critical | **Dependencies:** Story 4.1 (RBAC)
  - **Deliverables:**
    - Complete team creation wizard with validation and confirmation
    - Team information management with logo upload and settings
    - Sport-specific configuration with analysis preferences
    - Team URL generation with availability checking
    - Comprehensive API with rate limiting and validation

- [ ] **Task 4.2.2: Email-Based Invitation System** ⏳
  - [ ] Create invitation email templates with responsive design and branding
  - [ ] Implement invitation workflow with role pre-assignment and custom messages
  - [ ] Add invitation link generation with secure token and expiration
  - [ ] Create batch invitation functionality for multiple users
  - [ ] Implement invitation tracking with delivery status and read receipts
  - [ ] Add invitation customization with team branding and personalization
  - [ ] Create invitation reminder system with automated follow-up
  - [ ] Implement invitation validation with email verification
  - [ ] Add invitation analytics with acceptance rates and user engagement
  - [ ] Create invitation API with comprehensive webhook support
  - [ ] Implement invitation security with token validation and fraud prevention
  - [ ] Add invitation internationalization with multi-language support
  - [ ] Create invitation accessibility features with screen reader compatibility
  - [ ] Implement invitation integration with external email services
  - [ ] Add invitation compliance features with GDPR and privacy regulations
  - **Estimate:** 18 hours | **Priority:** Critical | **Dependencies:** Task 4.2.1
  - **Deliverables:**
    - Professional email templates with team branding
    - Secure invitation system with token validation and expiration
    - Batch invitation tools with progress tracking
    - Automated reminder system with analytics
    - Comprehensive API with webhook and integration support

- [ ] **Task 4.2.3: Invitation Acceptance & Account Creation Flow** ⏳
  - [ ] Create invitation acceptance landing page with team information preview
  - [ ] Implement account creation flow for new users with role assignment
  - [ ] Add existing account linking with invitation token validation
  - [ ] Create user onboarding flow with role-specific feature introduction
  - [ ] Implement invitation acceptance validation with business rule enforcement
  - [ ] Add invitation decline functionality with feedback collection
  - [ ] Create account verification process with email confirmation
  - [ ] Implement invitation acceptance analytics with user journey tracking
  - [ ] Add invitation acceptance security with fraud detection
  - [ ] Create invitation acceptance API with comprehensive error handling
  - [ ] Implement invitation acceptance testing with automated validation
  - [ ] Add invitation acceptance accessibility features for inclusive experience
  - [ ] Create invitation acceptance documentation with user guides
  - [ ] Implement invitation acceptance integration with authentication systems
  - [ ] Add invitation acceptance compliance with data protection regulations
  - **Estimate:** 16 hours | **Priority:** Critical | **Dependencies:** Task 4.2.2
  - **Deliverables:**
    - Comprehensive invitation acceptance flow with account creation
    - Role-specific onboarding with feature introduction
    - Account linking with existing user validation
    - Security measures with fraud detection and validation
    - Complete API with error handling and testing

- [ ] **Task 4.2.4: Team Member Management Interface** ⏳
  - [ ] Create team member listing with role indicators and activity status
  - [ ] Implement member search and filtering with advanced query options
  - [ ] Add member profile management with contact information and preferences
  - [ ] Create member role assignment interface with bulk operations
  - [ ] Implement member activity tracking with engagement metrics
  - [ ] Add member communication tools with messaging and notifications
  - [ ] Create member export functionality with data formatting options
  - [ ] Implement member analytics with contribution analysis
  - [ ] Add member integration with external directory services
  - [ ] Create member validation with data quality checking
  - [ ] Implement member security with access control and audit logging
  - [ ] Add member accessibility features with assistive technology support
  - [ ] Create member documentation with management best practices
  - [ ] Implement member testing with automated interaction validation
  - [ ] Add member compliance features with privacy and data protection
  - **Estimate:** 14 hours | **Priority:** High | **Dependencies:** Task 4.2.3
  - **Deliverables:**
    - Comprehensive member management interface with advanced features
    - Role-based member operations with bulk assignment tools
    - Activity tracking with engagement analytics
    - Communication tools with notification integration
    - Security and compliance features with audit logging

- [ ] **Task 4.2.5: Team Settings & Subscription Management** ⏳
  - [ ] Create team settings interface with comprehensive configuration options
  - [ ] Implement subscription tier management with feature access control
  - [ ] Add billing integration with usage tracking and cost monitoring
  - [ ] Create feature flag management with subscription-based availability
  - [ ] Implement usage quota management with alerts and enforcement
  - [ ] Add team branding configuration with logo and color customization
  - [ ] Create data retention settings with backup and archival policies
  - [ ] Implement integration settings with external service connections
  - [ ] Add security settings with access control and authentication policies
  - [ ] Create notification settings with team-wide alert preferences
  - [ ] Implement team settings validation with business rule enforcement
  - [ ] Add team settings analytics with configuration usage tracking
  - [ ] Create team settings API with comprehensive validation and testing
  - [ ] Implement team settings documentation with configuration guides
  - [ ] Add team settings accessibility with screen reader and keyboard support
  - **Estimate:** 22 hours | **Priority:** High | **Dependencies:** Task 4.2.4
  - **Deliverables:**
    - Complete team settings interface with subscription integration
    - Billing and usage management with cost monitoring
    - Feature flag system with subscription-based access control
    - Branding and customization tools
    - Comprehensive validation and documentation

- [ ] **Task 4.2.6: Member Removal & Content Preservation** ⏳
  - [ ] Create member removal workflow with content ownership transfer
  - [ ] Implement soft deletion with member reactivation capabilities
  - [ ] Add content preservation with ownership reassignment options
  - [ ] Create member deactivation with access revocation and cleanup
  - [ ] Implement removal confirmation with impact assessment
  - [ ] Add removal audit logging with detailed action tracking
  - [ ] Create bulk removal functionality with batch processing
  - [ ] Implement removal validation with business rule enforcement
  - [ ] Add removal notification system with team member alerts
  - [ ] Create removal analytics with departure pattern analysis
  - [ ] Implement removal API with comprehensive error handling
  - [ ] Add removal security with fraud prevention and validation
  - [ ] Create removal documentation with process guidelines
  - [ ] Implement removal testing with data integrity validation
  - [ ] Add removal compliance with data protection and privacy regulations
  - **Estimate:** 16 hours | **Priority:** Medium | **Dependencies:** Task 4.2.5
  - **Deliverables:**
    - Safe member removal with content preservation
    - Soft deletion with reactivation capabilities
    - Ownership transfer tools with validation
    - Comprehensive audit logging and analytics
    - API with security and compliance features

- [ ] **Task 4.2.7: Team Ownership Transfer System** ⏳
  - [ ] Create team ownership transfer workflow with validation and confirmation
  - [ ] Implement ownership transfer interface with candidate selection
  - [ ] Add transfer approval process with multi-step verification
  - [ ] Create ownership transition with gradual permission transfer
  - [ ] Implement transfer validation with business rule enforcement
  - [ ] Add transfer notification system with stakeholder alerts
  - [ ] Create transfer audit logging with detailed change tracking
  - [ ] Implement transfer rollback capabilities with emergency procedures
  - [ ] Add transfer analytics with ownership change pattern analysis
  - [ ] Create transfer API with comprehensive security measures
  - [ ] Implement transfer testing with data integrity validation
  - [ ] Add transfer documentation with legal and procedural guidelines
  - [ ] Create transfer accessibility features with inclusive design
  - [ ] Implement transfer integration with billing and subscription systems
  - [ ] Add transfer compliance with legal and regulatory requirements
  - **Estimate:** 18 hours | **Priority:** Medium | **Dependencies:** Task 4.2.6
  - **Deliverables:**
    - Secure team ownership transfer system
    - Multi-step approval process with validation
    - Gradual permission transition with rollback capabilities
    - Comprehensive audit logging and analytics
    - Legal compliance and documentation

- [ ] **Task 4.2.8: Subscription Integration & User Limits** ⏳
  - [ ] Create subscription tier management with feature access control
  - [ ] Implement user limit enforcement with subscription validation
  - [ ] Add billing integration with usage-based pricing and metering
  - [ ] Create subscription upgrade/downgrade workflows with impact assessment
  - [ ] Implement usage monitoring with quota tracking and alerts
  - [ ] Add subscription analytics with usage pattern analysis
  - [ ] Create subscription notification system with billing alerts
  - [ ] Implement subscription API with comprehensive billing integration
  - [ ] Add subscription security with fraud detection and validation
  - [ ] Create subscription documentation with pricing and feature guides
  - [ ] Implement subscription testing with payment and billing validation
  - [ ] Add subscription accessibility with inclusive pricing interfaces
  - [ ] Create subscription compliance with billing and tax regulations
  - [ ] Implement subscription integration with external payment systems
  - [ ] Add subscription support with customer service integration
  - **Estimate:** 20 hours | **Priority:** High | **Dependencies:** Task 4.2.7
  - **Deliverables:**
    - Complete subscription management with billing integration
    - User limit enforcement with validation and alerts
    - Usage monitoring with analytics and optimization
    - Upgrade/downgrade workflows with impact assessment
    - Comprehensive API with security and compliance

## API Implementation ⏳

### Team Management Endpoints (20 endpoints)
- [ ] **POST /teams** - Create new team
  - Request: team_name, sport_type, description, initial_settings, logo_url
  - Response: team_id, team_slug, creation_status, subscription_info
  - Features: Team creation, validation, initial setup

- [ ] **GET /teams/{team_id}** - Get team information
  - Response: team_details, member_count, subscription_status, settings_summary
  - Features: Complete team profile, member statistics, subscription details

- [ ] **PUT /teams/{team_id}** - Update team information
  - Request: team_updates, settings_changes, branding_updates
  - Response: update_status, validation_results, change_log
  - Features: Team profile updates, settings management, change tracking

- [ ] **DELETE /teams/{team_id}** - Delete team
  - Request: deletion_confirmation, data_export_options, transfer_settings
  - Response: deletion_status, data_export_info, cleanup_summary
  - Features: Safe deletion, data export, member notification

- [ ] **POST /teams/{team_id}/invitations** - Send team invitations
  - Request: invitee_emails, roles, custom_message, expiration_date
  - Response: invitation_ids, email_status, delivery_confirmation
  - Features: Batch invitations, role assignment, custom messaging

- [ ] **GET /teams/{team_id}/invitations** - Get team invitations
  - Response: invitations_list, status_summary, acceptance_analytics
  - Features: Invitation tracking, status monitoring, analytics

- [ ] **PUT /invitations/{invitation_id}/resend** - Resend invitation
  - Response: resend_status, delivery_confirmation, updated_expiration
  - Features: Invitation management, delivery tracking

- [ ] **DELETE /invitations/{invitation_id}** - Cancel invitation
  - Response: cancellation_status, cleanup_actions, notification_sent
  - Features: Invitation cancellation, automatic cleanup

- [ ] **POST /invitations/{invitation_id}/accept** - Accept team invitation
  - Request: acceptance_data, user_preferences, account_info
  - Response: acceptance_status, team_membership_info, onboarding_steps
  - Features: Account creation/linking, role assignment, onboarding

- [ ] **POST /invitations/{invitation_id}/decline** - Decline invitation
  - Request: decline_reason, feedback
  - Response: decline_status, feedback_recorded
  - Features: Invitation decline, feedback collection

- [ ] **GET /teams/{team_id}/members** - Get team members
  - Response: members_list, role_distribution, activity_summary
  - Features: Member listing, role indicators, activity tracking

- [ ] **POST /teams/{team_id}/members** - Add team member
  - Request: user_id, role, permissions, notification_settings
  - Response: membership_id, assignment_status, welcome_sent
  - Features: Direct member addition, role assignment

- [ ] **PUT /teams/{team_id}/members/{user_id}** - Update member
  - Request: role_updates, permission_changes, settings_updates
  - Response: update_status, change_log, notification_sent
  - Features: Member management, role updates, change tracking

- [ ] **DELETE /teams/{team_id}/members/{user_id}** - Remove member
  - Request: removal_reason, content_transfer, deactivation_type
  - Response: removal_status, content_transfer_info, cleanup_summary
  - Features: Member removal, content preservation, soft deletion

- [ ] **POST /teams/{team_id}/transfer-ownership** - Transfer team ownership
  - Request: new_owner_id, transfer_reason, effective_date
  - Response: transfer_id, approval_workflow, notification_sent
  - Features: Ownership transfer, approval process, validation

- [ ] **GET /teams/{team_id}/settings** - Get team settings
  - Response: team_config, subscription_details, feature_flags, preferences
  - Features: Settings management, subscription info, feature access

- [ ] **PUT /teams/{team_id}/settings** - Update team settings
  - Request: settings_updates, subscription_changes, feature_preferences
  - Response: update_status, validation_results, billing_impact
  - Features: Settings management, subscription updates, validation

- [ ] **GET /teams/{team_id}/subscription** - Get subscription details
  - Response: subscription_info, usage_stats, billing_history, limits
  - Features: Subscription management, usage tracking, billing info

- [ ] **PUT /teams/{team_id}/subscription** - Update subscription
  - Request: subscription_tier, feature_additions, billing_preferences
  - Response: update_status, billing_changes, effective_date
  - Features: Subscription changes, billing updates, feature access

- [ ] **GET /teams/{team_id}/analytics** - Get team analytics
  - Response: usage_metrics, member_activity, feature_adoption, trends
  - Features: Team analytics, usage patterns, optimization insights

## Frontend Component Architecture ⏳

### Team Management Components
```typescript
// Core team management interfaces
interface TeamManagementProps {
  onTeamCreate?: (team: Team) => void;
  onTeamUpdate?: (teamId: string, updates: TeamUpdate) => void;
  onMemberInvite?: (invitations: Invitation[]) => void;
}

// Main team management components
export const TeamCreationWizard: React.FC<TeamCreationProps>
export const TeamDashboard: React.FC<TeamDashboardProps>
export const InvitationManager: React.FC<InvitationManagerProps>
export const MemberManagement: React.FC<MemberManagementProps>
export const TeamSettings: React.FC<TeamSettingsProps>

// Invitation components
export const InvitationForm: React.FC<InvitationFormProps>
export const InvitationAcceptance: React.FC<InvitationAcceptanceProps>
export const InvitationTracker: React.FC<InvitationTrackerProps>
export const BulkInvitationTool: React.FC<BulkInvitationProps>

// Member management components
export const MemberList: React.FC<MemberListProps>
export const MemberProfile: React.FC<MemberProfileProps>
export const RoleAssignment: React.FC<RoleAssignmentProps>
export const MemberRemovalDialog: React.FC<MemberRemovalProps>

// Settings components
export const SubscriptionManager: React.FC<SubscriptionManagerProps>
export const TeamBranding: React.FC<TeamBrandingProps>
export const UsageMonitor: React.FC<UsageMonitorProps>
export const OwnershipTransfer: React.FC<OwnershipTransferProps>
```

### Team State Management
```typescript
interface TeamManagementState {
  // Team information
  currentTeam: Team | null;
  userTeams: Team[];
  teamSettings: TeamSettings;
  subscriptionInfo: SubscriptionInfo;
  
  // Members and invitations
  teamMembers: TeamMember[];
  pendingInvitations: Invitation[];
  memberRoles: RoleAssignment[];
  
  // UI state
  creationWizardStep: number;
  selectedMembers: string[];
  invitationDialog: InvitationDialog | null;
  memberRemovalDialog: MemberRemovalDialog | null;
  
  // Analytics and usage
  teamAnalytics: TeamAnalytics;
  usageMetrics: UsageMetrics;
  billingInfo: BillingInfo;
  
  // Actions
  createTeam: (teamData: CreateTeamRequest) => Promise<Team>;
  updateTeam: (teamId: string, updates: TeamUpdate) => Promise<void>;
  inviteMembers: (invitations: InvitationRequest[]) => Promise<void>;
  removeMember: (userId: string, reason: string) => Promise<void>;
  
  // Subscription actions
  updateSubscription: (tier: SubscriptionTier) => Promise<void>;
  monitorUsage: () => Promise<UsageMetrics>;
  
  // Transfer actions
  transferOwnership: (newOwnerId: string) => Promise<void>;
  
  // Analytics actions
  loadTeamAnalytics: (timeRange: TimeRange) => Promise<void>;
  exportTeamData: (options: ExportOptions) => Promise<void>;
}
```

## Team Management Implementation ⏳

### Team Creation System
```typescript
// Team Creation Wizard Component
import React, { useState, useCallback } from 'react';
import { TeamCreationState, CreateTeamRequest, SportType } from './types';

export const TeamCreationWizard: React.FC<TeamCreationProps> = ({
  onTeamCreate,
  onCancel
}) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [teamData, setTeamData] = useState<CreateTeamRequest>({
    name: '',
    sport: SportType.SOCCER,
    description: '',
    logo: null,
    settings: {
      defaultAnalysisSettings: {},
      notificationPreferences: {},
      privacySettings: {}
    }
  });
  const [validation, setValidation] = useState<ValidationResult>({});
  const [isLoading, setIsLoading] = useState(false);

  const steps = [
    'Basic Information',
    'Sport Configuration', 
    'Team Settings',
    'Confirmation'
  ];

  // Validate current step
  const validateStep = useCallback((step: number): boolean => {
    const errors: Record<string, string> = {};
    
    switch (step) {
      case 0: // Basic Information
        if (!teamData.name.trim()) {
          errors.name = 'Team name is required';
        } else if (teamData.name.length < 2) {
          errors.name = 'Team name must be at least 2 characters';
        }
        
        if (!teamData.description.trim()) {
          errors.description = 'Team description is required';
        }
        break;
        
      case 1: // Sport Configuration
        if (!teamData.sport) {
          errors.sport = 'Sport selection is required';
        }
        break;
        
      case 2: // Team Settings
        // Validate settings if needed
        break;
    }
    
    setValidation({ errors, isValid: Object.keys(errors).length === 0 });
    return Object.keys(errors).length === 0;
  }, [teamData]);

  // Handle next step
  const handleNext = useCallback(() => {
    if (validateStep(currentStep)) {
      if (currentStep < steps.length - 1) {
        setCurrentStep(prev => prev + 1);
      } else {
        handleSubmit();
      }
    }
  }, [currentStep, validateStep]);

  // Handle previous step  
  const handlePrevious = useCallback(() => {
    if (currentStep > 0) {
      setCurrentStep(prev => prev - 1);
    }
  }, [currentStep]);

  // Submit team creation
  const handleSubmit = useCallback(async () => {
    setIsLoading(true);
    
    try {
      // Check team name availability
      const isAvailable = await checkTeamNameAvailability(teamData.name);
      if (!isAvailable) {
        setValidation({
          errors: { name: 'Team name is already taken' },
          isValid: false
        });
        setCurrentStep(0);
        return;
      }
      
      // Create team
      const newTeam = await createTeam(teamData);
      
      // Show success message
      showSuccessMessage('Team created successfully!');
      
      // Call parent callback
      onTeamCreate?.(newTeam);
      
    } catch (error) {
      console.error('Team creation failed:', error);
      showErrorMessage('Failed to create team. Please try again.');
    } finally {
      setIsLoading(false);
    }
  }, [teamData, onTeamCreate]);

  // Render step content
  const renderStepContent = () => {
    switch (currentStep) {
      case 0:
        return (
          <BasicInformationStep
            data={teamData}
            validation={validation}
            onChange={(updates) => setTeamData(prev => ({ ...prev, ...updates }))}
          />
        );
        
      case 1:
        return (
          <SportConfigurationStep
            data={teamData}
            validation={validation}
            onChange={(updates) => setTeamData(prev => ({ ...prev, ...updates }))}
          />
        );
        
      case 2:
        return (
          <TeamSettingsStep
            data={teamData}
            validation={validation}
            onChange={(updates) => setTeamData(prev => ({ ...prev, ...updates }))}
          />
        );
        
      case 3:
        return (
          <ConfirmationStep
            data={teamData}
            onEdit={(step) => setCurrentStep(step)}
          />
        );
        
      default:
        return null;
    }
  };

  return (
    <div className="team-creation-wizard">
      <div className="wizard-header">
        <h2>Create New Team</h2>
        <div className="step-indicator">
          {steps.map((step, index) => (
            <div
              key={index}
              className={`step ${index === currentStep ? 'active' : ''} ${
                index < currentStep ? 'completed' : ''
              }`}
            >
              <div className="step-number">{index + 1}</div>
              <div className="step-label">{step}</div>
            </div>
          ))}
        </div>
      </div>
      
      <div className="wizard-content">
        {renderStepContent()}
      </div>
      
      <div className="wizard-actions">
        <button
          type="button"
          onClick={onCancel}
          className="btn btn-secondary"
          disabled={isLoading}
        >
          Cancel
        </button>
        
        {currentStep > 0 && (
          <button
            type="button"
            onClick={handlePrevious}
            className="btn btn-outline"
            disabled={isLoading}
          >
            Previous
          </button>
        )}
        
        <button
          type="button"
          onClick={handleNext}
          className="btn btn-primary"
          disabled={isLoading || (validation.errors && Object.keys(validation.errors).length > 0)}
        >
          {isLoading ? (
            <span className="loading-spinner">Creating...</span>
          ) : currentStep === steps.length - 1 ? (
            'Create Team'
          ) : (
            'Next'
          )}
        </button>
      </div>
    </div>
  );
};

// Basic Information Step Component
const BasicInformationStep: React.FC<{
  data: CreateTeamRequest;
  validation: ValidationResult;
  onChange: (updates: Partial<CreateTeamRequest>) => void;
}> = ({ data, validation, onChange }) => {
  const [logoPreview, setLogoPreview] = useState<string | null>(null);
  
  const handleLogoUpload = useCallback((file: File) => {
    // Validate file
    if (file.size > 5 * 1024 * 1024) { // 5MB limit
      showErrorMessage('Logo file size must be less than 5MB');
      return;
    }
    
    if (!file.type.startsWith('image/')) {
      showErrorMessage('Logo must be an image file');
      return;
    }
    
    // Create preview
    const reader = new FileReader();
    reader.onload = (e) => {
      setLogoPreview(e.target?.result as string);
    };
    reader.readAsDataURL(file);
    
    // Update data
    onChange({ logo: file });
  }, [onChange]);
  
  return (
    <div className="basic-information-step">
      <div className="form-group">
        <label htmlFor="team-name">Team Name *</label>
        <input
          id="team-name"
          type="text"
          value={data.name}
          onChange={(e) => onChange({ name: e.target.value })}
          className={validation.errors?.name ? 'error' : ''}
          placeholder="Enter your team name"
          maxLength={100}
        />
        {validation.errors?.name && (
          <div className="error-message">{validation.errors.name}</div>
        )}
      </div>
      
      <div className="form-group">
        <label htmlFor="team-description">Team Description *</label>
        <textarea
          id="team-description"
          value={data.description}
          onChange={(e) => onChange({ description: e.target.value })}
          className={validation.errors?.description ? 'error' : ''}
          placeholder="Describe your team and its goals"
          rows={4}
          maxLength={500}
        />
        {validation.errors?.description && (
          <div className="error-message">{validation.errors.description}</div>
        )}
      </div>
      
      <div className="form-group">
        <label>Team Logo (Optional)</label>
        <div className="logo-upload">
          {logoPreview ? (
            <div className="logo-preview">
              <img src={logoPreview} alt="Team logo preview" />
              <button
                type="button"
                onClick={() => {
                  setLogoPreview(null);
                  onChange({ logo: null });
                }}
                className="remove-logo"
              >
                Remove
              </button>
            </div>
          ) : (
            <div
              className="logo-dropzone"
              onDrop={(e) => {
                e.preventDefault();
                const file = e.dataTransfer.files[0];
                if (file) handleLogoUpload(file);
              }}
              onDragOver={(e) => e.preventDefault()}
            >
              <input
                type="file"
                accept="image/*"
                onChange={(e) => {
                  const file = e.target.files?.[0];
                  if (file) handleLogoUpload(file);
                }}
                className="hidden-file-input"
                id="logo-upload"
              />
              <label htmlFor="logo-upload" className="upload-label">
                <div className="upload-icon">📁</div>
                <div>Click to upload or drag and drop</div>
                <div className="upload-hint">PNG, JPG up to 5MB</div>
              </label>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

// API Functions
async function checkTeamNameAvailability(name: string): Promise<boolean> {
  const response = await fetch(`/api/teams/check-availability`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name })
  });
  
  const result = await response.json();
  return result.available;
}

async function createTeam(teamData: CreateTeamRequest): Promise<Team> {
  const formData = new FormData();
  
  // Add basic data
  formData.append('name', teamData.name);
  formData.append('sport', teamData.sport);
  formData.append('description', teamData.description);
  formData.append('settings', JSON.stringify(teamData.settings));
  
  // Add logo if present
  if (teamData.logo) {
    formData.append('logo', teamData.logo);
  }
  
  const response = await fetch('/api/teams', {
    method: 'POST',
    body: formData
  });
  
  if (!response.ok) {
    throw new Error('Failed to create team');
  }
  
  return response.json();
}

// Invitation System Implementation
export class InvitationService {
  async sendInvitations(
    teamId: string,
    invitations: InvitationRequest[]
  ): Promise<InvitationResult[]> {
    const response = await fetch(`/api/teams/${teamId}/invitations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ invitations })
    });
    
    if (!response.ok) {
      throw new Error('Failed to send invitations');
    }
    
    return response.json();
  }
  
  async acceptInvitation(
    invitationId: string,
    acceptanceData: InvitationAcceptanceData
  ): Promise<AcceptanceResult> {
    const response = await fetch(`/api/invitations/${invitationId}/accept`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(acceptanceData)
    });
    
    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.message || 'Failed to accept invitation');
    }
    
    return response.json();
  }
  
  async declineInvitation(
    invitationId: string,
    reason?: string
  ): Promise<void> {
    await fetch(`/api/invitations/${invitationId}/decline`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reason })
    });
  }
  
  async getTeamInvitations(teamId: string): Promise<Invitation[]> {
    const response = await fetch(`/api/teams/${teamId}/invitations`);
    const result = await response.json();
    return result.invitations;
  }
  
  async resendInvitation(invitationId: string): Promise<void> {
    await fetch(`/api/invitations/${invitationId}/resend`, {
      method: 'PUT'
    });
  }
  
  async cancelInvitation(invitationId: string): Promise<void> {
    await fetch(`/api/invitations/${invitationId}`, {
      method: 'DELETE'
    });
  }
}
```

## Performance Optimization ⏳

### Team Management Performance
- [ ] **Data Loading Optimization**
  - Lazy loading for team member lists and invitation history
  - Pagination for large team member datasets
  - Efficient caching for team settings and subscription data
  - Background prefetching for frequently accessed team information
  - Optimized queries for team analytics and usage metrics

- [ ] **UI Performance**
  - Virtual scrolling for large member lists
  - Debounced search and filtering operations
  - Optimized re-rendering with React optimization techniques
  - Progressive loading for team creation wizard
  - Efficient bulk operations with progress indicators

### Invitation System Performance
- [ ] **Email Processing**
  - Asynchronous email sending with queue processing
  - Batch email operations for bulk invitations
  - Email template caching and optimization
  - Delivery status tracking with webhook integration
  - Failed email retry mechanisms with exponential backoff

## Security Implementation ⏳

### Team Creation Security
- [ ] **Input Validation**
  - Server-side validation for all team creation inputs
  - File upload security with virus scanning and type validation
  - Team name uniqueness validation with collision prevention
  - Logo image processing with security sanitization
  - Settings validation with business rule enforcement

- [ ] **Access Control**
  - Team creation rate limiting per user and IP address
  - Subscription tier validation for team creation limits
  - Owner role assignment validation and verification
  - Team deletion protection with multi-factor confirmation
  - Audit logging for all team management operations

### Invitation Security
- [ ] **Token Security**
  - Cryptographically secure invitation token generation
  - Token expiration with automatic cleanup
  - Single-use token validation to prevent replay attacks
  - IP address validation for invitation acceptance
  - Brute force protection for invitation token attempts

## Testing Strategy ⏳

### Team Management Testing
- [ ] **Functional Testing**
  - Team creation workflow with validation and error handling
  - Member invitation and acceptance flow testing
  - Role assignment and permission validation
  - Subscription integration and billing functionality
  - Team transfer and ownership change procedures

- [ ] **Integration Testing**
  - Email service integration with delivery confirmation
  - Billing system integration with subscription management
  - Authentication system integration with account linking
  - External directory service integration for member import
  - Analytics integration with usage tracking

### User Experience Testing
- [ ] **Usability Testing**
  - Team creation wizard flow and user experience
  - Invitation acceptance process and onboarding
  - Member management interface usability
  - Mobile and tablet team management experience
  - Accessibility compliance for all team management features

## Monitoring and Analytics ⏳

### Team Creation Analytics
- [ ] **Creation Metrics**
  - Team creation completion rates and abandonment points
  - Sport type distribution and popular configurations
  - Team size patterns and growth trajectories
  - Feature adoption rates for new teams
  - Geographic distribution of team creation

- [ ] **Invitation Analytics**
  - Invitation delivery rates and email engagement
  - Acceptance rates by role type and invitation method
  - Time-to-acceptance patterns and optimization opportunities
  - Invitation decline reasons and feedback analysis
  - Bulk invitation efficiency and error rates

### Usage Monitoring
- [ ] **Team Activity**
  - Team member engagement and activity levels
  - Feature usage patterns across different team sizes
  - Subscription tier utilization and upgrade patterns
  - Team retention rates and churn analysis
  - Support request patterns and common issues

## Definition of Done ✅
**This story is complete when:**
- ✅ Team creation wizard guides users through complete setup process
- ✅ Email-based invitation system sends professional branded invitations
- ✅ Invitation acceptance flow creates accounts and assigns roles correctly
- ✅ Team member management interface provides comprehensive member oversight
- ✅ Team settings integrate with subscription tiers and billing systems
- ✅ Member removal preserves content while revoking access appropriately
- ✅ Team ownership transfer system validates and processes ownership changes
- ✅ Subscription integration enforces user limits and feature access
- ✅ Cross-browser compatibility testing passes for all team management features
- ✅ Performance benchmarks meet targets for team operations (<2s response)
- ✅ Security testing passes with no unauthorized access vulnerabilities
- ✅ All tests pass with >95% coverage including edge cases and error scenarios

## Dependencies
- **Internal:** Story 4.1 (role-based access control), Story 1.2 (authentication)
- **External:** Email service integration for invitation delivery
- **External:** Billing system integration for subscription management
- **External:** File storage service for team logos and assets

## Risks & Mitigation
- **Risk:** Email delivery issues affecting invitation acceptance rates
- **Mitigation:** Multiple email service providers, delivery tracking, and alternative invitation methods
- **Risk:** Complex subscription integration causing billing and access issues
- **Mitigation:** Comprehensive testing, clear billing logic, and customer support integration
- **Risk:** Team creation abuse leading to resource consumption and spam
- **Mitigation:** Rate limiting, validation, and monitoring with automated abuse detection
- **Risk:** Ownership transfer errors causing team management disruption
- **Mitigation:** Multi-step validation, rollback capabilities, and comprehensive audit logging

## Change Log
| Date | Version | Description | Author |
| :--- | :--- | :--- | :--- |
| 2025-01-23 | 1.0 | Initial story creation with comprehensive team creation and invitation system | Sarah (Product Owner) |
| 2025-01-23 | 1.1 | Added detailed invitation workflow and subscription integration | Sarah (Product Owner) |
| 2025-01-23 | 1.2 | Enhanced with security measures and performance optimization | Sarah (Product Owner) |