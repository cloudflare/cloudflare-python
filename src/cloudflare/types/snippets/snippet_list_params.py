# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnippetListParams"]


class SnippetListParams(TypedDict, total=False):
    zone_id: Required[str]
    """The unique ID of the zone."""

    page: int
    """The current page number."""

    per_page: int
    """The number of results to return per page."""
