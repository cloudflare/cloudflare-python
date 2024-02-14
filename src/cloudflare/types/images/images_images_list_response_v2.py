# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List, Union

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ImagesImagesListResponseV2", "Error", "Message", "Result", "ResultImage"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class ResultImage(BaseModel):
    id: Optional[str] = None
    """Image unique identifier."""

    filename: Optional[str] = None
    """Image file name."""

    meta: Optional[object] = None
    """User modifiable key-value store.

    Can be used for keeping references to another system of record for managing
    images. Metadata must not exceed 1024 bytes.
    """

    require_signed_urls: Optional[bool] = FieldInfo(alias="requireSignedURLs", default=None)
    """Indicates whether the image can be a accessed only using it's UID.

    If set to true, a signed token needs to be generated with a signing key to view
    the image.
    """

    uploaded: Optional[datetime] = None
    """When the media item was uploaded."""

    variants: Optional[List[Union[str, str, str]]] = None
    """Object specifying available variants for an image."""


class Result(BaseModel):
    continuation_token: Optional[str] = None
    """Continuation token to fetch next page.

    Passed as a query param when requesting List V2 api endpoint.
    """

    images: Optional[List[ResultImage]] = None


class ImagesImagesListResponseV2(BaseModel):
    errors: List[Error]

    messages: List[Message]

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""
