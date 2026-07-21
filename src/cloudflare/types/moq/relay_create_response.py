# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "RelayCreateResponse",
    "Config",
    "ConfigUpstreams",
    "ConfigUpstreamsUpstream",
    "Issuer",
    "IssuerCloudflareToken",
]


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


class IssuerCloudflareToken(BaseModel):
    created: datetime

    expires: datetime
    """Mandatory; no more than 1 year after `created`."""

    jti: str
    """Token identity and registry key (32 hex chars)."""

    operations: List[Literal["publish", "subscribe"]]
    """Signed allowlist of what the token may do.

    V1 coarse roles; the array form extends to fine-grained MoQT message names later
    without a breaking change.
    """

    label: Optional[str] = None
    """Optional, customer-set."""

    secret: Optional[str] = None
    """The signed JWT.

    Present ONLY in create / auto-create responses (shown once); never returned by
    list, never stored.
    """


class Issuer(BaseModel):
    """One arm of the discriminated-union token collection."""

    cloudflare_tokens: List[IssuerCloudflareToken]
    """Always present ([] when empty)."""

    issuer: Literal["cloudflare"]

    type: Literal["cloudflare_jwt"]


class RelayCreateResponse(BaseModel):
    """
    Relay with its auto-created default token pair (one full-access
    [publish, subscribe] and one [subscribe]-only), each with its one-time
    secret, wrapped in the issuers envelope.
    """

    config: Config

    created: datetime

    issuers: List[Issuer]
    """Token collection (discriminated union on `type`).

    On create this holds the auto-created default pair, each including its one-time
    secret.
    """

    modified: datetime

    name: str

    uid: str
    """Server-generated unique identifier (32 hex chars)."""
