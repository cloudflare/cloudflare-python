# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ...shared import ResponseInfo
from ...._models import BaseModel

__all__ = ["PackageGetResponse", "LegacyJhsAPIResponseSingle", "Result"]


class LegacyJhsAPIResponseSingle(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    result: Union[str, object, None] = None

    success: Literal[True]
    """Whether the API call was successful"""


class Result(BaseModel):
    result: Optional[object] = None


PackageGetResponse = Union[LegacyJhsAPIResponseSingle, Result]
