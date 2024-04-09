# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .dns import DNS
from ..shared import ResponseInfo
from ..._models import BaseModel

__all__ = ["DNSListResponse"]


class DNSListResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: DNS

    success: Literal[True]
    """Whether the API call was successful"""
