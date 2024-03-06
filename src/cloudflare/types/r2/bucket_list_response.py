# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BucketListResponse", "BucketListResponseItem"]


class BucketListResponseItem(BaseModel):
    creation_date: Optional[str] = None
    """Creation timestamp"""

    location: Optional[Literal["apac", "eeur", "enam", "weur", "wnam"]] = None
    """Location of the bucket"""

    name: Optional[str] = None
    """Name of the bucket"""


BucketListResponse = List[BucketListResponseItem]
