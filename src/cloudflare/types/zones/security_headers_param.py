# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecurityHeadersParam", "Value", "ValueStrictTransportSecurity"]


class ValueStrictTransportSecurity(TypedDict, total=False):
    enabled: bool
    """Whether or not strict transport security is enabled."""

    include_subdomains: bool
    """Include all subdomains for strict transport security."""

    max_age: float
    """Max age in seconds of the strict transport security."""

    nosniff: bool
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""

    preload: bool
    """Enable automatic preload of the HSTS configuration."""


class Value(TypedDict, total=False):
    strict_transport_security: ValueStrictTransportSecurity
    """Strict Transport Security."""


class SecurityHeadersParam(TypedDict, total=False):
    id: Required[Literal["security_header"]]
    """ID of the zone's security header."""

    value: Required[Value]
    """Current value of the zone setting."""
