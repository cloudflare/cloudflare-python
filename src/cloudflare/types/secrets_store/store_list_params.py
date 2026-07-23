# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StoreListParams"]


class StoreListParams(TypedDict, total=False):
    account_id: Required[str]

    direction: Literal["asc", "desc"]
    """Direction to sort objects."""

    order: Literal["name", "created", "modified"]
    """Order stores by values in the given field."""

    page: int
    """Page number."""

    per_page: int
    """Number of objects to return per page."""
