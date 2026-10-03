# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PermissionGroupGetResponse", "Meta"]


class Meta(BaseModel):
    """Attributes associated to the permission group."""

    category: Optional[str] = None
    """A category used to group permission groups."""

    deprecated: Optional[str] = None
    """Indicates whether the permission group is deprecated."""

    description: Optional[str] = None
    """Additional information about the permission group."""

    editable: Optional[str] = None
    """Indicates whether the permission group can be edited."""

    eol_at: Optional[datetime] = None
    """The planned end-of-life date and time, when provided."""

    label: Optional[str] = None
    """A label identifying the permission group."""

    scopes: Optional[str] = None
    """The scope associated with the permission group."""

    visibility: Optional[str] = None
    """Indicates the permission group's availability or visibility."""


class PermissionGroupGetResponse(BaseModel):
    """
    A named group of permissions that map to a group of operations against resources.
    """

    id: str
    """Identifier of the permission group."""

    meta: Optional[Meta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the permission group."""
