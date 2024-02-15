# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["V1CloudflareImagesUploadAnImageViaURLParams", "ImagesImageUploadViaFile", "ImagesImageUploadViaURL"]


class ImagesImageUploadViaFile(TypedDict, total=False):
    file: Required[object]
    """An image binary data."""


class ImagesImageUploadViaURL(TypedDict, total=False):
    url: Required[str]
    """A URL to fetch an image from origin."""


V1CloudflareImagesUploadAnImageViaURLParams = Union[ImagesImageUploadViaFile, ImagesImageUploadViaURL]
