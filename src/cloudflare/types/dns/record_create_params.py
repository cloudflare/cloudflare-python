# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "RecordCreateParams",
    "DNSRecordsARecord",
    "DNSRecordsAAAARecord",
    "DNSRecordsCAARecord",
    "DNSRecordsCAARecordData",
    "DNSRecordsCERTRecord",
    "DNSRecordsCERTRecordData",
    "DNSRecordsCNAMERecord",
    "DNSRecordsDNSKEYRecord",
    "DNSRecordsDNSKEYRecordData",
    "DNSRecordsDSRecord",
    "DNSRecordsDSRecordData",
    "DNSRecordsHTTPSRecord",
    "DNSRecordsHTTPSRecordData",
    "DNSRecordsLOCRecord",
    "DNSRecordsLOCRecordData",
    "DNSRecordsMXRecord",
    "DNSRecordsNAPTRRecord",
    "DNSRecordsNAPTRRecordData",
    "DNSRecordsNSRecord",
    "DNSRecordsPTRRecord",
    "DNSRecordsSMIMEARecord",
    "DNSRecordsSMIMEARecordData",
    "DNSRecordsSRVRecord",
    "DNSRecordsSRVRecordData",
    "DNSRecordsSSHFPRecord",
    "DNSRecordsSSHFPRecordData",
    "DNSRecordsSVCBRecord",
    "DNSRecordsSVCBRecordData",
    "DNSRecordsTLSARecord",
    "DNSRecordsTLSARecordData",
    "DNSRecordsTXTRecord",
    "DNSRecordsURIRecord",
    "DNSRecordsURIRecordData",
]


class DNSRecordsARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """A valid IPv4 address."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["A"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
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


class DNSRecordsAAAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """A valid IPv6 address."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["AAAA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
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


class DNSRecordsCAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsCAARecordData]
    """Components of a CAA record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CAA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsCAARecordData(TypedDict, total=False):
    flags: float
    """Flags for the CAA record."""

    tag: str
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: str
    """Value of the record. This field's semantics depend on the chosen tag."""


class DNSRecordsCERTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsCERTRecordData]
    """Components of a CERT record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CERT"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsCERTRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    certificate: str
    """Certificate."""

    key_tag: float
    """Key Tag."""

    type: float
    """Type."""


class DNSRecordsCNAMERecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[object]
    """A valid hostname. Must not match the record's name."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CNAME"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
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


class DNSRecordsDNSKEYRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsDNSKEYRecordData]
    """Components of a DNSKEY record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["DNSKEY"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsDNSKEYRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    flags: float
    """Flags."""

    protocol: float
    """Protocol."""

    public_key: str
    """Public Key."""


class DNSRecordsDSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsDSRecordData]
    """Components of a DS record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["DS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsDSRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    digest: str
    """Digest."""

    digest_type: float
    """Digest Type."""

    key_tag: float
    """Key Tag."""


class DNSRecordsHTTPSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsHTTPSRecordData]
    """Components of a HTTPS record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["HTTPS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsHTTPSRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class DNSRecordsLOCRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsLOCRecordData]
    """Components of a LOC record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["LOC"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsLOCRecordData(TypedDict, total=False):
    altitude: float
    """Altitude of location in meters."""

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

    precision_horz: float
    """Horizontal precision of location."""

    precision_vert: float
    """Vertical precision of location."""

    size: float
    """Size of location in meters."""


class DNSRecordsMXRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """A valid mail server hostname."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: Required[float]
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Required[Literal["MX"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsNAPTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsNAPTRRecordData]
    """Components of a NAPTR record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["NAPTR"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsNAPTRRecordData(TypedDict, total=False):
    flags: str
    """Flags."""

    order: float
    """Order."""

    preference: float
    """Preference."""

    regex: str
    """Regex."""

    replacement: str
    """Replacement."""

    service: str
    """Service."""


class DNSRecordsNSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """A valid name server host name."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["NS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsPTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """Domain name pointing to the address."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["PTR"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsSMIMEARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsSMIMEARecordData]
    """Components of a SMIMEA record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SMIMEA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsSMIMEARecordData(TypedDict, total=False):
    certificate: str
    """Certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class DNSRecordsSRVRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsSRVRecordData]
    """Components of a SRV record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode.

    For SRV records, the first label is normally a service and the second a protocol
    name, each starting with an underscore.
    """

    type: Required[Literal["SRV"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsSRVRecordData(TypedDict, total=False):
    name: str
    """A valid hostname.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field represents the remainder of the full 'name' after the service and
    protocol.
    """

    port: float
    """The port of the service."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proto: str
    """A valid protocol, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the second label of that 'name'.
    """

    service: str
    """A service type, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the first label of that 'name'.
    """

    target: str
    """A valid hostname."""

    weight: float
    """The record weight."""


class DNSRecordsSSHFPRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsSSHFPRecordData]
    """Components of a SSHFP record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SSHFP"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsSSHFPRecordData(TypedDict, total=False):
    algorithm: float
    """algorithm."""

    fingerprint: str
    """fingerprint."""

    type: float
    """type."""


class DNSRecordsSVCBRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsSVCBRecordData]
    """Components of a SVCB record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SVCB"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsSVCBRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class DNSRecordsTLSARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsTLSARecordData]
    """Components of a TLSA record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["TLSA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsTLSARecordData(TypedDict, total=False):
    certificate: str
    """certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class DNSRecordsTXTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: Required[str]
    """Text content for the record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["TXT"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsURIRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: Required[DNSRecordsURIRecordData]
    """Components of a URI record."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: Required[float]
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Required[Literal["URI"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    tags: List[str]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1]]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsURIRecordData(TypedDict, total=False):
    content: str
    """The record content."""

    weight: float
    """The record weight."""


RecordCreateParams = Union[
    DNSRecordsARecord,
    DNSRecordsAAAARecord,
    DNSRecordsCAARecord,
    DNSRecordsCERTRecord,
    DNSRecordsCNAMERecord,
    DNSRecordsDNSKEYRecord,
    DNSRecordsDSRecord,
    DNSRecordsHTTPSRecord,
    DNSRecordsLOCRecord,
    DNSRecordsMXRecord,
    DNSRecordsNAPTRRecord,
    DNSRecordsNSRecord,
    DNSRecordsPTRRecord,
    DNSRecordsSMIMEARecord,
    DNSRecordsSRVRecord,
    DNSRecordsSSHFPRecord,
    DNSRecordsSVCBRecord,
    DNSRecordsTLSARecord,
    DNSRecordsTXTRecord,
    DNSRecordsURIRecord,
]
