# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["VariantEditParams", "Value"]


class VariantEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    avif: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for avif.
    """

    bmp: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for bmp.
    """

    gif: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for gif.
    """

    jp2: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jp2.
    """

    jpeg: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpeg.
    """

    jpg: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg.
    """

    jpg2: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg2.
    """

    png: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for png.
    """

    tif: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for tif.
    """

    tiff: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for tiff.
    """

    webp: List[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for webp.
    """
