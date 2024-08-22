# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["TestStatOverTime", "Slot"]


class Slot(BaseModel):
    timestamp: str

    value: int


class TestStatOverTime(BaseModel):
    __test__ = False
    slots: List[Slot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""
