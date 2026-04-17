# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    email: Required[str]
    """The email of the user."""

    name: str
    """The name of the user."""
