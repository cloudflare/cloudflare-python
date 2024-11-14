# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    email: str
    """The email of the user."""

    name: str
    """The name of the user."""

    search: str
    """Search for users by other listed query parameters."""
