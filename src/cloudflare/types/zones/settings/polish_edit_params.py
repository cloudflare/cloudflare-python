# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .polish_param import PolishParam

__all__ = ["PolishEditParams"]


class PolishEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[PolishParam]
    """Removes metadata and compresses your images for faster page load times.

    Basic (Lossless): Reduce the size of PNG, JPEG, and GIF files - no impact on
    visual quality. Basic + JPEG (Lossy): Further reduce the size of JPEG files for
    faster image loading. Larger JPEGs are converted to progressive images, loading
    a lower-resolution image first and ending in a higher-resolution version. Not
    recommended for hi-res photography sites.
    """
