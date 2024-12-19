# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .ttl import TTL
from .a_record import ARecord
from ..._models import BaseModel
from .ds_record import DSRecord
from .mx_record import MXRecord
from .ns_record import NSRecord
from .caa_record import CAARecord
from .loc_record import LOCRecord
from .ptr_record import PTRRecord
from .srv_record import SRVRecord
from .txt_record import TXTRecord
from .uri_record import URIRecord
from .aaaa_record import AAAARecord
from .cert_record import CERTRecord
from .record_tags import RecordTags
from .svcb_record import SVCBRecord
from .tlsa_record import TLSARecord
from .cname_record import CNAMERecord
from .https_record import HTTPSRecord
from .naptr_record import NAPTRRecord
from .sshfp_record import SSHFPRecord
from .dnskey_record import DNSKEYRecord
from .smimea_record import SMIMEARecord

__all__ = [
    "RecordBatchResponse",
    "Delete",
    "DeleteDNSRecordsOpenpgpkeyRecord",
    "DeleteDNSRecordsOpenpgpkeyRecordSettings",
    "Patch",
    "PatchDNSRecordsOpenpgpkeyRecord",
    "PatchDNSRecordsOpenpgpkeyRecordSettings",
    "Post",
    "PostDNSRecordsOpenpgpkeyRecord",
    "PostDNSRecordsOpenpgpkeyRecordSettings",
    "Put",
    "PutDNSRecordsOpenpgpkeyRecord",
    "PutDNSRecordsOpenpgpkeyRecordSettings",
]


class DeleteDNSRecordsOpenpgpkeyRecordSettings(BaseModel):
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


class DeleteDNSRecordsOpenpgpkeyRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: Optional[DeleteDNSRecordsOpenpgpkeyRecordSettings] = None
    """Settings for the DNS record."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Delete: TypeAlias = Union[
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
    DeleteDNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TXTRecord,
    URIRecord,
]


class PatchDNSRecordsOpenpgpkeyRecordSettings(BaseModel):
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


class PatchDNSRecordsOpenpgpkeyRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: Optional[PatchDNSRecordsOpenpgpkeyRecordSettings] = None
    """Settings for the DNS record."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Patch: TypeAlias = Union[
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
    PatchDNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TXTRecord,
    URIRecord,
]


class PostDNSRecordsOpenpgpkeyRecordSettings(BaseModel):
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


class PostDNSRecordsOpenpgpkeyRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: Optional[PostDNSRecordsOpenpgpkeyRecordSettings] = None
    """Settings for the DNS record."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Post: TypeAlias = Union[
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
    PostDNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TXTRecord,
    URIRecord,
]


class PutDNSRecordsOpenpgpkeyRecordSettings(BaseModel):
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


class PutDNSRecordsOpenpgpkeyRecord(BaseModel):
    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Optional[str] = None
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: Optional[PutDNSRecordsOpenpgpkeyRecordSettings] = None
    """Settings for the DNS record."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Optional[Literal["OPENPGPKEY"]] = None
    """Record type."""


Put: TypeAlias = Union[
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
    PutDNSRecordsOpenpgpkeyRecord,
    PTRRecord,
    SMIMEARecord,
    SRVRecord,
    SSHFPRecord,
    SVCBRecord,
    TLSARecord,
    TXTRecord,
    URIRecord,
]


class RecordBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
