# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["URLScannerScanResponse", "Task"]


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


class URLScannerScanResponse(BaseModel):
    tasks: List[Task]
