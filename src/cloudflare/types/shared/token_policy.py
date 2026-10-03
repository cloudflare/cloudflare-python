# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta"]


class PermissionGroupMeta(BaseModel):
    """Attributes associated to the permission group."""

    category: Optional[str] = None
    """A category used to group permission groups."""

    deprecated: Optional[str] = None
    """Indicates whether the permission group is deprecated."""

    description: Optional[str] = None
    """Additional information about the permission group."""

    editable: Optional[str] = None
    """Indicates whether the permission group can be edited."""

    eol_at: Optional[datetime] = None
    """The planned end-of-life date and time, when provided."""

    label: Optional[str] = None
    """A label identifying the permission group."""

    scopes: Optional[str] = None
    """The scope associated with the permission group."""

    visibility: Optional[str] = None
    """Indicates the permission group's availability or visibility."""


class PermissionGroup(BaseModel):
    """
    A named group of permissions that map to a group of operations against resources.
    """

    id: str
    """Identifier of the permission group."""

    meta: Optional[PermissionGroupMeta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the permission group."""


class TokenPolicy(BaseModel):
    id: str
    """Policy identifier."""

    effect: Literal["allow", "deny"]
    """Allow or deny operations against the resources."""

    permission_groups: List[PermissionGroup]
    """A set of permission groups that are specified to the policy."""

    resources: Union[Dict[str, str], Dict[str, Dict[str, str]]]
    """A list of resource names that the policy applies to."""
