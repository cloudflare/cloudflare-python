# File generated from our OpenAPI spec by Stainless.

from datetime import datetime

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

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
