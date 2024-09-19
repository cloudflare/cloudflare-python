# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = ["RecordListResponse", "Meta"]


class Meta(BaseModel):
    auto_added: Optional[bool] = None
    """
    Will exist if Cloudflare automatically added this DNS record during initial
    setup.
    """


class RecordListResponse(BaseModel):
    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

    comment_modified_on: datetime
    """When the record comment was last modified."""

    created_on: datetime
    """When the record was created."""

    meta: Meta
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

    tags_modified_on: datetime
    """When the record tags were last modified."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """
