# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TokenCreateResponse", "Issuer", "IssuerCloudflareToken"]


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


class TokenCreateResponse(BaseModel):
    """A relay's token collection, keyed on issuer `type` (a discriminated
    union).

    V1 ships exactly one arm (`cloudflare_jwt`). Clients iterate
    `issuers`, switch on `type`, and ignore unknown types — that contract is
    what makes adding or removing an arm non-breaking.
    """

    issuers: List[Issuer]
