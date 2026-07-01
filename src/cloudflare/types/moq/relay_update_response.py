# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RelayUpdateResponse", "Config", "ConfigLingeringSubscribe", "ConfigUpstreams", "ConfigUpstreamsUpstream"]


class ConfigLingeringSubscribe(BaseModel):
    enabled: Optional[bool] = None

    max_timeout_ms: Optional[int] = None
    """Relay-level ceiling on lingering subscribe timeout (ms). Default 30000."""


class ConfigUpstreamsUpstream(BaseModel):
    """A single upstream MOQT server publisher."""

    url: Optional[str] = None
    """Upstream MOQT server publisher URL."""


class ConfigUpstreams(BaseModel):
    """
    Upstreams are external MOQT server publishers that a relay falls back
    to when it has no local publisher for a requested namespace/track.
    """

    enabled: Optional[bool] = None

    upstreams: Optional[List[ConfigUpstreamsUpstream]] = None
    """Ordered list of upstream MOQT server publishers.

    Each entry is an object (not a bare string) so per-upstream configuration can be
    added in the future without another breaking change.
    """


class Config(BaseModel):
    """upstreams and lingering_subscribe are mutually exclusive."""

    lingering_subscribe: Optional[ConfigLingeringSubscribe] = None

    upstreams: Optional[ConfigUpstreams] = None
    """
    Upstreams are external MOQT server publishers that a relay falls back to when it
    has no local publisher for a requested namespace/track.
    """


class RelayUpdateResponse(BaseModel):
    """Full relay details (no tokens)."""

    config: Config
    """upstreams and lingering_subscribe are mutually exclusive."""

    created: datetime

    modified: datetime

    name: str

    uid: str

    status: Optional[Literal["connected"]] = None
    """\"connected" when active, omitted otherwise."""
