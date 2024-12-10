# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["HostListResponse"]


class HostListResponse(BaseModel):
    created_at: datetime

    hosts: List[str]
    """Hosts serving the schema, e.g zone.host.com"""

    name: str
    """Name of the schema"""

    schema_id: str
    """UUID"""
