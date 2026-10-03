# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TokenPolicy", "PermissionGroup", "PermissionGroupMeta"]


class PermissionGroupMeta(TypedDict, total=False):
    """Attributes associated to the permission group."""

    category: str
    """A category used to group permission groups."""

    deprecated: str
    """Indicates whether the permission group is deprecated."""

    description: str
    """Additional information about the permission group."""

    editable: str
    """Indicates whether the permission group can be edited."""

    eol_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The planned end-of-life date and time, when provided."""

    label: str
    """A label identifying the permission group."""

    scopes: str
    """The scope associated with the permission group."""

    visibility: str
    """Indicates the permission group's availability or visibility."""


class PermissionGroup(TypedDict, total=False):
    """
    A named group of permissions that map to a group of operations against resources.
    """

    id: Required[str]
    """Identifier of the permission group."""

    meta: PermissionGroupMeta
    """Attributes associated to the permission group."""


class TokenPolicy(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[Union[Dict[str, str], Dict[str, Dict[str, str]]]]
    """A list of resource names that the policy applies to."""
