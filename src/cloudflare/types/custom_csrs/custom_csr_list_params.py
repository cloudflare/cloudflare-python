# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CustomCsrListParams"]


class CustomCsrListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    direction: Literal["asc", "desc"]
    """The direction to sort by."""

    order: Literal["name", "account_tag", "created_at"]
    """The field to sort the returned custom CSRs by."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of custom CSRs per page."""
