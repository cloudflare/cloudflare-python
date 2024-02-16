# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["V1CloudflareImagesUploadAnImageViaURLParams", "ImagesImageUploadViaFile", "ImagesImageUploadViaURL"]


class ImagesImageUploadViaFile(TypedDict, total=False):
    file: Required[object]
    """An image binary data."""


class ImagesImageUploadViaURL(TypedDict, total=False):
    url: Required[str]
    """A URL to fetch an image from origin."""


V1CloudflareImagesUploadAnImageViaURLParams = Union[ImagesImageUploadViaFile, ImagesImageUploadViaURL]
