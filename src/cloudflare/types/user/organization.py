# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.permission import Permission
from ..accounts.member_status import MemberStatus

__all__ = ["Organization"]


class Organization(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Organization name."""

    permissions: Optional[List[Permission]] = None
    """Access permissions for this User."""

    roles: Optional[List[str]] = None
    """List of roles that a user has within an organization."""

    status: Optional[MemberStatus] = None
    """Whether the user is a member of the organization or has an inivitation pending."""
