# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .login_design import LoginDesign

__all__ = ["Organization", "CustomPages", "MfaConfig", "MfaSSHPivKeyRequirements"]


class CustomPages(BaseModel):
    forbidden: Optional[str] = None
    """
    The uid of the custom page to use when a user is denied access after failing a
    non-identity rule.
    """

    identity_denied: Optional[str] = None
    """The uid of the custom page to use when a user is denied access."""


class MfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings for an organization."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key", "ssh_piv_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    amr_matching_session_duration: Optional[str] = None
    """
    Allows a user to skip MFA via Authentication Method Reference (AMR) matching
    when the AMR claim provided by the IdP the user used to authenticate contains
    "mfa". Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30
    days).
    """

    required_aaguids: Optional[str] = None
    """Specifies a Cloudflare List of required FIDO2 authenticator device AAGUIDs."""

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class MfaSSHPivKeyRequirements(BaseModel):
    """Configures SSH PIV key requirements for MFA using hardware security keys."""

    pin_policy: Optional[Literal["never", "once", "always"]] = None
    """Defines when a PIN is required to use the SSH key.

    Valid values: `never` (no PIN required), `once` (PIN required once per session),
    `always` (PIN required for each use).
    """

    require_fips_device: Optional[bool] = None
    """
    Requires the SSH PIV key to be stored on a FIPS 140-2 Level 1 or higher
    validated device.
    """

    ssh_key_size: Optional[List[Literal[256, 384, 521, 2048, 3072, 4096]]] = None
    """Specifies the allowed SSH key sizes in bits.

    Valid sizes depend on key type. Ed25519 has a fixed key size and does not accept
    this parameter.
    """

    ssh_key_type: Optional[List[Literal["ecdsa", "ed25519", "rsa"]]] = None
    """Specifies the allowed SSH key types.

    Valid values are `ecdsa`, `ed25519`, and `rsa`.
    """

    touch_policy: Optional[Literal["never", "always", "cached"]] = None
    """Defines when physical touch is required to use the SSH key.

    Valid values: `never` (no touch required), `always` (touch required for each
    use), `cached` (touch cached for 15 seconds).
    """


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

    custom_pages: Optional[CustomPages] = None

    deny_unmatched_requests: Optional[bool] = None
    """
    Determines whether to deny all requests to Cloudflare-protected resources that
    lack an associated Access application. If enabled, you must explicitly configure
    an Access application and policy to allow traffic to your Cloudflare-protected
    resources. For domains you want to be public across all subdomains, add the
    domain to the `deny_unmatched_requests_exempted_zone_names` array.
    """

    deny_unmatched_requests_exempted_zone_names: Optional[List[str]] = None
    """Contains zone names to exempt from the `deny_unmatched_requests` feature.

    Requests to a subdomain in an exempted zone will block unauthenticated traffic
    by default if there is a configured Access application and policy that matches
    the request.
    """

    is_ui_read_only: Optional[bool] = None
    """Lock all settings as Read-Only in the Dashboard, regardless of user permission.

    Updates may only be made via the API or Terraform for this account when enabled.
    """

    login_design: Optional[LoginDesign] = None

    mfa_config: Optional[MfaConfig] = None
    """Configures multi-factor authentication (MFA) settings for an organization."""

    mfa_required_for_all_apps: Optional[bool] = None
    """Determines whether global MFA settings apply to applications by default.

    The organization must have MFA enabled with at least one authentication method
    and a session duration configured.
    """

    mfa_ssh_piv_key_requirements: Optional[MfaSSHPivKeyRequirements] = None
    """Configures SSH PIV key requirements for MFA using hardware security keys."""

    name: Optional[str] = None
    """The name of your Zero Trust organization."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    ui_read_only_toggle_reason: Optional[str] = None
    """A description of the reason why the UI read only field is being toggled."""

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
