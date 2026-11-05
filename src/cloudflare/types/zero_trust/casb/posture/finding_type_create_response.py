# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["FindingTypeCreateResponse", "Category"]


class Category(BaseModel):
    """Category information for a finding."""

    observation: Literal["Issue", "Insight", "Activity"]
    """The type of the observation."""

    product: Literal["SaaS", "Cloud"]
    """The product category."""

    type: Literal["Content", "Posture"]
    """The type of the finding category."""


class FindingTypeCreateResponse(BaseModel):
    """Basic finding type information."""

    id: str
    """The unique identifier of the finding."""

    applies_to_all_integrations: bool
    """
    Whether this finding type applies to every current and future integration of the
    vendor.
    """

    asset_class: str
    """Asset class the finding type's policy evaluates."""

    asset_vendor: Literal[
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
    """Canonical vendor enum value."""

    category: Category
    """Category information for a finding."""

    created_at: datetime
    """Timestamp when the finding type was created."""

    description: Optional[str] = None
    """Detailed description of the finding."""

    expression: str
    """Rego expression backing this finding type.

    For custom finding types, generated package and import declarations are omitted.
    System expressions are returned unchanged.
    """

    name: str
    """The name of the finding."""

    origin: Literal["system", "custom"]
    """Whether the finding type is system-managed or customer-created."""

    severity: Literal["Critical", "High", "Medium", "Low"]
    """Default severity used when no integration-specific severity override exists."""

    updated_at: datetime
    """Timestamp when the finding type was last updated."""

    vendor: str
    """The SaaS/Cloud vendor of the platform with which the finding is associated."""

    version: int
    """Current version of the finding type. Incremented on each update."""

    integration_ids: Optional[List[str]] = None
    """
    Integrations this finding type applies to when applies_to_all_integrations is
    false.
    """

    match_count: Optional[int] = None
    """Number of currently active finding instances across the account's integrations.

    Zero when none have been detected.
    """

    quarantined: Optional[bool] = None
    """Whether evaluation of this finding type is suspended by an operator.

    Present only when true.
    """
