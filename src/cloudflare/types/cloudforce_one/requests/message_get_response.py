# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

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
    """Whether the message is a follow-on request"""

    updated: datetime
    """Message last updated time"""

    created: Optional[datetime] = None
    """Message creation time"""


MessageGetResponse: TypeAlias = List[MessageGetResponseItem]
