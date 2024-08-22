# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PermissionGroupListParams"]


class PermissionGroupListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    id: str
    """ID of the permission group to be fetched."""

    label: str
    """Label of the permission group to be fetched."""

    name: str
    """Name of the permission group to be fetched."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Maximum number of results per page."""
