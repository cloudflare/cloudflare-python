# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Policy", "PermissionGroup"]


class PermissionGroup(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[object] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""


class Policy(BaseModel):
    id: str
    """Policy identifier."""

    effect: Literal["allow", "deny"]
    """Allow or deny operations against the resources."""

    permission_groups: List[PermissionGroup]
    """A set of permission groups that are specified to the policy."""

    resources: object
    """A list of resource names that the policy applies to."""
