# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserUpdateParams"]


class UserUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    email: Required[str]
    """The email of the user."""

    name: Required[str]
    """The name of the user."""
