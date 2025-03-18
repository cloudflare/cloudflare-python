# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ZeroTrustGroup", "Meta"]


class Meta(BaseModel):
    created: Optional[datetime] = None
    """The timestamp of when the SCIM resource was created."""

    last_modified: Optional[datetime] = FieldInfo(alias="lastModified", default=None)
    """The timestamp of when the SCIM resource was last modified."""


class ZeroTrustGroup(BaseModel):
    id: Optional[str] = None
    """The unique Cloudflare-generated Id of the SCIM resource."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """The display name of the SCIM Group resource."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """The IdP-generated Id of the SCIM resource."""

    meta: Optional[Meta] = None
    """The metadata of the SCIM resource."""

    schemas: Optional[List[str]] = None
    """
    The list of URIs which indicate the attributes contained within a SCIM resource.
    """
