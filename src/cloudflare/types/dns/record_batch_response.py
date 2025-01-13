# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .record_response import RecordResponse

__all__ = ["RecordBatchResponse"]


class RecordBatchResponse(BaseModel):
    deletes: Optional[List[RecordResponse]] = None

    patches: Optional[List[RecordResponse]] = None

    posts: Optional[List[RecordResponse]] = None

    puts: Optional[List[RecordResponse]] = None
