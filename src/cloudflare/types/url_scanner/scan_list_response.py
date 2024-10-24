# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ScanListResponse", "Task"]


class Task(BaseModel):
    country: str
    """Alpha-2 country code"""

    success: bool
    """Whether scan was successful or not"""

    time: datetime
    """When scan was submitted (UTC)"""

    url: str
    """Scan url (after redirects)"""

    uuid: str
    """Scan id"""

    visibility: str
    """Visibility status."""


class ScanListResponse(BaseModel):
    tasks: List[Task]
