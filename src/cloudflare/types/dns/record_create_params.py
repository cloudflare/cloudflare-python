# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, TypeAlias

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = [
    "RecordCreateParams",
    "ARecord",
    "AAAARecord",
    "CAARecord",
    "CAARecordData",
    "CERTRecord",
    "CERTRecordData",
    "CNAMERecord",
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

    content: str
    """A valid IPv4 address."""

    type: Literal["A"]
    """Record type."""


class AAAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: str
    """A valid IPv6 address."""

    type: Literal["AAAA"]
    """Record type."""


class CAARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: CAARecordData
    """Components of a CAA record."""

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

    data: CERTRecordData
    """Components of a CERT record."""

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

    content: str
    """A valid hostname. Must not match the record's name."""

    type: Literal["CNAME"]
    """Record type."""


class DNSKEYRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: DNSKEYRecordData
    """Components of a DNSKEY record."""

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

    data: DSRecordData
    """Components of a DS record."""

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

    data: HTTPSRecordData
    """Components of a HTTPS record."""

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

    data: LOCRecordData
    """Components of a LOC record."""

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

    content: str
    """A valid mail server hostname."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Literal["MX"]
    """Record type."""


class NAPTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: NAPTRRecordData
    """Components of a NAPTR record."""

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

    content: str
    """A valid name server host name."""

    type: Literal["NS"]
    """Record type."""


class DNSRecordsOpenpgpkeyRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    type: Literal["OPENPGPKEY"]
    """Record type."""


class PTRRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    content: str
    """Domain name pointing to the address."""

    type: Literal["PTR"]
    """Record type."""


class SMIMEARecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: SMIMEARecordData
    """Components of a SMIMEA record."""

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

    data: SRVRecordData
    """Components of a SRV record."""

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

    data: SSHFPRecordData
    """Components of a SSHFP record."""

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

    data: SVCBRecordData
    """Components of a SVCB record."""

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

    data: TLSARecordData
    """Components of a TLSA record."""

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

    content: str
    """Text content for the record."""

    type: Literal["TXT"]
    """Record type."""


class URIRecord(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    data: URIRecordData
    """Components of a URI record."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Literal["URI"]
    """Record type."""


class URIRecordData(TypedDict, total=False):
    target: str
    """The record content."""

    weight: float
    """The record weight."""


RecordCreateParams: TypeAlias = Union[
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
