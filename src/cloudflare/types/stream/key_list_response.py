# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["KeyListResponse", "KeyListResponseItem"]


class KeyListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""


KeyListResponse = List[KeyListResponseItem]
