# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["EventListResponse", "Item"]


class Item(BaseModel):
    a: float
    """Time the Event was collected (seconds since the Unix epoch)"""

    k: str
    """Kind"""

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""


class EventListResponse(BaseModel):
    count: float

    items: List[Item]

    cursor: Optional[str] = None
