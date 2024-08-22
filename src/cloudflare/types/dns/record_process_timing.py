# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RecordProcessTiming"]

class RecordProcessTiming(BaseModel):
    end_time: Optional[datetime] = None
    """When the file parsing ended."""

    process_time: Optional[float] = None
    """Processing time of the file in seconds."""

    start_time: Optional[datetime] = None
    """When the file parsing started."""