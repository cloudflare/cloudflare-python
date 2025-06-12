# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .ttl_param import TTLParam
from .record_tags import RecordTags

__all__ = [
    "RecordUpdateParams",
    "ARecord",
    "ARecordSettings",
    "AAAARecord",
    "AAAARecordSettings",
    "CNAMERecord",
    "CNAMERecordSettings",
    "MXRecord",
    "MXRecordSettings",
    "NSRecord",
    "NSRecordSettings",
    "DNSRecordsOpenpgpkeyRecord",
    "DNSRecordsOpenpgpkeyRecordSettings",
    "PTRRecord",
    "PTRRecordSettings",
    "TXTRecord",
    "TXTRecordSettings",
    "CAARecord",
    "CAARecordData",
    "CAARecordSettings",
    "CERTRecord",
    "CERTRecordData",
    "CERTRecordSettings",
    "DNSKEYRecord",
    "DNSKEYRecordData",
    "DNSKEYRecordSettings",
    "DSRecord",
    "DSRecordData",
    "DSRecordSettings",
    "HTTPSRecord",
    "HTTPSRecordData",
    "HTTPSRecordSettings",
    "LOCRecord",
    "LOCRecordData",
    "LOCRecordSettings",
    "NAPTRRecord",
    "NAPTRRecordData",
    "NAPTRRecordSettings",
    "SMIMEARecord",
    "SMIMEARecordData",
    "SMIMEARecordSettings",
    "SRVRecord",
    "SRVRecordData",
    "SRVRecordSettings",
    "SSHFPRecord",
    "SSHFPRecordData",
    "SSHFPRecordSettings",
    "SVCBRecord",
    "SVCBRecordData",
    "SVCBRecordSettings",
    "TLSARecord",
    "TLSARecordData",
    "TLSARecordSettings",
    "URIRecord",
    "URIRecordData",
    "URIRecordSettings",
]


class ARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["A"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid IPv4 address."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: ARecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class ARecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class AAAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["AAAA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid IPv6 address."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: AAAARecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class AAAARecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class CNAMERecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CNAME"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid hostname. Must not match the record's name."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: CNAMERecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class CNAMERecordSettings(TypedDict, total=False):
    flatten_cname: bool
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting is unavailable for proxied records, since they are always
    flattened.
    """

    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class MXRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["MX"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid mail server hostname."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: MXRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class MXRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class NSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["NS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid name server host name."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: NSRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class NSRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class DNSRecordsOpenpgpkeyRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["OPENPGPKEY"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: DNSRecordsOpenpgpkeyRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSRecordsOpenpgpkeyRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class PTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["PTR"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """Domain name pointing to the address."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: PTRRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class PTRRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class TXTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["TXT"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """Text content for the record.

    The content must consist of quoted "character strings" (RFC 1035), each with a
    length of up to 255 bytes. Strings exceeding this allowed maximum length are
    automatically split.

    Learn more at
    <https://www.cloudflare.com/learning/dns/dns-records/dns-txt-record/>.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: TXTRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class TXTRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class CAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CAA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: CAARecordData
    """Components of a CAA record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: CAARecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class CAARecordData(TypedDict, total=False):
    flags: float
    """Flags for the CAA record."""

    tag: str
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: str
    """Value of the record. This field's semantics depend on the chosen tag."""


class CAARecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class CERTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["CERT"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: CERTRecordData
    """Components of a CERT record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: CERTRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class CERTRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    certificate: str
    """Certificate."""

    key_tag: float
    """Key Tag."""

    type: float
    """Type."""


class CERTRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class DNSKEYRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["DNSKEY"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: DNSKEYRecordData
    """Components of a DNSKEY record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: DNSKEYRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DNSKEYRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    flags: float
    """Flags."""

    protocol: float
    """Protocol."""

    public_key: str
    """Public Key."""


class DNSKEYRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class DSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["DS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: DSRecordData
    """Components of a DS record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: DSRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class DSRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    digest: str
    """Digest."""

    digest_type: float
    """Digest Type."""

    key_tag: float
    """Key Tag."""


class DSRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class HTTPSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["HTTPS"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: HTTPSRecordData
    """Components of a HTTPS record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: HTTPSRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class HTTPSRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class HTTPSRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class LOCRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["LOC"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: LOCRecordData
    """Components of a LOC record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: LOCRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class LOCRecordData(TypedDict, total=False):
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


class LOCRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class NAPTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["NAPTR"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: NAPTRRecordData
    """Components of a NAPTR record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: NAPTRRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class NAPTRRecordData(TypedDict, total=False):
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


class NAPTRRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class SMIMEARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SMIMEA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SMIMEARecordData
    """Components of a SMIMEA record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: SMIMEARecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class SMIMEARecordData(TypedDict, total=False):
    certificate: str
    """Certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class SMIMEARecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class SRVRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SRV"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SRVRecordData
    """Components of a SRV record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: SRVRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class SRVRecordData(TypedDict, total=False):
    port: float
    """The port of the service."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    target: str
    """A valid hostname."""

    weight: float
    """The record weight."""


class SRVRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class SSHFPRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SSHFP"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SSHFPRecordData
    """Components of a SSHFP record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: SSHFPRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class SSHFPRecordData(TypedDict, total=False):
    algorithm: float
    """algorithm."""

    fingerprint: str
    """fingerprint."""

    type: float
    """type."""


class SSHFPRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class SVCBRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["SVCB"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SVCBRecordData
    """Components of a SVCB record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: SVCBRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class SVCBRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class SVCBRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class TLSARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["TLSA"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: TLSARecordData
    """Components of a TLSA record."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: TLSARecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class TLSARecordData(TypedDict, total=False):
    certificate: str
    """certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class TLSARecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


class URIRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["URI"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: URIRecordData
    """Components of a URI record."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: URIRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class URIRecordData(TypedDict, total=False):
    target: str
    """The record content."""

    weight: float
    """The record weight."""


class URIRecordSettings(TypedDict, total=False):
    ipv4_only: bool
    """
    When enabled, only A records will be generated, and AAAA records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """

    ipv6_only: bool
    """
    When enabled, only AAAA records will be generated, and A records will not be
    created. This setting is intended for exceptional cases. Note that this option
    only applies to proxied records and it has no effect on whether Cloudflare
    communicates with the origin using IPv4 or IPv6.
    """


RecordUpdateParams: TypeAlias = Union[
    ARecord,
    AAAARecord,
    CNAMERecord,
    MXRecord,
    NSRecord,
    DNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    TXTRecord,
    CAARecord,
    CERTRecord,
    DNSKEYRecord,
    DSRecord,
    HTTPSRecord,
    LOCRecord,
    NAPTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    URIRecord,
]
