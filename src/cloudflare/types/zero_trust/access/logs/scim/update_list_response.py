# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["UpdateListResponse"]


class UpdateListResponse(BaseModel):
    cf_resource_id: Optional[str] = None
    """The unique Cloudflare-generated Id of the SCIM resource."""

    error_description: Optional[str] = None
    """
    The error message which is generated when the status of the SCIM request is
    'FAILURE'.
    """

    idp_id: Optional[str] = None
    """The unique Id of the IdP that has SCIM enabled."""

    idp_resource_id: Optional[str] = None
    """The IdP-generated Id of the SCIM resource."""

    logged_at: Optional[datetime] = None

    request_body: Optional[str] = None
    """The JSON-encoded string body of the SCIM request."""

    request_method: Optional[str] = None
    """The request method of the SCIM request."""

    resource_group_name: Optional[str] = None
    """The display name of the SCIM Group resource if it exists."""

    resource_type: Optional[str] = None
    """The resource type of the SCIM request."""

    resource_user_email: Optional[str] = None
    """The email address of the SCIM User resource if it exists."""

    status: Optional[str] = None
    """The status of the SCIM request."""
