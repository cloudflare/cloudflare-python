# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["ItemZeroTrustListsZeroTrustListItemsResponse", "ItemZeroTrustListsZeroTrustListItemsResponseItem"]


class ItemZeroTrustListsZeroTrustListItemsResponseItem(BaseModel):
    created_at: Optional[datetime] = None

    value: Optional[str] = None
    """The value of the item in a list."""


ItemZeroTrustListsZeroTrustListItemsResponse = List[List[ItemZeroTrustListsZeroTrustListItemsResponseItem]]
