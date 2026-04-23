# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnippetListParams"]


class SnippetListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Use this field to specify the unique ID of the zone."""

    page: int
    """Specifies the current page number."""

    per_page: int
    """Specifies how many results to return per page."""
