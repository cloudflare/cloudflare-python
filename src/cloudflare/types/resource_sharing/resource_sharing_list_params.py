# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResourceSharingListParams"]


class ResourceSharingListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier."""

    direction: Literal["asc", "desc"]
    """Direction to sort objects."""

    kind: Literal["sent", "received"]
    """Filter shares by kind."""

    order: Literal["name", "created"]
    """Order shares by values in the given field."""

    page: int
    """Page number."""

    per_page: int
    """Number of objects to return per page."""

    status: Literal["active", "deleting", "deleted"]
    """Filter shares by status."""

    target_type: Literal["account", "organization"]
    """Filter shares by target_type."""
