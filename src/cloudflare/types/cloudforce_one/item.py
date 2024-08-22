# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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