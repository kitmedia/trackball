# Story 6.4: Subscription Management and Billing System

## Status
🟡 **PENDING** - Comprehensive subscription management and billing system with multiple tiers, flexible billing options, usage tracking, and automated payment processing

## Story
**As a** customer,
**I want** flexible subscription management with transparent billing,
**so that** I can choose the right plan for my team and manage costs effectively.

## Acceptance Criteria
1. Multiple subscription tiers (Starter, Professional, Elite) with clear feature differentiation ⏳
2. Flexible billing options including monthly, annual, and seasonal subscriptions ⏳
3. Usage-based billing with transparent pricing for storage and processing overages ⏳
4. Subscription upgrade/downgrade capabilities with prorated billing ⏳
5. Team member management with per-user pricing and bulk discounts ⏳
6. Invoice generation and automated billing with multiple payment methods ⏳
7. Usage monitoring and cost alerts to prevent unexpected charges ⏳
8. Cancellation and refund processing with clear terms and conditions ⏳

## Tasks / Subtasks

- [ ] **Task 6.4.1: Subscription Tier Management & Feature Configuration** ⏳
  - [ ] Create subscription tier framework with feature flags and access control
  - [ ] Implement Starter tier with basic features and usage limits
  - [ ] Add Professional tier with advanced features and higher limits
  - [ ] Create Elite tier with premium features and unlimited access
  - [ ] Implement feature differentiation system with dynamic access control
  - [ ] Add subscription comparison tools with feature matrix and pricing display
  - [ ] Create subscription analytics with tier adoption and usage tracking
  - [ ] Implement subscription testing with trial periods and feature validation
  - [ ] Add subscription documentation with feature descriptions and limitations
  - [ ] Create subscription optimization with conversion tracking and tier recommendations
  - [ ] Implement subscription security with access validation and audit logging
  - [ ] Add subscription compliance with pricing regulations and tax requirements
  - [ ] Create subscription integration with feature management and deployment systems
  - [ ] Implement subscription automation with tier assignment and feature provisioning
  - [ ] Add subscription scalability with multi-tenant architecture and resource allocation
  - **Estimate:** 32 hours | **Priority:** Critical | **Dependencies:** Story 4.1 (user management)
  - **Deliverables:**
    - Three-tier subscription system with feature differentiation
    - Dynamic access control with feature flags
    - Comparison tools with pricing matrix
    - Analytics with adoption tracking
    - Complete compliance and security implementation

- [ ] **Task 6.4.2: Flexible Billing System & Payment Processing** ⏳
  - [ ] Integrate Stripe payment processing with secure payment handling
  - [ ] Implement multiple billing cycles (monthly, annual, seasonal) with discount structures
  - [ ] Add payment method management with credit cards, bank transfers, and digital wallets
  - [ ] Create invoice generation with professional layouts and branding customization
  - [ ] Implement automated billing with retry logic and failure handling
  - [ ] Add payment security with PCI compliance and fraud protection
  - [ ] Create billing analytics with revenue tracking and payment method analysis
  - [ ] Implement billing notifications with payment confirmations and failure alerts
  - [ ] Add billing documentation with payment terms and privacy policies
  - [ ] Create billing testing with payment simulation and validation
  - [ ] Implement billing optimization with conversion rate analysis and payment flow improvement
  - [ ] Add billing integration with accounting systems and financial reporting
  - [ ] Create billing compliance with tax regulations and international payment laws
  - [ ] Implement billing scalability with high-volume transaction processing
  - [ ] Add billing support with payment dispute resolution and customer service integration
  - **Estimate:** 36 hours | **Priority:** Critical | **Dependencies:** Task 6.4.1
  - **Deliverables:**
    - Stripe integration with secure payment processing
    - Multiple billing cycles with automated processing
    - Professional invoice generation with branding
    - Payment method management with security compliance
    - Complete analytics and optimization framework

- [ ] **Task 6.4.3: Usage-Based Billing & Overage Management** ⏳
  - [ ] Create usage tracking system with real-time metering and aggregation
  - [ ] Implement storage usage billing with tiered pricing and optimization recommendations
  - [ ] Add processing time billing with minute-based pricing and bulk discounts
  - [ ] Create bandwidth usage tracking with CDN costs and geographic pricing
  - [ ] Implement usage alerts with threshold monitoring and cost projections
  - [ ] Add usage analytics with trend analysis and optimization insights
  - [ ] Create usage reporting with detailed breakdowns and visualization
  - [ ] Implement usage forecasting with predictive modeling and budget planning
  - [ ] Add usage optimization recommendations with cost-saving suggestions
  - [ ] Create usage validation with accuracy checking and dispute resolution
  - [ ] Implement usage security with access control and audit logging
  - [ ] Add usage integration with billing systems and invoice generation
  - [ ] Create usage documentation with pricing explanations and calculation methods
  - [ ] Implement usage testing with simulation and validation frameworks
  - [ ] Add usage compliance with data protection and privacy regulations
  - **Estimate:** 30 hours | **Priority:** Critical | **Dependencies:** Task 6.4.2
  - **Deliverables:**
    - Real-time usage tracking with metering
    - Tiered pricing for storage and processing
    - Usage alerts with threshold monitoring
    - Analytics with trend analysis and forecasting
    - Complete validation and optimization system

- [ ] **Task 6.4.4: Subscription Lifecycle Management & Plan Changes** ⏳
  - [ ] Create subscription upgrade system with immediate feature access and prorated billing
  - [ ] Implement subscription downgrade with feature restrictions and credit handling
  - [ ] Add plan change validation with compatibility checking and limitation warnings
  - [ ] Create proration calculation with accurate billing adjustments and tax handling
  - [ ] Implement subscription pause/resume with billing suspension and feature access control
  - [ ] Add subscription renewal with automatic processing and payment failure handling
  - [ ] Create subscription history with change tracking and audit trails
  - [ ] Implement subscription notifications with change confirmations and billing updates
  - [ ] Add subscription analytics with churn analysis and retention metrics
  - [ ] Create subscription optimization with upgrade recommendations and retention strategies
  - [ ] Implement subscription security with change authorization and fraud prevention
  - [ ] Add subscription integration with CRM systems and customer success workflows
  - [ ] Create subscription documentation with change policies and billing explanations
  - [ ] Implement subscription testing with plan change validation and billing accuracy
  - [ ] Add subscription compliance with contract terms and regulatory requirements
  - **Estimate:** 28 hours | **Priority:** Critical | **Dependencies:** Task 6.4.3
  - **Deliverables:**
    - Seamless upgrade/downgrade with prorated billing
    - Plan change validation with compatibility checking
    - Subscription lifecycle tracking with history
    - Automated renewal with failure handling
    - Complete analytics and optimization framework

- [ ] **Task 6.4.5: Team Member Management & User-Based Pricing** ⏳
  - [ ] Create team member invitation system with role assignment and billing integration
  - [ ] Implement per-user pricing with automatic billing adjustments
  - [ ] Add bulk discount calculation with volume-based pricing tiers
  - [ ] Create team size monitoring with usage tracking and optimization recommendations
  - [ ] Implement user deactivation with billing adjustments and data retention
  - [ ] Add team analytics with member activity tracking and engagement metrics
  - [ ] Create team billing with consolidated invoicing and cost allocation
  - [ ] Implement team permissions with role-based access and billing visibility
  - [ ] Add team optimization with usage analysis and cost-saving recommendations
  - [ ] Create team validation with member verification and access control
  - [ ] Implement team security with access logging and permission auditing
  - [ ] Add team integration with user management and subscription systems
  - [ ] Create team documentation with pricing policies and member management guides
  - [ ] Implement team testing with member scenarios and billing validation
  - [ ] Add team compliance with data protection and privacy regulations
  - **Estimate:** 26 hours | **Priority:** High | **Dependencies:** Task 6.4.4
  - **Deliverables:**
    - Team member management with role-based billing
    - Per-user pricing with bulk discounts
    - Consolidated team billing and invoicing
    - Member activity tracking and analytics
    - Complete security and compliance implementation

- [ ] **Task 6.4.6: Invoice Management & Financial Reporting** ⏳
  - [ ] Create automated invoice generation with professional templates and branding
  - [ ] Implement invoice delivery with email automation and portal access
  - [ ] Add invoice customization with company branding and payment terms
  - [ ] Create invoice tracking with delivery confirmation and payment status
  - [ ] Implement invoice history with searchable archive and download capabilities
  - [ ] Add invoice analytics with payment patterns and collection metrics
  - [ ] Create invoice integration with accounting systems and ERP platforms
  - [ ] Implement invoice validation with accuracy checking and error handling
  - [ ] Add invoice security with access control and audit logging
  - [ ] Create invoice optimization with template improvement and delivery enhancement
  - [ ] Implement invoice compliance with tax regulations and accounting standards
  - [ ] Add invoice testing with generation validation and delivery confirmation
  - [ ] Create invoice documentation with formatting guides and customization options
  - [ ] Implement invoice automation with scheduled generation and delivery
  - [ ] Add invoice support with customer inquiries and dispute resolution
  - **Estimate:** 24 hours | **Priority:** High | **Dependencies:** Task 6.4.5
  - **Deliverables:**
    - Automated invoice generation with professional templates
    - Invoice delivery with email and portal access
    - Invoice tracking with payment status monitoring
    - Integration with accounting systems
    - Complete compliance and optimization framework

- [ ] **Task 6.4.7: Usage Monitoring & Cost Alert System** ⏳
  - [ ] Create real-time usage dashboard with current consumption and projections
  - [ ] Implement cost alert system with customizable thresholds and notifications
  - [ ] Add usage trend analysis with historical data and predictive modeling
  - [ ] Create budget management with spending limits and automatic controls
  - [ ] Implement usage optimization recommendations with cost-saving suggestions
  - [ ] Add usage reporting with detailed breakdowns and visualization
  - [ ] Create usage forecasting with predictive analytics and budget planning
  - [ ] Implement usage validation with accuracy monitoring and dispute resolution
  - [ ] Add usage integration with billing systems and invoice generation
  - [ ] Create usage security with access control and data protection
  - [ ] Implement usage analytics with pattern recognition and anomaly detection
  - [ ] Add usage automation with alert delivery and escalation procedures
  - [ ] Create usage documentation with monitoring guides and alert configuration
  - [ ] Implement usage testing with threshold validation and alert simulation
  - [ ] Add usage compliance with data privacy and financial regulations
  - **Estimate:** 22 hours | **Priority:** High | **Dependencies:** Task 6.4.6
  - **Deliverables:**
    - Real-time usage dashboard with projections
    - Customizable cost alerts with notifications
    - Budget management with spending controls
    - Usage optimization with recommendations
    - Complete analytics and forecasting system

- [ ] **Task 6.4.8: Cancellation & Refund Management System** ⏳
  - [ ] Create subscription cancellation workflow with retention strategies and feedback collection
  - [ ] Implement immediate vs. end-of-period cancellation with feature access management
  - [ ] Add refund processing with automated calculations and payment reversals
  - [ ] Create cancellation analytics with churn analysis and reason tracking
  - [ ] Implement retention offers with discount proposals and plan modifications
  - [ ] Add cancellation validation with confirmation requirements and cooling-off periods
  - [ ] Create cancellation documentation with terms, conditions, and policy explanations
  - [ ] Implement cancellation notifications with confirmations and next steps
  - [ ] Add cancellation integration with customer support and success management
  - [ ] Create cancellation optimization with retention rate improvement and churn reduction
  - [ ] Implement cancellation security with fraud prevention and abuse protection
  - [ ] Add cancellation testing with workflow validation and refund accuracy
  - [ ] Create cancellation compliance with consumer protection and regulatory requirements
  - [ ] Implement cancellation reporting with metrics tracking and trend analysis
  - [ ] Add cancellation automation with workflow triggers and escalation procedures
  - **Estimate:** 20 hours | **Priority:** Medium | **Dependencies:** Task 6.4.7
  - **Deliverables:**
    - Subscription cancellation with retention strategies
    - Automated refund processing with validation
    - Cancellation analytics with churn tracking
    - Retention offers with plan modifications
    - Complete compliance and optimization framework

## API Implementation

### Subscription Management and Billing Endpoints

```typescript
// Subscription management endpoints
GET    /api/v1/subscriptions                        // List subscription tiers
GET    /api/v1/subscriptions/current                 // Get current subscription
POST   /api/v1/subscriptions/upgrade                 // Upgrade subscription
POST   /api/v1/subscriptions/downgrade               // Downgrade subscription
POST   /api/v1/subscriptions/cancel                  // Cancel subscription
GET    /api/v1/subscriptions/usage                   // Get usage metrics
POST   /api/v1/subscriptions/pause                   // Pause subscription

// Billing and payment endpoints
GET    /api/v1/billing/invoices                      // List invoices
GET    /api/v1/billing/invoices/{id}                 // Get invoice details
POST   /api/v1/billing/payment-methods               // Add payment method
PUT    /api/v1/billing/payment-methods/{id}          // Update payment method
DELETE /api/v1/billing/payment-methods/{id}          // Remove payment method
GET    /api/v1/billing/usage                         // Get detailed usage
POST   /api/v1/billing/alerts                       // Create usage alert

// Team management endpoints
GET    /api/v1/teams/members                         // List team members
POST   /api/v1/teams/members/invite                  // Invite team member
DELETE /api/v1/teams/members/{id}                    // Remove team member
GET    /api/v1/teams/billing                         // Get team billing info
PUT    /api/v1/teams/billing/settings                // Update billing settings
```

### Subscription Management System Implementation

```python
# Backend: Subscription Management System
from typing import Dict, List, Optional, Any, Union
import asyncio
import json
import logging
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
from decimal import Decimal
import stripe
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Text, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class SubscriptionTier(Enum):
    STARTER = "starter"
    PROFESSIONAL = "professional"
    ELITE = "elite"

class BillingCycle(Enum):
    MONTHLY = "monthly"
    ANNUAL = "annual"
    SEASONAL = "seasonal"

class SubscriptionStatus(Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    TRIAL = "trial"

@dataclass
class UsageMetrics:
    storage_gb: float
    processing_minutes: int
    bandwidth_gb: float
    api_calls: int
    active_users: int
    period_start: datetime
    period_end: datetime

@dataclass
class BillingCalculation:
    base_amount: Decimal
    usage_charges: Decimal
    discounts: Decimal
    tax_amount: Decimal
    total_amount: Decimal
    currency: str

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, nullable=False)
    tier = Column(String, nullable=False)
    status = Column(String, nullable=False)
    billing_cycle = Column(String, nullable=False)
    current_period_start = Column(DateTime, nullable=False)
    current_period_end = Column(DateTime, nullable=False)
    trial_end = Column(DateTime)
    cancel_at = Column(DateTime)
    cancelled_at = Column(DateTime)
    stripe_subscription_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Invoice(Base):
    __tablename__ = 'invoices'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    subscription_id = Column(String, ForeignKey('subscriptions.id'), nullable=False)
    invoice_number = Column(String, unique=True, nullable=False)
    amount_due = Column(Numeric(10, 2), nullable=False)
    amount_paid = Column(Numeric(10, 2), default=0)
    currency = Column(String, default='USD')
    status = Column(String, nullable=False)  # draft, open, paid, void
    due_date = Column(DateTime, nullable=False)
    paid_at = Column(DateTime)
    stripe_invoice_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    subscription = relationship("Subscription")

class UsageRecord(Base):
    __tablename__ = 'usage_records'
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    subscription_id = Column(String, ForeignKey('subscriptions.id'), nullable=False)
    metric_type = Column(String, nullable=False)  # storage, processing, bandwidth, etc.
    quantity = Column(Numeric(10, 4), nullable=False)
    unit_price = Column(Numeric(10, 4))
    total_cost = Column(Numeric(10, 2))
    recorded_at = Column(DateTime, default=datetime.utcnow)
    billing_period_start = Column(DateTime, nullable=False)
    billing_period_end = Column(DateTime, nullable=False)
    
    subscription = relationship("Subscription")

class SubscriptionManager:
    """Comprehensive subscription management and billing system"""
    
    def __init__(self, db_session, stripe_api_key: str):
        self.db = db_session
        self.logger = logging.getLogger(__name__)
        
        # Initialize Stripe
        stripe.api_key = stripe_api_key
        
        # Subscription configuration
        self.subscription_tiers = self._load_subscription_tiers()
        self.billing_cycles = self._load_billing_cycles()
        self.usage_pricing = self._load_usage_pricing()
        
        # Components
        self.usage_tracker = UsageTracker()
        self.billing_calculator = BillingCalculator()
        self.invoice_generator = InvoiceGenerator()
        self.payment_processor = PaymentProcessor()
        
    def _load_subscription_tiers(self) -> Dict[str, Dict]:
        """Load subscription tier configurations"""
        return {
            SubscriptionTier.STARTER.value: {
                'name': 'Starter',
                'monthly_price': Decimal('29.00'),
                'annual_price': Decimal('290.00'),  # 2 months free
                'features': [
                    'up_to_5_users',
                    'basic_video_analysis',
                    '10gb_storage',
                    '50_processing_minutes',
                    'email_support'
                ],
                'limits': {
                    'users': 5,
                    'storage_gb': 10,
                    'processing_minutes': 50,
                    'projects': 5
                },
                'stripe_price_ids': {
                    'monthly': 'price_starter_monthly',
                    'annual': 'price_starter_annual'
                }
            },
            SubscriptionTier.PROFESSIONAL.value: {
                'name': 'Professional',
                'monthly_price': Decimal('99.00'),
                'annual_price': Decimal('990.00'),  # 2 months free
                'features': [
                    'up_to_25_users',
                    'advanced_tactical_analysis',
                    '100gb_storage',
                    '500_processing_minutes',
                    'priority_support',
                    'api_access',
                    'custom_reports'
                ],
                'limits': {
                    'users': 25,
                    'storage_gb': 100,
                    'processing_minutes': 500,
                    'projects': 50
                },
                'stripe_price_ids': {
                    'monthly': 'price_professional_monthly',
                    'annual': 'price_professional_annual'
                }
            },
            SubscriptionTier.ELITE.value: {
                'name': 'Elite',
                'monthly_price': Decimal('299.00'),
                'annual_price': Decimal('2990.00'),  # 2 months free
                'features': [
                    'unlimited_users',
                    'all_features',
                    'unlimited_storage',
                    'unlimited_processing',
                    'dedicated_support',
                    'custom_integrations',
                    'white_label_options'
                ],
                'limits': {
                    'users': -1,  # unlimited
                    'storage_gb': -1,  # unlimited
                    'processing_minutes': -1,  # unlimited
                    'projects': -1  # unlimited
                },
                'stripe_price_ids': {
                    'monthly': 'price_elite_monthly',
                    'annual': 'price_elite_annual'
                }
            }
        }
    
    async def create_subscription(self, customer_id: str, tier: str, 
                                billing_cycle: str, payment_method_id: str) -> Dict[str, Any]:
        """Create new subscription with Stripe integration"""
        try:
            # Validate tier and billing cycle
            if tier not in self.subscription_tiers:
                return {'success': False, 'error': 'Invalid subscription tier'}
            
            if billing_cycle not in [cycle.value for cycle in BillingCycle]:
                return {'success': False, 'error': 'Invalid billing cycle'}
            
            tier_config = self.subscription_tiers[tier]
            
            # Create Stripe customer if not exists
            stripe_customer = await self._get_or_create_stripe_customer(customer_id)
            
            # Attach payment method
            await stripe.PaymentMethod.attach(payment_method_id, customer=stripe_customer.id)
            
            # Set as default payment method
            await stripe.Customer.modify(
                stripe_customer.id,
                invoice_settings={'default_payment_method': payment_method_id}
            )
            
            # Create Stripe subscription
            stripe_price_id = tier_config['stripe_price_ids'][billing_cycle]
            
            stripe_subscription = await stripe.Subscription.create(
                customer=stripe_customer.id,
                items=[{'price': stripe_price_id}],
                payment_behavior='default_incomplete',
                payment_settings={'save_default_payment_method': 'on_subscription'},
                expand=['latest_invoice.payment_intent']
            )
            
            # Create local subscription record
            subscription = Subscription(
                customer_id=customer_id,
                tier=tier,
                status=SubscriptionStatus.ACTIVE.value,
                billing_cycle=billing_cycle,
                current_period_start=datetime.fromtimestamp(stripe_subscription.current_period_start),
                current_period_end=datetime.fromtimestamp(stripe_subscription.current_period_end),
                stripe_subscription_id=stripe_subscription.id
            )
            
            # Add trial period if applicable
            if hasattr(stripe_subscription, 'trial_end') and stripe_subscription.trial_end:
                subscription.trial_end = datetime.fromtimestamp(stripe_subscription.trial_end)
                subscription.status = SubscriptionStatus.TRIAL.value
            
            self.db.add(subscription)
            self.db.commit()
            
            # Initialize usage tracking
            await self.usage_tracker.initialize_subscription_usage(subscription.id)
            
            return {
                'success': True,
                'subscription_id': subscription.id,
                'stripe_subscription_id': stripe_subscription.id,
                'client_secret': stripe_subscription.latest_invoice.payment_intent.client_secret
            }
            
        except Exception as e:
            self.logger.error(f"Error creating subscription: {e}")
            self.db.rollback()
            return {'success': False, 'error': str(e)}
    
    async def upgrade_subscription(self, subscription_id: str, new_tier: str) -> Dict[str, Any]:
        """Upgrade subscription with prorated billing"""
        try:
            # Get current subscription
            subscription = self.db.query(Subscription).filter(
                Subscription.id == subscription_id
            ).first()
            
            if not subscription:
                return {'success': False, 'error': 'Subscription not found'}
            
            if subscription.status != SubscriptionStatus.ACTIVE.value:
                return {'success': False, 'error': 'Subscription not active'}
            
            # Validate new tier
            if new_tier not in self.subscription_tiers:
                return {'success': False, 'error': 'Invalid subscription tier'}
            
            current_tier_config = self.subscription_tiers[subscription.tier]
            new_tier_config = self.subscription_tiers[new_tier]
            
            # Check if it's actually an upgrade
            current_price = current_tier_config[f"{subscription.billing_cycle}_price"]
            new_price = new_tier_config[f"{subscription.billing_cycle}_price"]
            
            if new_price <= current_price:
                return {'success': False, 'error': 'New tier must be higher than current tier'}
            
            # Update Stripe subscription
            new_price_id = new_tier_config['stripe_price_ids'][subscription.billing_cycle]
            
            stripe_subscription = await stripe.Subscription.modify(
                subscription.stripe_subscription_id,
                items=[{
                    'id': subscription.stripe_subscription_id,
                    'price': new_price_id
                }],
                proration_behavior='create_prorations'
            )
            
            # Update local subscription
            subscription.tier = new_tier
            subscription.updated_at = datetime.utcnow()
            
            self.db.commit()
            
            # Calculate prorated amount
            proration_amount = await self._calculate_proration(
                subscription, current_price, new_price
            )
            
            # Update feature access
            await self._update_feature_access(subscription_id, new_tier)
            
            return {
                'success': True,
                'subscription_id': subscription_id,
                'new_tier': new_tier,
                'proration_amount': float(proration_amount),
                'effective_immediately': True
            }
            
        except Exception as e:
            self.logger.error(f"Error upgrading subscription: {e}")
            self.db.rollback()
            return {'success': False, 'error': str(e)}
    
    async def get_usage_metrics(self, subscription_id: str, 
                              period_start: Optional[datetime] = None,
                              period_end: Optional[datetime] = None) -> Dict[str, Any]:
        """Get comprehensive usage metrics for subscription"""
        try:
            subscription = self.db.query(Subscription).filter(
                Subscription.id == subscription_id
            ).first()
            
            if not subscription:
                return {'error': 'Subscription not found'}
            
            # Default to current billing period
            if not period_start:
                period_start = subscription.current_period_start
            if not period_end:
                period_end = subscription.current_period_end
            
            # Get usage records
            usage_records = self.db.query(UsageRecord).filter(
                UsageRecord.subscription_id == subscription_id,
                UsageRecord.recorded_at >= period_start,
                UsageRecord.recorded_at <= period_end
            ).all()
            
            # Aggregate usage by metric type
            usage_summary = {}
            total_overage_cost = Decimal('0.00')
            
            for record in usage_records:
                if record.metric_type not in usage_summary:
                    usage_summary[record.metric_type] = {
                        'quantity': Decimal('0.00'),
                        'cost': Decimal('0.00'),
                        'unit_price': record.unit_price or Decimal('0.00')
                    }
                
                usage_summary[record.metric_type]['quantity'] += record.quantity
                usage_summary[record.metric_type]['cost'] += record.total_cost or Decimal('0.00')
                total_overage_cost += record.total_cost or Decimal('0.00')
            
            # Get subscription limits
            tier_config = self.subscription_tiers[subscription.tier]
            limits = tier_config['limits']
            
            # Calculate usage percentages and overages
            usage_analysis = {}
            for metric_type, usage_data in usage_summary.items():
                limit_key = f"{metric_type}_gb" if metric_type in ['storage', 'bandwidth'] else metric_type
                limit = limits.get(limit_key, -1)
                
                if limit == -1:  # Unlimited
                    percentage = 0
                    overage = 0
                else:
                    percentage = min(100, (float(usage_data['quantity']) / limit) * 100)
                    overage = max(0, float(usage_data['quantity']) - limit)
                
                usage_analysis[metric_type] = {
                    'current_usage': float(usage_data['quantity']),
                    'limit': limit,
                    'percentage_used': percentage,
                    'overage': overage,
                    'overage_cost': float(usage_data['cost']),
                    'unit_price': float(usage_data['unit_price'])
                }
            
            # Project usage for rest of billing period
            days_elapsed = (datetime.utcnow() - period_start).days
            total_days = (period_end - period_start).days
            
            if days_elapsed > 0 and total_days > days_elapsed:
                projection_factor = total_days / days_elapsed
                
                for metric_type in usage_analysis:
                    current = usage_analysis[metric_type]['current_usage']
                    projected = current * projection_factor
                    usage_analysis[metric_type]['projected_usage'] = projected
                    
                    limit = usage_analysis[metric_type]['limit']
                    if limit != -1:
                        projected_overage = max(0, projected - limit)
                        usage_analysis[metric_type]['projected_overage'] = projected_overage
                        
                        unit_price = usage_analysis[metric_type]['unit_price']
                        usage_analysis[metric_type]['projected_overage_cost'] = projected_overage * unit_price
            
            return {
                'subscription_id': subscription_id,
                'period_start': period_start.isoformat(),
                'period_end': period_end.isoformat(),
                'tier': subscription.tier,
                'usage_summary': usage_analysis,
                'total_overage_cost': float(total_overage_cost),
                'billing_period_progress': min(100, (days_elapsed / total_days) * 100) if total_days > 0 else 0
            }
            
        except Exception as e:
            self.logger.error(f"Error getting usage metrics: {e}")
            return {'error': str(e)}
    
    async def cancel_subscription(self, subscription_id: str, 
                                cancel_immediately: bool = False,
                                cancellation_reason: Optional[str] = None) -> Dict[str, Any]:
        """Cancel subscription with retention strategies"""
        try:
            subscription = self.db.query(Subscription).filter(
                Subscription.id == subscription_id
            ).first()
            
            if not subscription:
                return {'success': False, 'error': 'Subscription not found'}
            
            if subscription.status == SubscriptionStatus.CANCELLED.value:
                return {'success': False, 'error': 'Subscription already cancelled'}
            
            # Implement retention strategies
            retention_offers = await self._generate_retention_offers(subscription)
            
            if cancel_immediately:
                # Cancel immediately with refund calculation
                stripe_subscription = await stripe.Subscription.delete(
                    subscription.stripe_subscription_id
                )
                
                subscription.status = SubscriptionStatus.CANCELLED.value
                subscription.cancelled_at = datetime.utcnow()
                
                # Calculate refund amount
                refund_amount = await self._calculate_refund(subscription)
                
                if refund_amount > 0:
                    # Process refund
                    await self._process_refund(subscription, refund_amount)
                
            else:
                # Cancel at period end
                await stripe.Subscription.modify(
                    subscription.stripe_subscription_id,
                    cancel_at_period_end=True
                )
                
                subscription.cancel_at = subscription.current_period_end
                refund_amount = Decimal('0.00')
            
            self.db.commit()
            
            # Record cancellation reason
            if cancellation_reason:
                await self._record_cancellation_feedback(subscription_id, cancellation_reason)
            
            # Send cancellation confirmation
            await self._send_cancellation_confirmation(subscription)
            
            return {
                'success': True,
                'subscription_id': subscription_id,
                'cancelled_immediately': cancel_immediately,
                'refund_amount': float(refund_amount),
                'access_until': subscription.current_period_end.isoformat() if not cancel_immediately else datetime.utcnow().isoformat(),
                'retention_offers': retention_offers
            }
            
        except Exception as e:
            self.logger.error(f"Error cancelling subscription: {e}")
            self.db.rollback()
            return {'success': False, 'error': str(e)}

class UsageTracker:
    """Real-time usage tracking and metering"""
    
    def __init__(self):
        self.usage_cache = {}  # Redis would be used in production
        
    async def track_usage(self, subscription_id: str, metric_type: str, 
                         quantity: float, metadata: Optional[Dict] = None) -> Dict[str, Any]:
        """Track usage event with real-time aggregation"""
        try:
            # Get subscription
            subscription = self.db.query(Subscription).filter(
                Subscription.id == subscription_id
            ).first()
            
            if not subscription:
                return {'success': False, 'error': 'Subscription not found'}
            
            # Create usage record
            usage_record = UsageRecord(
                subscription_id=subscription_id,
                metric_type=metric_type,
                quantity=Decimal(str(quantity)),
                billing_period_start=subscription.current_period_start,
                billing_period_end=subscription.current_period_end,
                recorded_at=datetime.utcnow()
            )
            
            # Calculate cost if overage
            tier_config = subscription_manager.subscription_tiers[subscription.tier]
            limit_key = f"{metric_type}_gb" if metric_type in ['storage', 'bandwidth'] else metric_type
            limit = tier_config['limits'].get(limit_key, -1)
            
            if limit != -1:  # Has limit
                # Get current usage for this period
                current_usage = await self._get_current_usage(
                    subscription_id, metric_type, 
                    subscription.current_period_start,
                    subscription.current_period_end
                )
                
                total_usage = current_usage + Decimal(str(quantity))
                
                if total_usage > limit:
                    # Calculate overage cost
                    overage = total_usage - limit
                    unit_price = self._get_overage_price(metric_type)
                    
                    usage_record.unit_price = unit_price
                    usage_record.total_cost = overage * unit_price
            
            self.db.add(usage_record)
            self.db.commit()
            
            # Update real-time cache
            cache_key = f"{subscription_id}:{metric_type}"
            if cache_key not in self.usage_cache:
                self.usage_cache[cache_key] = Decimal('0.00')
            
            self.usage_cache[cache_key] += Decimal(str(quantity))
            
            # Check for usage alerts
            await self._check_usage_alerts(subscription_id, metric_type, total_usage)
            
            return {
                'success': True,
                'usage_record_id': usage_record.id,
                'total_usage': float(total_usage),
                'overage_cost': float(usage_record.total_cost or 0)
            }
            
        except Exception as e:
            logging.error(f"Error tracking usage: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _check_usage_alerts(self, subscription_id: str, metric_type: str, 
                                current_usage: Decimal):
        """Check and trigger usage alerts"""
        try:
            # Get subscription limits
            subscription = self.db.query(Subscription).filter(
                Subscription.id == subscription_id
            ).first()
            
            tier_config = subscription_manager.subscription_tiers[subscription.tier]
            limit_key = f"{metric_type}_gb" if metric_type in ['storage', 'bandwidth'] else metric_type
            limit = tier_config['limits'].get(limit_key, -1)
            
            if limit == -1:  # Unlimited
                return
            
            usage_percentage = (float(current_usage) / limit) * 100
            
            # Define alert thresholds
            alert_thresholds = [50, 75, 90, 100]
            
            for threshold in alert_thresholds:
                if usage_percentage >= threshold:
                    await self._send_usage_alert(
                        subscription_id, metric_type, usage_percentage, threshold
                    )
                    break
                    
        except Exception as e:
            logging.error(f"Error checking usage alerts: {e}")

class BillingCalculator:
    """Billing calculation and proration logic"""
    
    def __init__(self):
        self.tax_rates = {
            'US': Decimal('0.08'),  # 8% average sales tax
            'EU': Decimal('0.20'),  # 20% VAT
            'UK': Decimal('0.20'),  # 20% VAT
            'CA': Decimal('0.13'),  # 13% HST
        }
        
    async def calculate_invoice_amount(self, subscription: Subscription,
                                    usage_records: List[UsageRecord],
                                    billing_period_start: datetime,
                                    billing_period_end: datetime) -> BillingCalculation:
        """Calculate total invoice amount including usage charges"""
        try:
            tier_config = subscription_manager.subscription_tiers[subscription.tier]
            
            # Base subscription amount
            if subscription.billing_cycle == BillingCycle.MONTHLY.value:
                base_amount = tier_config['monthly_price']
            elif subscription.billing_cycle == BillingCycle.ANNUAL.value:
                base_amount = tier_config['annual_price'] / 12  # Monthly portion
            else:  # Seasonal
                base_amount = tier_config['monthly_price'] * 3  # 3 months
            
            # Calculate usage charges
            usage_charges = Decimal('0.00')
            for record in usage_records:
                usage_charges += record.total_cost or Decimal('0.00')
            
            # Apply discounts (bulk, loyalty, promotional)
            discounts = await self._calculate_discounts(subscription, base_amount, usage_charges)
            
            # Calculate subtotal
            subtotal = base_amount + usage_charges - discounts
            
            # Calculate tax
            tax_amount = await self._calculate_tax(subscription, subtotal)
            
            # Total amount
            total_amount = subtotal + tax_amount
            
            return BillingCalculation(
                base_amount=base_amount,
                usage_charges=usage_charges,
                discounts=discounts,
                tax_amount=tax_amount,
                total_amount=total_amount,
                currency='USD'
            )
            
        except Exception as e:
            logging.error(f"Error calculating invoice amount: {e}")
            raise
    
    async def calculate_proration(self, subscription: Subscription,
                                old_amount: Decimal, new_amount: Decimal) -> Decimal:
        """Calculate prorated amount for subscription changes"""
        try:
            # Calculate remaining days in current period
            now = datetime.utcnow()
            total_days = (subscription.current_period_end - subscription.current_period_start).days
            remaining_days = (subscription.current_period_end - now).days
            
            if remaining_days <= 0:
                return Decimal('0.00')
            
            # Calculate daily rates
            old_daily_rate = old_amount / total_days
            new_daily_rate = new_amount / total_days
            
            # Calculate proration
            unused_credit = old_daily_rate * remaining_days
            new_charge = new_daily_rate * remaining_days
            
            proration = new_charge - unused_credit
            
            return max(Decimal('0.00'), proration)
            
        except Exception as e:
            logging.error(f"Error calculating proration: {e}")
            return Decimal('0.00')

class InvoiceGenerator:
    """Professional invoice generation and delivery"""
    
    def __init__(self):
        self.invoice_counter = 100000  # Starting invoice number
        
    async def generate_invoice(self, subscription: Subscription,
                             billing_calculation: BillingCalculation,
                             billing_period_start: datetime,
                             billing_period_end: datetime) -> str:
        """Generate professional invoice with branding"""
        try:
            # Generate unique invoice number
            invoice_number = f"TRB-{self.invoice_counter}"
            self.invoice_counter += 1
            
            # Create invoice record
            invoice = Invoice(
                subscription_id=subscription.id,
                invoice_number=invoice_number,
                amount_due=billing_calculation.total_amount,
                currency=billing_calculation.currency,
                status='open',
                due_date=datetime.utcnow() + timedelta(days=30)
            )
            
            self.db.add(invoice)
            self.db.commit()
            
            # Generate PDF invoice
            pdf_path = await self._generate_invoice_pdf(
                invoice, subscription, billing_calculation,
                billing_period_start, billing_period_end
            )
            
            # Send invoice email
            await self._send_invoice_email(invoice, pdf_path)
            
            return invoice.id
            
        except Exception as e:
            logging.error(f"Error generating invoice: {e}")
            raise
    
    async def _generate_invoice_pdf(self, invoice: Invoice, subscription: Subscription,
                                  billing_calculation: BillingCalculation,
                                  period_start: datetime, period_end: datetime) -> str:
        """Generate PDF invoice with professional layout"""
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.lib import colors
            from reportlab.lib.units import inch
            
            # Create PDF file
            pdf_path = f"/tmp/invoice_{invoice.id}.pdf"
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()
            
            # Company header
            story.append(Paragraph("Trackball Sports Analytics", styles['Title']))
            story.append(Paragraph("Professional Video Analysis Platform", styles['Normal']))
            story.append(Spacer(1, 20))
            
            # Invoice details
            invoice_data = [
                ['Invoice Number:', invoice.invoice_number],
                ['Invoice Date:', invoice.created_at.strftime('%B %d, %Y')],
                ['Due Date:', invoice.due_date.strftime('%B %d, %Y')],
                ['Billing Period:', f"{period_start.strftime('%B %d, %Y')} - {period_end.strftime('%B %d, %Y')}"]
            ]
            
            invoice_table = Table(invoice_data, colWidths=[2*inch, 3*inch])
            invoice_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ]))
            
            story.append(invoice_table)
            story.append(Spacer(1, 30))
            
            # Billing details
            billing_data = [
                ['Description', 'Amount'],
                [f'{subscription.tier.title()} Subscription', f'${billing_calculation.base_amount:.2f}'],
                ['Usage Charges', f'${billing_calculation.usage_charges:.2f}'],
                ['Discounts', f'-${billing_calculation.discounts:.2f}'],
                ['Tax', f'${billing_calculation.tax_amount:.2f}'],
                ['Total', f'${billing_calculation.total_amount:.2f}']
            ]
            
            billing_table = Table(billing_data, colWidths=[4*inch, 1.5*inch])
            billing_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('LINEBELOW', (0, -2), (-1, -2), 2, colors.black),
                ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ]))
            
            story.append(billing_table)
            story.append(Spacer(1, 30))
            
            # Payment instructions
            story.append(Paragraph("Payment Instructions", styles['Heading2']))
            story.append(Paragraph("Payment will be automatically charged to your default payment method.", styles['Normal']))
            story.append(Paragraph("Questions? Contact support@trackball.com", styles['Normal']))
            
            # Build PDF
            doc.build(story)
            
            return pdf_path
            
        except Exception as e:
            logging.error(f"Error generating invoice PDF: {e}")
            raise

class PaymentProcessor:
    """Payment processing and failure handling"""
    
    def __init__(self):
        self.retry_delays = [1, 3, 7]  # Days to retry failed payments
        
    async def process_payment(self, invoice: Invoice) -> Dict[str, Any]:
        """Process payment for invoice"""
        try:
            # Get subscription
            subscription = self.db.query(Subscription).filter(
                Subscription.id == invoice.subscription_id
            ).first()
            
            # Get Stripe customer
            stripe_customer = await stripe.Customer.retrieve(subscription.customer_id)
            
            # Create payment intent
            payment_intent = await stripe.PaymentIntent.create(
                amount=int(invoice.amount_due * 100),  # Convert to cents
                currency=invoice.currency.lower(),
                customer=stripe_customer.id,
                payment_method=stripe_customer.invoice_settings.default_payment_method,
                confirmation_method='automatic',
                confirm=True
            )
            
            if payment_intent.status == 'succeeded':
                # Update invoice
                invoice.status = 'paid'
                invoice.amount_paid = invoice.amount_due
                invoice.paid_at = datetime.utcnow()
                
                self.db.commit()
                
                # Send payment confirmation
                await self._send_payment_confirmation(invoice)
                
                return {'success': True, 'payment_intent_id': payment_intent.id}
            else:
                # Schedule retry
                await self._schedule_payment_retry(invoice)
                
                return {'success': False, 'status': payment_intent.status}
                
        except stripe.error.CardError as e:
            # Payment failed
            await self._handle_payment_failure(invoice, str(e))
            return {'success': False, 'error': str(e)}
        except Exception as e:
            logging.error(f"Error processing payment: {e}")
            return {'success': False, 'error': str(e)}
    
    async def _schedule_payment_retry(self, invoice: Invoice):
        """Schedule automatic payment retry"""
        try:
            # Implement retry logic with exponential backoff
            # This would typically use a task queue like Celery
            pass
        except Exception as e:
            logging.error(f"Error scheduling payment retry: {e}")
```

## Frontend Component Architecture

### Subscription Management Dashboard

```typescript
// Frontend: Subscription Management Dashboard
import React, { useState, useEffect } from 'react';
import {
  Box,
  Grid,
  Card,
  CardContent,
  Typography,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  LinearProgress,
  Alert,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  IconButton,
  Tooltip,
  Switch,
  FormControlLabel,
  Divider
} from '@mui/material';
import {
  CreditCard as BillingIcon,
  TrendingUp as UpgradeIcon,
  TrendingDown as DowngradeIcon,
  Cancel as CancelIcon,
  Receipt as InvoiceIcon,
  Warning as AlertIcon,
  People as TeamIcon,
  Settings as SettingsIcon,
  Download as DownloadIcon,
  Check as CheckIcon,
  Close as CloseIcon
} from '@mui/icons-material';

interface Subscription {
  id: string;
  tier: 'starter' | 'professional' | 'elite';
  status: 'active' | 'paused' | 'cancelled' | 'expired' | 'trial';
  billingCycle: 'monthly' | 'annual' | 'seasonal';
  currentPeriodStart: string;
  currentPeriodEnd: string;
  trialEnd?: string;
  cancelAt?: string;
}

interface UsageMetrics {
  subscriptionId: string;
  periodStart: string;
  periodEnd: string;
  tier: string;
  usageSummary: Record<string, UsageDetail>;
  totalOverageCost: number;
  billingPeriodProgress: number;
}

interface UsageDetail {
  currentUsage: number;
  limit: number;
  percentageUsed: number;
  overage: number;
  overageCost: number;
  unitPrice: number;
  projectedUsage?: number;
  projectedOverage?: number;
  projectedOverageCost?: number;
}

interface Invoice {
  id: string;
  invoiceNumber: string;
  amountDue: number;
  amountPaid: number;
  currency: string;
  status: 'draft' | 'open' | 'paid' | 'void';
  dueDate: string;
  paidAt?: string;
  createdAt: string;
}

export const SubscriptionManagementDashboard: React.FC = () => {
  const [subscription, setSubscription] = useState<Subscription | null>(null);
  const [usageMetrics, setUsageMetrics] = useState<UsageMetrics | null>(null);
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [upgradeDialogOpen, setUpgradeDialogOpen] = useState(false);
  const [cancelDialogOpen, setCancelDialogOpen] = useState(false);
  const [selectedNewTier, setSelectedNewTier] = useState('');
  const [loading, setLoading] = useState(true);

  const subscriptionTiers = {
    starter: {
      name: 'Starter',
      monthlyPrice: 29,
      annualPrice: 290,
      features: [
        'Up to 5 users',
        'Basic video analysis',
        '10GB storage',
        '50 processing minutes',
        'Email support'
      ]
    },
    professional: {
      name: 'Professional',
      monthlyPrice: 99,
      annualPrice: 990,
      features: [
        'Up to 25 users',
        'Advanced tactical analysis',
        '100GB storage',
        '500 processing minutes',
        'Priority support',
        'API access',
        'Custom reports'
      ]
    },
    elite: {
      name: 'Elite',
      monthlyPrice: 299,
      annualPrice: 2990,
      features: [
        'Unlimited users',
        'All features',
        'Unlimited storage',
        'Unlimited processing',
        'Dedicated support',
        'Custom integrations',
        'White label options'
      ]
    }
  };

  useEffect(() => {
    loadSubscriptionData();
  }, []);

  const loadSubscriptionData = async () => {
    try {
      setLoading(true);
      
      const [subRes, usageRes, invoicesRes] = await Promise.all([
        fetch('/api/v1/subscriptions/current'),
        fetch('/api/v1/subscriptions/usage'),
        fetch('/api/v1/billing/invoices')
      ]);
      
      const [subData, usageData, invoicesData] = await Promise.all([
        subRes.json(),
        usageRes.json(),
        invoicesRes.json()
      ]);
      
      setSubscription(subData);
      setUsageMetrics(usageData);
      setInvoices(invoicesData);
      
    } catch (err) {
      console.error('Error loading subscription data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleUpgrade = async () => {
    try {
      const response = await fetch('/api/v1/subscriptions/upgrade', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subscription_id: subscription?.id,
          new_tier: selectedNewTier
        })
      });
      
      if (response.ok) {
        setUpgradeDialogOpen(false);
        loadSubscriptionData();
      }
    } catch (err) {
      console.error('Error upgrading subscription:', err);
    }
  };

  const handleCancel = async (cancelImmediately: boolean) => {
    try {
      const response = await fetch('/api/v1/subscriptions/cancel', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subscription_id: subscription?.id,
          cancel_immediately: cancelImmediately,
          cancellation_reason: 'User requested'
        })
      });
      
      if (response.ok) {
        setCancelDialogOpen(false);
        loadSubscriptionData();
      }
    } catch (err) {
      console.error('Error cancelling subscription:', err);
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'active': return 'success';
      case 'trial': return 'info';
      case 'paused': return 'warning';
      case 'cancelled': return 'error';
      default: return 'default';
    }
  };

  const getUsageColor = (percentage: number) => {
    if (percentage >= 90) return 'error';
    if (percentage >= 75) return 'warning';
    return 'success';
  };

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD'
    }).format(amount);
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="400px">
        <LinearProgress sx={{ width: '300px' }} />
      </Box>
    );
  }

  return (
    <Box sx={{ p: 3 }}>
      <Box display="flex" justifyContent="between" alignItems="center" mb={3}>
        <Typography variant="h4" component="h1">
          Subscription & Billing
        </Typography>
        <BillingIcon fontSize="large" color="primary" />
      </Box>

      {/* Current Subscription Overview */}
      <Grid container spacing={3} mb={4}>
        <Grid item xs={12} md={8}>
          <Card>
            <CardContent>
              <Box display="flex" justifyContent="between" alignItems="start" mb={3}>
                <Box>
                  <Typography variant="h5" gutterBottom>
                    {subscription && subscriptionTiers[subscription.tier]?.name} Plan
                  </Typography>
                  <Chip
                    label={subscription?.status?.toUpperCase()}
                    color={getStatusColor(subscription?.status || '') as any}
                    sx={{ mb: 2 }}
                  />
                  <Typography variant="body2" color="text.secondary">
                    {subscription?.billingCycle === 'annual' ? 'Billed Annually' : 'Billed Monthly'}
                  </Typography>
                </Box>
                <Box textAlign="right">
                  <Typography variant="h4" color="primary">
                    {subscription && formatCurrency(
                      subscription.billingCycle === 'annual' 
                        ? subscriptionTiers[subscription.tier]?.annualPrice / 12
                        : subscriptionTiers[subscription.tier]?.monthlyPrice
                    )}
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    per month
                  </Typography>
                </Box>
              </Box>

              <Box mb={3}>
                <Typography variant="subtitle2" gutterBottom>
                  Current Billing Period
                </Typography>
                <Typography variant="body2">
                  {subscription && new Date(subscription.currentPeriodStart).toLocaleDateString()} - {' '}
                  {subscription && new Date(subscription.currentPeriodEnd).toLocaleDateString()}
                </Typography>
                <LinearProgress
                  variant="determinate"
                  value={usageMetrics?.billingPeriodProgress || 0}
                  sx={{ mt: 1, height: 6, borderRadius: 3 }}
                />
                <Typography variant="caption" color="text.secondary">
                  {usageMetrics?.billingPeriodProgress.toFixed(0)}% through billing period
                </Typography>
              </Box>

              <Typography variant="subtitle2" gutterBottom>
                Plan Features:
              </Typography>
              <List dense>
                {subscription && subscriptionTiers[subscription.tier]?.features.map((feature, index) => (
                  <ListItem key={index} sx={{ py: 0 }}>
                    <ListItemIcon>
                      <CheckIcon color="success" fontSize="small" />
                    </ListItemIcon>
                    <ListItemText primary={feature} />
                  </ListItem>
                ))}
              </List>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Subscription Actions</Typography>
              
              <Box display="flex" flexDirection="column" gap={2}>
                <Button
                  variant="contained"
                  startIcon={<UpgradeIcon />}
                  onClick={() => setUpgradeDialogOpen(true)}
                  disabled={subscription?.tier === 'elite'}
                  fullWidth
                >
                  Upgrade Plan
                </Button>
                
                <Button
                  variant="outlined"
                  startIcon={<SettingsIcon />}
                  fullWidth
                >
                  Manage Payment Methods
                </Button>
                
                <Button
                  variant="outlined"
                  color="error"
                  startIcon={<CancelIcon />}
                  onClick={() => setCancelDialogOpen(true)}
                  fullWidth
                >
                  Cancel Subscription
                </Button>
              </Box>

              {subscription?.trialEnd && (
                <Alert severity="info" sx={{ mt: 2 }}>
                  Trial ends on {new Date(subscription.trialEnd).toLocaleDateString()}
                </Alert>
              )}

              {subscription?.cancelAt && (
                <Alert severity="warning" sx={{ mt: 2 }}>
                  Subscription will cancel on {new Date(subscription.cancelAt).toLocaleDateString()}
                </Alert>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Usage Metrics */}
      <Grid container spacing={3} mb={4}>
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Usage This Period</Typography>
              
              <Grid container spacing={3}>
                {usageMetrics && Object.entries(usageMetrics.usageSummary).map(([metric, details]) => (
                  <Grid item xs={12} sm={6} md={3} key={metric}>
                    <Box>
                      <Typography variant="subtitle2" gutterBottom>
                        {metric.replace('_', ' ').toUpperCase()}
                      </Typography>
                      
                      <Box display="flex" alignItems="center" mb={1}>
                        <Typography variant="h6">
                          {details.currentUsage.toFixed(1)}
                        </Typography>
                        <Typography variant="body2" color="text.secondary" sx={{ ml: 1 }}>
                          {details.limit === -1 ? '/ Unlimited' : `/ ${details.limit}`}
                        </Typography>
                      </Box>
                      
                      {details.limit !== -1 && (
                        <LinearProgress
                          variant="determinate"
                          value={details.percentageUsed}
                          color={getUsageColor(details.percentageUsed) as any}
                          sx={{ mb: 1 }}
                        />
                      )}
                      
                      <Typography variant="caption" color="text.secondary">
                        {details.percentageUsed.toFixed(0)}% used
                      </Typography>
                      
                      {details.overage > 0 && (
                        <Chip
                          size="small"
                          label={`Overage: ${formatCurrency(details.overageCost)}`}
                          color="warning"
                          sx={{ mt: 1 }}
                        />
                      )}
                      
                      {details.projectedOverageCost && details.projectedOverageCost > 0 && (
                        <Typography variant="caption" display="block" color="warning.main">
                          Projected overage: {formatCurrency(details.projectedOverageCost)}
                        </Typography>
                      )}
                    </Box>
                  </Grid>
                ))}
              </Grid>
              
              {usageMetrics && usageMetrics.totalOverageCost > 0 && (
                <Alert severity="warning" sx={{ mt: 2 }}>
                  <Box display="flex" justifyContent="between" alignItems="center">
                    <Typography>
                      Total overage charges this period: {formatCurrency(usageMetrics.totalOverageCost)}
                    </Typography>
                    <Button size="small" variant="outlined">
                      View Details
                    </Button>
                  </Box>
                </Alert>
              )}
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Recent Invoices */}
      <Card>
        <CardContent>
          <Box display="flex" justifyContent="between" alignItems="center" mb={3}>
            <Typography variant="h6">Recent Invoices</Typography>
            <Button startIcon={<InvoiceIcon />} variant="outlined">
              View All Invoices
            </Button>
          </Box>
          
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Invoice #</TableCell>
                  <TableCell>Date</TableCell>
                  <TableCell>Amount</TableCell>
                  <TableCell>Status</TableCell>
                  <TableCell>Due Date</TableCell>
                  <TableCell align="right">Actions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {invoices.slice(0, 5).map((invoice) => (
                  <TableRow key={invoice.id}>
                    <TableCell>{invoice.invoiceNumber}</TableCell>
                    <TableCell>
                      {new Date(invoice.createdAt).toLocaleDateString()}
                    </TableCell>
                    <TableCell>{formatCurrency(invoice.amountDue)}</TableCell>
                    <TableCell>
                      <Chip
                        size="small"
                        label={invoice.status.toUpperCase()}
                        color={invoice.status === 'paid' ? 'success' : invoice.status === 'open' ? 'warning' : 'default'}
                      />
                    </TableCell>
                    <TableCell>
                      {new Date(invoice.dueDate).toLocaleDateString()}
                    </TableCell>
                    <TableCell align="right">
                      <Tooltip title="Download Invoice">
                        <IconButton size="small">
                          <DownloadIcon />
                        </IconButton>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </CardContent>
      </Card>

      {/* Upgrade Dialog */}
      <Dialog open={upgradeDialogOpen} onClose={() => setUpgradeDialogOpen(false)} maxWidth="md" fullWidth>
        <DialogTitle>Upgrade Your Subscription</DialogTitle>
        <DialogContent>
          <Grid container spacing={2}>
            {Object.entries(subscriptionTiers).map(([key, tier]) => (
              subscription?.tier !== key && (
                <Grid item xs={12} md={4} key={key}>
                  <Card 
                    variant={selectedNewTier === key ? "outlined" : "elevation"}
                    sx={{ 
                      cursor: 'pointer',
                      border: selectedNewTier === key ? '2px solid primary.main' : 'none'
                    }}
                    onClick={() => setSelectedNewTier(key)}
                  >
                    <CardContent>
                      <Typography variant="h6" gutterBottom>{tier.name}</Typography>
                      <Typography variant="h4" color="primary" gutterBottom>
                        {formatCurrency(tier.monthlyPrice)}
                        <Typography variant="body2" component="span">
                          /month
                        </Typography>
                      </Typography>
                      <List dense>
                        {tier.features.slice(0, 4).map((feature, index) => (
                          <ListItem key={index} sx={{ py: 0, px: 0 }}>
                            <ListItemIcon sx={{ minWidth: 24 }}>
                              <CheckIcon fontSize="small" color="success" />
                            </ListItemIcon>
                            <ListItemText 
                              primary={feature} 
                              primaryTypographyProps={{ variant: 'body2' }}
                            />
                          </ListItem>
                        ))}
                      </List>
                    </CardContent>
                  </Card>
                </Grid>
              )
            ))}
          </Grid>
          
          {selectedNewTier && (
            <Alert severity="info" sx={{ mt: 2 }}>
              You'll be charged a prorated amount for the remainder of your current billing period.
              Your new features will be available immediately.
            </Alert>
          )}
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setUpgradeDialogOpen(false)}>Cancel</Button>
          <Button 
            onClick={handleUpgrade} 
            variant="contained"
            disabled={!selectedNewTier}
          >
            Upgrade Now
          </Button>
        </DialogActions>
      </Dialog>

      {/* Cancel Dialog */}
      <Dialog open={cancelDialogOpen} onClose={() => setCancelDialogOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Cancel Subscription</DialogTitle>
        <DialogContent>
          <Typography variant="body1" paragraph>
            We're sorry to see you go! Are you sure you want to cancel your subscription?
          </Typography>
          
          <Alert severity="warning" sx={{ mb: 2 }}>
            Canceling will remove access to all premium features and your analysis history.
          </Alert>
          
          <Typography variant="subtitle2" gutterBottom>
            Cancellation Options:
          </Typography>
          
          <List>
            <ListItem>
              <ListItemText
                primary="Cancel at period end"
                secondary="Keep access until your current billing period ends"
              />
            </ListItem>
            <ListItem>
              <ListItemText
                primary="Cancel immediately"
                secondary="Lose access now but receive a prorated refund"
              />
            </ListItem>
          </List>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setCancelDialogOpen(false)}>Keep Subscription</Button>
          <Button 
            onClick={() => handleCancel(false)} 
            color="warning"
          >
            Cancel at Period End
          </Button>
          <Button 
            onClick={() => handleCancel(true)} 
            color="error"
          >
            Cancel Immediately
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};
```

## Performance Considerations

- **Real-time Usage Tracking**: Efficient metering with minimal performance impact
- **Billing Calculations**: Optimized proration and tax calculations
- **Payment Processing**: Fast and reliable payment handling with retry logic
- **Invoice Generation**: Efficient PDF generation and email delivery
- **Usage Analytics**: Quick aggregation of usage data for dashboards
- **Subscription Changes**: Immediate feature access updates

## Security

- **Payment Security**: PCI DSS compliance with Stripe integration
- **Data Protection**: Secure handling of billing and payment information
- **Access Control**: Role-based access to subscription and billing data
- **Audit Logging**: Comprehensive logging of all billing activities
- **Fraud Prevention**: Advanced fraud detection and prevention measures
- **API Security**: Secure endpoints with authentication and rate limiting

## Testing

- **Payment Testing**: Comprehensive testing with Stripe test mode
- **Billing Accuracy**: Validation of all billing calculations and prorations
- **Usage Tracking**: Accuracy testing of usage metering and aggregation
- **Integration Testing**: End-to-end testing of subscription workflows
- **Security Testing**: Penetration testing of payment and billing systems
- **Load Testing**: Performance testing under high transaction volumes

## Monitoring

- **Payment Success**: Monitoring of payment success rates and failures
- **Billing Accuracy**: Tracking of billing errors and corrections
- **Usage Metrics**: Real-time monitoring of customer usage patterns
- **Subscription Health**: Monitoring of churn rates and retention metrics
- **Revenue Tracking**: Comprehensive revenue analytics and reporting
- **Customer Satisfaction**: Tracking of billing-related support tickets

## Definition of Done

- [ ] Three-tier subscription system operational with feature differentiation
- [ ] Flexible billing system implemented with multiple payment methods
- [ ] Usage-based billing operational with real-time tracking
- [ ] Subscription lifecycle management implemented with prorated billing
- [ ] Team member management operational with per-user pricing
- [ ] Professional invoice generation and delivery implemented
- [ ] Usage monitoring and cost alerts operational
- [ ] Cancellation and refund processing implemented
- [ ] Stripe integration completed with PCI compliance
- [ ] Analytics dashboard operational for subscription metrics
- [ ] Security measures implemented with audit logging
- [ ] Testing completed with payment and billing validation
- [ ] Documentation completed with billing policies and procedures
- [ ] Customer support integration completed for billing inquiries

## Dependencies

- **Story 4.1**: User management for subscription assignment
- **Infrastructure**: Stripe, email services, PDF generation, accounting systems

## Risks

- **Payment Failures**: Risk of payment processing issues affecting revenue
- **Billing Complexity**: Complex usage calculations affecting accuracy
- **Compliance Requirements**: PCI DSS and financial regulations compliance challenges
- **Customer Churn**: Risk of cancellations due to billing issues
- **Integration Dependencies**: Reliance on third-party payment providers

## Change Log

| Date | Author | Changes | Reason |
|------|--------|---------|---------|
| 2024-03-15 | System | Initial story creation | Epic 6 development |
| 2024-03-15 | System | Added comprehensive subscription tiers | Market positioning requirements |
| 2024-03-15 | System | Added Stripe integration | Professional payment processing |
| 2024-03-15 | System | Added usage-based billing | Flexible pricing model |