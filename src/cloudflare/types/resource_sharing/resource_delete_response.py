# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceDeleteResponse"]


class ResourceDeleteResponse(BaseModel):
    id: str
    """Share Resource identifier."""

    created: datetime
    """When the share was created."""

    meta: object
    """Resource Metadata."""

    modified: datetime
    """When the share was modified."""

    resource_account_id: str
    """Account identifier."""

    resource_id: str
    """Share Resource identifier."""

    resource_type: Literal["custom-ruleset", "widget"]
    """Resource Type."""

    resource_version: int
    """Resource Version."""

    status: Literal["active", "deleting", "deleted"]
    """Resource Status."""
