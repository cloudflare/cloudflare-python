# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .cidr_list import CIDRList

from datetime import datetime

from .policy import Policy

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["TokenListResponse", "Condition", "ConditionRequestIP"]


class ConditionRequestIP(BaseModel):
    in_: Optional[List[CIDRList]] = FieldInfo(alias="in", default=None)
    """List of IPv4/IPv6 CIDR addresses."""

    not_in: Optional[List[CIDRList]] = None
    """List of IPv4/IPv6 CIDR addresses."""


class Condition(BaseModel):
    request_ip: Optional[ConditionRequestIP] = FieldInfo(alias="request.ip", default=None)
    """Client IP restrictions."""


class TokenListResponse(BaseModel):
    id: Optional[str] = None
    """Token identifier tag."""

    condition: Optional[Condition] = None

    expires_on: Optional[datetime] = None
    """
    The expiration time on or after which the JWT MUST NOT be accepted for
    processing.
    """

    issued_on: Optional[datetime] = None
    """The time on which the token was created."""

    last_used_on: Optional[datetime] = None
    """Last time the token was used."""

    modified_on: Optional[datetime] = None
    """Last time the token was modified."""

    name: Optional[str] = None
    """Token name."""

    not_before: Optional[datetime] = None
    """The time before which the token MUST NOT be accepted for processing."""

    policies: Optional[List[Policy]] = None
    """List of access policies assigned to the token."""

    status: Optional[Literal["active", "disabled", "expired"]] = None
    """Status of the token."""
