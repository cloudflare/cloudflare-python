# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .member_role_param import MemberRoleParam

__all__ = ["MemberUpdateParams"]


class MemberUpdateParams(TypedDict, total=False):
    account_id: Required[object]

    roles: Required[Iterable[MemberRoleParam]]
    """Roles assigned to this member."""
