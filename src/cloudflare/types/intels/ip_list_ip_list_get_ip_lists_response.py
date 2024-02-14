# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IPListIPListGetIPListsResponse", "IPListIPListGetIPListsResponseItem"]


class IPListIPListGetIPListsResponseItem(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    name: Optional[str] = None


IPListIPListGetIPListsResponse = List[IPListIPListGetIPListsResponseItem]
