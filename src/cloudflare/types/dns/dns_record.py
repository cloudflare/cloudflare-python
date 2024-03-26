# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "DNSRecord",
    "A",
    "AMeta",
    "AAAA",
    "AAAAMeta",
    "CAA",
    "CAAData",
    "CAAMeta",
    "CERT",
    "CERTData",
    "CERTMeta",
    "CNAME",
    "CNAMEMeta",
    "DNSKEY",
    "DNSKEYData",
    "DNSKEYMeta",
    "DS",
    "DSData",
    "DSMeta",
    "HTTPS",
    "HTTPSData",
    "HTTPSMeta",
    "LOC",
    "LOCData",
    "LOCMeta",
    "MX",
    "MXMeta",
    "NAPTR",
    "NAPTRData",
    "NAPTRMeta",
    "NS",
    "NSMeta",
    "PTR",
    "PTRMeta",
    "SMIMEA",
    "SMIMEAData",
    "SMIMEAMeta",
    "SRV",
    "SRVData",
    "SRVMeta",
    "SSHFP",
    "SSHFPData",
    "SSHFPMeta",
    "SVCB",
    "SVCBData",
    "SVCBMeta",
    "TLSA",
    "TLSAData",
    "TLSAMeta",
    "TXT",
    "TXTMeta",
    "URI",
    "URIData",
    "URIMeta",
]


class AMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class A(BaseModel):
    content: str
    """A valid IPv4 address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["A"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[AMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class AAAAMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class AAAA(BaseModel):
    content: str
    """A valid IPv6 address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["AAAA"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[AAAAMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class CAAData(BaseModel):
    flags: Optional[float] = None
    """Flags for the CAA record."""

    tag: Optional[str] = None
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: Optional[str] = None
    """Value of the record. This field's semantics depend on the chosen tag."""


class CAAMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class CAA(BaseModel):
    data: CAAData
    """Components of a CAA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["CAA"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted CAA content. See 'data' to set CAA properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[CAAMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class CERTData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    certificate: Optional[str] = None
    """Certificate."""

    key_tag: Optional[float] = None
    """Key Tag."""

    type: Optional[float] = None
    """Type."""


class CERTMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class CERT(BaseModel):
    data: CERTData
    """Components of a CERT record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["CERT"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted CERT content. See 'data' to set CERT properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[CERTMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class CNAMEMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class CNAME(BaseModel):
    content: object
    """A valid hostname. Must not match the record's name."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["CNAME"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[CNAMEMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    proxied: Optional[bool] = None
    """
    Whether the record is receiving the performance and security benefits of
    Cloudflare.
    """

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class DNSKEYData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    flags: Optional[float] = None
    """Flags."""

    protocol: Optional[float] = None
    """Protocol."""

    public_key: Optional[str] = None
    """Public Key."""


class DNSKEYMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSKEY(BaseModel):
    data: DNSKEYData
    """Components of a DNSKEY record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["DNSKEY"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted DNSKEY content. See 'data' to set DNSKEY properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[DNSKEYMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class DSData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    digest: Optional[str] = None
    """Digest."""

    digest_type: Optional[float] = None
    """Digest Type."""

    key_tag: Optional[float] = None
    """Key Tag."""


class DSMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DS(BaseModel):
    data: DSData
    """Components of a DS record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["DS"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted DS content. See 'data' to set DS properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[DSMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class HTTPSData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class HTTPSMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class HTTPS(BaseModel):
    data: HTTPSData
    """Components of a HTTPS record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["HTTPS"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted HTTPS content. See 'data' to set HTTPS properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[HTTPSMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class LOCData(BaseModel):
    altitude: Optional[float] = None
    """Altitude of location in meters."""

    lat_degrees: Optional[float] = None
    """Degrees of latitude."""

    lat_direction: Optional[Literal["N", "S"]] = None
    """Latitude direction."""

    lat_minutes: Optional[float] = None
    """Minutes of latitude."""

    lat_seconds: Optional[float] = None
    """Seconds of latitude."""

    long_degrees: Optional[float] = None
    """Degrees of longitude."""

    long_direction: Optional[Literal["E", "W"]] = None
    """Longitude direction."""

    long_minutes: Optional[float] = None
    """Minutes of longitude."""

    long_seconds: Optional[float] = None
    """Seconds of longitude."""

    precision_horz: Optional[float] = None
    """Horizontal precision of location."""

    precision_vert: Optional[float] = None
    """Vertical precision of location."""

    size: Optional[float] = None
    """Size of location in meters."""


class LOCMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class LOC(BaseModel):
    data: LOCData
    """Components of a LOC record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["LOC"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted LOC content. See 'data' to set LOC properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[LOCMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class MXMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class MX(BaseModel):
    content: str
    """A valid mail server hostname."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Literal["MX"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[MXMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class NAPTRData(BaseModel):
    flags: Optional[str] = None
    """Flags."""

    order: Optional[float] = None
    """Order."""

    preference: Optional[float] = None
    """Preference."""

    regex: Optional[str] = None
    """Regex."""

    replacement: Optional[str] = None
    """Replacement."""

    service: Optional[str] = None
    """Service."""


class NAPTRMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class NAPTR(BaseModel):
    data: NAPTRData
    """Components of a NAPTR record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["NAPTR"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted NAPTR content. See 'data' to set NAPTR properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[NAPTRMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class NSMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class NS(BaseModel):
    content: str
    """A valid name server host name."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["NS"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[NSMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class PTRMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class PTR(BaseModel):
    content: str
    """Domain name pointing to the address."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["PTR"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[PTRMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class SMIMEAData(BaseModel):
    certificate: Optional[str] = None
    """Certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class SMIMEAMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class SMIMEA(BaseModel):
    data: SMIMEAData
    """Components of a SMIMEA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["SMIMEA"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted SMIMEA content. See 'data' to set SMIMEA properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[SMIMEAMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class SRVData(BaseModel):
    name: Optional[str] = None
    """A valid hostname.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field represents the remainder of the full 'name' after the service and
    protocol.
    """

    port: Optional[float] = None
    """The port of the service."""

    priority: Optional[float] = None
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    proto: Optional[str] = None
    """A valid protocol, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the second label of that 'name'.
    """

    service: Optional[str] = None
    """A service type, prefixed with an underscore.

    Deprecated in favor of the regular 'name' outside the data map. This data map
    field normally represents the first label of that 'name'.
    """

    target: Optional[str] = None
    """A valid hostname."""

    weight: Optional[float] = None
    """The record weight."""


class SRVMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class SRV(BaseModel):
    data: SRVData
    """Components of a SRV record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode.

    For SRV records, the first label is normally a service and the second a protocol
    name, each starting with an underscore.
    """

    type: Literal["SRV"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Priority, weight, port, and SRV target.

    See 'data' for setting the individual component values.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[SRVMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class SSHFPData(BaseModel):
    algorithm: Optional[float] = None
    """algorithm."""

    fingerprint: Optional[str] = None
    """fingerprint."""

    type: Optional[float] = None
    """type."""


class SSHFPMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class SSHFP(BaseModel):
    data: SSHFPData
    """Components of a SSHFP record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["SSHFP"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted SSHFP content. See 'data' to set SSHFP properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[SSHFPMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class SVCBData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class SVCBMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class SVCB(BaseModel):
    data: SVCBData
    """Components of a SVCB record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["SVCB"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted SVCB content. See 'data' to set SVCB properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[SVCBMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class TLSAData(BaseModel):
    certificate: Optional[str] = None
    """certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class TLSAMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class TLSA(BaseModel):
    data: TLSAData
    """Components of a TLSA record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["TLSA"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted TLSA content. See 'data' to set TLSA properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[TLSAMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class TXTMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class TXT(BaseModel):
    content: str
    """Text content for the record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    type: Literal["TXT"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[TXTMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


class URIData(BaseModel):
    content: Optional[str] = None
    """The record content."""

    weight: Optional[float] = None
    """The record weight."""


class URIMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class URI(BaseModel):
    data: URIData
    """Components of a URI record."""

    name: str
    """DNS record name (or @ for the zone apex) in Punycode."""

    priority: float
    """Required for MX, SRV and URI records; unused by other record types.

    Records with lower priorities are preferred.
    """

    type: Literal["URI"]
    """Record type."""

    id: Optional[str] = None
    """Identifier"""

    comment: Optional[str] = None
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    content: Optional[str] = None
    """Formatted URI content. See 'data' to set URI properties."""

    created_on: Optional[datetime] = None
    """When the record was created."""

    locked: Optional[bool] = None
    """
    Whether this record can be modified/deleted (true means it's managed by
    Cloudflare).
    """

    meta: Optional[URIMeta] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[str]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Union[float, Literal[1], None] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""


DNSRecord = Annotated[
    Union[
        A, AAAA, CAA, CERT, CNAME, DNSKEY, DS, HTTPS, LOC, MX, NAPTR, NS, PTR, SMIMEA, SRV, SSHFP, SVCB, TLSA, TXT, URI
    ],
    PropertyInfo(discriminator="type"),
]
