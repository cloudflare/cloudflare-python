# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SiteInfoListParams"]


class SiteInfoListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    order_by: Literal["host", "created"]
    """The property used to sort the list of results."""

    page: float
    """Current page within the paginated list of results."""

    per_page: float
    """Number of items to return per page of results."""
