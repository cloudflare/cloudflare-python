# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "RelayGetResponse",
    "Config",
    "ConfigLingeringSubscribe",
    "ConfigOriginFallback",
    "ConfigOriginFallbackOrigin",
]


class ConfigLingeringSubscribe(BaseModel):
    enabled: Optional[bool] = None

    max_timeout_ms: Optional[int] = None
    """Relay-level ceiling on lingering subscribe timeout (ms). Default 30000."""


class ConfigOriginFallbackOrigin(BaseModel):
    """A single upstream origin relay."""

    url: Optional[str] = None
    """Upstream origin relay URL."""


class ConfigOriginFallback(BaseModel):
    enabled: Optional[bool] = None

    origins: Optional[List[ConfigOriginFallbackOrigin]] = None
    """Ordered list of upstream origin relays.

    Each entry is an object (not a bare string) so per-origin configuration can be
    added in the future without another breaking change.
    """


class Config(BaseModel):
    """origin_fallback and lingering_subscribe are mutually exclusive."""

    lingering_subscribe: Optional[ConfigLingeringSubscribe] = None

    origin_fallback: Optional[ConfigOriginFallback] = None


class RelayGetResponse(BaseModel):
    """Full relay details (no tokens)."""

    config: Config
    """origin_fallback and lingering_subscribe are mutually exclusive."""

    created: datetime

    modified: datetime

    name: str

    uid: str

    status: Optional[Literal["connected"]] = None
    """\"connected" when active, omitted otherwise."""
