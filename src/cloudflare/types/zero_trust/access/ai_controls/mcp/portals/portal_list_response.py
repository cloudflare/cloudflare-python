# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ......._models import BaseModel

__all__ = ["PortalListResponse"]


class PortalListResponse(BaseModel):
    id: str
    """portal id"""

    hostname: str

    name: str

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None
