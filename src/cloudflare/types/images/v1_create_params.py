# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

__all__ = ["V1CreateParams", "ImagesImageUploadViaFile", "ImagesImageUploadViaURL"]


class ImagesImageUploadViaFile(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    file: Required[object]
    """An image binary data."""


class ImagesImageUploadViaURL(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    url: Required[str]
    """A URL to fetch an image from origin."""


V1CreateParams = Union[ImagesImageUploadViaFile, ImagesImageUploadViaURL]
