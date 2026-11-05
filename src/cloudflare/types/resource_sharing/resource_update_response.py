# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ResourceUpdateResponse"]


class ResourceUpdateResponse(BaseModel):
    id: str
    """Share Resource identifier."""

    created: datetime
    """When the object was created."""

    meta: object
    """Resource Metadata."""

    modified: datetime
    """When the object was last modified."""

    resource_account_id: str
    """Account identifier."""

    resource_id: str
    """Identifier assigned by the service that owns the shared resource."""

    resource_type: Literal[
        "custom-ruleset",
        "gateway-policy",
        "gateway-destination-ip",
        "gateway-block-page-settings",
        "gateway-extended-email-matching",
        "idp-federation-grant",
        "trust-grant",
    ]
    """Resource Type."""

    resource_version: int
    """Resource Version."""

    status: Literal["active", "deleting", "deleted"]
    """Resource Status."""
