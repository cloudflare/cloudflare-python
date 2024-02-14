# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

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
