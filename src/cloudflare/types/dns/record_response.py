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
    "ARecordMeta",
    "AAAARecord",
    "AAAARecordMeta",
    "CNAMERecord",
    "CNAMERecordMeta",
    "MXRecord",
    "MXRecordMeta",
    "NSRecord",
    "NSRecordMeta",
    "OpenpgpkeyRecord",
    "OpenpgpkeyRecordMeta",
    "OpenpgpkeyRecordSettings",
    "PTRRecord",
    "PTRRecordMeta",
    "TXTRecord",
    "TXTRecordMeta",
    "CAARecord",
    "CAARecordMeta",
    "CERTRecord",
    "CERTRecordMeta",
    "DNSKEYRecord",
    "DNSKEYRecordMeta",
    "DSRecord",
    "DSRecordMeta",
    "HTTPSRecord",
    "HTTPSRecordMeta",
    "LOCRecord",
    "LOCRecordMeta",
    "NAPTRRecord",
    "NAPTRRecordMeta",
    "SMIMEARecord",
    "SMIMEARecordMeta",
    "SRVRecord",
    "SRVRecordMeta",
    "SSHFPRecord",
    "SSHFPRecordMeta",
    "SVCBRecord",
    "SVCBRecordMeta",
    "TLSARecord",
    "TLSARecordMeta",
    "URIRecord",
    "URIRecordMeta",
]


class ARecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class ARecord(a_record.ARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: ARecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class AAAARecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class AAAARecord(aaaa_record.AAAARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: AAAARecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CNAMERecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class CNAMERecord(cname_record.CNAMERecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: CNAMERecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class MXRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class MXRecord(mx_record.MXRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: MXRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class NSRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class NSRecord(ns_record.NSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: NSRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class OpenpgpkeyRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class OpenpgpkeyRecordSettings(BaseModel):
    """Settings for the DNS record."""

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

    meta: OpenpgpkeyRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    name: str
    """Complete DNS record name, including the zone name, in Punycode."""

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


class PTRRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class PTRRecord(ptr_record.PTRRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: PTRRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class TXTRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class TXTRecord(txt_record.TXTRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: TXTRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CAARecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class CAARecord(caa_record.CAARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: CAARecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class CERTRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class CERTRecord(cert_record.CERTRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: CERTRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class DNSKEYRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class DNSKEYRecord(dnskey_record.DNSKEYRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: DNSKEYRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class DSRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class DSRecord(ds_record.DSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: DSRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class HTTPSRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class HTTPSRecord(https_record.HTTPSRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: HTTPSRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class LOCRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class LOCRecord(loc_record.LOCRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: LOCRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class NAPTRRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class NAPTRRecord(naptr_record.NAPTRRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: NAPTRRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SMIMEARecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class SMIMEARecord(smimea_record.SMIMEARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: SMIMEARecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SRVRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class SRVRecord(srv_record.SRVRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: SRVRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SSHFPRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class SSHFPRecord(sshfp_record.SSHFPRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: SSHFPRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class SVCBRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class SVCBRecord(svcb_record.SVCBRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: SVCBRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class TLSARecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class TLSARecord(tlsa_record.TLSARecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: TLSARecordMeta
    """Extra Cloudflare-specific metadata about the record."""

    modified_on: datetime
    """When the record was last modified."""

    proxiable: bool
    """Whether the record can be proxied by Cloudflare or not."""

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class URIRecordMeta(BaseModel):
    """Extra Cloudflare-specific metadata about the record."""

    dead_glue: Optional[bool] = None
    """
    Whether this glue record is not served because a shallower NS delegation takes
    precedence over the deeper delegation that needs it. Present only when true;
    reachable glue carries only `is_glue`. See
    [Unreachable glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#unreachable-glue-records).
    """

    is_glue: Optional[bool] = None
    """Whether this A or AAAA record is glue for a subdomain NS delegation.

    See
    [Glue records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records#glue-records).
    """

    shadowed_by: Optional[List[str]] = None
    """IDs of the NS records that shadow this record.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """

    shadowed_records_count: Optional[int] = None
    """Number of records shadowed by this NS delegation.

    See
    [Shadowed records](https://developers.cloudflare.com/dns/manage-dns-records/reference/shadowed-records).
    """


class URIRecord(uri_record.URIRecord):
    id: str
    """Identifier."""

    created_on: datetime
    """When the record was created."""

    meta: URIRecordMeta
    """Extra Cloudflare-specific metadata about the record."""

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
