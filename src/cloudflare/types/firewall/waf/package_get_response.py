# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "PackageGetResponse",
    "FirewallAPIResponseSingle",
    "FirewallAPIResponseSingleError",
    "FirewallAPIResponseSingleMessage",
    "Result",
]


class FirewallAPIResponseSingleError(BaseModel):
    code: int

    message: str


class FirewallAPIResponseSingleMessage(BaseModel):
    code: int

    message: str


class FirewallAPIResponseSingle(BaseModel):
    errors: List[FirewallAPIResponseSingleError]

    messages: List[FirewallAPIResponseSingleMessage]

    result: Union[Optional[str], Optional[object]]

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse: TypeAlias = Union[FirewallAPIResponseSingle, Result]
