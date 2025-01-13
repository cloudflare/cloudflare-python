# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppListParams"]


class AppListParams(TypedDict, total=False):
    zone_id: Required[str]
    """Zone identifier."""

    direction: Literal["asc", "desc"]
    """Sets the direction by which results are ordered."""

    order: Literal["protocol", "app_id", "created_on", "modified_on", "dns"]
    """Application field by which results are ordered."""

    page: float
    """Page number of paginated results.

    This parameter is required in order to use other pagination parameters. If
    included in the query, `result_info` will be present in the response.
    """

    per_page: float
    """Sets the maximum number of results per page."""
