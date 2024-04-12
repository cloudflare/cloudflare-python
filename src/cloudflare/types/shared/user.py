# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..accounts import MemberRole

__all__ = ["User"]


class User(BaseModel):
    id: str
    """Membership identifier tag."""

    roles: List[MemberRole]
    """Roles assigned to this member."""

    status: object

    user: User
