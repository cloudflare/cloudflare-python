# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = [
    "InstanceListResponse",
    "Asset",
    "AssetCategory",
    "AssetField",
    "DLPContext",
    "Remediation",
    "Webhook",
    "WebhookLatestJob",
]


class AssetCategory(BaseModel):
    """Category information for an asset."""

    service: Optional[str] = None
    """The specific service within the vendor the asset is part of (often none).

    Example - AWS is the vendor, S3 is the service.
    """

    type: str
    """The type of asset."""

    vendor: str
    """The vendor the asset is part of."""

    id: Optional[str] = None
    """Unique identifier for the asset category."""


class AssetField(BaseModel):
    """Additional field information for an asset."""

    name: str
    """The name of the field."""

    value: str
    """The value of the field."""

    link: Optional[str] = None
    """Optional link associated with the field."""


class Asset(BaseModel):
    """Asset information including metadata and categorization."""

    category: AssetCategory
    """Category information for an asset."""

    external_id: str
    """External identifier from the source system."""

    fields: List[AssetField]
    """The fields associated with the asset."""

    name: str
    """Human-readable name of the asset."""

    id: Optional[str] = None
    """Unique identifier for the asset."""

    link: Optional[str] = None
    """Direct link to the asset."""


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


class Remediation(BaseModel):
    """Summary information about a remediation job."""

    id: str
    """Unique identifier for the remediation job."""

    created_at: datetime
    """When the remediation job was created."""

    stale: bool
    """
    Whether this remediation job is stale (created before the finding instance's
    affliction_date).
    """

    status: Literal["pending", "processing", "completed", "failed", "validating"]
    """Status of a remediation job."""


class WebhookLatestJob(BaseModel):
    """The most recent webhook job for this webhook configuration."""

    id: str
    """Unique identifier for the webhook job."""

    created_at: datetime
    """When the webhook job was created."""

    stale: bool
    """
    Whether this webhook job is stale (created before the finding instance's current
    affliction_date).
    """

    status: Literal["pending", "processing", "completed"]
    """Current status of the webhook job."""


class Webhook(BaseModel):
    """
    Summary of the most recent webhook job invocation for a specific webhook configuration.
    """

    latest_job: WebhookLatestJob
    """The most recent webhook job for this webhook configuration."""

    webhook_id: str
    """Unique identifier for the webhook configuration."""

    webhook_label: str
    """Account-specified display label for the webhook configuration."""


class InstanceListResponse(BaseModel):
    """A specific instance of a security finding.

    In the API interface, we refer to the 'finding' table in our DB as finding instances, optimized for the p99 use case.
    """

    affliction_date: datetime
    """When this specific instance was identified."""

    asset: Asset
    """Asset information including metadata and categorization."""

    dlp_contexts: List[DLPContext]
    """DLP context information if this is a content finding."""

    remediations: List[Remediation]
    """
    A list of the 10 most recent remediation jobs for this finding instance, ordered
    by creation time (most recent first). The 'stale' field indicates whether the
    remediation job was created before the finding instance's affliction_date (true)
    or after it (false). If there has never been a remediation job for this finding
    instance, this field will be an empty array.
    """

    webhooks: List[Webhook]
    """
    The most recent webhook job invocation for each webhook configuration associated
    with this finding instance. Each entry represents the latest job (any status)
    per webhook config. The 'stale' field indicates whether the job was invoked
    before the finding instance's current affliction_date. If no webhook jobs have
    been created, this field will be an empty array.
    """

    id: Optional[str] = None
    """Unique identifier for the finding instance."""

    is_archived: Optional[bool] = None
    """Whether this finding instance has been archived."""
