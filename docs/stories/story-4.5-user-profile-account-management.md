# Story 4.5: User Profile and Account Management

## Status
🟡 **PENDING** - Comprehensive user profile and account management with security features and personal preferences

## Story
**As a** user,
**I want** comprehensive user profile and account management capabilities,
**so that** I can manage my personal settings and preferences within the team environment.

## Acceptance Criteria
1. User profile management (name, email, avatar, contact information) ⏳
2. Password management and security settings with two-factor authentication ⏳
3. Personal notification preferences and communication settings ⏳
4. Individual overlay and interface preferences that persist across sessions ⏳
5. Personal dashboard with recent sessions, assignments, and activity ⏳
6. Account linking for single sign-on integration with team authentication systems ⏳
7. Personal analytics and usage statistics for individual productivity tracking ⏳
8. Account deletion and data export capabilities for GDPR compliance ⏳

## Tasks / Subtasks

- [ ] **Task 4.5.1: User Profile Management Interface** ⏳
  - [ ] Create comprehensive profile editing interface with real-time validation
  - [ ] Implement avatar upload and management with image processing and cropping
  - [ ] Add profile information validation with email verification and contact validation
  - [ ] Create profile visibility settings with privacy controls and team sharing
  - [ ] Implement profile change history with audit logging and rollback capabilities
  - [ ] Add profile completion tracking with guided setup and progress indicators
  - [ ] Create profile import/export functionality with data portability
  - [ ] Implement profile synchronization with external identity providers
  - [ ] Add profile accessibility features with screen reader and keyboard support
  - [ ] Create profile analytics with usage tracking and optimization insights
  - [ ] Implement profile security with access control and change validation
  - [ ] Add profile documentation with setup guides and best practices
  - [ ] Create profile testing framework with validation and user experience testing
  - [ ] Implement profile integration with team directory and collaboration systems
  - [ ] Add profile compliance features with privacy and data protection
  - **Estimate:** 20 hours | **Priority:** Critical | **Dependencies:** Story 4.1 (RBAC)
  - **Deliverables:**
    - Complete profile management interface with validation
    - Avatar upload with processing and cropping tools
    - Privacy controls and visibility settings
    - Change history with audit logging
    - Integration with external identity providers

- [ ] **Task 4.5.2: Password Management & Security Settings** ⏳
  - [ ] Create password change interface with strength validation and security requirements
  - [ ] Implement two-factor authentication with TOTP, SMS, and backup codes
  - [ ] Add security question setup with recovery options and validation
  - [ ] Create login history tracking with device recognition and anomaly detection
  - [ ] Implement account security dashboard with threat monitoring and alerts
  - [ ] Add password reset functionality with secure verification and time limits
  - [ ] Create security notification system with login alerts and suspicious activity
  - [ ] Implement security audit logging with detailed access tracking
  - [ ] Add device management with trusted device registration and revocation
  - [ ] Create security settings export for compliance and documentation
  - [ ] Implement security testing tools with vulnerability scanning and validation
  - [ ] Add security accessibility features with clear instructions and guidance
  - [ ] Create security documentation with best practices and user guides
  - [ ] Implement security integration with enterprise authentication systems
  - [ ] Add security compliance features with regulatory requirements and auditing
  - **Estimate:** 22 hours | **Priority:** Critical | **Dependencies:** Task 4.5.1
  - **Deliverables:**
    - Comprehensive password management with strength validation
    - Two-factor authentication with multiple method support
    - Security dashboard with threat monitoring and alerts
    - Device management with trusted device controls
    - Complete audit logging and compliance features

- [ ] **Task 4.5.3: Personal Notification Preferences** ⏳
  - [ ] Create notification preference interface with granular control options
  - [ ] Implement notification channel management with email, in-app, and push options
  - [ ] Add notification scheduling with do-not-disturb and business hours settings
  - [ ] Create notification category customization with priority levels and filtering
  - [ ] Implement notification testing tools with preview and delivery validation
  - [ ] Add notification history tracking with read status and engagement metrics
  - [ ] Create notification templates with personalization and branding options
  - [ ] Implement notification analytics with delivery tracking and effectiveness
  - [ ] Add notification integration with external communication platforms
  - [ ] Create notification accessibility features with screen reader and visual alerts
  - [ ] Implement notification security with privacy controls and opt-out management
  - [ ] Add notification documentation with setup guides and troubleshooting
  - [ ] Create notification testing framework with delivery and engagement validation
  - [ ] Implement notification compliance with privacy regulations and consent management
  - [ ] Add notification optimization with machine learning and user behavior analysis
  - **Estimate:** 16 hours | **Priority:** High | **Dependencies:** Task 4.5.2
  - **Deliverables:**
    - Granular notification preference management
    - Multi-channel notification with scheduling controls
    - Testing tools with delivery validation
    - Analytics and optimization with engagement tracking
    - Compliance features with privacy and consent management

- [ ] **Task 4.5.4: Individual Interface Preferences & Customization** ⏳
  - [ ] Create interface customization panel with theme and layout options
  - [ ] Implement video player preference settings with quality and control customization
  - [ ] Add overlay and analysis preference management with personal defaults
  - [ ] Create keyboard shortcut customization with conflict detection and validation
  - [ ] Implement accessibility preference settings with screen reader and contrast options
  - [ ] Add language and localization preferences with automatic detection
  - [ ] Create workspace layout customization with panel arrangement and sizing
  - [ ] Implement preference synchronization across devices and sessions
  - [ ] Add preference backup and restore functionality with cloud synchronization
  - [ ] Create preference analytics with usage pattern tracking and optimization
  - [ ] Implement preference security with access control and change validation
  - [ ] Add preference accessibility features with guided setup and clear descriptions
  - [ ] Create preference documentation with customization guides and examples
  - [ ] Implement preference testing framework with user experience validation
  - [ ] Add preference integration with team settings and organizational policies
  - **Estimate:** 18 hours | **Priority:** High | **Dependencies:** Task 4.5.3
  - **Deliverables:**
    - Complete interface customization with themes and layouts
    - Video player and overlay preference management
    - Keyboard shortcut customization with validation
    - Accessibility settings with comprehensive options
    - Cross-device synchronization with backup and restore

- [ ] **Task 4.5.5: Personal Dashboard & Activity Overview** ⏳
  - [ ] Create personalized dashboard with customizable widget layout
  - [ ] Implement recent activity feed with session, assignment, and collaboration tracking
  - [ ] Add task and assignment dashboard with deadline tracking and progress monitoring
  - [ ] Create personal analytics overview with productivity metrics and insights
  - [ ] Implement quick access tools with frequently used features and shortcuts
  - [ ] Add notification center with action items and priority alerts
  - [ ] Create dashboard customization with widget selection and arrangement
  - [ ] Implement dashboard analytics with usage tracking and optimization recommendations
  - [ ] Add dashboard export capabilities with activity reports and summaries
  - [ ] Create dashboard accessibility features with screen reader and keyboard navigation
  - [ ] Implement dashboard security with privacy controls and data filtering
  - [ ] Add dashboard documentation with setup guides and customization tips
  - [ ] Create dashboard testing framework with usability and performance validation
  - [ ] Implement dashboard integration with team systems and external tools
  - [ ] Add dashboard compliance features with data retention and privacy controls
  - **Estimate:** 20 hours | **Priority:** Medium | **Dependencies:** Task 4.5.4
  - **Deliverables:**
    - Personalized dashboard with customizable widgets
    - Activity feed with comprehensive tracking
    - Task and assignment management with progress monitoring
    - Personal analytics with productivity insights
    - Quick access tools and notification center

- [ ] **Task 4.5.6: Single Sign-On & Account Linking** ⏳
  - [ ] Create SSO integration interface with multiple identity provider support
  - [ ] Implement OAuth 2.0 and SAML integration with enterprise authentication systems
  - [ ] Add account linking functionality with existing account validation and merging
  - [ ] Create identity provider management with connection testing and validation
  - [ ] Implement SSO security with token validation and session management
  - [ ] Add SSO audit logging with detailed authentication tracking
  - [ ] Create SSO troubleshooting tools with connection diagnostics and error resolution
  - [ ] Implement SSO analytics with usage tracking and performance monitoring
  - [ ] Add SSO documentation with setup guides and configuration examples
  - [ ] Create SSO testing framework with authentication flow validation
  - [ ] Implement SSO accessibility features with clear instructions and error messages
  - [ ] Add SSO compliance features with regulatory requirements and security standards
  - [ ] Create SSO integration with team provisioning and role assignment
  - [ ] Implement SSO optimization with performance tuning and caching
  - [ ] Add SSO support with technical assistance and troubleshooting guides
  - **Estimate:** 24 hours | **Priority:** Medium | **Dependencies:** Task 4.5.5
  - **Deliverables:**
    - Multi-provider SSO integration with OAuth and SAML support
    - Account linking with validation and merging capabilities
    - Security features with token management and audit logging
    - Troubleshooting tools with diagnostics and error resolution
    - Complete documentation and testing framework

- [ ] **Task 4.5.7: Personal Analytics & Usage Statistics** ⏳
  - [ ] Create personal analytics dashboard with productivity metrics and trends
  - [ ] Implement usage tracking with session analysis and feature adoption
  - [ ] Add productivity insights with time management and efficiency recommendations
  - [ ] Create comparison analytics with team benchmarks and performance indicators
  - [ ] Implement goal setting and tracking with progress monitoring and achievements
  - [ ] Add activity pattern analysis with workflow optimization suggestions
  - [ ] Create analytics export capabilities with detailed reports and visualizations
  - [ ] Implement analytics privacy controls with data sharing and visibility settings
  - [ ] Add analytics accessibility features with clear visualizations and descriptions
  - [ ] Create analytics documentation with interpretation guides and best practices
  - [ ] Implement analytics security with data protection and access control
  - [ ] Add analytics testing framework with data accuracy and performance validation
  - [ ] Create analytics integration with team systems and external tools
  - [ ] Implement analytics optimization with machine learning and predictive insights
  - [ ] Add analytics compliance features with data retention and privacy regulations
  - **Estimate:** 18 hours | **Priority:** Medium | **Dependencies:** Task 4.5.6
  - **Deliverables:**
    - Personal analytics dashboard with productivity metrics
    - Usage tracking with comprehensive session analysis
    - Goal setting and achievement tracking system
    - Privacy controls with data sharing settings
    - Export capabilities with detailed reporting

- [ ] **Task 4.5.8: Account Deletion & Data Export (GDPR Compliance)** ⏳
  - [ ] Create account deletion workflow with data impact assessment and confirmation
  - [ ] Implement data export functionality with comprehensive data portability
  - [ ] Add data retention management with deletion scheduling and grace periods
  - [ ] Create data anonymization tools with personal information removal
  - [ ] Implement GDPR compliance features with right to be forgotten and data portability
  - [ ] Add data deletion audit logging with detailed tracking and verification
  - [ ] Create data recovery options with backup restoration and account reactivation
  - [ ] Implement data export validation with completeness checking and format verification
  - [ ] Add data deletion security with multi-factor confirmation and identity verification
  - [ ] Create data compliance documentation with legal requirements and procedures
  - [ ] Implement data deletion testing with validation and recovery testing
  - [ ] Add data accessibility features with clear instructions and progress tracking
  - [ ] Create data integration with team systems for content ownership transfer
  - [ ] Implement data optimization with efficient processing and storage cleanup
  - [ ] Add data support with assistance and troubleshooting for complex cases
  - **Estimate:** 22 hours | **Priority:** High | **Dependencies:** Task 4.5.7
  - **Deliverables:**
    - Complete account deletion workflow with impact assessment
    - Comprehensive data export with GDPR compliance
    - Data retention and anonymization tools
    - Audit logging with detailed tracking
    - Recovery options with backup and reactivation

## API Implementation ⏳

### User Profile & Account Management Endpoints (26 endpoints)
- [ ] **GET /users/{user_id}/profile** - Get user profile information
  - Response: profile_data, privacy_settings, completion_status, team_memberships
  - Features: Complete profile data, privacy controls, team associations

- [ ] **PUT /users/{user_id}/profile** - Update user profile
  - Request: profile_updates, privacy_changes, notification_preferences
  - Response: update_status, validation_results, change_log
  - Features: Profile management, validation, change tracking

- [ ] **POST /users/{user_id}/avatar** - Upload user avatar
  - Request: avatar_file, crop_settings, quality_options
  - Response: upload_status, avatar_url, processing_info
  - Features: Image upload, processing, quality optimization

- [ ] **DELETE /users/{user_id}/avatar** - Remove user avatar
  - Response: deletion_status, cleanup_actions
  - Features: Avatar removal, cleanup

- [ ] **GET /users/{user_id}/security** - Get security settings
  - Response: security_config, login_history, device_list, threat_alerts
  - Features: Security overview, device management, threat monitoring

- [ ] **PUT /users/{user_id}/password** - Change user password
  - Request: current_password, new_password, security_confirmation
  - Response: change_status, security_validation, notification_sent
  - Features: Password management, validation, security notifications

- [ ] **POST /users/{user_id}/2fa/setup** - Set up two-factor authentication
  - Request: method_type, phone_number, backup_options
  - Response: setup_status, qr_code, backup_codes
  - Features: 2FA setup, multiple methods, backup codes

- [ ] **POST /users/{user_id}/2fa/verify** - Verify two-factor authentication
  - Request: verification_code, method_type, device_trust
  - Response: verification_status, device_registration, session_info
  - Features: 2FA verification, device trust, session management

- [ ] **DELETE /users/{user_id}/2fa** - Disable two-factor authentication
  - Request: confirmation_code, security_verification
  - Response: disable_status, security_notification
  - Features: 2FA removal, security confirmation

- [ ] **GET /users/{user_id}/devices** - Get trusted devices
  - Response: device_list, trust_status, last_activity, location_info
  - Features: Device management, activity tracking, location data

- [ ] **DELETE /users/{user_id}/devices/{device_id}** - Remove trusted device
  - Response: removal_status, security_notification
  - Features: Device removal, security alerts

- [ ] **GET /users/{user_id}/notifications** - Get notification preferences
  - Response: notification_config, channel_settings, history_summary
  - Features: Preference management, channel configuration, history

- [ ] **PUT /users/{user_id}/notifications** - Update notification preferences
  - Request: preference_updates, channel_changes, schedule_settings
  - Response: update_status, validation_results, test_options
  - Features: Preference updates, validation, testing

- [ ] **POST /users/{user_id}/notifications/test** - Test notification delivery
  - Request: notification_type, delivery_method, test_content
  - Response: test_results, delivery_status, performance_metrics
  - Features: Delivery testing, performance monitoring

- [ ] **GET /users/{user_id}/preferences** - Get interface preferences
  - Response: ui_preferences, theme_settings, accessibility_options, shortcuts
  - Features: Interface customization, themes, accessibility, shortcuts

- [ ] **PUT /users/{user_id}/preferences** - Update interface preferences
  - Request: preference_updates, theme_changes, accessibility_settings
  - Response: update_status, sync_status, validation_results
  - Features: Preference management, synchronization, validation

- [ ] **GET /users/{user_id}/dashboard** - Get personal dashboard data
  - Response: dashboard_config, recent_activity, assignments, analytics_summary
  - Features: Dashboard configuration, activity feed, task overview

- [ ] **PUT /users/{user_id}/dashboard** - Update dashboard configuration
  - Request: widget_config, layout_changes, visibility_settings
  - Response: update_status, layout_validation, sync_info
  - Features: Dashboard customization, layout management, synchronization

- [ ] **GET /users/{user_id}/activity** - Get user activity history
  - Request: time_range, activity_filter, pagination
  - Response: activity_entries, summary_stats, trend_analysis
  - Features: Activity tracking, filtering, analytics

- [ ] **POST /users/{user_id}/sso/link** - Link SSO account
  - Request: provider_type, identity_token, account_mapping
  - Response: linking_status, account_validation, security_verification
  - Features: SSO linking, validation, security checks

- [ ] **GET /users/{user_id}/sso/providers** - Get linked SSO providers
  - Response: provider_list, connection_status, last_used
  - Features: Provider management, status monitoring

- [ ] **DELETE /users/{user_id}/sso/{provider_id}** - Unlink SSO provider
  - Response: unlink_status, security_notification, backup_access
  - Features: Provider removal, security alerts, access preservation

- [ ] **GET /users/{user_id}/analytics** - Get personal analytics
  - Response: usage_metrics, productivity_insights, goal_progress, comparisons
  - Features: Personal analytics, productivity tracking, goal monitoring

- [ ] **POST /users/{user_id}/export** - Export user data
  - Request: export_scope, format_options, delivery_method
  - Response: export_job_id, processing_status, estimated_completion
  - Features: Data export, GDPR compliance, format selection

- [ ] **GET /users/{user_id}/export/{export_id}** - Get export status
  - Response: export_status, progress_percentage, download_url, file_info
  - Features: Export tracking, download management

- [ ] **DELETE /users/{user_id}/account** - Delete user account
  - Request: deletion_confirmation, data_handling, transfer_options
  - Response: deletion_job_id, grace_period, recovery_options
  - Features: Account deletion, data handling, recovery period

## Frontend Component Architecture ⏳

### User Profile Components
```typescript
// Core user profile interfaces
interface UserProfileProps {
  userId: string;
  currentUser: User;
  onProfileUpdate?: (updates: ProfileUpdate) => void;
  onSecurityUpdate?: (security: SecurityUpdate) => void;
}

// Main profile management components
export const UserProfileManager: React.FC<UserProfileProps>
export const ProfileEditForm: React.FC<ProfileEditProps>
export const SecuritySettings: React.FC<SecuritySettingsProps>
export const NotificationPreferences: React.FC<NotificationPreferencesProps>
export const InterfaceCustomization: React.FC<InterfaceCustomizationProps>

// Security components
export const PasswordManager: React.FC<PasswordManagerProps>
export const TwoFactorAuthSetup: React.FC<TwoFactorAuthProps>
export const DeviceManager: React.FC<DeviceManagerProps>
export const SecurityDashboard: React.FC<SecurityDashboardProps>

// Dashboard components
export const PersonalDashboard: React.FC<PersonalDashboardProps>
export const ActivityFeed: React.FC<ActivityFeedProps>
export const TaskOverview: React.FC<TaskOverviewProps>
export const AnalyticsSummary: React.FC<AnalyticsSummaryProps>

// Account management components
export const SSOManager: React.FC<SSOManagerProps>
export const DataExporter: React.FC<DataExporterProps>
export const AccountDeletion: React.FC<AccountDeletionProps>
export const PrivacyControls: React.FC<PrivacyControlsProps>

// Utility components
export const AvatarUploader: React.FC<AvatarUploaderProps>
export const PreferenceSync: React.FC<PreferenceSyncProps>
export const ComplianceTools: React.FC<ComplianceToolsProps>
```

### User Profile State Management
```typescript
interface UserProfileState {
  // Profile data
  userProfile: UserProfile;
  securitySettings: SecuritySettings;
  notificationPreferences: NotificationPreferences;
  interfacePreferences: InterfacePreferences;
  
  // Security state
  twoFactorEnabled: boolean;
  trustedDevices: TrustedDevice[];
  loginHistory: LoginHistoryEntry[];
  securityAlerts: SecurityAlert[];
  
  // Dashboard state
  dashboardConfig: DashboardConfig;
  recentActivity: ActivityEntry[];
  assignments: Assignment[];
  personalAnalytics: PersonalAnalytics;
  
  // SSO and linking
  linkedProviders: SSOProvider[];
  accountLinking: AccountLinking[];
  
  // Data management
  dataExports: DataExport[];
  privacySettings: PrivacySettings;
  complianceStatus: ComplianceStatus;
  
  // UI state
  activeProfileTab: string;
  profileValidation: ValidationResult;
  savingState: SavingState;
  
  // Actions
  updateProfile: (updates: ProfileUpdate) => Promise<void>;
  changePassword: (passwordData: PasswordChangeRequest) => Promise<void>;
  setupTwoFactor: (method: TwoFactorMethod) => Promise<void>;
  updateNotifications: (preferences: NotificationPreferences) => Promise<void>;
  
  // Security actions
  addTrustedDevice: (device: DeviceInfo) => Promise<void>;
  removeTrustedDevice: (deviceId: string) => Promise<void>;
  reviewSecurityAlert: (alertId: string) => Promise<void>;
  
  // Dashboard actions
  updateDashboard: (config: DashboardConfig) => Promise<void>;
  customizeInterface: (preferences: InterfacePreferences) => Promise<void>;
  
  // Account management actions
  linkSSOProvider: (provider: SSOProviderInfo) => Promise<void>;
  exportData: (options: DataExportOptions) => Promise<void>;
  deleteAccount: (confirmation: AccountDeletionRequest) => Promise<void>;
}
```

## User Profile Implementation ⏳

### Comprehensive Profile Management System
```typescript
// User Profile Manager Component
import React, { useState, useCallback, useEffect } from 'react';
import { UserProfileState, ProfileUpdate, SecurityUpdate } from './types';

export const UserProfileManager: React.FC<UserProfileProps> = ({
  userId,
  currentUser,
  onProfileUpdate,
  onSecurityUpdate
}) => {
  const [profileState, setProfileState] = useState<UserProfileState>({
    activeProfileTab: 'profile',
    userProfile: null,
    securitySettings: null,
    notificationPreferences: null,
    interfacePreferences: null,
    profileValidation: { isValid: true, errors: [] },
    savingState: { isSaving: false, lastSaved: null }
  });

  const [unsavedChanges, setUnsavedChanges] = useState<Record<string, any>>({});

  // Load user profile data
  useEffect(() => {
    const loadProfileData = async () => {
      try {
        const profileData = await fetchUserProfile(userId);
        setProfileState(prev => ({
          ...prev,
          userProfile: profileData.profile,
          securitySettings: profileData.security,
          notificationPreferences: profileData.notifications,
          interfacePreferences: profileData.preferences,
          dashboardConfig: profileData.dashboard,
          personalAnalytics: profileData.analytics
        }));
      } catch (error) {
        console.error('Failed to load profile data:', error);
        showErrorMessage('Failed to load profile information');
      }
    };

    loadProfileData();
  }, [userId]);

  // Handle profile updates with validation
  const handleProfileUpdate = useCallback(async (
    section: string,
    updates: any
  ): Promise<void> => {
    try {
      // Store unsaved changes
      setUnsavedChanges(prev => ({
        ...prev,
        [section]: { ...prev[section], ...updates }
      }));

      // Validate changes
      const validation = await validateProfileUpdate(section, updates);
      
      if (!validation.isValid) {
        setProfileState(prev => ({
          ...prev,
          profileValidation: validation
        }));
        return;
      }

      // Apply to local state immediately for UI responsiveness
      setProfileState(prev => ({
        ...prev,
        [section]: { ...prev[section], ...updates },
        profileValidation: { isValid: true, errors: [] }
      }));

    } catch (error) {
      console.error('Profile update failed:', error);
      showErrorMessage('Failed to update profile');
    }
  }, []);

  // Save all pending changes
  const saveAllChanges = useCallback(async (): Promise<void> => {
    if (Object.keys(unsavedChanges).length === 0) return;

    setProfileState(prev => ({
      ...prev,
      savingState: { isSaving: true, lastSaved: prev.savingState.lastSaved }
    }));

    try {
      const saveResult = await saveProfileChanges(userId, unsavedChanges);
      
      if (saveResult.success) {
        setUnsavedChanges({});
        setProfileState(prev => ({
          ...prev,
          savingState: { isSaving: false, lastSaved: new Date() }
        }));
        
        showSuccessMessage('Profile saved successfully');
        onProfileUpdate?.(saveResult.appliedChanges);
      } else {
        setProfileState(prev => ({
          ...prev,
          profileValidation: {
            isValid: false,
            errors: saveResult.errors
          },
          savingState: { isSaving: false, lastSaved: prev.savingState.lastSaved }
        }));
      }
      
    } catch (error) {
      console.error('Failed to save profile changes:', error);
      showErrorMessage('Failed to save changes');
      setProfileState(prev => ({
        ...prev,
        savingState: { isSaving: false, lastSaved: prev.savingState.lastSaved }
      }));
    }
  }, [userId, unsavedChanges, onProfileUpdate]);

  // Profile tabs configuration
  const profileTabs = [
    { id: 'profile', label: 'Profile', icon: '👤' },
    { id: 'security', label: 'Security', icon: '🔒' },
    { id: 'notifications', label: 'Notifications', icon: '🔔' },
    { id: 'preferences', label: 'Preferences', icon: '⚙️' },
    { id: 'dashboard', label: 'Dashboard', icon: '📊' },
    { id: 'analytics', label: 'Analytics', icon: '📈' },
    { id: 'privacy', label: 'Privacy & Data', icon: '🛡️' }
  ];

  // Render active tab content
  const renderTabContent = () => {
    switch (profileState.activeProfileTab) {
      case 'profile':
        return (
          <ProfileEditForm
            profile={profileState.userProfile}
            validation={profileState.profileValidation}
            onUpdate={(updates) => handleProfileUpdate('userProfile', updates)}
            onAvatarUpload={(file) => handleAvatarUpload(file)}
          />
        );
        
      case 'security':
        return (
          <SecuritySettings
            settings={profileState.securitySettings}
            twoFactorEnabled={profileState.twoFactorEnabled}
            trustedDevices={profileState.trustedDevices}
            onUpdate={(updates) => handleProfileUpdate('securitySettings', updates)}
            onPasswordChange={(data) => handlePasswordChange(data)}
            onTwoFactorSetup={(method) => handleTwoFactorSetup(method)}
          />
        );
        
      case 'notifications':
        return (
          <NotificationPreferences
            preferences={profileState.notificationPreferences}
            onUpdate={(updates) => handleProfileUpdate('notificationPreferences', updates)}
            onTest={(type, method) => testNotificationDelivery(type, method)}
          />
        );
        
      case 'preferences':
        return (
          <InterfaceCustomization
            preferences={profileState.interfacePreferences}
            onUpdate={(updates) => handleProfileUpdate('interfacePreferences', updates)}
            onThemeChange={(theme) => handleThemeChange(theme)}
            onShortcutChange={(shortcuts) => handleShortcutChange(shortcuts)}
          />
        );
        
      case 'dashboard':
        return (
          <PersonalDashboard
            config={profileState.dashboardConfig}
            recentActivity={profileState.recentActivity}
            assignments={profileState.assignments}
            onConfigUpdate={(config) => handleProfileUpdate('dashboardConfig', config)}
          />
        );
        
      case 'analytics':
        return (
          <AnalyticsSummary
            analytics={profileState.personalAnalytics}
            onExport={(options) => exportAnalyticsData(options)}
            onGoalSet={(goal) => setProductivityGoal(goal)}
          />
        );
        
      case 'privacy':
        return (
          <PrivacyControls
            privacySettings={profileState.privacySettings}
            linkedProviders={profileState.linkedProviders}
            dataExports={profileState.dataExports}
            onExportData={(options) => exportUserData(options)}
            onDeleteAccount={(confirmation) => deleteUserAccount(confirmation)}
            onLinkProvider={(provider) => linkSSOProvider(provider)}
          />
        );
        
      default:
        return <div>Profile section not found</div>;
    }
  };

  const hasUnsavedChanges = Object.keys(unsavedChanges).length > 0;

  return (
    <div className="user-profile-manager">
      {/* Profile header with save controls */}
      <div className="profile-header">
        <div className="profile-title">
          <h2>My Profile</h2>
          {profileState.savingState.lastSaved && (
            <span className="last-saved">
              Last saved: {formatTimestamp(profileState.savingState.lastSaved)}
            </span>
          )}
        </div>
        
        {hasUnsavedChanges && (
          <div className="save-controls">
            <span className="unsaved-indicator">
              Unsaved changes
            </span>
            <button
              onClick={() => setUnsavedChanges({})}
              className="btn btn-secondary"
              disabled={profileState.savingState.isSaving}
            >
              Discard
            </button>
            <button
              onClick={saveAllChanges}
              className="btn btn-primary"
              disabled={profileState.savingState.isSaving}
            >
              {profileState.savingState.isSaving ? 'Saving...' : 'Save Changes'}
            </button>
          </div>
        )}
      </div>

      {/* Validation errors */}
      {!profileState.profileValidation.isValid && (
        <div className="validation-errors">
          <h4>Please fix the following errors:</h4>
          <ul>
            {profileState.profileValidation.errors.map((error, index) => (
              <li key={index}>
                {error.field}: {error.message}
              </li>
            ))}
          </ul>
        </div>
      )}

      <div className="profile-content">
        {/* Profile navigation tabs */}
        <div className="profile-navigation">
          {profileTabs.map(tab => (
            <button
              key={tab.id}
              onClick={() => setProfileState(prev => ({
                ...prev,
                activeProfileTab: tab.id
              }))}
              className={`nav-tab ${
                profileState.activeProfileTab === tab.id ? 'active' : ''
              }`}
            >
              <span className="tab-icon">{tab.icon}</span>
              <span className="tab-label">{tab.label}</span>
              {unsavedChanges[tab.id] && (
                <span className="unsaved-dot">•</span>
              )}
            </button>
          ))}
        </div>

        {/* Active tab content */}
        <div className="profile-panel">
          {renderTabContent()}
        </div>
      </div>
    </div>
  );
};

// Profile Edit Form Component
export const ProfileEditForm: React.FC<{
  profile: UserProfile | null;
  validation: ValidationResult;
  onUpdate: (updates: Partial<UserProfile>) => void;
  onAvatarUpload: (file: File) => Promise<void>;
}> = ({ profile, validation, onUpdate, onAvatarUpload }) => {
  const [avatarPreview, setAvatarPreview] = useState<string | null>(
    profile?.avatarUrl || null
  );
  const [isUploadingAvatar, setIsUploadingAvatar] = useState(false);

  const handleAvatarUpload = useCallback(async (file: File) => {
    if (file.size > 5 * 1024 * 1024) {
      showErrorMessage('Avatar file size must be less than 5MB');
      return;
    }

    if (!file.type.startsWith('image/')) {
      showErrorMessage('Avatar must be an image file');
      return;
    }

    setIsUploadingAvatar(true);
    
    try {
      // Create preview
      const reader = new FileReader();
      reader.onload = (e) => {
        setAvatarPreview(e.target?.result as string);
      };
      reader.readAsDataURL(file);

      // Upload avatar
      await onAvatarUpload(file);
      showSuccessMessage('Avatar updated successfully');
      
    } catch (error) {
      console.error('Avatar upload failed:', error);
      showErrorMessage('Failed to upload avatar');
      setAvatarPreview(profile?.avatarUrl || null);
    } finally {
      setIsUploadingAvatar(false);
    }
  }, [profile?.avatarUrl, onAvatarUpload]);

  return (
    <div className="profile-edit-form">
      <div className="form-section">
        <h3>Basic Information</h3>
        
        <div className="avatar-section">
          <div className="avatar-display">
            {avatarPreview ? (
              <img src={avatarPreview} alt="User avatar" className="current-avatar" />
            ) : (
              <div className="default-avatar">
                {profile?.name?.charAt(0)?.toUpperCase() || '?'}
              </div>
            )}
            
            {isUploadingAvatar && (
              <div className="upload-overlay">
                <div className="upload-spinner">Uploading...</div>
              </div>
            )}
          </div>
          
          <div className="avatar-controls">
            <input
              type="file"
              accept="image/*"
              onChange={(e) => {
                const file = e.target.files?.[0];
                if (file) handleAvatarUpload(file);
              }}
              className="hidden-file-input"
              id="avatar-upload"
              disabled={isUploadingAvatar}
            />
            <label
              htmlFor="avatar-upload"
              className="btn btn-secondary"
            >
              Change Avatar
            </label>
            
            {profile?.avatarUrl && (
              <button
                onClick={() => {
                  setAvatarPreview(null);
                  onUpdate({ avatarUrl: null });
                }}
                className="btn btn-outline"
                disabled={isUploadingAvatar}
              >
                Remove
              </button>
            )}
          </div>
        </div>
        
        <div className="form-group">
          <label htmlFor="full-name">Full Name</label>
          <input
            id="full-name"
            type="text"
            value={profile?.name || ''}
            onChange={(e) => onUpdate({ name: e.target.value })}
            className={validation.errors?.some(e => e.field === 'name') ? 'error' : ''}
            placeholder="Enter your full name"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="email">Email Address</label>
          <input
            id="email"
            type="email"
            value={profile?.email || ''}
            onChange={(e) => onUpdate({ email: e.target.value })}
            className={validation.errors?.some(e => e.field === 'email') ? 'error' : ''}
            placeholder="Enter your email address"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="job-title">Job Title</label>
          <input
            id="job-title"
            type="text"
            value={profile?.jobTitle || ''}
            onChange={(e) => onUpdate({ jobTitle: e.target.value })}
            placeholder="e.g., Head Coach, Video Analyst"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="bio">Bio</label>
          <textarea
            id="bio"
            value={profile?.bio || ''}
            onChange={(e) => onUpdate({ bio: e.target.value })}
            placeholder="Tell us about yourself and your coaching experience"
            rows={3}
            maxLength={500}
          />
          <div className="character-count">
            {(profile?.bio || '').length}/500
          </div>
        </div>
      </div>

      <div className="form-section">
        <h3>Contact Information</h3>
        
        <div className="form-group">
          <label htmlFor="phone">Phone Number</label>
          <input
            id="phone"
            type="tel"
            value={profile?.phone || ''}
            onChange={(e) => onUpdate({ phone: e.target.value })}
            placeholder="+1 (555) 123-4567"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="location">Location</label>
          <input
            id="location"
            type="text"
            value={profile?.location || ''}
            onChange={(e) => onUpdate({ location: e.target.value })}
            placeholder="City, State/Country"
          />
        </div>
        
        <div className="form-group">
          <label htmlFor="website">Website</label>
          <input
            id="website"
            type="url"
            value={profile?.website || ''}
            onChange={(e) => onUpdate({ website: e.target.value })}
            placeholder="https://your-website.com"
          />
        </div>
      </div>

      <div className="form-section">
        <h3>Privacy Settings</h3>
        
        <div className="form-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={profile?.profileVisibility === 'public'}
              onChange={(e) => onUpdate({
                profileVisibility: e.target.checked ? 'public' : 'team-only'
              })}
            />
            Make my profile visible to other teams
          </label>
        </div>
        
        <div className="form-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={profile?.showActivity || false}
              onChange={(e) => onUpdate({ showActivity: e.target.checked })}
            />
            Show my recent activity to team members
          </label>
        </div>
        
        <div className="form-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={profile?.allowMessages || false}
              onChange={(e) => onUpdate({ allowMessages: e.target.checked })}
            />
            Allow direct messages from team members
          </label>
        </div>
      </div>
    </div>
  );
};

// API Functions
async function fetchUserProfile(userId: string): Promise<any> {
  const response = await fetch(`/api/users/${userId}/profile`);
  if (!response.ok) {
    throw new Error('Failed to fetch user profile');
  }
  return response.json();
}

async function saveProfileChanges(
  userId: string,
  changes: Record<string, any>
): Promise<any> {
  const response = await fetch(`/api/users/${userId}/profile`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ changes })
  });
  
  if (!response.ok) {
    throw new Error('Failed to save profile changes');
  }
  
  return response.json();
}

async function validateProfileUpdate(
  section: string,
  updates: any
): Promise<ValidationResult> {
  const response = await fetch('/api/users/profile/validate', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ section, updates })
  });
  
  return response.json();
}

async function uploadUserAvatar(file: File): Promise<{ avatarUrl: string }> {
  const formData = new FormData();
  formData.append('avatar', file);
  
  const response = await fetch('/api/users/avatar', {
    method: 'POST',
    body: formData
  });
  
  if (!response.ok) {
    throw new Error('Failed to upload avatar');
  }
  
  return response.json();
}
```

## Performance Optimization ⏳

### Profile Management Performance
- [ ] **Data Loading Optimization**
  - Lazy loading for profile sections with on-demand data fetching
  - Efficient caching for frequently accessed profile data
  - Background prefetching for related user information
  - Progressive loading for complex preference interfaces
  - Optimized queries for user analytics and activity data

- [ ] **UI Performance**
  - Virtual scrolling for large activity feeds and history lists
  - Debounced validation for real-time profile updates
  - Optimized re-rendering with React optimization techniques
  - Efficient image processing for avatar uploads
  - Smooth animations with performance optimization

### Security Performance
- [ ] **Authentication Optimization**
  - Efficient 2FA token validation with caching
  - Optimized device fingerprinting and recognition
  - Fast security audit log queries with indexing
  - Efficient password hashing and validation
  - Streamlined SSO token processing and validation

## Security Implementation ⏳

### Profile Security
- [ ] **Data Protection**
  - End-to-end encryption for sensitive profile information
  - Secure avatar storage with access control and validation
  - Input validation and sanitization for all profile fields
  - Protection against profile manipulation and impersonation
  - Audit logging for all profile changes and access

- [ ] **Authentication Security**
  - Multi-factor authentication with backup options
  - Secure password policies with strength validation
  - Device trust management with anomaly detection
  - Session security with timeout and concurrent session control
  - SSO security with token validation and secure storage

### Privacy Protection
- [ ] **Data Privacy**
  - GDPR compliance with data portability and deletion rights
  - Privacy controls with granular visibility settings
  - Data anonymization for analytics and reporting
  - Consent management for data processing and sharing
  - Regular privacy audits and compliance validation

## Testing Strategy ⏳

### Profile Functionality Testing
- [ ] **Profile Management Testing**
  - Profile update validation and business rule enforcement
  - Avatar upload and processing functionality validation
  - Notification preference testing with delivery confirmation
  - Interface customization persistence and synchronization
  - Dashboard configuration and widget functionality

- [ ] **Security Testing**
  - Two-factor authentication setup and validation flow
  - Password change security and strength validation
  - Device trust management and anomaly detection
  - SSO integration and token security validation
  - Account deletion and data export compliance

### User Experience Testing
- [ ] **Profile UX Testing**
  - Profile setup and completion flow usability
  - Settings navigation and organization effectiveness
  - Mobile and tablet profile management experience
  - Accessibility compliance for all profile interfaces
  - Cross-browser compatibility for profile features

## Monitoring and Analytics ⏳

### Profile Usage Analytics
- [ ] **User Engagement Metrics**
  - Profile completion rates and abandonment points
  - Feature usage patterns and preference adoption
  - Security feature adoption and effectiveness
  - Dashboard customization patterns and engagement
  - Cross-platform usage distribution and optimization

- [ ] **Security Monitoring**
  - Authentication failure rates and security incidents
  - Two-factor authentication adoption and effectiveness
  - Device trust anomalies and security alerts
  - Password strength distribution and compliance
  - Account security audit trail completeness

### Privacy and Compliance Monitoring
- [ ] **Compliance Metrics**
  - GDPR request processing times and completion rates
  - Data export accuracy and completeness validation
  - Privacy setting adoption and effectiveness
  - Consent management compliance and validation
  - Security audit findings and remediation tracking

## Definition of Done ✅
**This story is complete when:**
- ✅ User profile management provides comprehensive information editing with validation
- ✅ Password management and 2FA support secure authentication with multiple methods
- ✅ Personal notification preferences allow granular control with testing capabilities
- ✅ Interface preferences persist across sessions with cross-device synchronization
- ✅ Personal dashboard displays relevant activity and customizable widgets
- ✅ Account linking supports SSO integration with enterprise authentication systems
- ✅ Personal analytics provide productivity insights with goal tracking
- ✅ Account deletion and data export comply with GDPR requirements
- ✅ Cross-browser compatibility testing passes for all profile management features
- ✅ Performance benchmarks meet targets for profile operations (<2s response)
- ✅ Security testing passes with no authentication vulnerabilities
- ✅ All tests pass with >95% coverage including security and privacy scenarios

## Dependencies
- **Internal:** Story 4.1 (RBAC), Story 4.2 (team management), Story 4.4 (team settings)
- **External:** Email service for notification delivery and verification
- **External:** File storage service for avatar and document management
- **External:** SSO identity providers for authentication integration

## Risks & Mitigation
- **Risk:** Complex profile interface overwhelming users with configuration options
- **Mitigation:** Progressive disclosure, guided setup wizards, and intuitive organization
- **Risk:** Security feature adoption issues affecting account protection
- **Mitigation:** Clear security guidance, mandatory security features, and user education
- **Risk:** Data export and deletion complexity causing compliance issues
- **Mitigation:** Automated compliance tools, clear procedures, and legal review
- **Risk:** Cross-device synchronization issues affecting user experience
- **Mitigation:** Robust synchronization algorithms, conflict resolution, and fallback mechanisms

## Change Log
| Date | Version | Description | Author |
| :--- | :--- | :--- | :--- |
| 2025-01-23 | 1.0 | Initial story creation with comprehensive user profile and account management | Sarah (Product Owner) |
| 2025-01-23 | 1.1 | Added detailed security features and SSO integration | Sarah (Product Owner) |
| 2025-01-23 | 1.2 | Enhanced with GDPR compliance and privacy protection features | Sarah (Product Owner) |