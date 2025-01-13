# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WidgetListParams"]


class WidgetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to order widgets."""

    order: Literal["id", "sitekey", "name", "created_on", "modified_on"]
    """Field to order widgets by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
