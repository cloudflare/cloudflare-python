# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page. Must be a multiple of 5."""
