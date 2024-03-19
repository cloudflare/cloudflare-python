# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecurityHeaderEditParams", "Value", "ValueStrictTransportSecurity"]


class SecurityHeaderEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Value]


class ValueStrictTransportSecurity(TypedDict, total=False):
    enabled: bool
    """Whether or not strict transport security is enabled."""

    include_subdomains: bool
    """Include all subdomains for strict transport security."""

    max_age: float
    """Max age in seconds of the strict transport security."""

    nosniff: bool
    """Whether or not to include 'X-Content-Type-Options: nosniff' header."""


class Value(TypedDict, total=False):
    strict_transport_security: ValueStrictTransportSecurity
    """Strict Transport Security."""
