# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AccessUser", "Email", "Meta"]


class Email(BaseModel):
    primary: Optional[bool] = None
    """
    Indicates if the email address is the primary email belonging to the SCIM User
    resource.
    """

    type: Optional[str] = None
    """Indicates the type of the email address."""

    value: Optional[str] = None
    """The email address of the SCIM User resource."""


class Meta(BaseModel):
    created: Optional[datetime] = None
    """The timestamp of when the SCIM resource was created."""

    last_modified: Optional[datetime] = FieldInfo(alias="lastModified", default=None)
    """The timestamp of when the SCIM resource was last modified."""


class AccessUser(BaseModel):
    id: Optional[str] = None
    """The unique Cloudflare-generated Id of the SCIM resource."""

    active: Optional[bool] = None
    """Determines the status of the SCIM User resource."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """The name of the SCIM User resource."""

    emails: Optional[List[Email]] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)
    """The IdP-generated Id of the SCIM resource."""

    meta: Optional[Meta] = None
    """The metadata of the SCIM resource."""

    schemas: Optional[List[str]] = None
    """
    The list of URIs which indicate the attributes contained within a SCIM resource.
    """
