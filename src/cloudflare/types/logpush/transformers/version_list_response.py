# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["VersionListResponse"]


class VersionListResponse(BaseModel):
    id: Optional[int] = None
    """Unique identifier for this version."""

    created_at: Optional[datetime] = None
    """When this version was created (RFC 3339)."""

    version: Optional[int] = None
    """Sequential version number."""
