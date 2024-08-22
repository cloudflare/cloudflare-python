# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RequestConstants"]

class RequestConstants(BaseModel):
    priority: Optional[List[Literal["routine", "high", "urgent"]]] = None

    status: Optional[List[Literal["open", "accepted", "reported", "approved", "completed", "declined"]]] = None

    tlp: Optional[List[Literal["clear", "amber", "amber-strict", "green", "red"]]] = None