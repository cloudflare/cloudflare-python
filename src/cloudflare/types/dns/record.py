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
from .record_metadata import RecordMetadata

__all__ = ["Record", "Openpgpkey"]


class Openpgpkey(BaseModel):
    content: str
    """A single Base64-encoded OpenPGP Transferable Public Key (RFC 4880 Section 11.1)"""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["OPENPGPKEY"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    meta: Optional[RecordMetadata] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """


Record: TypeAlias = Annotated[
    Union[
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
        Openpgpkey,
        PTRRecord,
        SMIMEARecord,
        SRVRecord,
        SSHFPRecord,
        SVCBRecord,
        TLSARecord,
        TXTRecord,
        URIRecord,
    ],
    PropertyInfo(discriminator="type"),
]
