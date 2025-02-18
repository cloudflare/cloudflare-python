# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SearchListResponse", "Resource"]


class Resource(BaseModel):
    reference_type: Optional[Literal["referral", "referrer"]] = None
    """When listed as a reference, the type (direction) of the reference."""

    references: Optional[List[object]] = None
    """A list of references to (referrer) or from (referral) this resource."""

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None
    """The human-identifiable name of the resource."""

    resource_type: Optional[Literal["load_balancer", "monitor", "pool"]] = None
    """The type of the resource."""


class SearchListResponse(BaseModel):
    resources: Optional[List[Resource]] = None
    """A list of resources matching the search query."""
