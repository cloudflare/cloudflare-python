# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .bucket import Bucket
from ..._models import BaseModel

__all__ = ["BucketListResponse"]


class BucketListResponse(BaseModel):
    buckets: List[Bucket]
