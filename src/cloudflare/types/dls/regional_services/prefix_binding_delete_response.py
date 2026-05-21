# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.response_info import ResponseInfo

__all__ = ["PrefixBindingDeleteResponse"]


class PrefixBindingDeleteResponse(BaseModel):
    messages: List[ResponseInfo]

    success: bool

    errors: Optional[List[ResponseInfo]] = None
