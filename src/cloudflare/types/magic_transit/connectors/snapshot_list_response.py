# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["SnapshotListResponse", "Item"]


class Item(BaseModel):
    a: float
    """Time the Snapshot was collected (seconds since the Unix epoch)"""

    t: float
    """Time the Snapshot was recorded (seconds since the Unix epoch)"""


class SnapshotListResponse(BaseModel):
    count: float

    items: List[Item]

    cursor: Optional[str] = None
