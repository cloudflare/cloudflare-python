# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemberCreateParams"]


class MemberCreateParams(TypedDict, total=False):
    account_id: Required[object]

    email: Required[str]
    """The contact email address of the user."""

    roles: Required[List[str]]
    """Array of roles associated with this member."""

    status: Literal["accepted", "pending"]
