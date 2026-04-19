# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WorkerListParams"]


class WorkerListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    order: Literal["asc", "desc"]
    """Sort direction."""

    order_by: Literal["deployed_on", "updated_on", "created_on", "name"]
    """Property to sort results by."""

    page: int
    """Current page."""

    per_page: int
    """Items per-page."""
