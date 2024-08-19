# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RequestConstants"]


class RequestConstants(BaseModel):
    priority: Optional[List[Literal["routine", "high", "urgent"]]] = None

    status: Optional[List[Literal["open", "accepted", "reported", "approved", "completed", "declined"]]] = None

    tlp: Optional[List[Literal["clear", "amber", "amber-strict", "green", "red"]]] = None
