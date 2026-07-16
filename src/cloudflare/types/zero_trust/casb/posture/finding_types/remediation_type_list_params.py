# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RemediationTypeListParams"]


class RemediationTypeListParams(TypedDict, total=False):
    account_id: Required[str]

    cursor: str
    """A cursor for pagination."""

    integration_id: str
    """Filter by an integration ID"""

    page: int
    """A page number within the paginated result set."""

    per_page: int
    """Number of results to return per page."""
