# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..user.tokens import Permission

__all__ = ["MemberListResponse", "Role"]


class Role(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[Permission]
    """Access permissions for this User."""


class MemberListResponse(BaseModel):
    id: str
    """Identifier"""

    email: str
    """The contact email address of the user."""

    name: Optional[str] = None
    """Member Name."""

    roles: List[Role]
    """Roles assigned to this Member."""

    status: Literal["accepted", "invited"]
    """A member's status in the organization."""
