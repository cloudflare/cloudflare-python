# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .bucket import Bucket
from ..._models import BaseModel

__all__ = ["BucketListResponse"]


class BucketListResponse(BaseModel):
    buckets: Optional[List[Bucket]] = None
