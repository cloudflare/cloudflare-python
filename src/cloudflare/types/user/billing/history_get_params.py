# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HistoryGetParams"]


class HistoryGetParams(TypedDict, total=False):
    order: Literal["type", "occured_at", "action"]
    """Field to order billing history by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
