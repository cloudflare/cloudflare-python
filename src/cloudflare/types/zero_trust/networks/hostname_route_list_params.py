# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameRouteListParams"]


class HostnameRouteListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    id: str
    """The hostname route ID."""

    comment: str
    """If set, only list hostname routes with the given comment."""

    existed_at: str
    """
    If provided, include only resources that were created (and not deleted) before
    this time. URL encoded.
    """

    hostname: str
    """
    If set, only list hostname routes that contain a substring of the given value,
    the filter is case-insensitive.
    """

    is_deleted: bool
    """If `true`, only return deleted hostname routes.

    If `false`, exclude deleted hostname routes.
    """

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    tunnel_id: str
    """If set, only list hostname routes that point to a specific tunnel."""
