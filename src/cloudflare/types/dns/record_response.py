# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from . import (
    a_record,
    ds_record,
    mx_record,
    ns_record,
    caa_record,
    loc_record,
    ptr_record,
    srv_record,
    txt_record,
    uri_record,
    aaaa_record,
    cert_record,
    svcb_record,
    tlsa_record,
    cname_record,
    https_record,
    naptr_record,
    sshfp_record,
    dnskey_record,
    smimea_record,
)
from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = [
    "RecordResponse",
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


class ARecord(a_record.ARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class AAAARecord(aaaa_record.AAAARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CNAMERecord(cname_record.CNAMERecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class MXRecord(mx_record.MXRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class NSRecord(ns_record.NSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class OpenpgpkeyRecordSettings(BaseModel):
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


class OpenpgpkeyRecord(BaseModel):
    id: str
    """Identifier."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    settings: OpenpgpkeyRecordSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["OPENPGPKEY"]
    """Record type."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class PTRRecord(ptr_record.PTRRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class TXTRecord(txt_record.TXTRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CAARecord(caa_record.CAARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CERTRecord(cert_record.CERTRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class DNSKEYRecord(dnskey_record.DNSKEYRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class DSRecord(ds_record.DSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class HTTPSRecord(https_record.HTTPSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class LOCRecord(loc_record.LOCRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class NAPTRRecord(naptr_record.NAPTRRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SMIMEARecord(smimea_record.SMIMEARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SRVRecord(srv_record.SRVRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SSHFPRecord(sshfp_record.SSHFPRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SVCBRecord(svcb_record.SVCBRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class TLSARecord(tlsa_record.TLSARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class URIRecord(uri_record.URIRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: object
    """Extra Cloudflare-specific information about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


RecordResponse: TypeAlias = Union[
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
