# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .unnamed_schema_ref_669bfbb16c0913af7077c3c194fbfcd0 import UnnamedSchemaRef669bfbb16c0913af7077c3c194fbfcd0

__all__ = ["VariantEditResponse", "Value"]


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


class VariantEditResponse(BaseModel):
    id: UnnamedSchemaRef669bfbb16c0913af7077c3c194fbfcd0
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Value
    """Value of the zone setting."""
