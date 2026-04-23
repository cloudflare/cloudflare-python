# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PermissionGroupGetParams"]


class PermissionGroupGetParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: str
    """Filter by the name of the permission group. The value must be URL-encoded."""

    scope: str
    """Filter by the scope of the permission group. The value must be URL-encoded."""
