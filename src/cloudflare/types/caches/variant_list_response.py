# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["VariantListResponse", "Value"]


class Value(BaseModel):
    avif: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for avif.
    """

    bmp: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for bmp.
    """

    gif: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for gif.
    """

    jp2: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for jp2.
    """

    jpeg: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for jpeg.
    """

    jpg: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg.
    """

    jpg2: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg2.
    """

    png: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for png.
    """

    tif: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for tif.
    """

    tiff: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for tiff.
    """

    webp: Optional[List[object]] = None
    """
    List of strings with the MIME types of all the variants that should be served
    for webp.
    """


class VariantListResponse(BaseModel):
    id: Literal["variants"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Value
    """Value of the zone setting."""
