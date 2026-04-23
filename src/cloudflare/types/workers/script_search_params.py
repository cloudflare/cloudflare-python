# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ScriptSearchParams"]


class ScriptSearchParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    id: str
    """Worker ID (also called tag) to search for. Only exact matches are returned."""

    name: str
    """Worker name to search for. Both exact and partial matches are returned."""

    order_by: Literal["created_on", "modified_on", "name"]
    """Property to sort results by. Results are sorted in ascending order."""

    page: int
    """Current page."""

    per_page: int
    """Items per page."""
