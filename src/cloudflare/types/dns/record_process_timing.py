# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["RecordProcessTiming"]


class RecordProcessTiming(BaseModel):
    end_time: Optional[datetime] = None
    """When the file parsing ended."""

    process_time: Optional[float] = None
    """Processing time of the file in seconds."""

    start_time: Optional[datetime] = None
    """When the file parsing started."""
