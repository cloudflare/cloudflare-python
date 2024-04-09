# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..user.tokens import Permission

__all__ = ["RoleListResponse"]


class RoleListResponse(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[Permission]
    """Access permissions for this User."""
