# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .automatic_platform_optimization_param import AutomaticPlatformOptimizationParam

__all__ = [
    "SettingEditParams",
    "Variant0",
    "Variant1",
    "Variant1Value",
    "Variant1ValueZonesCacheRulesAegisValue",
    "Variant1ValueZonesNELValue",
    "Variant1ValueZonesSecurityHeaderValue",
    "Variant1ValueZonesSecurityHeaderValueStrictTransportSecurity",
]


class Variant0(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: bool
    """ssl-recommender enrollment setting."""


class Variant1(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Variant1Value
    """Value of the zone setting."""


class Variant1ValueZonesCacheRulesAegisValue(TypedDict, total=False):
    """Value of the zone setting."""

    enabled: bool
    """Whether the feature is enabled or not."""

    pool_id: str
    """
    Egress pool id which refers to a grouping of dedicated egress IPs through which
    Cloudflare will connect to origin.
    """


class Variant1ValueZonesNELValue(TypedDict, total=False):
    """Value of the zone setting."""

    enabled: bool


class Variant1ValueZonesSecurityHeaderValueStrictTransportSecurity(TypedDict, total=False):
    """Strict Transport Security."""

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


class Variant1ValueZonesSecurityHeaderValue(TypedDict, total=False):
    strict_transport_security: Variant1ValueZonesSecurityHeaderValueStrictTransportSecurity
    """Strict Transport Security."""


Variant1Value: TypeAlias = Union[
    Variant1ValueZonesCacheRulesAegisValue,
    SequenceNotStr[str],
    Variant1ValueZonesNELValue,
    float,
    AutomaticPlatformOptimizationParam,
    Variant1ValueZonesSecurityHeaderValue,
    object,
]

SettingEditParams: TypeAlias = Union[Variant0, Variant1]
