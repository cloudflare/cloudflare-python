# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta", "Resources"]


class PermissionGroupMeta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PermissionGroup(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[PermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""


class Resources(BaseModel):
    resource: Optional[str] = None

    scope: Optional[str] = None


class TokenPolicy(BaseModel):
    id: str
    """Policy identifier."""

    effect: Literal["allow", "deny"]
    """Allow or deny operations against the resources."""

    permission_groups: List[PermissionGroup]
    """A set of permission groups that are specified to the policy."""

    resources: Resources
    """A list of resource names that the policy applies to."""