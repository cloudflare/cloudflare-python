# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo
from ....types import shared_params

__all__ = ["VariantUpdateParams", "Options"]


class VariantUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    options: Required[Options]
    """Allows you to define image resizing sizes for different use cases."""

    never_require_signed_urls: Annotated[bool, PropertyInfo(alias="neverRequireSignedURLs")]
    """
    Indicates whether the variant can access an image without a signature,
    regardless of image access control.
    """


class Options(TypedDict, total=False):
    fit: Required[Literal["scale-down", "contain", "cover", "crop", "pad"]]
    """
    The fit property describes how the width and height dimensions should be
    interpreted.
    """

    height: Required[float]
    """Maximum height in image pixels."""

    metadata: Required[Literal["keep", "copyright", "none"]]
    """What EXIF data should be preserved in the output image."""

    width: Required[float]
    """Maximum width in image pixels."""
