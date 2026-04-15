# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LogoCreateParams"]


class LogoCreateParams(TypedDict, total=False):
    account_id: str

    image_data: Required[str]
    """Base64 encoded image data.

    Can include data URI prefix (e.g., 'data:image/png;base64,...') or just the
    base64 string.
    """

    similarity_threshold: Required[float]
    """Minimum similarity score (0-1) required for visual matches"""

    tag: Required[str]
    """Unique identifier for the logo query"""

    search_lookback: bool
    """
    If true, search historic scanned images for matches above the similarity
    threshold
    """
