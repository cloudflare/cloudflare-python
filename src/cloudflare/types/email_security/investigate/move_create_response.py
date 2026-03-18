# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["MoveCreateResponse"]


class MoveCreateResponse(BaseModel):
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
