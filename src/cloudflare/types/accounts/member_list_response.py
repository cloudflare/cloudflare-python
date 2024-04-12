# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..shared import Role
from ..._models import BaseModel

__all__ = ["MemberListResponse"]


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
