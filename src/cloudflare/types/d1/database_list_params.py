# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatabaseListParams"]


class DatabaseListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: str
    """a database name to search for."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
