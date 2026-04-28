# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["MoveBulkResponse"]


class MoveBulkResponse(BaseModel):
    success: bool
    """Whether the operation succeeded"""

    completed_at: Optional[datetime] = None
    """When the move operation completed (UTC)"""

    completed_timestamp: Optional[datetime] = None
    """Deprecated, use `completed_at` instead. End of life: November 1, 2026."""

    destination: Optional[str] = None
    """Destination folder for the message"""

    item_count: Optional[int] = None
    """Number of items moved. End of life: November 1, 2026."""

    message_id: Optional[str] = None
    """Message identifier"""

    operation: Optional[str] = None
    """Type of operation performed"""

    recipient: Optional[str] = None
    """Recipient email address"""

    status: Optional[str] = None
    """Operation status"""
