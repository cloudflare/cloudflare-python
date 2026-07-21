# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RelayUpdateParams", "Config", "ConfigUpstreams", "ConfigUpstreamsUpstream"]


class RelayUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account identifier."""

    config: Config

    name: str


class ConfigUpstreamsUpstream(TypedDict, total=False):
    """A single upstream MOQT server publisher."""

    url: Required[str]
    """Upstream MOQT server publisher URL.

    Must be an absolute URL with a host and a scheme crique can dial: moqt:// (raw
    QUIC) or https:// (WebTransport). Validated on update (PUT); rejected
    with 21013.
    """


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
    upstreams: ConfigUpstreams
    """
    Upstreams are external MOQT server publishers that a relay falls back to when it
    has no local publisher for a requested namespace/track.
    """
