# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    status: Literal["success", "fail"]
    """Filter users by their policy evaluation status."""
