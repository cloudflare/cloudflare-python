# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RegionListParams"]


class RegionListParams(TypedDict, total=False):
    account_id: Required[int]

    cursor: str
    """Opaque token for cursor-based pagination.

    Omit for the first page. Pass the value from a previous response to fetch the
    next page.
    """

    per_page: int

    type: Literal["managed", "custom"]
    """Filter regions by type. Omit to return all regions."""
