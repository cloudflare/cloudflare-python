# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List, Union

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = [
    "DNSRecordListResponse",
    "DNSRecordListResponseItem",
    "DNSRecordListResponseItemDNSRecordsARecord",
    "DNSRecordListResponseItemDNSRecordsARecordMeta",
    "DNSRecordListResponseItemDNSRecordsAaaaRecord",
    "DNSRecordListResponseItemDNSRecordsAaaaRecordMeta",
    "DNSRecordListResponseItemDNSRecordsCaaRecord",
    "DNSRecordListResponseItemDNSRecordsCaaRecordData",
    "DNSRecordListResponseItemDNSRecordsCaaRecordMeta",
    "DNSRecordListResponseItemDNSRecordsCertRecord",
    "DNSRecordListResponseItemDNSRecordsCertRecordData",
    "DNSRecordListResponseItemDNSRecordsCertRecordMeta",
    "DNSRecordListResponseItemDNSRecordsCnameRecord",
    "DNSRecordListResponseItemDNSRecordsCnameRecordMeta",
    "DNSRecordListResponseItemDNSRecordsDnskeyRecord",
    "DNSRecordListResponseItemDNSRecordsDnskeyRecordData",
    "DNSRecordListResponseItemDNSRecordsDnskeyRecordMeta",
    "DNSRecordListResponseItemDNSRecordsDsRecord",
    "DNSRecordListResponseItemDNSRecordsDsRecordData",
    "DNSRecordListResponseItemDNSRecordsDsRecordMeta",
    "DNSRecordListResponseItemDNSRecordsHTTPsRecord",
    "DNSRecordListResponseItemDNSRecordsHTTPsRecordData",
    "DNSRecordListResponseItemDNSRecordsHTTPsRecordMeta",
    "DNSRecordListResponseItemDNSRecordsLocRecord",
    "DNSRecordListResponseItemDNSRecordsLocRecordData",
    "DNSRecordListResponseItemDNSRecordsLocRecordMeta",
    "DNSRecordListResponseItemDNSRecordsMxRecord",
    "DNSRecordListResponseItemDNSRecordsMxRecordMeta",
    "DNSRecordListResponseItemDNSRecordsNaptrRecord",
    "DNSRecordListResponseItemDNSRecordsNaptrRecordData",
    "DNSRecordListResponseItemDNSRecordsNaptrRecordMeta",
    "DNSRecordListResponseItemDNSRecordsNsRecord",
    "DNSRecordListResponseItemDNSRecordsNsRecordMeta",
    "DNSRecordListResponseItemDNSRecordsPtrRecord",
    "DNSRecordListResponseItemDNSRecordsPtrRecordMeta",
    "DNSRecordListResponseItemDNSRecordsSmimeaRecord",
    "DNSRecordListResponseItemDNSRecordsSmimeaRecordData",
    "DNSRecordListResponseItemDNSRecordsSmimeaRecordMeta",
    "DNSRecordListResponseItemDNSRecordsSrvRecord",
    "DNSRecordListResponseItemDNSRecordsSrvRecordData",
    "DNSRecordListResponseItemDNSRecordsSrvRecordMeta",
    "DNSRecordListResponseItemDNSRecordsSshfpRecord",
    "DNSRecordListResponseItemDNSRecordsSshfpRecordData",
    "DNSRecordListResponseItemDNSRecordsSshfpRecordMeta",
    "DNSRecordListResponseItemDNSRecordsSvcbRecord",
    "DNSRecordListResponseItemDNSRecordsSvcbRecordData",
    "DNSRecordListResponseItemDNSRecordsSvcbRecordMeta",
    "DNSRecordListResponseItemDNSRecordsTlsaRecord",
    "DNSRecordListResponseItemDNSRecordsTlsaRecordData",
    "DNSRecordListResponseItemDNSRecordsTlsaRecordMeta",
    "DNSRecordListResponseItemDNSRecordsTxtRecord",
    "DNSRecordListResponseItemDNSRecordsTxtRecordMeta",
    "DNSRecordListResponseItemDNSRecordsUriRecord",
    "DNSRecordListResponseItemDNSRecordsUriRecordData",
    "DNSRecordListResponseItemDNSRecordsUriRecordMeta",
]


class DNSRecordListResponseItemDNSRecordsARecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsARecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsARecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsAaaaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsAaaaRecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsAaaaRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsCaaRecordData(BaseModel):
    flags: Optional[float] = None
    """Flags for the CAA record."""

    tag: Optional[str] = None
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: Optional[str] = None
    """Value of the record. This field's semantics depend on the chosen tag."""


class DNSRecordListResponseItemDNSRecordsCaaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsCaaRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsCaaRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsCaaRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsCertRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    certificate: Optional[str] = None
    """Certificate."""

    key_tag: Optional[float] = None
    """Key Tag."""

    type: Optional[float] = None
    """Type."""


class DNSRecordListResponseItemDNSRecordsCertRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsCertRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsCertRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsCertRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsCnameRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsCnameRecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsCnameRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsDnskeyRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    flags: Optional[float] = None
    """Flags."""

    protocol: Optional[float] = None
    """Protocol."""

    public_key: Optional[str] = None
    """Public Key."""


class DNSRecordListResponseItemDNSRecordsDnskeyRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsDnskeyRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsDnskeyRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsDnskeyRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsDsRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    digest: Optional[str] = None
    """Digest."""

    digest_type: Optional[float] = None
    """Digest Type."""

    key_tag: Optional[float] = None
    """Key Tag."""


class DNSRecordListResponseItemDNSRecordsDsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsDsRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsDsRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsDsRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsHTTPsRecordData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class DNSRecordListResponseItemDNSRecordsHTTPsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsHTTPsRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsHTTPsRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsHTTPsRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsLocRecordData(BaseModel):
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


class DNSRecordListResponseItemDNSRecordsLocRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsLocRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsLocRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsLocRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsMxRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsMxRecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsMxRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsNaptrRecordData(BaseModel):
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


class DNSRecordListResponseItemDNSRecordsNaptrRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsNaptrRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsNaptrRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsNaptrRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsNsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsNsRecord(BaseModel):
    content: object
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsNsRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsPtrRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsPtrRecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsPtrRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsSmimeaRecordData(BaseModel):
    certificate: Optional[str] = None
    """Certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class DNSRecordListResponseItemDNSRecordsSmimeaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsSmimeaRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsSmimeaRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsSmimeaRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsSrvRecordData(BaseModel):
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


class DNSRecordListResponseItemDNSRecordsSrvRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsSrvRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsSrvRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsSrvRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsSshfpRecordData(BaseModel):
    algorithm: Optional[float] = None
    """algorithm."""

    fingerprint: Optional[str] = None
    """fingerprint."""

    type: Optional[float] = None
    """type."""


class DNSRecordListResponseItemDNSRecordsSshfpRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsSshfpRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsSshfpRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsSshfpRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsSvcbRecordData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class DNSRecordListResponseItemDNSRecordsSvcbRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsSvcbRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsSvcbRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsSvcbRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsTlsaRecordData(BaseModel):
    certificate: Optional[str] = None
    """certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class DNSRecordListResponseItemDNSRecordsTlsaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsTlsaRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsTlsaRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsTlsaRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsTxtRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsTxtRecord(BaseModel):
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsTxtRecordMeta] = None
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


class DNSRecordListResponseItemDNSRecordsUriRecordData(BaseModel):
    content: Optional[str] = None
    """The record content."""

    weight: Optional[float] = None
    """The record weight."""


class DNSRecordListResponseItemDNSRecordsUriRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordListResponseItemDNSRecordsUriRecord(BaseModel):
    data: DNSRecordListResponseItemDNSRecordsUriRecordData
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

    meta: Optional[DNSRecordListResponseItemDNSRecordsUriRecordMeta] = None
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


DNSRecordListResponseItem = Union[
    DNSRecordListResponseItemDNSRecordsARecord,
    DNSRecordListResponseItemDNSRecordsAaaaRecord,
    DNSRecordListResponseItemDNSRecordsCaaRecord,
    DNSRecordListResponseItemDNSRecordsCertRecord,
    DNSRecordListResponseItemDNSRecordsCnameRecord,
    DNSRecordListResponseItemDNSRecordsDnskeyRecord,
    DNSRecordListResponseItemDNSRecordsDsRecord,
    DNSRecordListResponseItemDNSRecordsHTTPsRecord,
    DNSRecordListResponseItemDNSRecordsLocRecord,
    DNSRecordListResponseItemDNSRecordsMxRecord,
    DNSRecordListResponseItemDNSRecordsNaptrRecord,
    DNSRecordListResponseItemDNSRecordsNsRecord,
    DNSRecordListResponseItemDNSRecordsPtrRecord,
    DNSRecordListResponseItemDNSRecordsSmimeaRecord,
    DNSRecordListResponseItemDNSRecordsSrvRecord,
    DNSRecordListResponseItemDNSRecordsSshfpRecord,
    DNSRecordListResponseItemDNSRecordsSvcbRecord,
    DNSRecordListResponseItemDNSRecordsTlsaRecord,
    DNSRecordListResponseItemDNSRecordsTxtRecord,
    DNSRecordListResponseItemDNSRecordsUriRecord,
]

DNSRecordListResponse = List[DNSRecordListResponseItem]
