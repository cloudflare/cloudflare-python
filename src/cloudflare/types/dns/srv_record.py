# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = ["SRVRecord", "Data", "Settings"]


class Data(BaseModel):
    port: Optional[float] = None
    """The port of the service."""

    priority: Optional[float] = None
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    target: Optional[str] = None
    """A valid hostname."""

    weight: Optional[float] = None
    """The record weight."""


class Settings(BaseModel):
    ipv4_only: Optional[bool] = None
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: Optional[bool] = None
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class SRVRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Priority, weight, port, and SRV target.

    See 'data' for setting the individual component values.
    """

    data: Optional[Data] = None
    """Components of a SRV record."""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: Optional[Settings] = None
    """Settings for the DNS record."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["SRV"]] = None
    """Record type."""
