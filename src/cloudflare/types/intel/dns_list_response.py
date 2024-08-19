# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .dns import DNS
from ..._models import BaseModel
from ..shared.response_info import ResponseInfo

__all__ = ["DNSListResponse"]


class DNSListResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[DNS] = None
