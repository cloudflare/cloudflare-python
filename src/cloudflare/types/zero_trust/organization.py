# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .login_design import LoginDesign

__all__ = ["Organization", "CustomPages"]


class CustomPages(BaseModel):
    forbidden: Optional[str] = None
    """
    The uid of the custom page to use when a user is denied access after failing a
    non-identity rule.
    """

    identity_denied: Optional[str] = None
    """The uid of the custom page to use when a user is denied access."""


class Organization(BaseModel):
    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate via WARP for any application in your
    organization. Application settings will take precedence over this value.
    """

    auth_domain: Optional[str] = None
    """The unique subdomain assigned to your Zero Trust organization."""

    auto_redirect_to_identity: Optional[bool] = None
    """
    When set to `true`, users skip the identity provider selection step during
    login.
    """

    created_at: Optional[datetime] = None

    custom_pages: Optional[CustomPages] = None

    is_ui_read_only: Optional[bool] = None
    """Lock all settings as Read-Only in the Dashboard, regardless of user permission.

    Updates may only be made via the API or Terraform for this account when enabled.
    """

    login_design: Optional[LoginDesign] = None

    name: Optional[str] = None
    """The name of your Zero Trust organization."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    ui_read_only_toggle_reason: Optional[str] = None
    """A description of the reason why the UI read only field is being toggled."""

    updated_at: Optional[datetime] = None

    user_seat_expiration_inactive_time: Optional[str] = None
    """The amount of time a user seat is inactive before it expires.

    When the user seat exceeds the set time of inactivity, the user is removed as an
    active seat and no longer counts against your Teams seat count. Minimum value
    for this setting is 1 month (730h). Must be in the format `300ms` or `2h45m`.
    Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.
    """

    warp_auth_session_duration: Optional[str] = None
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `30m` or `2h45m`. Valid time units are: m, h.
    """
