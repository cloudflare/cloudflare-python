# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .ttl_param import TTLParam
from .record_tags import RecordTags

__all__ = [
    "RecordEditParams",
    "ARecord",
    "AAAARecord",
    "CAARecord",
    "CAARecordData",
    "CERTRecord",
    "CERTRecordData",
    "CNAMERecord",
    "CNAMERecordSettings",
    "DNSKEYRecord",
    "DNSKEYRecordData",
    "DSRecord",
    "DSRecordData",
    "HTTPSRecord",
    "HTTPSRecordData",
    "LOCRecord",
    "LOCRecordData",
    "MXRecord",
    "NAPTRRecord",
    "NAPTRRecordData",
    "NSRecord",
    "DNSRecordsOpenpgpkeyRecord",
    "PTRRecord",
    "SMIMEARecord",
    "SMIMEARecordData",
    "SRVRecord",
    "SRVRecordData",
    "SSHFPRecord",
    "SSHFPRecordData",
    "SVCBRecord",
    "SVCBRecordData",
    "TLSARecord",
    "TLSARecordData",
    "TXTRecord",
    "URIRecord",
    "URIRecordData",
]


class ARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid IPv4 address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["A"]
    """Record type."""


class AAAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid IPv6 address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["AAAA"]
    """Record type."""


class CAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: CAARecordData
    """Components of a CAA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["CAA"]
    """Record type."""


class CAARecordData(TypedDict, total=False):
    flags: float
    """Flags for the CAA record."""

    tag: str
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: str
    """Value of the record. This field's semantics depend on the chosen tag."""


class CERTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: CERTRecordData
    """Components of a CERT record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["CERT"]
    """Record type."""


class CERTRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    certificate: str
    """Certificate."""

    key_tag: float
    """Key Tag."""

    type: float
    """Type."""


class CNAMERecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid hostname. Must not match the record's name."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: CNAMERecordSettings

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["CNAME"]
    """Record type."""


class CNAMERecordSettings(TypedDict, total=False):
    flatten_cname: bool
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class DNSKEYRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: DNSKEYRecordData
    """Components of a DNSKEY record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["DNSKEY"]
    """Record type."""


class DNSKEYRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    flags: float
    """Flags."""

    protocol: float
    """Protocol."""

    public_key: str
    """Public Key."""


class DSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: DSRecordData
    """Components of a DS record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["DS"]
    """Record type."""


class DSRecordData(TypedDict, total=False):
    algorithm: float
    """Algorithm."""

    digest: str
    """Digest."""

    digest_type: float
    """Digest Type."""

    key_tag: float
    """Key Tag."""


class HTTPSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: HTTPSRecordData
    """Components of a HTTPS record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["HTTPS"]
    """Record type."""


class HTTPSRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class LOCRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: LOCRecordData
    """Components of a LOC record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["LOC"]
    """Record type."""


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


class MXRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid mail server hostname."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["MX"]
    """Record type."""


class NAPTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: NAPTRRecordData
    """Components of a NAPTR record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["NAPTR"]
    """Record type."""


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


class NSRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A valid name server host name."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["NS"]
    """Record type."""


class DNSRecordsOpenpgpkeyRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["OPENPGPKEY"]
    """Record type."""


class PTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """Domain name pointing to the address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["PTR"]
    """Record type."""


class SMIMEARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SMIMEARecordData
    """Components of a SMIMEA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["SMIMEA"]
    """Record type."""


class SMIMEARecordData(TypedDict, total=False):
    certificate: str
    """Certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class SRVRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SRVRecordData
    """Components of a SRV record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["SRV"]
    """Record type."""


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


class SSHFPRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SSHFPRecordData
    """Components of a SSHFP record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["SSHFP"]
    """Record type."""


class SSHFPRecordData(TypedDict, total=False):
    algorithm: float
    """algorithm."""

    fingerprint: str
    """fingerprint."""

    type: float
    """type."""


class SVCBRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: SVCBRecordData
    """Components of a SVCB record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["SVCB"]
    """Record type."""


class SVCBRecordData(TypedDict, total=False):
    priority: float
    """priority."""

    target: str
    """target."""

    value: str
    """value."""


class TLSARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: TLSARecordData
    """Components of a TLSA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["TLSA"]
    """Record type."""


class TLSARecordData(TypedDict, total=False):
    certificate: str
    """certificate."""

    matching_type: float
    """Matching Type."""

    selector: float
    """Selector."""

    usage: float
    """Usage."""


class TXTRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

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

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["TXT"]
    """Record type."""


class URIRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    data: URIRecordData
    """Components of a URI record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["URI"]
    """Record type."""


class URIRecordData(TypedDict, total=False):
    target: str
    """The record content."""

    weight: float
    """The record weight."""


RecordEditParams: TypeAlias = Union[
    ARecord,
    AAAARecord,
    CAARecord,
    CERTRecord,
    CNAMERecord,
    DNSKEYRecord,
    DSRecord,
    HTTPSRecord,
    LOCRecord,
    MXRecord,
    NAPTRRecord,
    NSRecord,
    DNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TXTRecord,
    URIRecord,
]
