# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WidgetListParams"]


class WidgetListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    direction: Literal["asc", "desc"]
    """Direction to order widgets."""

    filter: str
    """
    Filter widgets by field using case-insensitive substring matching. Format:
    `field:value`

    Supported fields:

    - `name` - Filter by widget name (e.g., `filter=name:login-form`)
    - `sitekey` - Filter by sitekey (e.g., `filter=sitekey:0x4AAA`)

    Returns 400 Bad Request if the field is unsupported or format is invalid. An
    empty filter value returns all results.
    """

    order: Literal["id", "sitekey", "name", "created_on", "modified_on"]
    """Field to order widgets by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
