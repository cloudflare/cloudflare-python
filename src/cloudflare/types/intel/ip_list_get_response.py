# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IPListGetResponse", "IPListGetResponseItem"]


class IPListGetResponseItem(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    name: Optional[str] = None


IPListGetResponse = List[IPListGetResponseItem]
