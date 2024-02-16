# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["BucketListResponse", "BucketListResponseItem"]


class BucketListResponseItem(BaseModel):
    creation_date: Optional[str] = None
    """Creation timestamp"""

    location: Optional[Literal["apac", "eeur", "enam", "weur", "wnam"]] = None
    """Location of the bucket"""

    name: Optional[str] = None
    """Name of the bucket"""


BucketListResponse = List[BucketListResponseItem]
