# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ListItem"]


class ListItem(BaseModel):
    id: str
    """UUID"""

    created: datetime
    """Request creation time"""

    priority: Literal["routine", "high", "urgent"]

    request: str
    """Requested information from request"""

    summary: str
    """Brief description of the request"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""

    updated: datetime
    """Request last updated time"""

    completed: Optional[datetime] = None
    """Request completion time"""

    message_tokens: Optional[int] = None
    """Tokens for the request messages"""

    readable_id: Optional[str] = None
    """Readable Request ID"""

    status: Optional[Literal["open", "accepted", "reported", "approved", "completed", "declined"]] = None
    """Request Status"""

    tokens: Optional[int] = None
    """Tokens for the request"""
