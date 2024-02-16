# File generated from our OpenAPI spec by Stainless.

from typing import List

from .._models import BaseModel

__all__ = ["RoleAccountRolesListRolesResponse", "RoleAccountRolesListRolesResponseItem"]


class RoleAccountRolesListRolesResponseItem(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[str]
    """Access permissions for this User."""


RoleAccountRolesListRolesResponse = List[RoleAccountRolesListRolesResponseItem]
