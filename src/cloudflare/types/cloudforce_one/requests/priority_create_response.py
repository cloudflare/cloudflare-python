# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PriorityCreateResponse"]


class PriorityCreateResponse(BaseModel):
    id: str
    """UUID"""

    created: datetime
    """Priority creation time"""

    labels: List[str]
    """List of labels"""

    priority: int
    """Priority"""

    requirement: str
    """Requirement"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""

    updated: datetime
    """Priority last updated time"""
