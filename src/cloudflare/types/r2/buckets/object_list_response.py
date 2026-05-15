# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ObjectListResponse", "HTTPMetadata"]


class HTTPMetadata(BaseModel):
    """HTTP metadata associated with an R2 object."""

    cache_control: Optional[str] = FieldInfo(alias="cacheControl", default=None)
    """Specifies caching behavior for the object."""

    cache_expiry: Optional[datetime] = FieldInfo(alias="cacheExpiry", default=None)
    """The date and time at which the object's cache entry expires."""

    content_disposition: Optional[str] = FieldInfo(alias="contentDisposition", default=None)
    """Specifies presentational information for the object."""

    content_encoding: Optional[str] = FieldInfo(alias="contentEncoding", default=None)
    """Specifies the content encoding applied to the object."""

    content_language: Optional[str] = FieldInfo(alias="contentLanguage", default=None)
    """The language of the object content."""

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)
    """The MIME type of the object."""


class ObjectListResponse(BaseModel):
    """Metadata for an R2 object."""

    custom_metadata: Optional[Dict[str, str]] = None
    """Custom metadata key-value pairs associated with the object."""

    etag: Optional[str] = None
    """The entity tag for the object.

    In JSON list/get responses this is the raw hex digest (without surrounding
    quotes). The HTTP `ETag` response header on Get Object follows RFC 7232 and IS
    wrapped in surrounding double-quotes.
    """

    http_metadata: Optional[HTTPMetadata] = None
    """HTTP metadata associated with an R2 object."""

    key: Optional[str] = None
    """The object key (name)."""

    last_modified: Optional[datetime] = None
    """The date and time the object was last modified."""

    size: Optional[int] = None
    """The size of the object in bytes."""

    ssec: Optional[bool] = None
    """Whether the object is encrypted with a customer-supplied encryption key."""

    storage_class: Optional[Literal["Standard", "InfrequentAccess"]] = None
    """Storage class for newly uploaded objects, unless specified otherwise."""
