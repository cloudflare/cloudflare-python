# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MemberListParams"]


class MemberListParams(TypedDict, total=False):
    account_id: str
    """Account identifier tag."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
