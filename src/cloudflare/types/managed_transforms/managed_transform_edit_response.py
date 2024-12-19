# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "ManagedTransformEditResponse",
    "ManagedRequestHeader",
    "ManagedRequestHeaderConflictsWith",
    "ManagedResponseHeader",
    "ManagedResponseHeaderConflictsWith",
]


class ManagedRequestHeaderConflictsWith:
    pass


class ManagedRequestHeader(BaseModel):
    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[ManagedRequestHeaderConflictsWith]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class ManagedResponseHeaderConflictsWith:
    pass


class ManagedResponseHeader(BaseModel):
    id: str
    """The human-readable identifier of the Managed Transform."""

    enabled: bool
    """Whether the Managed Transform is enabled."""

    has_conflict: bool
    """
    Whether the Managed Transform conflicts with the currently-enabled Managed
    Transforms.
    """

    conflicts_with: Optional[List[ManagedResponseHeaderConflictsWith]] = None
    """The Managed Transforms that this Managed Transform conflicts with."""


class ManagedTransformEditResponse(BaseModel):
    managed_request_headers: List[ManagedRequestHeader]
    """The list of Managed Request Transforms."""

    managed_response_headers: List[ManagedResponseHeader]
    """The list of Managed Response Transforms."""
