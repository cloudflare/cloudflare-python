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
    "DNSRecordGetResponse",
    "DNSRecordsARecord",
    "DNSRecordsARecordMeta",
    "DNSRecordsAaaaRecord",
    "DNSRecordsAaaaRecordMeta",
    "DNSRecordsCaaRecord",
    "DNSRecordsCaaRecordData",
    "DNSRecordsCaaRecordMeta",
    "DNSRecordsCertRecord",
    "DNSRecordsCertRecordData",
    "DNSRecordsCertRecordMeta",
    "DNSRecordsCnameRecord",
    "DNSRecordsCnameRecordMeta",
    "DNSRecordsDnskeyRecord",
    "DNSRecordsDnskeyRecordData",
    "DNSRecordsDnskeyRecordMeta",
    "DNSRecordsDsRecord",
    "DNSRecordsDsRecordData",
    "DNSRecordsDsRecordMeta",
    "DNSRecordsHTTPsRecord",
    "DNSRecordsHTTPsRecordData",
    "DNSRecordsHTTPsRecordMeta",
    "DNSRecordsLocRecord",
    "DNSRecordsLocRecordData",
    "DNSRecordsLocRecordMeta",
    "DNSRecordsMxRecord",
    "DNSRecordsMxRecordMeta",
    "DNSRecordsNaptrRecord",
    "DNSRecordsNaptrRecordData",
    "DNSRecordsNaptrRecordMeta",
    "DNSRecordsNsRecord",
    "DNSRecordsNsRecordMeta",
    "DNSRecordsPtrRecord",
    "DNSRecordsPtrRecordMeta",
    "DNSRecordsSmimeaRecord",
    "DNSRecordsSmimeaRecordData",
    "DNSRecordsSmimeaRecordMeta",
    "DNSRecordsSrvRecord",
    "DNSRecordsSrvRecordData",
    "DNSRecordsSrvRecordMeta",
    "DNSRecordsSshfpRecord",
    "DNSRecordsSshfpRecordData",
    "DNSRecordsSshfpRecordMeta",
    "DNSRecordsSvcbRecord",
    "DNSRecordsSvcbRecordData",
    "DNSRecordsSvcbRecordMeta",
    "DNSRecordsTlsaRecord",
    "DNSRecordsTlsaRecordData",
    "DNSRecordsTlsaRecordMeta",
    "DNSRecordsTxtRecord",
    "DNSRecordsTxtRecordMeta",
    "DNSRecordsUriRecord",
    "DNSRecordsUriRecordData",
    "DNSRecordsUriRecordMeta",
]


class DNSRecordsARecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsARecord(BaseModel):
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

    meta: Optional[DNSRecordsARecordMeta] = None
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


class DNSRecordsAaaaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsAaaaRecord(BaseModel):
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

    meta: Optional[DNSRecordsAaaaRecordMeta] = None
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


class DNSRecordsCaaRecordData(BaseModel):
    flags: Optional[float] = None
    """Flags for the CAA record."""

    tag: Optional[str] = None
    """Name of the property controlled by this record (e.g.: issue, issuewild, iodef)."""

    value: Optional[str] = None
    """Value of the record. This field's semantics depend on the chosen tag."""


class DNSRecordsCaaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsCaaRecord(BaseModel):
    data: DNSRecordsCaaRecordData
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

    meta: Optional[DNSRecordsCaaRecordMeta] = None
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


class DNSRecordsCertRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    certificate: Optional[str] = None
    """Certificate."""

    key_tag: Optional[float] = None
    """Key Tag."""

    type: Optional[float] = None
    """Type."""


class DNSRecordsCertRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsCertRecord(BaseModel):
    data: DNSRecordsCertRecordData
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

    meta: Optional[DNSRecordsCertRecordMeta] = None
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


class DNSRecordsCnameRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsCnameRecord(BaseModel):
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

    meta: Optional[DNSRecordsCnameRecordMeta] = None
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


class DNSRecordsDnskeyRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    flags: Optional[float] = None
    """Flags."""

    protocol: Optional[float] = None
    """Protocol."""

    public_key: Optional[str] = None
    """Public Key."""


class DNSRecordsDnskeyRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsDnskeyRecord(BaseModel):
    data: DNSRecordsDnskeyRecordData
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

    meta: Optional[DNSRecordsDnskeyRecordMeta] = None
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


class DNSRecordsDsRecordData(BaseModel):
    algorithm: Optional[float] = None
    """Algorithm."""

    digest: Optional[str] = None
    """Digest."""

    digest_type: Optional[float] = None
    """Digest Type."""

    key_tag: Optional[float] = None
    """Key Tag."""


class DNSRecordsDsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsDsRecord(BaseModel):
    data: DNSRecordsDsRecordData
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

    meta: Optional[DNSRecordsDsRecordMeta] = None
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


class DNSRecordsHTTPsRecordData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class DNSRecordsHTTPsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsHTTPsRecord(BaseModel):
    data: DNSRecordsHTTPsRecordData
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

    meta: Optional[DNSRecordsHTTPsRecordMeta] = None
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


class DNSRecordsLocRecordData(BaseModel):
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


class DNSRecordsLocRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsLocRecord(BaseModel):
    data: DNSRecordsLocRecordData
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

    meta: Optional[DNSRecordsLocRecordMeta] = None
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


class DNSRecordsMxRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsMxRecord(BaseModel):
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

    meta: Optional[DNSRecordsMxRecordMeta] = None
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


class DNSRecordsNaptrRecordData(BaseModel):
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


class DNSRecordsNaptrRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsNaptrRecord(BaseModel):
    data: DNSRecordsNaptrRecordData
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

    meta: Optional[DNSRecordsNaptrRecordMeta] = None
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


class DNSRecordsNsRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsNsRecord(BaseModel):
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

    meta: Optional[DNSRecordsNsRecordMeta] = None
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


class DNSRecordsPtrRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsPtrRecord(BaseModel):
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

    meta: Optional[DNSRecordsPtrRecordMeta] = None
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


class DNSRecordsSmimeaRecordData(BaseModel):
    certificate: Optional[str] = None
    """Certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class DNSRecordsSmimeaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsSmimeaRecord(BaseModel):
    data: DNSRecordsSmimeaRecordData
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

    meta: Optional[DNSRecordsSmimeaRecordMeta] = None
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


class DNSRecordsSrvRecordData(BaseModel):
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


class DNSRecordsSrvRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsSrvRecord(BaseModel):
    data: DNSRecordsSrvRecordData
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

    meta: Optional[DNSRecordsSrvRecordMeta] = None
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


class DNSRecordsSshfpRecordData(BaseModel):
    algorithm: Optional[float] = None
    """algorithm."""

    fingerprint: Optional[str] = None
    """fingerprint."""

    type: Optional[float] = None
    """type."""


class DNSRecordsSshfpRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsSshfpRecord(BaseModel):
    data: DNSRecordsSshfpRecordData
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

    meta: Optional[DNSRecordsSshfpRecordMeta] = None
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


class DNSRecordsSvcbRecordData(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class DNSRecordsSvcbRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsSvcbRecord(BaseModel):
    data: DNSRecordsSvcbRecordData
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

    meta: Optional[DNSRecordsSvcbRecordMeta] = None
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


class DNSRecordsTlsaRecordData(BaseModel):
    certificate: Optional[str] = None
    """certificate."""

    matching_type: Optional[float] = None
    """Matching Type."""

    selector: Optional[float] = None
    """Selector."""

    usage: Optional[float] = None
    """Usage."""


class DNSRecordsTlsaRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsTlsaRecord(BaseModel):
    data: DNSRecordsTlsaRecordData
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

    meta: Optional[DNSRecordsTlsaRecordMeta] = None
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


class DNSRecordsTxtRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsTxtRecord(BaseModel):
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

    meta: Optional[DNSRecordsTxtRecordMeta] = None
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


class DNSRecordsUriRecordData(BaseModel):
    content: Optional[str] = None
    """The record content."""

    weight: Optional[float] = None
    """The record weight."""


class DNSRecordsUriRecordMeta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """

    source: Optional[str] = None
    """Where the record originated from."""


class DNSRecordsUriRecord(BaseModel):
    data: DNSRecordsUriRecordData
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

    meta: Optional[DNSRecordsUriRecordMeta] = None
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


DNSRecordGetResponse = Union[
    DNSRecordsARecord,
    DNSRecordsAaaaRecord,
    DNSRecordsCaaRecord,
    DNSRecordsCertRecord,
    DNSRecordsCnameRecord,
    DNSRecordsDnskeyRecord,
    DNSRecordsDsRecord,
    DNSRecordsHTTPsRecord,
    DNSRecordsLocRecord,
    DNSRecordsMxRecord,
    DNSRecordsNaptrRecord,
    DNSRecordsNsRecord,
    DNSRecordsPtrRecord,
    DNSRecordsSmimeaRecord,
    DNSRecordsSrvRecord,
    DNSRecordsSshfpRecord,
    DNSRecordsSvcbRecord,
    DNSRecordsTlsaRecord,
    DNSRecordsTxtRecord,
    DNSRecordsUriRecord,
]
