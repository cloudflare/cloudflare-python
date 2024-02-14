# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Iterable, Union, List

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["TokenUserAPITokensCreateTokenParams", "Policy", "PolicyPermissionGroup", "Condition", "ConditionRequestIP"]


class TokenUserAPITokensCreateTokenParams(TypedDict, total=False):
    name: Required[str]
    """Token name."""

    policies: Required[Iterable[Policy]]
    """List of access policies assigned to the token."""

    condition: Condition

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time before which the token MUST NOT be accepted for processing."""


class PolicyPermissionGroup(TypedDict, total=False):
    pass


class Policy(TypedDict, total=False):
    effect: Required[Literal["allow", "deny"]]
    """Allow or deny operations against the resources."""

    permission_groups: Required[Iterable[PolicyPermissionGroup]]
    """A set of permission groups that are specified to the policy."""

    resources: Required[object]
    """A list of resource names that the policy applies to."""


_ConditionRequestIPReservedKeywords = TypedDict(
    "_ConditionRequestIPReservedKeywords",
    {
        "in": List[str],
    },
    total=False,
)


class ConditionRequestIP(_ConditionRequestIPReservedKeywords, total=False):
    not_in: List[str]
    """List of IPv4/IPv6 CIDR addresses."""


class Condition(TypedDict, total=False):
    request_ip: ConditionRequestIP
    """Client IP restrictions."""
