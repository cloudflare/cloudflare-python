# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .audit_log import AuditLog
from .response_info import ResponseInfo

__all__ = ["Result", "UnionMember0", "AaaAPIResponseCommon"]


class UnionMember0(BaseModel):
    errors: Optional[object] = None

    messages: Optional[List[object]] = None

    result: Optional[List[AuditLog]] = None

    success: Optional[bool] = None


class AaaAPIResponseCommon(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: Union[List[object], str, object]

    success: Literal[True]
    """Whether the API call was successful"""


Result = Union[UnionMember0, AaaAPIResponseCommon]
