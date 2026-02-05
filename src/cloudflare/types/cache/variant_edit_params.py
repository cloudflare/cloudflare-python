# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["VariantEditParams", "Value"]


class VariantEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    value: Required[Value]
    """Value of the zone setting."""


class Value(TypedDict, total=False):
    """Value of the zone setting."""

    avif: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for avif.
    """

    bmp: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for bmp.
    """

    gif: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for gif.
    """

    jp2: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jp2.
    """

    jpeg: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpeg.
    """

    jpg: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg.
    """

    jpg2: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for jpg2.
    """

    png: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for png.
    """

    tif: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for tif.
    """

    tiff: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for tiff.
    """

    webp: SequenceNotStr[str]
    """
    List of strings with the MIME types of all the variants that should be served
    for webp.
    """
