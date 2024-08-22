# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Message"]

class Message(BaseModel):
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