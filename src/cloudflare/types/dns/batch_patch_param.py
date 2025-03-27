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
    "BatchPatchParam",
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


class A(ARecordParam, total=False):
    id: Required[str]
    """Identifier"""


class AAAA(AAAARecordParam, total=False):
    id: Required[str]
    """Identifier"""


class CAA(CAARecordParam, total=False):
    id: Required[str]
    """Identifier"""


class CERT(CERTRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class CNAME(CNAMERecordParam, total=False):
    id: Required[str]
    """Identifier"""


class DNSKEY(DNSKEYRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class DS(DSRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class HTTPS(HTTPSRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class LOC(LOCRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class MX(MXRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class NAPTR(NAPTRRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class NS(NSRecordParam, total=False):
    id: Required[str]
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
    id: Required[str]
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

    settings: OpenpgpkeySettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["OPENPGPKEY"]
    """Record type."""


class PTR(PTRRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class SMIMEA(SMIMEARecordParam, total=False):
    id: Required[str]
    """Identifier"""


class SRV(SRVRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class SSHFP(SSHFPRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class SVCB(SVCBRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class TLSA(TLSARecordParam, total=False):
    id: Required[str]
    """Identifier"""


class TXT(TXTRecordParam, total=False):
    id: Required[str]
    """Identifier"""


class URI(URIRecordParam, total=False):
    id: Required[str]
    """Identifier"""


BatchPatchParam: TypeAlias = Union[
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
