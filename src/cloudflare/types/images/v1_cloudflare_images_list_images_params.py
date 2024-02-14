# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1CloudflareImagesListImagesParams"]


class V1CloudflareImagesListImagesParams(TypedDict, total=False):
    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
