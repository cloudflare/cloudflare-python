# File generated from our OpenAPI spec by Stainless.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["URLScannerScanResponse", "Task"]


class Task(BaseModel):
    success: bool
    """Whether scan was successful or not"""

    time: datetime
    """When scan was submitted (UTC)"""

    url: str
    """Scan url (after redirects)"""

    uuid: str
    """Scan id"""


class URLScannerScanResponse(BaseModel):
    tasks: List[Task]
