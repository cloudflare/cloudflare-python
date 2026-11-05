# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SecurityHeaders",
    "Value",
    "ValueStrictTransportSecurity",
    "ValueStrictTransportSecurityStrictTransportSecurity",
]


class ValueStrictTransportSecurityStrictTransportSecurity(BaseModel):
    """Strict Transport Security."""

    enabled: Optional[bool] = None
    """Whether or not strict transport security is enabled."""

    include_subdomains: Optional[bool] = None
    """Include all subdomains for strict transport security."""

    max_age: Optional[float] = None
    """Max age in seconds of the strict transport security."""

    nosniff: Optional[bool] = None
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""

    preload: Optional[bool] = None
    """Enable automatic preload of the HSTS configuration."""


class ValueStrictTransportSecurity(BaseModel):
    strict_transport_security: Optional[ValueStrictTransportSecurityStrictTransportSecurity] = None
    """Strict Transport Security."""


Value: TypeAlias = Union[
    ValueStrictTransportSecurity,
    ValueStrictTransportSecurity,
    ValueStrictTransportSecurity,
    ValueStrictTransportSecurity,
    ValueStrictTransportSecurity,
]


class SecurityHeaders(BaseModel):
    """Cloudflare security header for a zone."""

    id: Literal["security_header"]
    """ID of the zone's security header."""

    value: Value
    """Current value of the zone setting."""

    editable: Optional[Literal[True, False]] = None
    """
    Whether or not this setting can be modified for this zone (based on your
    Cloudflare plan level).
    """

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
