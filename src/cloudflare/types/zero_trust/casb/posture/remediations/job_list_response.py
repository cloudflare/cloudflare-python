# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["JobListResponse", "Asset", "AssetCategory", "AssetField"]


class AssetCategory(BaseModel):
    """Category information for a remediation job asset."""

    service: str
    """Specific service within the vendor."""

    type: str
    """Asset type."""

    vendor: Literal[
        "AWS",
        "Anthropic",
        "Bitbucket",
        "Box",
        "Confluence",
        "Dropbox",
        "GitHub",
        "Google Cloud Platform",
        "Google Workspace",
        "Jira",
        "Microsoft",
        "Microsoft Internal",
        "Okta",
        "OpenAI",
        "Slack",
        "Salesforce",
        "ServiceNow",
        "Workday",
        "Zoom",
    ]
    """Display names for vendor types."""


class AssetField(BaseModel):
    """Additional field information for a remediation job asset."""

    name: str
    """Field name."""

    value: Union[str, float, bool]
    """Field value (can be string, number, or boolean)."""

    link: Optional[str] = None
    """Optional link associated with the field."""


class Asset(BaseModel):
    """Asset information for a remediation job."""

    id: str
    """Unique identifier for the asset."""

    category: AssetCategory
    """Category information for a remediation job asset."""

    external_id: str
    """External identifier from the source system."""

    fields: List[AssetField]
    """Additional fields associated with the asset."""

    name: str
    """Human-readable name of the asset."""

    link: Optional[str] = None
    """Direct link to the asset."""


class JobListResponse(BaseModel):
    """Information about a remediation job."""

    id: str
    """Unique identifier for the remediation job."""

    asset: Asset
    """Asset information for a remediation job."""

    created_at: datetime
    """When the remediation job was created."""

    finding_id: str
    """Encoded finding ID."""

    finding_instance_id: str
    """ID of the finding instance being remediated."""

    finding_type_id: str
    """ID of the finding type."""

    finding_type_name: str
    """Name of the finding type."""

    integration_name: str
    """Name of the integration."""

    last_updated: datetime
    """When the remediation job was last updated."""

    remediation_type: str
    """Type of remediation being performed."""

    status: Literal["pending", "processing", "completed", "failed", "validating"]
    """Status of a remediation job."""

    triggered_by_user: str
    """Email of the user who triggered the remediation.

    For account-token actors this is the literal "Account API Token"; for policy
    actors this is empty.
    """

    triggered_by_actor: Optional[Literal["user", "account_token"]] = None
    """Type of actor that triggered the remediation job.

    Null on legacy rows created before this column was populated.
    """

    triggered_by_id: Optional[str] = None
    """ID of the actor that triggered the job.

    Meaning depends on triggered_by_actor. Null on legacy rows.
    """
