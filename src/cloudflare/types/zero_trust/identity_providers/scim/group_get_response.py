# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["GroupGetResponse", "Member", "Meta"]


class Member(BaseModel):
    value: str
    """The unique Cloudflare-generated Id of the member resource."""

    ref: Optional[str] = FieldInfo(alias="$ref", default=None)
    """The URI of the member resource."""

    display: Optional[str] = None
    """The display name of the member resource."""

    type: Optional[Literal["User", "Group"]] = None
    """The SCIM resource type of the member."""


class Meta(BaseModel):
    """The metadata of the SCIM resource."""

    created: Optional[datetime] = None
    """The timestamp of when the SCIM resource was created."""

    last_modified: Optional[datetime] = FieldInfo(alias="lastModified", default=None)
    """The timestamp of when the SCIM resource was last modified."""


class GroupGetResponse(BaseModel):
    id: Optional[str] = None
    """The unique Cloudflare-generated Id of the SCIM resource."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """The display name of the SCIM Group resource."""

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """The IdP-generated Id of the SCIM resource."""

    members: Optional[List[Member]] = None
    """The direct members of the SCIM Group resource."""

    meta: Optional[Meta] = None
    """The metadata of the SCIM resource."""

    schemas: Optional[List[str]] = None
    """
    The list of URIs which indicate the attributes contained within a SCIM resource.
    """
