# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Watermark"]


class Watermark(BaseModel):
    created: Optional[datetime] = None
    """The date and a time a watermark profile was created."""

    downloaded_from: Optional[str] = FieldInfo(alias="downloadedFrom", default=None)
    """The source URL for a downloaded image.

    If the watermark profile was created via direct upload, this field is null.
    """

    height: Optional[int] = None
    """The height of the image in pixels."""

    name: Optional[str] = None
    """A short description of the watermark profile."""

    opacity: Optional[float] = None
    """The translucency of the image.

    A value of `0.0` makes the image completely transparent, and `1.0` makes the
    image completely opaque. Note that if the image is already semi-transparent,
    setting this to `1.0` will not make the image completely opaque.
    """

    padding: Optional[float] = None
    """
    The whitespace between the adjacent edges (determined by position) of the video
    and the image. `0.0` indicates no padding, and `1.0` indicates a fully padded
    video width or length, as determined by the algorithm.
    """

    position: Optional[str] = None
    """The location of the image.

    Valid positions are: `upperRight`, `upperLeft`, `lowerLeft`, `lowerRight`, and
    `center`. Note that `center` ignores the `padding` parameter.
    """

    scale: Optional[float] = None
    """The size of the image relative to the overall size of the video.

    This parameter will adapt to horizontal and vertical videos automatically. `0.0`
    indicates no scaling (use the size of the image as-is), and `1.0 `fills the
    entire video.
    """

    size: Optional[float] = None
    """The size of the image in bytes."""

    uid: Optional[str] = None
    """The unique identifier for a watermark profile."""

    width: Optional[int] = None
    """The width of the image in pixels."""
