# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ItemZeroTrustListsZeroTrustListItemsResponse", "ItemZeroTrustListsZeroTrustListItemsResponseItem"]


class ItemZeroTrustListsZeroTrustListItemsResponseItem(BaseModel):
    created_at: Optional[datetime] = None

    value: Optional[str] = None
    """The value of the item in a list."""


ItemZeroTrustListsZeroTrustListItemsResponse = List[List[ItemZeroTrustListsZeroTrustListItemsResponseItem]]
