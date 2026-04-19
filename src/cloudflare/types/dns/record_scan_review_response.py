# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .record_response import RecordResponse

__all__ = ["RecordScanReviewResponse"]


class RecordScanReviewResponse(BaseModel):
    accepts: Optional[List[RecordResponse]] = None

    rejects: Optional[List[str]] = None
