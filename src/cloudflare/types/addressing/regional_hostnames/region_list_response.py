# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["RegionListResponse"]


class RegionListResponse(BaseModel):
    key: Optional[str] = None
    """Identifying key for the region"""

    label: Optional[str] = None
    """Human-readable text label for the region"""
