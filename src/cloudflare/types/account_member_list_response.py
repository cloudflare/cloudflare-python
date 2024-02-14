# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["AccountMemberListResponse", "AccountMemberListResponseItem", "AccountMemberListResponseItemRole"]


class AccountMemberListResponseItemRole(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[str]
    """Access permissions for this User."""


class AccountMemberListResponseItem(BaseModel):
    id: str
    """Identifier"""

    email: str
    """The contact email address of the user."""

    name: Optional[str] = None
    """Member Name."""

    roles: List[AccountMemberListResponseItemRole]
    """Roles assigned to this Member."""

    status: Literal["accepted", "invited"]
    """A member's status in the organization."""


AccountMemberListResponse = List[AccountMemberListResponseItem]
