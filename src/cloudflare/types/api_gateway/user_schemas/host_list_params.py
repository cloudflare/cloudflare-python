# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostListParams"]


class HostListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    page: int
    """Page number of paginated results."""

    per_page: int
    """Maximum number of results per page."""
