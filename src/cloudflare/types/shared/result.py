# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .audit_log import AuditLog

__all__ = [
    "Result",
    "UnionMember0",
    "UnionMember0Error",
    "UnionMember0Message",
    "AaaAPIResponseCommon",
    "AaaAPIResponseCommonError",
    "AaaAPIResponseCommonMessage",
]


class UnionMember0Error(BaseModel):
    code: int

    message: str


class UnionMember0Message(BaseModel):
    code: int

    message: str


class UnionMember0(BaseModel):
    errors: Optional[List[UnionMember0Error]] = None

    messages: Optional[List[UnionMember0Message]] = None

    result: Optional[List[AuditLog]] = None

    success: Optional[bool] = None


class AaaAPIResponseCommonError(BaseModel):
    code: int

    message: str


class AaaAPIResponseCommonMessage(BaseModel):
    code: int

    message: str


class AaaAPIResponseCommon(BaseModel):
    errors: List[AaaAPIResponseCommonError]

    messages: List[AaaAPIResponseCommonMessage]

    success: Literal[True]
    """Whether the API call was successful"""


Result: TypeAlias = Union[UnionMember0, AaaAPIResponseCommon]
