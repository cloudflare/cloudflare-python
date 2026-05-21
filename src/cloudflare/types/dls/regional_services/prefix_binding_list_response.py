# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["PrefixBindingListResponse"]


class PrefixBindingListResponse(BaseModel):
    id: str
    """The ID of the binding."""

    cidr: str
    """The CIDR that is bound."""

    prefix_id: str
    """The ID of the parent prefix."""

    region_key: str
    """The region key used for the binding."""
