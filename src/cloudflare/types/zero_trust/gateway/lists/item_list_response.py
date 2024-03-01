# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["ItemListResponse", "ItemListResponseItem"]


class ItemListResponseItem(BaseModel):
    created_at: Optional[datetime] = None

    value: Optional[str] = None
    """The value of the item in a list."""


ItemListResponse = List[List[ItemListResponseItem]]
