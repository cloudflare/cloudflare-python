# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import List

from .label import Label

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Priority"]

class Priority(BaseModel):
    id: str
    """UUID"""

    created: datetime
    """Priority creation time"""

    labels: List[Label]
    """List of labels"""

    priority: int
    """Priority"""

    requirement: str
    """Requirement"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""

    updated: datetime
    """Priority last updated time"""