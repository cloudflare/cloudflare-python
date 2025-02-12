# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PermissionGroupListResponse", "Meta"]


class Meta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PermissionGroupListResponse(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[Meta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""
