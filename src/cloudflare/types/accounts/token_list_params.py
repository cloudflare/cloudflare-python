# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenListParams"]


class TokenListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    direction: Literal["asc", "desc"]
    """Direction to order results."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
