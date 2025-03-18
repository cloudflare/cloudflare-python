# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AssetGetResponse"]


class AssetGetResponse(BaseModel):
    id: int
    """Asset ID"""

    name: str
    """Asset name"""

    created: Optional[datetime] = None
    """Asset creation time"""

    description: Optional[str] = None
    """Asset description"""

    file_type: Optional[str] = None
    """Asset file type"""
