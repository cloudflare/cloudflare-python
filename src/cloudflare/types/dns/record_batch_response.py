# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .ttl import TTL
from ..._models import BaseModel
from .record_tags import RecordTags

__all__ = [
    "RecordBatchResponse",
    "Delete",
    "DeleteSettings",
    "Patch",
    "PatchSettings",
    "Post",
    "PostSettings",
    "Put",
    "PutSettings",
]


class DeleteSettings(BaseModel):
    flatten_cname: Optional[bool] = None
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class Delete(BaseModel):
    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

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

    settings: DeleteSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class PatchSettings(BaseModel):
    flatten_cname: Optional[bool] = None
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class Patch(BaseModel):
    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

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

    settings: PatchSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class PostSettings(BaseModel):
    flatten_cname: Optional[bool] = None
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class Post(BaseModel):
    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

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

    settings: PostSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class PutSettings(BaseModel):
    flatten_cname: Optional[bool] = None
    """
    If enabled, causes the CNAME record to be resolved externally and the resulting
    address records (e.g., A and AAAA) to be returned instead of the CNAME record
    itself. This setting has no effect on proxied records, which are always
    flattened.
    """


class Put(BaseModel):
    id: str
    """Identifier"""

    comment: str
    """Comments or notes about the DNS record.

    This field has no effect on DNS responses.
    """

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

    settings: PutSettings
    """Settings for the DNS record."""

    tags: List[RecordTags]
    """Custom tags for the DNS record. This field has no effect on DNS responses."""

    ttl: TTL
    """Time To Live (TTL) of the DNS record in seconds.

    Setting to 1 means 'automatic'. Value must be between 60 and 86400, with the
    minimum reduced to 30 for Enterprise zones.
    """

    comment_modified_on: Optional[datetime] = None
    """When the record comment was last modified. Omitted if there is no comment."""

    tags_modified_on: Optional[datetime] = None
    """When the record tags were last modified. Omitted if there are no tags."""


class RecordBatchResponse(BaseModel):
    deletes: Optional[List[Delete]] = None

    patches: Optional[List[Patch]] = None

    posts: Optional[List[Post]] = None

    puts: Optional[List[Put]] = None
