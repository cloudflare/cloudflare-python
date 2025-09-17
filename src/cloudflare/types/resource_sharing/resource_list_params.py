# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceListParams"]


class ResourceListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    page: int
    """Page number."""

    per_page: int
    """Number of objects to return per page."""

    resource_type: Literal["custom-ruleset", "widget"]
    """Filter share resources by resource_type."""

    status: Literal["active", "deleting", "deleted"]
    """Filter share resources by status."""
