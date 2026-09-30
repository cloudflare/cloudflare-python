# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.token_value import TokenValue
from ..shared.token_policy import TokenPolicy
from ..shared.token_condition_cidr_list import TokenConditionCIDRList

__all__ = ["TokenCreateResponse", "Condition", "ConditionRequestIP"]


class ConditionRequestIP(BaseModel):
    """Client IP restrictions."""

    in_: Optional[List[TokenConditionCIDRList]] = FieldInfo(alias="in", default=None)
    """List of IPv4/IPv6 CIDR addresses."""

    not_in: Optional[List[TokenConditionCIDRList]] = None
    """List of IPv4/IPv6 CIDR addresses."""


class Condition(BaseModel):
    request_ip: Optional[ConditionRequestIP] = None
    """Client IP restrictions."""


class TokenCreateResponse(BaseModel):
    id: Optional[str] = None
    """Token identifier tag."""

    condition: Optional[Condition] = None

    creator_email_at_creation: Optional[str] = None
    """The email address of the user who created the token at the time of creation.

    Only present for Account Owned API Tokens when a creator email was available.
    """

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

    policies: Optional[List[TokenPolicy]] = None
    """List of access policies assigned to the token."""

    provisioner_id: Optional[str] = None
    """The identifier of the service that provisioned the token.

    For an OAuth-provisioned token, this is the OAuth client identifier. Present
    when `provisioner_type` is present and null when the identifier is unavailable.
    """

    provisioner_type: Optional[str] = None
    """The type of service that provisioned the token.

    Only present for provisioned Account Owned API Tokens.
    """

    status: Optional[Literal["active", "disabled", "expired"]] = None
    """Status of the token."""

    value: Optional[TokenValue] = None
    """The token value."""
