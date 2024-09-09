# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .request_model import RequestModel

__all__ = ["ManagedHeaderListResponse"]


class ManagedHeaderListResponse(BaseModel):
    managed_request_headers: Optional[List[RequestModel]] = None

    managed_response_headers: Optional[List[RequestModel]] = None
