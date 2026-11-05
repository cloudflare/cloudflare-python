# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ......_models import BaseModel

__all__ = [
    "TagDeleteResponse",
    "WorkersTagsKVResponse",
    "WorkersTagsKVResponseError",
    "WorkersTagsKVResponseErrorSource",
    "WorkersTagsKVResponseMessage",
    "WorkersTagsKVResponseMessageSource",
    "WorkersAPIResponseNullResult",
    "WorkersAPIResponseNullResultError",
    "WorkersAPIResponseNullResultErrorSource",
    "WorkersAPIResponseNullResultMessage",
    "WorkersAPIResponseNullResultMessageSource",
]


class WorkersTagsKVResponseErrorSource(BaseModel):
    pointer: Optional[str] = None


class WorkersTagsKVResponseError(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[WorkersTagsKVResponseErrorSource] = None


class WorkersTagsKVResponseMessageSource(BaseModel):
    pointer: Optional[str] = None


class WorkersTagsKVResponseMessage(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[WorkersTagsKVResponseMessageSource] = None


class WorkersTagsKVResponse(BaseModel):
    errors: List[WorkersTagsKVResponseError]

    messages: List[WorkersTagsKVResponseMessage]

    result: Dict[str, str]
    """Tags associated with the Worker, as a key/value object.

    Each complete UTF-8 encoded tag (the key plus `=` and the value when the value
    is non-empty) must not exceed 1024 bytes.
    """

    success: Literal[True]
    """Whether the API call was successful."""


class WorkersAPIResponseNullResultErrorSource(BaseModel):
    pointer: Optional[str] = None


class WorkersAPIResponseNullResultError(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[WorkersAPIResponseNullResultErrorSource] = None


class WorkersAPIResponseNullResultMessageSource(BaseModel):
    pointer: Optional[str] = None


class WorkersAPIResponseNullResultMessage(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[WorkersAPIResponseNullResultMessageSource] = None


class WorkersAPIResponseNullResult(BaseModel):
    errors: List[WorkersAPIResponseNullResultError]

    messages: List[WorkersAPIResponseNullResultMessage]

    success: Literal[True]
    """Whether the API call was successful."""

    result: Optional[object] = None


TagDeleteResponse: TypeAlias = Union[WorkersTagsKVResponse, WorkersAPIResponseNullResult]
