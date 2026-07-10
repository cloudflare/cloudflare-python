# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "RelayUpdateParams",
    "Config",
    "ConfigLingeringSubscribe",
    "ConfigOriginFallback",
    "ConfigOriginFallbackOrigin",
]


class RelayUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    config: Config
    """origin_fallback and lingering_subscribe are mutually exclusive."""

    name: str


class ConfigLingeringSubscribe(TypedDict, total=False):
    enabled: bool

    max_timeout_ms: int
    """Relay-level ceiling on lingering subscribe timeout (ms). Default 30000."""


class ConfigOriginFallbackOrigin(TypedDict, total=False):
    """A single upstream origin relay."""

    url: str
    """Upstream origin relay URL."""


class ConfigOriginFallback(TypedDict, total=False):
    enabled: bool

    origins: Iterable[ConfigOriginFallbackOrigin]
    """Ordered list of upstream origin relays.

    Each entry is an object (not a bare string) so per-origin configuration can be
    added in the future without another breaking change.
    """


class Config(TypedDict, total=False):
    """origin_fallback and lingering_subscribe are mutually exclusive."""

    lingering_subscribe: ConfigLingeringSubscribe

    origin_fallback: ConfigOriginFallback
