# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["FindingTypeListResponse", "Category"]


class Category(BaseModel):
    """Category information for a finding."""

    observation: Literal["Issue", "Insight", "Activity"]
    """The type of the observation."""

    product: Literal["SaaS", "Cloud"]
    """The product category."""

    type: Literal["Content", "Posture"]
    """The type of the finding category."""


class FindingTypeListResponse(BaseModel):
    """Basic finding type information."""

    id: str
    """The unique identifier of the finding."""

    category: Category
    """Category information for a finding."""

    name: str
    """The name of the finding."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """Default severity used when no integration-specific severity override exists."""

    vendor: str
    """The SaaS/Cloud vendor of the platform with which the finding is associated."""

    applies_to_all_integrations: Optional[bool] = None
    """
    Whether this finding type applies to every current and future integration of the
    vendor.
    """

    asset_class: Optional[str] = None
    """Asset class the finding type's policy evaluates."""

    asset_vendor: Optional[
        Literal[
            "ANTHROPIC",
            "AWS",
            "BITBUCKET",
            "BOX",
            "CONFLUENCE",
            "DROPBOX",
            "GITHUB",
            "GOOGLE_CLOUD_PLATFORM",
            "GOOGLE_WORKSPACE",
            "JIRA",
            "MICROSOFT",
            "OPENAI",
            "SALESFORCE",
            "SERVICENOW",
            "SLACK",
            "ZOOM",
        ]
    ] = None
    """Canonical vendor enum value."""

    created_at: Optional[datetime] = None
    """Timestamp when the finding type was created."""

    description: Optional[str] = None
    """Detailed description of the finding."""

    expression: Optional[str] = None
    """Rego expression backing this finding type.

    For custom finding types, generated package and import declarations are omitted.
    System expressions are returned unchanged.
    """

    integration_ids: Optional[List[str]] = None
    """
    Integrations this finding type applies to when applies_to_all_integrations is
    false.
    """

    match_count: Optional[int] = None
    """Number of currently active finding instances across the account's integrations.

    Zero when none have been detected.
    """

    origin: Optional[Literal["system", "custom"]] = None
    """Whether the finding type is system-managed or customer-created."""

    quarantined: Optional[bool] = None
    """Whether evaluation of this finding type is suspended by an operator.

    Present only when true.
    """

    updated_at: Optional[datetime] = None
    """Timestamp when the finding type was last updated."""

    version: Optional[int] = None
    """Current version of the finding type. Incremented on each update."""
