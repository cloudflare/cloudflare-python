# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1ListParams"]


class V1ListParams(TypedDict, total=False):
    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
