# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "FindingResetSeverityResponse",
    "Finding",
    "FindingCategory",
    "FindingRemediation",
    "Integration",
    "IntegrationPolicy",
    "IntegrationVendor",
    "IntegrationZtEnrollment",
    "SeverityOverride",
]


class FindingCategory(BaseModel):
    """Category information for a finding."""

    observation: Literal["Issue", "Insight", "Activity"]
    """The type of the observation."""

    product: Literal["SaaS", "Cloud"]
    """The product category."""

    type: Literal["Content", "Posture"]
    """The type of the finding category."""


class FindingRemediation(BaseModel):
    """Remediation guide information for a finding."""

    id: str
    """Remediation Id."""

    frameworks: List[str]
    """Relevant Compliance Frameworks."""

    guide: str
    """Remediation guide text."""

    impact: str
    """Description of the potential impact."""

    locale: str
    """I18N Locale."""

    threat: str
    """Description of the threat."""


class Finding(BaseModel):
    """Basic finding type information."""

    id: str
    """The unique identifier of the finding."""

    category: FindingCategory
    """Category information for a finding."""

    name: str
    """The name of the finding."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """The severity level of a finding."""

    vendor: str
    """The SaaS/Cloud vendor of the platform with which the finding is associated."""

    description: Optional[str] = None
    """Detailed description of the finding."""

    remediation: Optional[FindingRemediation] = None
    """Remediation guide information for a finding."""


class IntegrationPolicy(BaseModel):
    """Policy configuration for an integration."""

    id: Optional[str] = None
    """Policy identifier."""

    client_id: Optional[str] = None
    """OAuth client ID for the policy."""

    compliance_level: Optional[str] = None
    """Compliance level for the policy."""

    dlp_enabled: Optional[bool] = None
    """Whether DLP is enabled for this policy."""

    link: Optional[str] = None
    """Link to policy documentation."""

    name: Optional[str] = None
    """Policy name."""

    permissions: Optional[List[str]] = None
    """List of permissions included in the policy."""


class IntegrationVendor(BaseModel):
    """Information about a vendor/service provider."""

    id: str
    """The id of the vendor."""

    description: Optional[str] = None
    """Detailed information about what kinds of issues are detected for this vendor."""

    display_name: str
    """The display name of the vendor."""

    logo: str
    """Logo URL for the vendor."""

    name: str
    """The name of the vendor."""

    static_logo: str
    """Static logo URL for the vendor."""

    zt_enrollments: List[str]
    """The vendor's compatible Zero Trust products."""

    policies: Optional[List[Dict[str, object]]] = None
    """The policies related to the vendor."""


class IntegrationZtEnrollment(BaseModel):
    """Information about a Zero Trust product integration."""

    id: Optional[str] = None
    """The internal identifier of the Zero Trust Product."""

    description: Optional[str] = None
    """Brief description of the Zero Trust Product."""

    display_name: Optional[str] = None
    """The verbose name of the Zero Trust Product."""

    enabled: Optional[bool] = None
    """
    Flag to enable/disable access to the listed integration from the corresponding
    Cloudflare product.
    """


class Integration(BaseModel):
    """Summary information about an integration."""

    created: datetime
    """When entity was created."""

    last_hydrated: datetime
    """When were the integration credentials last updated."""

    name: str
    """Name of the integration."""

    permissions: List[str]
    """The vendor-specific permissions associated with the integration."""

    policy: IntegrationPolicy
    """Policy configuration for an integration."""

    status: str
    """Current status of the integration."""

    updated: datetime
    """Last entity was updated."""

    upgradable: bool
    """Whether the integrations permissions can be updated."""

    vendor: IntegrationVendor
    """Information about a vendor/service provider."""

    zt_enrollments: List[IntegrationZtEnrollment]
    """Zero Trust products associated with this integration."""

    id: Optional[str] = None
    """Integration ID."""

    credential_health_status: Optional[Literal["Initializing", "Healthy", "Unhealthy"]] = None
    """Health status of integration credentials."""

    credentials_expiry: Optional[datetime] = None
    """The date and time when the integration credentials will expire."""

    is_paused: Optional[bool] = None
    """Whether the given integration is paused by the user."""

    upgrade_dismissed: Optional[bool] = None
    """UI State as to whether a potential permissions upgrade has been dismissed."""


class SeverityOverride(BaseModel):
    """Override information for finding severity."""

    created_by: str
    """User ID who created the override."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """The severity level of a finding."""


class FindingResetSeverityResponse(BaseModel):
    """Aggregated finding information with counts and metadata.

    This is optimized for list API queries and represents a finding along with its instance statistics.
    """

    id: str
    """Base64 encoded identifier of the security finding."""

    active_count: int
    """Number of active problematic instances identified in the security finding."""

    archived_count: int
    """Number of archived instances identified in the security finding."""

    finding: Finding
    """Basic finding type information."""

    ignored: bool
    """Determines if finding is currently ignored."""

    instance_count: int
    """
    Number of total (Active or archived) problematic instances identified in the
    security finding.
    """

    integration: Integration
    """Summary information about an integration."""

    latest_affliction_date: datetime
    """Timestamp of the latest affliction date of an active finding."""

    severity_override: Optional[SeverityOverride] = None
    """Override information for finding severity."""
