# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from .login_design_param import LoginDesignParam

__all__ = ["OrganizationCreateParams", "MfaConfig", "MfaSSHPivKeyRequirements"]


class OrganizationCreateParams(TypedDict, total=False):
    auth_domain: Required[str]
    """The unique subdomain assigned to your Zero Trust organization."""

    name: Required[str]
    """The name of your Zero Trust organization."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate via WARP for any application in your
    organization. Application settings will take precedence over this value.
    """

    auto_redirect_to_identity: bool
    """
    When set to `true`, users skip the identity provider selection step during
    login.
    """

    deny_unmatched_requests: bool
    """
    Determines whether to deny all requests to Cloudflare-protected resources that
    lack an associated Access application. If enabled, you must explicitly configure
    an Access application and policy to allow traffic to your Cloudflare-protected
    resources. For domains you want to be public across all subdomains, add the
    domain to the `deny_unmatched_requests_exempted_zone_names` array.
    """

    deny_unmatched_requests_exempted_zone_names: SequenceNotStr[str]
    """Contains zone names to exempt from the `deny_unmatched_requests` feature.

    Requests to a subdomain in an exempted zone will block unauthenticated traffic
    by default if there is a configured Access application and policy that matches
    the request.
    """

    is_ui_read_only: bool
    """Lock all settings as Read-Only in the Dashboard, regardless of user permission.

    Updates may only be made via the API or Terraform for this account when enabled.
    """

    login_design: LoginDesignParam

    mfa_config: MfaConfig
    """Configures multi-factor authentication (MFA) settings for an organization."""

    mfa_required_for_all_apps: bool
    """Determines whether global MFA settings apply to applications by default.

    The organization must have MFA enabled with at least one authentication method
    and a session duration configured.
    """

    mfa_ssh_piv_key_requirements: MfaSSHPivKeyRequirements
    """Configures SSH PIV key requirements for MFA using hardware security keys."""

    session_duration: str
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    ui_read_only_toggle_reason: str
    """A description of the reason why the UI read only field is being toggled."""

    user_seat_expiration_inactive_time: str
    """The amount of time a user seat is inactive before it expires.

    When the user seat exceeds the set time of inactivity, the user is removed as an
    active seat and no longer counts against your Teams seat count. Minimum value
    for this setting is 1 month (730h). Must be in the format `300ms` or `2h45m`.
    Valid time units are: `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`.
    """

    warp_auth_session_duration: str
    """The amount of time that tokens issued for applications will be valid.

    Must be in the format `30m` or `2h45m`. Valid time units are: m, h.
    """


class MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings for an organization."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key", "ssh_piv_key"]]
    """Lists the MFA methods that users can authenticate with."""

    amr_matching_session_duration: str
    """
    Allows a user to skip MFA via Authentication Method Reference (AMR) matching
    when the AMR claim provided by the IdP the user used to authenticate contains
    "mfa". Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30
    days).
    """

    required_aaguids: str
    """Specifies a Cloudflare List of required FIDO2 authenticator device AAGUIDs."""

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class MfaSSHPivKeyRequirements(TypedDict, total=False):
    """Configures SSH PIV key requirements for MFA using hardware security keys."""

    pin_policy: Literal["never", "once", "always"]
    """Defines when a PIN is required to use the SSH key.

    Valid values: `never` (no PIN required), `once` (PIN required once per session),
    `always` (PIN required for each use).
    """

    require_fips_device: bool
    """
    Requires the SSH PIV key to be stored on a FIPS 140-2 Level 1 or higher
    validated device.
    """

    ssh_key_size: Iterable[Literal[256, 384, 521, 2048, 3072, 4096]]
    """Specifies the allowed SSH key sizes in bits.

    Valid sizes depend on key type. Ed25519 has a fixed key size and does not accept
    this parameter.
    """

    ssh_key_type: List[Literal["ecdsa", "ed25519", "rsa"]]
    """Specifies the allowed SSH key types.

    Valid values are `ecdsa`, `ed25519`, and `rsa`.
    """

    touch_policy: Literal["never", "always", "cached"]
    """Defines when physical touch is required to use the SSH key.

    Valid values: `never` (no touch required), `always` (touch required for each
    use), `cached` (touch cached for 15 seconds).
    """
