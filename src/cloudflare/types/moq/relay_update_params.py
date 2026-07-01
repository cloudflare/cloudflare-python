# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RelayUpdateParams", "Config", "ConfigLingeringSubscribe", "ConfigUpstreams", "ConfigUpstreamsUpstream"]


class RelayUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    config: Config
    """upstreams and lingering_subscribe are mutually exclusive."""

    name: str


class ConfigLingeringSubscribe(TypedDict, total=False):
    enabled: bool

    max_timeout_ms: int
    """Relay-level ceiling on lingering subscribe timeout (ms). Default 30000."""


class ConfigUpstreamsUpstream(TypedDict, total=False):
    """A single upstream MOQT server publisher."""

    url: str
    """Upstream MOQT server publisher URL."""


class ConfigUpstreams(TypedDict, total=False):
    """
    Upstreams are external MOQT server publishers that a relay falls back
    to when it has no local publisher for a requested namespace/track.
    """

    enabled: bool

    upstreams: Iterable[ConfigUpstreamsUpstream]
    """Ordered list of upstream MOQT server publishers.

    Each entry is an object (not a bare string) so per-upstream configuration can be
    added in the future without another breaking change.
    """


class Config(TypedDict, total=False):
    """upstreams and lingering_subscribe are mutually exclusive."""

    lingering_subscribe: ConfigLingeringSubscribe

    upstreams: ConfigUpstreams
    """
    Upstreams are external MOQT server publishers that a relay falls back to when it
    has no local publisher for a requested namespace/track.
    """
