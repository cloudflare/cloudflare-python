# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MemberUpdateParams", "Role"]


class MemberUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    roles: Required[Iterable[Role]]
    """Roles assigned to this member."""


class Role(TypedDict, total=False):
    id: Required[str]
    """Role identifier tag."""
