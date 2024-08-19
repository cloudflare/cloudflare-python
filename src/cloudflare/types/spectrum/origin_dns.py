# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OriginDNS"]


class OriginDNS(BaseModel):
    name: Optional[str] = None
    """The name of the DNS record associated with the origin."""

    ttl: Optional[int] = None
    """The TTL of our resolution of your DNS record in seconds."""

    type: Optional[Literal["", "A", "AAAA", "SRV"]] = None
    """The type of DNS record associated with the origin.

    "" is used to specify a combination of A/AAAA records.
    """
