# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
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
    "DeleteARecord",
    "DeleteAAAARecord",
    "DeleteCAARecord",
    "DeleteCERTRecord",
    "DeleteCNAMERecord",
    "DeleteDNSKEYRecord",
    "DeleteDSRecord",
    "DeleteHTTPSRecord",
    "DeleteLOCRecord",
    "DeleteMXRecord",
    "DeleteNAPTRRecord",
    "DeleteNSRecord",
    "DeleteOpenpgpkeyRecord",
    "DeletePTRRecord",
    "DeleteSMIMEARecord",
    "DeleteSRVRecord",
    "DeleteSSHFPRecord",
    "DeleteSVCBRecord",
    "DeleteTLSARecord",
    "DeleteTXTRecord",
    "DeleteURIRecord",
    "Patch",
    "PatchARecord",
    "PatchAAAARecord",
    "PatchCAARecord",
    "PatchCERTRecord",
    "PatchCNAMERecord",
    "PatchDNSKEYRecord",
    "PatchDSRecord",
    "PatchHTTPSRecord",
    "PatchLOCRecord",
    "PatchMXRecord",
    "PatchNAPTRRecord",
    "PatchNSRecord",
    "PatchOpenpgpkeyRecord",
    "PatchPTRRecord",
    "PatchSMIMEARecord",
    "PatchSRVRecord",
    "PatchSSHFPRecord",
    "PatchSVCBRecord",
    "PatchTLSARecord",
    "PatchTXTRecord",
    "PatchURIRecord",
    "Post",
    "PostARecord",
    "PostAAAARecord",
    "PostCAARecord",
    "PostCERTRecord",
    "PostCNAMERecord",
    "PostDNSKEYRecord",
    "PostDSRecord",
    "PostHTTPSRecord",
    "PostLOCRecord",
    "PostMXRecord",
    "PostNAPTRRecord",
    "PostNSRecord",
    "PostOpenpgpkeyRecord",
    "PostPTRRecord",
    "PostSMIMEARecord",
    "PostSRVRecord",
    "PostSSHFPRecord",
    "PostSVCBRecord",
    "PostTLSARecord",
    "PostTXTRecord",
    "PostURIRecord",
    "Put",
    "PutARecord",
    "PutAAAARecord",
    "PutCAARecord",
    "PutCERTRecord",
    "PutCNAMERecord",
    "PutDNSKEYRecord",
    "PutDSRecord",
    "PutHTTPSRecord",
    "PutLOCRecord",
    "PutMXRecord",
    "PutNAPTRRecord",
    "PutNSRecord",
    "PutOpenpgpkeyRecord",
    "PutPTRRecord",
    "PutSMIMEARecord",
    "PutSRVRecord",
    "PutSSHFPRecord",
    "PutSVCBRecord",
    "PutTLSARecord",
    "PutTXTRecord",
    "PutURIRecord",
]


class DeleteARecord(ARecord):
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


class DeleteAAAARecord(AAAARecord):
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


class DeleteCAARecord(CAARecord):
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


class DeleteCERTRecord(CERTRecord):
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


class DeleteCNAMERecord(CNAMERecord):
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


class DeleteDNSKEYRecord(DNSKEYRecord):
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


class DeleteDSRecord(DSRecord):
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


class DeleteHTTPSRecord(HTTPSRecord):
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


class DeleteLOCRecord(LOCRecord):
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


class DeleteMXRecord(MXRecord):
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


class DeleteNAPTRRecord(NAPTRRecord):
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


class DeleteNSRecord(NSRecord):
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


class DeleteOpenpgpkeyRecord(BaseModel):
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


class DeletePTRRecord(PTRRecord):
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


class DeleteSMIMEARecord(SMIMEARecord):
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


class DeleteSRVRecord(SRVRecord):
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


class DeleteSSHFPRecord(SSHFPRecord):
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


class DeleteSVCBRecord(SVCBRecord):
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


class DeleteTLSARecord(TLSARecord):
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


class DeleteTXTRecord(TXTRecord):
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


class DeleteURIRecord(URIRecord):
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


Delete: TypeAlias = Union[
    DeleteARecord,
    DeleteAAAARecord,
    DeleteCAARecord,
    DeleteCERTRecord,
    DeleteCNAMERecord,
    DeleteDNSKEYRecord,
    DeleteDSRecord,
    DeleteHTTPSRecord,
    DeleteLOCRecord,
    DeleteMXRecord,
    DeleteNAPTRRecord,
    DeleteNSRecord,
    DeleteOpenpgpkeyRecord,
    DeletePTRRecord,
    DeleteSMIMEARecord,
    DeleteSRVRecord,
    DeleteSSHFPRecord,
    DeleteSVCBRecord,
    DeleteTLSARecord,
    DeleteTXTRecord,
    DeleteURIRecord,
]


class PatchARecord(ARecord):
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


class PatchAAAARecord(AAAARecord):
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


class PatchCAARecord(CAARecord):
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


class PatchCERTRecord(CERTRecord):
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


class PatchCNAMERecord(CNAMERecord):
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


class PatchDNSKEYRecord(DNSKEYRecord):
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


class PatchDSRecord(DSRecord):
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


class PatchHTTPSRecord(HTTPSRecord):
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


class PatchLOCRecord(LOCRecord):
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


class PatchMXRecord(MXRecord):
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


class PatchNAPTRRecord(NAPTRRecord):
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


class PatchNSRecord(NSRecord):
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


class PatchOpenpgpkeyRecord(BaseModel):
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


class PatchPTRRecord(PTRRecord):
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


class PatchSMIMEARecord(SMIMEARecord):
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


class PatchSRVRecord(SRVRecord):
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


class PatchSSHFPRecord(SSHFPRecord):
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


class PatchSVCBRecord(SVCBRecord):
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


class PatchTLSARecord(TLSARecord):
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


class PatchTXTRecord(TXTRecord):
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


class PatchURIRecord(URIRecord):
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


Patch: TypeAlias = Union[
    PatchARecord,
    PatchAAAARecord,
    PatchCAARecord,
    PatchCERTRecord,
    PatchCNAMERecord,
    PatchDNSKEYRecord,
    PatchDSRecord,
    PatchHTTPSRecord,
    PatchLOCRecord,
    PatchMXRecord,
    PatchNAPTRRecord,
    PatchNSRecord,
    PatchOpenpgpkeyRecord,
    PatchPTRRecord,
    PatchSMIMEARecord,
    PatchSRVRecord,
    PatchSSHFPRecord,
    PatchSVCBRecord,
    PatchTLSARecord,
    PatchTXTRecord,
    PatchURIRecord,
]


class PostARecord(ARecord):
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


class PostAAAARecord(AAAARecord):
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


class PostCAARecord(CAARecord):
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


class PostCERTRecord(CERTRecord):
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


class PostCNAMERecord(CNAMERecord):
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


class PostDNSKEYRecord(DNSKEYRecord):
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


class PostDSRecord(DSRecord):
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


class PostHTTPSRecord(HTTPSRecord):
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


class PostLOCRecord(LOCRecord):
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


class PostMXRecord(MXRecord):
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


class PostNAPTRRecord(NAPTRRecord):
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


class PostNSRecord(NSRecord):
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


class PostOpenpgpkeyRecord(BaseModel):
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


class PostPTRRecord(PTRRecord):
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


class PostSMIMEARecord(SMIMEARecord):
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


class PostSRVRecord(SRVRecord):
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


class PostSSHFPRecord(SSHFPRecord):
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


class PostSVCBRecord(SVCBRecord):
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


class PostTLSARecord(TLSARecord):
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


class PostTXTRecord(TXTRecord):
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


class PostURIRecord(URIRecord):
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


Post: TypeAlias = Union[
    PostARecord,
    PostAAAARecord,
    PostCAARecord,
    PostCERTRecord,
    PostCNAMERecord,
    PostDNSKEYRecord,
    PostDSRecord,
    PostHTTPSRecord,
    PostLOCRecord,
    PostMXRecord,
    PostNAPTRRecord,
    PostNSRecord,
    PostOpenpgpkeyRecord,
    PostPTRRecord,
    PostSMIMEARecord,
    PostSRVRecord,
    PostSSHFPRecord,
    PostSVCBRecord,
    PostTLSARecord,
    PostTXTRecord,
    PostURIRecord,
]


class PutARecord(ARecord):
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


class PutAAAARecord(AAAARecord):
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


class PutCAARecord(CAARecord):
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


class PutCERTRecord(CERTRecord):
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


class PutCNAMERecord(CNAMERecord):
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


class PutDNSKEYRecord(DNSKEYRecord):
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


class PutDSRecord(DSRecord):
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


class PutHTTPSRecord(HTTPSRecord):
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


class PutLOCRecord(LOCRecord):
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


class PutMXRecord(MXRecord):
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


class PutNAPTRRecord(NAPTRRecord):
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


class PutNSRecord(NSRecord):
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


class PutOpenpgpkeyRecord(BaseModel):
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


class PutPTRRecord(PTRRecord):
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


class PutSMIMEARecord(SMIMEARecord):
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


class PutSRVRecord(SRVRecord):
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


class PutSSHFPRecord(SSHFPRecord):
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


class PutSVCBRecord(SVCBRecord):
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


class PutTLSARecord(TLSARecord):
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


class PutTXTRecord(TXTRecord):
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


class PutURIRecord(URIRecord):
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


Put: TypeAlias = Union[
    PutARecord,
    PutAAAARecord,
    PutCAARecord,
    PutCERTRecord,
    PutCNAMERecord,
    PutDNSKEYRecord,
    PutDSRecord,
    PutHTTPSRecord,
    PutLOCRecord,
    PutMXRecord,
    PutNAPTRRecord,
    PutNSRecord,
    PutOpenpgpkeyRecord,
    PutPTRRecord,
    PutSMIMEARecord,
    PutSRVRecord,
    PutSSHFPRecord,
    PutSVCBRecord,
    PutTLSARecord,
    PutTXTRecord,
    PutURIRecord,
]


class RecordBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
