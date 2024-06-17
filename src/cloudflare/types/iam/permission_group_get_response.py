# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PermissionGroupGetResponse"]


class PermissionGroupGetResponse(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[object] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""
