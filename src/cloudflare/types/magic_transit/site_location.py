# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SiteLocation"]


class SiteLocation(BaseModel):
    lat: Optional[str] = None
    """Latitude"""

    lon: Optional[str] = None
    """Longitude"""
