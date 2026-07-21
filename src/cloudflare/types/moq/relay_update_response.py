# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RelayUpdateResponse", "Config", "ConfigUpstreams", "ConfigUpstreamsUpstream"]


class ConfigUpstreamsUpstream(BaseModel):
    """A single upstream MOQT server publisher."""

    url: str
    """Upstream MOQT server publisher URL.

    Must be an absolute URL with a host and a scheme crique can dial: moqt:// (raw
    QUIC) or https:// (WebTransport). Validated on update (PUT); rejected
    with 21013.
    """


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
    upstreams: Optional[ConfigUpstreams] = None
    """
    Upstreams are external MOQT server publishers that a relay falls back to when it
    has no local publisher for a requested namespace/track.
    """


class RelayUpdateResponse(BaseModel):
    """Full relay details (no tokens)."""

    config: Config

    created: datetime

    modified: datetime

    name: str

    uid: str

    status: Optional[Literal["connected"]] = None
    """\"connected" when active, omitted otherwise."""
