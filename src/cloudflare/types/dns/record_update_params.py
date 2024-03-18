# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RecordUpdateParams", "Data", "Meta"]


class RecordUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[
        Literal[
            "URI",
            "TXT",
            "TLSA",
            "SVCB",
            "SSHFP",
            "SRV",
            "SMIMEA",
            "PTR",
            "NS",
            "NAPTR",
            "MX",
            "LOC",
            "HTTPS",
            "DS",
            "DNSKEY",
            "CNAME",
            "CERT",
            "CAA",
            "AAAA",
            "A",
        ]
    ]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: object
    """Formatted URI content. See 'data' to set URI properties."""

    data: Data

    meta: Meta

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class Data(TypedDict, total=False):
    algorithm: float
    """algorithm."""

    altitude: float
    """Altitude of location in meters."""

    certificate: str
    """certificate."""

    content: str
    """The record content."""

    digest: str
    """Digest."""

    digest_type: float
    """Digest Type."""

    fingerprint: str
    """fingerprint."""

    flags: object
    """Flags."""

    key_tag: float
    """Key Tag."""

    lat_degrees: float
    """Degrees of latitude."""

    lat_direction: Literal["N", "S"]
    """Latitude direction."""

    lat_minutes: float
    """Minutes of latitude."""

    lat_seconds: float
    """Seconds of latitude."""

    long_degrees: float
    """Degrees of longitude."""

    long_direction: Literal["E", "W"]
    """Longitude direction."""

    long_minutes: float
    """Minutes of longitude."""

    long_seconds: float
    """Seconds of longitude."""

    matching_type: float
    """Matching Type."""

    name: str
    """A valid hostname.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field represents the remainder of the full 'name' after the service and
    protocol.
    """

    order: float
    """Order."""

    port: float
    """The port of the service."""

    precision_horz: float
    """Horizontal precision of location."""

    precision_vert: float
    """Vertical precision of location."""

    preference: float
    """Preference."""

    priority: float
    """priority."""

    proto: str
    """A valid protocol, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the second label of that 'name'.
    """

    protocol: float
    """Protocol."""

    public_key: str
    """Public Key."""

    regex: str
    """Regex."""

    replacement: str
    """Replacement."""

    selector: float
    """Selector."""

    service: str
    """A service type, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the first label of that 'name'.
    """

    size: float
    """Size of location in meters."""

    tag: str
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    target: str
    """target."""

    type: float
    """type."""

    usage: float
    """Usage."""

    value: str
    """value."""

    weight: float
    """The record weight."""


class Meta(TypedDict, total=False):
    auto_added: bool
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: str
    """Where the record originated from."""
