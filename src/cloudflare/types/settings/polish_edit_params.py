# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolishEditParams", "Value"]


class PolishEditParams(TypedDict, total=False):
    value: Required[Value]
    """Removes metadata and compresses your images for faster page load times.

    Basic (Lossless): Reduce the size of PNG, JPEG, and GIF files - no impact on
    visual quality. Basic + JPEG (Lossy): Further reduce the size of JPEG files for
    faster image loading. Larger JPEGs are converted to progressive images, loading
    a lower-resolution image first and ending in a higher-resolution version. Not
    recommended for hi-res photography sites.
    """


class Value(TypedDict, total=False):
    id: Required[Literal["polish"]]
    """ID of the zone setting."""

    value: Required[Literal["off", "lossless", "lossy"]]
    """Current value of the zone setting."""
