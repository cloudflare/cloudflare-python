# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags
from .record_metadata import RecordMetadata

__all__ = ["NAPTRRecord", "Data"]


class Data(BaseModel):
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


class NAPTRRecord(BaseModel):
    data: Data
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

    meta: Optional[RecordMetadata] = None
    """Extra Cloudflare-specific information about the record."""

    modified_on: Optional[datetime] = None
    """When the record was last modified."""

    proxiable: Optional[bool] = None
    """Whether the record can be proxied by Cloudflare or not."""

    tags: Optional[List[RecordTags]] = None
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: Optional[TTL] = None
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    zone_id: Optional[str] = None
    """Identifier"""

    zone_name: Optional[str] = None
    """The domain of the record."""
