# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["V2ListParams"]


class V2ListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    continuation_token: Optional[str]
    """Continuation token for a next page. List images V2 returns continuation_token"""

    per_page: float
    """Number of items per page."""

    sort_order: Literal["asc", "desc"]
    """Sorting order by upload time."""
