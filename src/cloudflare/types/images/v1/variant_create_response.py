# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VariantCreateResponse", "Variant", "VariantOptions"]


class VariantOptions(BaseModel):
    fit: Literal["scale-down", "contain", "cover", "crop", "pad"]
    """
    The fit property describes how the width and height dimensions should be
    interpreted.
    """

    height: float
    """Maximum height in image pixels."""

    metadata: Literal["keep", "copyright", "none"]
    """What EXIF data should be preserved in the output image."""

    width: float
    """Maximum width in image pixels."""


class Variant(BaseModel):
    id: str

    options: VariantOptions
    """Allows you to define image resizing sizes for different use cases."""

    never_require_signed_urls: Optional[bool] = FieldInfo(alias="neverRequireSignedURLs", default=None)
    """
    Indicates whether the variant can access an image without a signature,
    regardless of image access control.
    """


class VariantCreateResponse(BaseModel):
    variant: Optional[Variant] = None
