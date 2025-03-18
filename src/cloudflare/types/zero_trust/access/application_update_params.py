# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .decision import Decision
from .allowed_idps import AllowedIdPs
from .application_type import ApplicationType
from .cors_headers_param import CORSHeadersParam
from .oidc_saas_app_param import OIDCSaaSAppParam
from .saml_saas_app_param import SAMLSaaSAppParam
from .self_hosted_domains import SelfHostedDomains
from .approval_group_param import ApprovalGroupParam
from .scim_config_mapping_param import SCIMConfigMappingParam
from .applications.access_rule_param import AccessRuleParam
from .scim_config_authentication_oauth2_param import SCIMConfigAuthenticationOauth2Param
from .scim_config_authentication_http_basic_param import SCIMConfigAuthenticationHTTPBasicParam
from .scim_config_authentication_oauth_bearer_token_param import SCIMConfigAuthenticationOAuthBearerTokenParam

__all__ = [
    "ApplicationUpdateParams",
    "SelfHostedApplication",
    "SelfHostedApplicationDestination",
    "SelfHostedApplicationDestinationPublicDestination",
    "SelfHostedApplicationDestinationPrivateDestination",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationPolicyAccessAppPolicyLink",
    "SelfHostedApplicationPolicyUnionMember2",
    "SelfHostedApplicationSCIMConfig",
    "SelfHostedApplicationSCIMConfigAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationPolicyAccessAppPolicyLink",
    "SaaSApplicationPolicyUnionMember2",
    "SaaSApplicationSaaSApp",
    "SaaSApplicationSCIMConfig",
    "SaaSApplicationSCIMConfigAuthentication",
    "SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserSSHApplication",
    "BrowserSSHApplicationDestination",
    "BrowserSSHApplicationDestinationPublicDestination",
    "BrowserSSHApplicationDestinationPrivateDestination",
    "BrowserSSHApplicationPolicy",
    "BrowserSSHApplicationPolicyAccessAppPolicyLink",
    "BrowserSSHApplicationPolicyUnionMember2",
    "BrowserSSHApplicationSCIMConfig",
    "BrowserSSHApplicationSCIMConfigAuthentication",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserVNCApplication",
    "BrowserVNCApplicationDestination",
    "BrowserVNCApplicationDestinationPublicDestination",
    "BrowserVNCApplicationDestinationPrivateDestination",
    "BrowserVNCApplicationPolicy",
    "BrowserVNCApplicationPolicyAccessAppPolicyLink",
    "BrowserVNCApplicationPolicyUnionMember2",
    "BrowserVNCApplicationSCIMConfig",
    "BrowserVNCApplicationSCIMConfigAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "AppLauncherApplication",
    "AppLauncherApplicationFooterLink",
    "AppLauncherApplicationLandingPageDesign",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationPolicyAccessAppPolicyLink",
    "AppLauncherApplicationPolicyUnionMember2",
    "AppLauncherApplicationSCIMConfig",
    "AppLauncherApplicationSCIMConfigAuthentication",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationFooterLink",
    "DeviceEnrollmentPermissionsApplicationLandingPageDesign",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2",
    "DeviceEnrollmentPermissionsApplicationSCIMConfig",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationFooterLink",
    "BrowserIsolationPermissionsApplicationLandingPageDesign",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2",
    "BrowserIsolationPermissionsApplicationSCIMConfig",
    "BrowserIsolationPermissionsApplicationSCIMConfigAuthentication",
    "BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BookmarkApplication",
    "BookmarkApplicationSCIMConfig",
    "BookmarkApplicationSCIMConfigAuthentication",
    "BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "InfrastructureApplication",
    "InfrastructureApplicationTargetCriterion",
    "InfrastructureApplicationPolicy",
    "InfrastructureApplicationPolicyConnectionRules",
    "InfrastructureApplicationPolicyConnectionRulesSSH",
    "BrowserRdpApplication",
    "BrowserRdpApplicationTargetCriterion",
    "BrowserRdpApplicationDestination",
    "BrowserRdpApplicationDestinationPublicDestination",
    "BrowserRdpApplicationDestinationPrivateDestination",
    "BrowserRdpApplicationPolicy",
    "BrowserRdpApplicationPolicyAccessAppPolicyLink",
    "BrowserRdpApplicationPolicyUnionMember2",
    "BrowserRdpApplicationSCIMConfig",
    "BrowserRdpApplicationSCIMConfigAuthentication",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
]


class SelfHostedApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Required[str]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: CORSHeadersParam

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[SelfHostedApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: List[SelfHostedApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: SelfHostedApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class SelfHostedApplicationDestinationPublicDestination(TypedDict, total=False):
    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class SelfHostedApplicationDestinationPrivateDestination(TypedDict, total=False):
    cidr: str
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: str
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Literal["tcp", "udp"]
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: str
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Literal["private"]

    vnet_id: str
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


SelfHostedApplicationDestination: TypeAlias = Union[
    SelfHostedApplicationDestinationPublicDestination, SelfHostedApplicationDestinationPrivateDestination
]


class SelfHostedApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SelfHostedApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


SelfHostedApplicationPolicy: TypeAlias = Union[
    SelfHostedApplicationPolicyAccessAppPolicyLink, str, SelfHostedApplicationPolicyUnionMember2
]


class SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

SelfHostedApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class SelfHostedApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: SelfHostedApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class SaaSApplication(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    policies: List[SaaSApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    saas_app: SaaSApplicationSaaSApp

    scim_config: SaaSApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


class SaaSApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SaaSApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


SaaSApplicationPolicy: TypeAlias = Union[
    SaaSApplicationPolicyAccessAppPolicyLink, str, SaaSApplicationPolicyUnionMember2
]

SaaSApplicationSaaSApp: TypeAlias = Union[SAMLSaaSAppParam, OIDCSaaSAppParam]


class SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(TypedDict, total=False):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

SaaSApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class SaaSApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: SaaSApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserSSHApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Required[str]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: CORSHeadersParam

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[BrowserSSHApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: List[BrowserSSHApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserSSHApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class BrowserSSHApplicationDestinationPublicDestination(TypedDict, total=False):
    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserSSHApplicationDestinationPrivateDestination(TypedDict, total=False):
    cidr: str
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: str
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Literal["tcp", "udp"]
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: str
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Literal["private"]

    vnet_id: str
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


BrowserSSHApplicationDestination: TypeAlias = Union[
    BrowserSSHApplicationDestinationPublicDestination, BrowserSSHApplicationDestinationPrivateDestination
]


class BrowserSSHApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserSSHApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserSSHApplicationPolicy: TypeAlias = Union[
    BrowserSSHApplicationPolicyAccessAppPolicyLink, str, BrowserSSHApplicationPolicyUnionMember2
]


class BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserSSHApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserSSHApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserSSHApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserVNCApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Required[str]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: CORSHeadersParam

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[BrowserVNCApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: List[BrowserVNCApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserVNCApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class BrowserVNCApplicationDestinationPublicDestination(TypedDict, total=False):
    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserVNCApplicationDestinationPrivateDestination(TypedDict, total=False):
    cidr: str
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: str
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Literal["tcp", "udp"]
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: str
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Literal["private"]

    vnet_id: str
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


BrowserVNCApplicationDestination: TypeAlias = Union[
    BrowserVNCApplicationDestinationPublicDestination, BrowserVNCApplicationDestinationPrivateDestination
]


class BrowserVNCApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserVNCApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserVNCApplicationPolicy: TypeAlias = Union[
    BrowserVNCApplicationPolicyAccessAppPolicyLink, str, BrowserVNCApplicationPolicyUnionMember2
]


class BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserVNCApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserVNCApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserVNCApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class AppLauncherApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_logo_url: str
    """The image URL of the logo shown in the App Launcher header."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    bg_color: str
    """The background color of the App Launcher page."""

    footer_links: Iterable[AppLauncherApplicationFooterLink]
    """The links in the App Launcher footer."""

    header_bg_color: str
    """The background color of the App Launcher header."""

    landing_page_design: AppLauncherApplicationLandingPageDesign
    """The design of the App Launcher landing page shown to users when they log in."""

    policies: List[AppLauncherApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: AppLauncherApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: bool
    """Determines when to skip the App Launcher landing page."""


class AppLauncherApplicationFooterLink(TypedDict, total=False):
    name: Required[str]
    """The hypertext in the footer link."""

    url: Required[str]
    """the hyperlink in the footer link."""


class AppLauncherApplicationLandingPageDesign(TypedDict, total=False):
    button_color: str
    """The background color of the log in button on the landing page."""

    button_text_color: str
    """The color of the text in the log in button on the landing page."""

    image_url: str
    """The URL of the image shown on the landing page."""

    message: str
    """The message shown on the landing page."""

    title: str
    """The title shown on the landing page."""


class AppLauncherApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class AppLauncherApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


AppLauncherApplicationPolicy: TypeAlias = Union[
    AppLauncherApplicationPolicyAccessAppPolicyLink, str, AppLauncherApplicationPolicyUnionMember2
]


class AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

AppLauncherApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class AppLauncherApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: AppLauncherApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class DeviceEnrollmentPermissionsApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_logo_url: str
    """The image URL of the logo shown in the App Launcher header."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    bg_color: str
    """The background color of the App Launcher page."""

    footer_links: Iterable[DeviceEnrollmentPermissionsApplicationFooterLink]
    """The links in the App Launcher footer."""

    header_bg_color: str
    """The background color of the App Launcher header."""

    landing_page_design: DeviceEnrollmentPermissionsApplicationLandingPageDesign
    """The design of the App Launcher landing page shown to users when they log in."""

    policies: List[DeviceEnrollmentPermissionsApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: DeviceEnrollmentPermissionsApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: bool
    """Determines when to skip the App Launcher landing page."""


class DeviceEnrollmentPermissionsApplicationFooterLink(TypedDict, total=False):
    name: Required[str]
    """The hypertext in the footer link."""

    url: Required[str]
    """the hyperlink in the footer link."""


class DeviceEnrollmentPermissionsApplicationLandingPageDesign(TypedDict, total=False):
    button_color: str
    """The background color of the log in button on the landing page."""

    button_text_color: str
    """The color of the text in the log in button on the landing page."""

    image_url: str
    """The URL of the image shown on the landing page."""

    message: str
    """The message shown on the landing page."""

    title: str
    """The title shown on the landing page."""


class DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class DeviceEnrollmentPermissionsApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


DeviceEnrollmentPermissionsApplicationPolicy: TypeAlias = Union[
    DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink,
    str,
    DeviceEnrollmentPermissionsApplicationPolicyUnionMember2,
]


class DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class DeviceEnrollmentPermissionsApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserIsolationPermissionsApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_logo_url: str
    """The image URL of the logo shown in the App Launcher header."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    bg_color: str
    """The background color of the App Launcher page."""

    footer_links: Iterable[BrowserIsolationPermissionsApplicationFooterLink]
    """The links in the App Launcher footer."""

    header_bg_color: str
    """The background color of the App Launcher header."""

    landing_page_design: BrowserIsolationPermissionsApplicationLandingPageDesign
    """The design of the App Launcher landing page shown to users when they log in."""

    policies: List[BrowserIsolationPermissionsApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: BrowserIsolationPermissionsApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: bool
    """Determines when to skip the App Launcher landing page."""


class BrowserIsolationPermissionsApplicationFooterLink(TypedDict, total=False):
    name: Required[str]
    """The hypertext in the footer link."""

    url: Required[str]
    """the hyperlink in the footer link."""


class BrowserIsolationPermissionsApplicationLandingPageDesign(TypedDict, total=False):
    button_color: str
    """The background color of the log in button on the landing page."""

    button_text_color: str
    """The color of the text in the log in button on the landing page."""

    image_url: str
    """The URL of the image shown on the landing page."""

    message: str
    """The message shown on the landing page."""

    title: str
    """The title shown on the landing page."""


class BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserIsolationPermissionsApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserIsolationPermissionsApplicationPolicy: TypeAlias = Union[
    BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink,
    str,
    BrowserIsolationPermissionsApplicationPolicyUnionMember2,
]


class BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserIsolationPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserIsolationPermissionsApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserIsolationPermissionsApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BookmarkApplication(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    domain: str
    """The URL or domain of the bookmark."""

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    scim_config: BookmarkApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


class BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BookmarkApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BookmarkApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BookmarkApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class InfrastructureApplication(TypedDict, total=False):
    target_criteria: Required[Iterable[InfrastructureApplicationTargetCriterion]]

    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    name: str
    """The name of the application."""

    policies: Iterable[InfrastructureApplicationPolicy]
    """The policies that Access applies to the application."""


class InfrastructureApplicationTargetCriterion(TypedDict, total=False):
    port: Required[int]
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Required[Literal["ssh"]]
    """The communication protocol your application secures."""

    target_attributes: Required[Dict[str, List[str]]]
    """Contains a map of target attribute keys to target attribute values."""


class InfrastructureApplicationPolicyConnectionRulesSSH(TypedDict, total=False):
    usernames: Required[List[str]]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: bool
    """Enables using Identity Provider email alias as SSH username."""


class InfrastructureApplicationPolicyConnectionRules(TypedDict, total=False):
    ssh: InfrastructureApplicationPolicyConnectionRulesSSH
    """
    The SSH-specific rules that define how users may connect to the targets secured
    by your application.
    """


class InfrastructureApplicationPolicy(TypedDict, total=False):
    decision: Required[Decision]
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    connection_rules: InfrastructureApplicationPolicyConnectionRules
    """
    The rules that define how users may connect to the targets secured by your
    application.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """


class BrowserRdpApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    target_criteria: Required[Iterable[BrowserRdpApplicationTargetCriterion]]

    type: Required[str]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allow_authenticate_via_warp: bool
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: List[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: bool
    """Displays the application in the App Launcher."""

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: CORSHeadersParam

    custom_deny_message: str
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: str
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: List[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[BrowserRdpApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: bool
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: bool
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: List[BrowserRdpApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserRdpApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: bool
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class BrowserRdpApplicationTargetCriterion(TypedDict, total=False):
    port: Required[int]
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Required[Literal["ssh"]]
    """The communication protocol your application secures."""

    target_attributes: Required[Dict[str, List[str]]]
    """Contains a map of target attribute keys to target attribute values."""


class BrowserRdpApplicationDestinationPublicDestination(TypedDict, total=False):
    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserRdpApplicationDestinationPrivateDestination(TypedDict, total=False):
    cidr: str
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: str
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Literal["tcp", "udp"]
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: str
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Literal["private"]

    vnet_id: str
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


BrowserRdpApplicationDestination: TypeAlias = Union[
    BrowserRdpApplicationDestinationPublicDestination, BrowserRdpApplicationDestinationPrivateDestination
]


class BrowserRdpApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserRdpApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: str
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: bool
    """Require users to enter a justification when they log in to the application."""

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserRdpApplicationPolicy: TypeAlias = Union[
    BrowserRdpApplicationPolicyAccessAppPolicyLink, str, BrowserRdpApplicationPolicyUnionMember2
]


class BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    client_id: Required[str]
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: Required[str]
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Required[Literal["access_service_token"]]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserRdpApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserRdpApplicationSCIMConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserRdpApplicationSCIMConfigAuthentication
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: bool
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: bool
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Iterable[SCIMConfigMappingParam]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


ApplicationUpdateParams: TypeAlias = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVNCApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    BookmarkApplication,
    InfrastructureApplication,
    BrowserRdpApplication,
]
