# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .ttl_param import TTLParam
from .record_tags import RecordTags
from .a_record_param import ARecordParam
from .ds_record_param import DSRecordParam
from .mx_record_param import MXRecordParam
from .ns_record_param import NSRecordParam
from .caa_record_param import CAARecordParam
from .loc_record_param import LOCRecordParam
from .ptr_record_param import PTRRecordParam
from .srv_record_param import SRVRecordParam
from .txt_record_param import TXTRecordParam
from .uri_record_param import URIRecordParam
from .aaaa_record_param import AAAARecordParam
from .cert_record_param import CERTRecordParam
from .svcb_record_param import SVCBRecordParam
from .tlsa_record_param import TLSARecordParam
from .cname_record_param import CNAMERecordParam
from .https_record_param import HTTPSRecordParam
from .naptr_record_param import NAPTRRecordParam
from .sshfp_record_param import SSHFPRecordParam
from .dnskey_record_param import DNSKEYRecordParam
from .smimea_record_param import SMIMEARecordParam

__all__ = [
    "BatchPutParam",
    "ARecord",
    "AAAARecord",
    "CNAMERecord",
    "MXRecord",
    "NSRecord",
    "OpenpgpkeyRecord",
    "OpenpgpkeyRecordSettings",
    "PTRRecord",
    "TXTRecord",
    "CAARecord",
    "CERTRecord",
    "DNSKEYRecord",
    "DSRecord",
    "HTTPSRecord",
    "LOCRecord",
    "NAPTRRecord",
    "SMIMEARecord",
    "SRVRecord",
    "SSHFPRecord",
    "SVCBRecord",
    "TLSARecord",
    "URIRecord",
]


class ARecord(ARecordParam, total=False):
    id: Required[str]
    """Identifier."""


class AAAARecord(AAAARecordParam, total=False):
    id: Required[str]
    """Identifier."""


class CNAMERecord(CNAMERecordParam, total=False):
    id: Required[str]
    """Identifier."""


class MXRecord(MXRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class NSRecord(NSRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class OpenpgpkeyRecordSettings(TypedDict, total=False):
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


class OpenpgpkeyRecord(TypedDict, total=False):
    id: Required[str]
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

    settings: OpenpgpkeyRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class PTRRecord(PTRRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class TXTRecord(TXTRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class CAARecord(CAARecordParam, total=False):
    id: Required[str]
    """Identifier."""


class CERTRecord(CERTRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class DNSKEYRecord(DNSKEYRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class DSRecord(DSRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class HTTPSRecord(HTTPSRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class LOCRecord(LOCRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class NAPTRRecord(NAPTRRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class SMIMEARecord(SMIMEARecordParam, total=False):
    id: Required[str]
    """Identifier."""


class SRVRecord(SRVRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class SSHFPRecord(SSHFPRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class SVCBRecord(SVCBRecordParam, total=False):
    id: Required[str]
    """Identifier."""


class TLSARecord(TLSARecordParam, total=False):
    id: Required[str]
    """Identifier."""


class URIRecord(URIRecordParam, total=False):
    id: Required[str]
    """Identifier."""


BatchPutParam: TypeAlias = Union[
    ARecord,
    AAAARecord,
    CNAMERecord,
    MXRecord,
    NSRecord,
    OpenpgpkeyRecord,
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
