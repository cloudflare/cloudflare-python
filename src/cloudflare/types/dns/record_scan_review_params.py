# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
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
    "RecordScanReviewParams",
    "Accept",
    "AcceptDNSRecordsOpenpgpkeyRecord",
    "AcceptDNSRecordsOpenpgpkeyRecordSettings",
    "Reject",
]


class RecordScanReviewParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier."""

    accepts: Iterable[Accept]

    rejects: Iterable[Reject]


class AcceptDNSRecordsOpenpgpkeyRecordSettings(TypedDict, total=False):
    """Settings for the DNS record."""

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


class AcceptDNSRecordsOpenpgpkeyRecord(TypedDict, total=False):
    name: Required[str]
    """Complete DNS record name, including the zone name, in Punycode."""

    ttl: Required[TTLParam]
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

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

    settings: AcceptDNSRecordsOpenpgpkeyRecordSettings
    """Settings for the DNS record."""

    tags: SequenceNotStr[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""


Accept: TypeAlias = Union[
    ARecordParam,
    AAAARecordParam,
    CNAMERecordParam,
    MXRecordParam,
    NSRecordParam,
    AcceptDNSRecordsOpenpgpkeyRecord,
    PTRRecordParam,
    TXTRecordParam,
    CAARecordParam,
    CERTRecordParam,
    DNSKEYRecordParam,
    DSRecordParam,
    HTTPSRecordParam,
    LOCRecordParam,
    NAPTRRecordParam,
    SMIMEARecordParam,
    SRVRecordParam,
    SSHFPRecordParam,
    SVCBRecordParam,
    TLSARecordParam,
    URIRecordParam,
]


class Reject(TypedDict, total=False):
    id: Required[str]
    """Identifier."""
