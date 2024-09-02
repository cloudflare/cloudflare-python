# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .bucket import Bucket

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BucketListResponse"]


class BucketListResponse(BaseModel):
    buckets: Optional[List[Bucket]] = None
