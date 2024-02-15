# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "PackageGetResponse",
    "LegacyJhsAPIResponseSingle",
    "LegacyJhsAPIResponseSingleError",
    "LegacyJhsAPIResponseSingleMessage",
    "Result",
]


class LegacyJhsAPIResponseSingleError(BaseModel):
    code: int

    message: str


class LegacyJhsAPIResponseSingleMessage(BaseModel):
    code: int

    message: str


class LegacyJhsAPIResponseSingle(BaseModel):
    errors: List[LegacyJhsAPIResponseSingleError]

    messages: List[LegacyJhsAPIResponseSingleMessage]

    result: Union[object, str, None] = None

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse = Union[LegacyJhsAPIResponseSingle, Result]
