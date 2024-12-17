# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuditListResponse", "Account", "Action", "Actor", "Raw", "Resource", "Zone"]


class Account(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the account."""

    name: Optional[str] = None
    """A string that identifies the account name."""


class Action(BaseModel):
    description: Optional[str] = None
    """A short description of the action performed."""

    result: Optional[str] = None
    """The result of the action, indicating success or failure."""

    time: Optional[datetime] = None
    """A timestamp indicating when the action was logged."""

    type: Optional[str] = None
    """A short string that describes the action that was performed."""


class Actor(BaseModel):
    id: Optional[str] = None
    """The ID of the actor who performed the action.

    If a user performed the action, this will be their User ID.
    """

    context: Optional[Literal["api_key", "api_token", "dash", "oauth", "origin_ca_key"]] = None

    email: Optional[str] = None
    """The email of the actor who performed the action."""

    ip_address: Optional[str] = None
    """The IP address of the request that performed the action."""

    token_id: Optional[str] = None
    """Filters by the API token ID when the actor context is an api_token."""

    token_name: Optional[str] = None
    """Filters by the API token name when the actor context is an api_token."""

    type: Optional[Literal["user", "account", "cloudflare-admin"]] = None
    """The type of actor."""


class Raw(BaseModel):
    cf_rayid: Optional[str] = FieldInfo(alias="cf_ray_id", default=None)
    """The Cloudflare Ray ID for the request."""

    method: Optional[str] = None
    """The HTTP method of the request."""

    status_code: Optional[int] = None
    """The HTTP response status code returned by the API."""

    uri: Optional[str] = None
    """The URI of the request."""

    user_agent: Optional[str] = None
    """The client's user agent string sent with the request."""


class Resource(BaseModel):
    id: Optional[str] = None
    """The unique identifier for the affected resource."""

    product: Optional[str] = None
    """The Cloudflare product associated with the resource."""

    request: Optional[object] = None

    response: Optional[object] = None

    scope: Optional[object] = None
    """The scope of the resource."""

    type: Optional[str] = None
    """The type of the resource."""


class Zone(BaseModel):
    id: Optional[str] = None
    """A string that identifies the zone id."""

    name: Optional[str] = None
    """A string that identifies the zone name."""


class AuditListResponse(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the audit log entry."""

    account: Optional[Account] = None
    """Contains account related information."""

    action: Optional[Action] = None
    """Provides information about the action performed."""

    actor: Optional[Actor] = None
    """Provides details about the actor who performed the action."""

    raw: Optional[Raw] = None
    """Provides raw information about the request and response."""

    resource: Optional[Resource] = None
    """Provides details about the affected resource."""

    zone: Optional[Zone] = None
    """Provides details about the zone affected by the action."""
