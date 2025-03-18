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
    "A",
    "AAAA",
    "CAA",
    "CERT",
    "CNAME",
    "DNSKEY",
    "DS",
    "HTTPS",
    "LOC",
    "MX",
    "NAPTR",
    "NS",
    "Openpgpkey",
    "OpenpgpkeySettings",
    "PTR",
    "SMIMEA",
    "SRV",
    "SSHFP",
    "SVCB",
    "TLSA",
    "TXT",
    "URI",
]


class A(ARecordParam):
    id: str
    """Identifier"""


class AAAA(AAAARecordParam):
    id: str
    """Identifier"""


class CAA(CAARecordParam):
    id: str
    """Identifier"""


class CERT(CERTRecordParam):
    id: str
    """Identifier"""


class CNAME(CNAMERecordParam):
    id: str
    """Identifier"""


class DNSKEY(DNSKEYRecordParam):
    id: str
    """Identifier"""


class DS(DSRecordParam):
    id: str
    """Identifier"""


class HTTPS(HTTPSRecordParam):
    id: str
    """Identifier"""


class LOC(LOCRecordParam):
    id: str
    """Identifier"""


class MX(MXRecordParam):
    id: str
    """Identifier"""


class NAPTR(NAPTRRecordParam):
    id: str
    """Identifier"""


class NS(NSRecordParam):
    id: str
    """Identifier"""


class OpenpgpkeySettings(TypedDict, total=False):
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


class Openpgpkey(TypedDict, total=False):
    content: Required[str]
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["OPENPGPKEY"]]
    """Record type."""

    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: OpenpgpkeySettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class PTR(PTRRecordParam):
    id: str
    """Identifier"""


class SMIMEA(SMIMEARecordParam):
    id: str
    """Identifier"""


class SRV(SRVRecordParam):
    id: str
    """Identifier"""


class SSHFP(SSHFPRecordParam):
    id: str
    """Identifier"""


class SVCB(SVCBRecordParam):
    id: str
    """Identifier"""


class TLSA(TLSARecordParam):
    id: str
    """Identifier"""


class TXT(TXTRecordParam):
    id: str
    """Identifier"""


class URI(URIRecordParam):
    id: str
    """Identifier"""


BatchPutParam: TypeAlias = Union[
    A,
    AAAA,
    CAA,
    CERT,
    CNAME,
    DNSKEY,
    DS,
    HTTPS,
    LOC,
    MX,
    NAPTR,
    NS,
    Openpgpkey,
    PTR,
    SMIMEA,
    SRV,
    SSHFP,
    SVCB,
    TLSA,
    TXT,
    URI,
]
