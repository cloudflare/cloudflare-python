# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.token_policy import TokenPolicy
from ..shared.token_condition_cidr_list import TokenConditionCIDRList

__all__ = ["TokenCreateParams", "Condition", "ConditionRequestIP"]


class TokenCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    name: Required[str]
    """Token name."""

    policies: Required[Iterable[TokenPolicy]]
    """List of access policies assigned to the token."""

    condition: Condition

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The time before which the token MUST NOT be accepted for processing."""


_ConditionRequestIPReservedKeywords = TypedDict(
    "_ConditionRequestIPReservedKeywords",
    {
        "in": List[TokenConditionCIDRList],
    },
    total=False,
)


class ConditionRequestIP(_ConditionRequestIPReservedKeywords, total=False):
    not_in: List[TokenConditionCIDRList]
    """List of IPv4/IPv6 CIDR addresses."""


class Condition(TypedDict, total=False):
    request_ip: ConditionRequestIP
    """Client IP restrictions."""
