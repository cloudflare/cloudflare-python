# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProjectListParams"]


class ProjectListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    page: int
    """Page number of results to return."""

    per_page: int
    """Number of results to return per page."""
