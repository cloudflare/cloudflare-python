# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = ["LOCRecord", "Data", "Settings"]


class Data(BaseModel):
    altitude: Optional[float] = None
    """Altitude of location in meters."""

    lat_degrees: Optional[float] = None
    """Degrees of latitude."""

    lat_direction: Optional[Literal["N", "S"]] = None
    """Latitude direction."""

    lat_minutes: Optional[float] = None
    """Minutes of latitude."""

    lat_seconds: Optional[float] = None
    """Seconds of latitude."""

    long_degrees: Optional[float] = None
    """Degrees of longitude."""

    long_direction: Optional[Literal["E", "W"]] = None
    """Longitude direction."""

    long_minutes: Optional[float] = None
    """Minutes of longitude."""

    long_seconds: Optional[float] = None
    """Seconds of longitude."""

    precision_horz: Optional[float] = None
    """Horizontal precision of location."""

    precision_vert: Optional[float] = None
    """Vertical precision of location."""

    size: Optional[float] = None
    """Size of location in meters."""


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


class LOCRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted LOC content. See 'data' to set LOC properties."""

    data: Optional[Data] = None
    """Components of a LOC record."""

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

    type: Optional[Literal["LOC"]] = None
    """Record type."""
