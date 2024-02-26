# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["MessageGetResponse", "MessageGetResponseItem"]


class MessageGetResponseItem(BaseModel):
    id: int
    """Message ID"""

    author: str
    """Author of message"""

    content: str
    """Content of message"""

    is_follow_on_request: bool
    """Message is a follow-on request"""

    updated: datetime
    """Message last updated time"""

    created: Optional[datetime] = None
    """Message creation time"""


MessageGetResponse = List[MessageGetResponseItem]
