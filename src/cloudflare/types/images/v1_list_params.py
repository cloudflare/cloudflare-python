# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1ListParams"]


class V1ListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of items per page."""
