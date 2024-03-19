# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["VariantEditParams", "Value"]


class VariantEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    avif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for avif.
    """

    bmp: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for bmp.
    """

    gif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for gif.
    """

    jp2: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jp2.
    """

    jpeg: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpeg.
    """

    jpg: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg.
    """

    jpg2: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg2.
    """

    png: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for png.
    """

    tif: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for tif.
    """

    tiff: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for tiff.
    """

    webp: Iterable[object]
    """
    List of strings with the MIME types of all the variants that should be served
    for webp.
    """
