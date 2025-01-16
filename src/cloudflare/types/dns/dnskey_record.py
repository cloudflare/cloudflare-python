# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = ["DNSKEYRecord", "Data"]


class Data(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    flags: Optional[float] = None
    """Flags."""

    protocol: Optional[float] = None
    """Protocol."""

    public_key: Optional[str] = None
    """Public Key."""


class DNSKEYRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted DNSKEY content. See 'data' to set DNSKEY properties."""

    data: Optional[Data] = None
    """Components of a DNSKEY record."""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["DNSKEY"]] = None
    """Record type."""
