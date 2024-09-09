# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Item"]


class Item(BaseModel):
    id: str
    """UUID"""

    content: str
    """Request content"""

    created: datetime

    priority: datetime

    request: str
    """Requested information from request"""

    summary: str
    """Brief description of the request"""

    tlp: Literal["clear", "amber", "amber-strict", "green", "red"]
    """The CISA defined Traffic Light Protocol (TLP)"""

    updated: datetime

    completed: Optional[datetime] = None

    message_tokens: Optional[int] = None
    """Tokens for the request messages"""

    readable_id: Optional[str] = None
    """Readable Request ID"""

    status: Optional[Literal["open", "accepted", "reported", "approved", "completed", "declined"]] = None
    """Request Status"""

    tokens: Optional[int] = None
    """Tokens for the request"""
