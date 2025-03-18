# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .ttl import TTL
from ..._utils import PropertyInfo
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
    "RecordResponse",
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


class A(ARecord):
    id: str
    """Identifier"""

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


class AAAA(AAAARecord):
    id: str
    """Identifier"""

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


class CAA(CAARecord):
    id: str
    """Identifier"""

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


class CERT(CERTRecord):
    id: str
    """Identifier"""

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


class CNAME(CNAMERecord):
    id: str
    """Identifier"""

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


class DNSKEY(DNSKEYRecord):
    id: str
    """Identifier"""

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


class DS(DSRecord):
    id: str
    """Identifier"""

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


class HTTPS(HTTPSRecord):
    id: str
    """Identifier"""

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


class LOC(LOCRecord):
    id: str
    """Identifier"""

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


class MX(MXRecord):
    id: str
    """Identifier"""

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


class NAPTR(NAPTRRecord):
    id: str
    """Identifier"""

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


class NS(NSRecord):
    id: str
    """Identifier"""

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


class OpenpgpkeySettings(BaseModel):
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


class Openpgpkey(BaseModel):
    id: str
    """Identifier"""

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

    settings: OpenpgpkeySettings
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


class PTR(PTRRecord):
    id: str
    """Identifier"""

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


class SMIMEA(SMIMEARecord):
    id: str
    """Identifier"""

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


class SRV(SRVRecord):
    id: str
    """Identifier"""

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


class SSHFP(SSHFPRecord):
    id: str
    """Identifier"""

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


class SVCB(SVCBRecord):
    id: str
    """Identifier"""

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


class TLSA(TLSARecord):
    id: str
    """Identifier"""

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


class TXT(TXTRecord):
    id: str
    """Identifier"""

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


class URI(URIRecord):
    id: str
    """Identifier"""

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


RecordResponse: TypeAlias = Annotated[
    Union[
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
    ],
    PropertyInfo(discriminator="type"),
]
