# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["MoveCreateResponse", "MoveCreateResponseItem"]


class MoveCreateResponseItem(BaseModel):
    completed_timestamp: datetime
    """Deprecated, use `completed_at` instead"""

    item_count: int

    success: bool

    completed_at: Optional[datetime] = None

    destination: Optional[str] = None

    message_id: Optional[str] = None

    operation: Optional[str] = None

    recipient: Optional[str] = None

    status: Optional[str] = None


MoveCreateResponse: TypeAlias = List[MoveCreateResponseItem]
