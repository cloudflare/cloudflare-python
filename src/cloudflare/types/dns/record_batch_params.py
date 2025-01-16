# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .ttl_param import TTLParam
from .record_tags import RecordTags
from .record_param import RecordParam
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
    "RecordBatchParams",
    "Delete",
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


class RecordBatchParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    deletes: Iterable[Delete]

    patches: Iterable[Patch]

    posts: Iterable[RecordParam]

    puts: Iterable[Put]


class Delete(TypedDict, total=False):
    id: Required[str]
    """Identifier"""


class PatchARecord(ARecordParam):
    id: Required[str]
    """Identifier"""


class PatchAAAARecord(AAAARecordParam):
    id: Required[str]
    """Identifier"""


class PatchCAARecord(CAARecordParam):
    id: Required[str]
    """Identifier"""


class PatchCERTRecord(CERTRecordParam):
    id: Required[str]
    """Identifier"""


class PatchCNAMERecord(CNAMERecordParam):
    id: Required[str]
    """Identifier"""


class PatchDNSKEYRecord(DNSKEYRecordParam):
    id: Required[str]
    """Identifier"""


class PatchDSRecord(DSRecordParam):
    id: Required[str]
    """Identifier"""


class PatchHTTPSRecord(HTTPSRecordParam):
    id: Required[str]
    """Identifier"""


class PatchLOCRecord(LOCRecordParam):
    id: Required[str]
    """Identifier"""


class PatchMXRecord(MXRecordParam):
    id: Required[str]
    """Identifier"""


class PatchNAPTRRecord(NAPTRRecordParam):
    id: Required[str]
    """Identifier"""


class PatchNSRecord(NSRecordParam):
    id: Required[str]
    """Identifier"""


class PatchOpenpgpkeyRecord(TypedDict, total=False):
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

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    type: Literal["OPENPGPKEY"]
    """Record type."""


class PatchPTRRecord(PTRRecordParam):
    id: Required[str]
    """Identifier"""


class PatchSMIMEARecord(SMIMEARecordParam):
    id: Required[str]
    """Identifier"""


class PatchSRVRecord(SRVRecordParam):
    id: Required[str]
    """Identifier"""


class PatchSSHFPRecord(SSHFPRecordParam):
    id: Required[str]
    """Identifier"""


class PatchSVCBRecord(SVCBRecordParam):
    id: Required[str]
    """Identifier"""


class PatchTLSARecord(TLSARecordParam):
    id: Required[str]
    """Identifier"""


class PatchTXTRecord(TXTRecordParam):
    id: Required[str]
    """Identifier"""


class PatchURIRecord(URIRecordParam):
    id: Required[str]
    """Identifier"""


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


class PutARecord(ARecordParam):
    id: Required[str]
    """Identifier"""


class PutAAAARecord(AAAARecordParam):
    id: Required[str]
    """Identifier"""


class PutCAARecord(CAARecordParam):
    id: Required[str]
    """Identifier"""


class PutCERTRecord(CERTRecordParam):
    id: Required[str]
    """Identifier"""


class PutCNAMERecord(CNAMERecordParam):
    id: Required[str]
    """Identifier"""


class PutDNSKEYRecord(DNSKEYRecordParam):
    id: Required[str]
    """Identifier"""


class PutDSRecord(DSRecordParam):
    id: Required[str]
    """Identifier"""


class PutHTTPSRecord(HTTPSRecordParam):
    id: Required[str]
    """Identifier"""


class PutLOCRecord(LOCRecordParam):
    id: Required[str]
    """Identifier"""


class PutMXRecord(MXRecordParam):
    id: Required[str]
    """Identifier"""


class PutNAPTRRecord(NAPTRRecordParam):
    id: Required[str]
    """Identifier"""


class PutNSRecord(NSRecordParam):
    id: Required[str]
    """Identifier"""


class PutOpenpgpkeyRecord(TypedDict, total=False):
    id: Required[str]
    """Identifier"""

    content: Required[str]
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: Required[str]
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Required[Literal["OPENPGPKEY"]]
    """Record type."""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    proxied: bool
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTLParam
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


class PutPTRRecord(PTRRecordParam):
    id: Required[str]
    """Identifier"""


class PutSMIMEARecord(SMIMEARecordParam):
    id: Required[str]
    """Identifier"""


class PutSRVRecord(SRVRecordParam):
    id: Required[str]
    """Identifier"""


class PutSSHFPRecord(SSHFPRecordParam):
    id: Required[str]
    """Identifier"""


class PutSVCBRecord(SVCBRecordParam):
    id: Required[str]
    """Identifier"""


class PutTLSARecord(TLSARecordParam):
    id: Required[str]
    """Identifier"""


class PutTXTRecord(TXTRecordParam):
    id: Required[str]
    """Identifier"""


class PutURIRecord(URIRecordParam):
    id: Required[str]
    """Identifier"""


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
