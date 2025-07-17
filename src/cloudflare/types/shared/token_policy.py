# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta", "Resources"]


class PermissionGroupMeta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class PermissionGroup(BaseModel):
    id: str
    """Identifier of the permission group."""

    meta: Optional[PermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the permission group."""


class Resources(BaseModel):
    nested: Optional[Dict[str, Dict[str, str]]] = None
    """Nested resource permissions for hierarchical scoping."""

    simple: Optional[Dict[str, str]] = None
    """Simple resource permissions where each resource maps to a permission string."""


class TokenPolicy(BaseModel):
    id: str
    """Policy identifier."""

    effect: Literal["allow", "deny"]
    """Allow or deny operations against the resources."""

    permission_groups: List[PermissionGroup]
    """A set of permission groups that are specified to the policy."""

    resources: Resources
    """Resource permissions for the policy. Use either simple or nested permissions."""
