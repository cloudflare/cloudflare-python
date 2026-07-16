# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "ContentListResponse",
    "DLPContext",
    "Integration",
    "IntegrationPolicy",
    "IntegrationVendor",
    "IntegrationZtEnrollment",
]


class DLPContext(BaseModel):
    """DLP context information for a finding."""

    created: datetime
    """When the DLP context was created."""

    entry_ids: List[str]
    """DLP Entry IDs."""

    profile_id: str
    """DLP Profile ID."""

    updated: datetime
    """When the DLP context was last updated."""

    id: Optional[str] = None
    """Unique identifier for the DLP context."""

    deleted: Optional[datetime] = None
    """When the DLP context was deleted."""

    match_context_max_extent: Optional[int] = None
    """DLP Right Boundary of match context."""

    match_context_min_extent: Optional[int] = None
    """DLP Left Boundary of match context."""

    match_context_payload: Optional[Dict[str, object]] = None
    """DLP Match context payload that matched the profile in question."""


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


class ContentListResponse(BaseModel):
    """Content asset with DLP information."""

    asset_id: str
    """Unique identifier for the asset."""

    asset_name: str
    """Name of the asset."""

    dlp_contexts: List[DLPContext]
    """DLP context information for this asset."""

    dlp_profile_count: int
    """Number of DLP profiles that flagged this asset."""

    dlp_profile_ids: List[str]
    """IDs of DLP profiles that flagged this asset."""

    integration: Integration
    """Summary information about an integration."""

    latest_affliction_date: datetime
    """Most recent date this asset was flagged."""
