# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .account import Account
from .._models import BaseModel
from .accounts import MemberRoles
from .user.tokens import Permission

__all__ = ["Membership"]


class Membership(BaseModel):
    id: Optional[str] = None
    """Membership identifier tag."""

    account: Optional[Account] = None

    api_access_enabled: Optional[bool] = None
    """Enterprise only.

    Indicates whether or not API access is enabled specifically for this user on a
    given account.
    """

    code: Optional[str] = None
    """The unique activation code for the account membership."""

    permissions: Optional[Permission] = None
    """All access permissions for the user at the account."""

    roles: Optional[MemberRoles] = None
    """List of role names for the user at the account."""

    status: Optional[Literal["accepted", "pending", "rejected"]] = None
    """Status of this membership."""
