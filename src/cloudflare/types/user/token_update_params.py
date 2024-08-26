# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import Iterable, Union, List

from .policy_param import PolicyParam

from datetime import datetime

from ..._utils import PropertyInfo

from .cidr_list import CIDRList

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["TokenUpdateParams", "Condition", "ConditionRequestIP"]

class TokenUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Token name."""

    policies: Required[Iterable[PolicyParam]]
    """List of access policies assigned to the token."""

    status: Required[Literal["active", "disabled", "expired"]]
    """Status of the token."""

    condition: Condition

    expires_on: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    not_before: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """The time before which the token MUST NOT be accepted for processing."""

_ConditionRequestIPReservedKeywords = TypedDict("_ConditionRequestIPReservedKeywords", {
    "in": List[CIDRList],
}, total=False)

class ConditionRequestIP(_ConditionRequestIPReservedKeywords, total=False):
    not_in: List[CIDRList]
    """List of IPv4/IPv6 CIDR addresses."""

class Condition(TypedDict, total=False):
    request_ip: Annotated[ConditionRequestIP, PropertyInfo(alias="request.ip")]
    """Client IP restrictions."""