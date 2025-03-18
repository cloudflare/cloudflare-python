# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AccessRequest"]


class AccessRequest(BaseModel):
    action: Optional[str] = None
    """The event that occurred, such as a login attempt."""

    allowed: Optional[bool] = None
    """The result of the authentication event."""

    app_domain: Optional[str] = None
    """The URL of the Access application."""

    app_uid: Optional[str] = None
    """The unique identifier for the Access application."""

    connection: Optional[str] = None
    """The IdP used to authenticate."""

    created_at: Optional[datetime] = None

    ip_address: Optional[str] = None
    """The IP address of the authenticating user."""

    rayid: Optional[str] = FieldInfo(alias="ray_id", default=None)
    """The unique identifier for the request to Cloudflare."""

    user_email: Optional[str] = None
    """The email address of the authenticating user."""
