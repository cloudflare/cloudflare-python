# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .decision import Decision
from ...._types import SequenceNotStr
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
    "SelfHostedApplicationDestinationViaMcpServerPortalDestination",
    "SelfHostedApplicationMfaConfig",
    "SelfHostedApplicationOAuthConfiguration",
    "SelfHostedApplicationOAuthConfigurationDynamicClientRegistration",
    "SelfHostedApplicationOAuthConfigurationGrant",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationPolicyAccessAppPolicyLink",
    "SelfHostedApplicationPolicyUnionMember2",
    "SelfHostedApplicationPolicyUnionMember2ConnectionRules",
    "SelfHostedApplicationPolicyUnionMember2ConnectionRulesRDP",
    "SelfHostedApplicationPolicyUnionMember2MfaConfig",
    "SelfHostedApplicationSCIMConfig",
    "SelfHostedApplicationSCIMConfigAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationPolicyAccessAppPolicyLink",
    "SaaSApplicationPolicyUnionMember2",
    "SaaSApplicationPolicyUnionMember2ConnectionRules",
    "SaaSApplicationPolicyUnionMember2ConnectionRulesRDP",
    "SaaSApplicationPolicyUnionMember2MfaConfig",
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
    "BrowserSSHApplicationDestinationViaMcpServerPortalDestination",
    "BrowserSSHApplicationMfaConfig",
    "BrowserSSHApplicationOAuthConfiguration",
    "BrowserSSHApplicationOAuthConfigurationDynamicClientRegistration",
    "BrowserSSHApplicationOAuthConfigurationGrant",
    "BrowserSSHApplicationPolicy",
    "BrowserSSHApplicationPolicyAccessAppPolicyLink",
    "BrowserSSHApplicationPolicyUnionMember2",
    "BrowserSSHApplicationPolicyUnionMember2ConnectionRules",
    "BrowserSSHApplicationPolicyUnionMember2ConnectionRulesRDP",
    "BrowserSSHApplicationPolicyUnionMember2MfaConfig",
    "BrowserSSHApplicationSCIMConfig",
    "BrowserSSHApplicationSCIMConfigAuthentication",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserVNCApplication",
    "BrowserVNCApplicationDestination",
    "BrowserVNCApplicationDestinationPublicDestination",
    "BrowserVNCApplicationDestinationPrivateDestination",
    "BrowserVNCApplicationDestinationViaMcpServerPortalDestination",
    "BrowserVNCApplicationMfaConfig",
    "BrowserVNCApplicationOAuthConfiguration",
    "BrowserVNCApplicationOAuthConfigurationDynamicClientRegistration",
    "BrowserVNCApplicationOAuthConfigurationGrant",
    "BrowserVNCApplicationPolicy",
    "BrowserVNCApplicationPolicyAccessAppPolicyLink",
    "BrowserVNCApplicationPolicyUnionMember2",
    "BrowserVNCApplicationPolicyUnionMember2ConnectionRules",
    "BrowserVNCApplicationPolicyUnionMember2ConnectionRulesRDP",
    "BrowserVNCApplicationPolicyUnionMember2MfaConfig",
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
    "AppLauncherApplicationPolicyUnionMember2ConnectionRules",
    "AppLauncherApplicationPolicyUnionMember2ConnectionRulesRDP",
    "AppLauncherApplicationPolicyUnionMember2MfaConfig",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRules",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2MfaConfig",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRules",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2MfaConfig",
    "GatewayIdentityProxyEndpointApplication",
    "GatewayIdentityProxyEndpointApplicationPolicy",
    "GatewayIdentityProxyEndpointApplicationPolicyAccessAppPolicyLink",
    "GatewayIdentityProxyEndpointApplicationPolicyUnionMember2",
    "GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRules",
    "GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRulesRDP",
    "GatewayIdentityProxyEndpointApplicationPolicyUnionMember2MfaConfig",
    "BookmarkApplication",
    "BookmarkApplicationPolicy",
    "BookmarkApplicationPolicyAccessAppPolicyLink",
    "BookmarkApplicationPolicyUnionMember2",
    "BookmarkApplicationPolicyUnionMember2ConnectionRules",
    "BookmarkApplicationPolicyUnionMember2ConnectionRulesRDP",
    "BookmarkApplicationPolicyUnionMember2MfaConfig",
    "InfrastructureApplication",
    "InfrastructureApplicationTargetCriterion",
    "InfrastructureApplicationPolicy",
    "InfrastructureApplicationPolicyConnectionRules",
    "InfrastructureApplicationPolicyConnectionRulesSSH",
    "BrowserRDPApplication",
    "BrowserRDPApplicationTargetCriterion",
    "BrowserRDPApplicationDestination",
    "BrowserRDPApplicationDestinationPublicDestination",
    "BrowserRDPApplicationDestinationPrivateDestination",
    "BrowserRDPApplicationDestinationViaMcpServerPortalDestination",
    "BrowserRDPApplicationMfaConfig",
    "BrowserRDPApplicationOAuthConfiguration",
    "BrowserRDPApplicationOAuthConfigurationDynamicClientRegistration",
    "BrowserRDPApplicationOAuthConfigurationGrant",
    "BrowserRDPApplicationPolicy",
    "BrowserRDPApplicationPolicyAccessAppPolicyLink",
    "BrowserRDPApplicationPolicyUnionMember2",
    "BrowserRDPApplicationPolicyUnionMember2ConnectionRules",
    "BrowserRDPApplicationPolicyUnionMember2ConnectionRulesRDP",
    "BrowserRDPApplicationPolicyUnionMember2MfaConfig",
    "BrowserRDPApplicationSCIMConfig",
    "BrowserRDPApplicationSCIMConfigAuthentication",
    "BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "McpServerApplication",
    "McpServerApplicationDestination",
    "McpServerApplicationDestinationPublicDestination",
    "McpServerApplicationDestinationPrivateDestination",
    "McpServerApplicationDestinationViaMcpServerPortalDestination",
    "McpServerApplicationOAuthConfiguration",
    "McpServerApplicationOAuthConfigurationDynamicClientRegistration",
    "McpServerApplicationOAuthConfigurationGrant",
    "McpServerApplicationPolicy",
    "McpServerApplicationPolicyAccessAppPolicyLink",
    "McpServerApplicationPolicyUnionMember2",
    "McpServerApplicationPolicyUnionMember2ConnectionRules",
    "McpServerApplicationPolicyUnionMember2ConnectionRulesRDP",
    "McpServerApplicationPolicyUnionMember2MfaConfig",
    "McpServerApplicationSCIMConfig",
    "McpServerApplicationSCIMConfigAuthentication",
    "McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "McpServerPortalApplication",
    "McpServerPortalApplicationDestination",
    "McpServerPortalApplicationDestinationPublicDestination",
    "McpServerPortalApplicationDestinationPrivateDestination",
    "McpServerPortalApplicationDestinationViaMcpServerPortalDestination",
    "McpServerPortalApplicationOAuthConfiguration",
    "McpServerPortalApplicationOAuthConfigurationDynamicClientRegistration",
    "McpServerPortalApplicationOAuthConfigurationGrant",
    "McpServerPortalApplicationPolicy",
    "McpServerPortalApplicationPolicyAccessAppPolicyLink",
    "McpServerPortalApplicationPolicyUnionMember2",
    "McpServerPortalApplicationPolicyUnionMember2ConnectionRules",
    "McpServerPortalApplicationPolicyUnionMember2ConnectionRulesRDP",
    "McpServerPortalApplicationPolicyUnionMember2MfaConfig",
    "McpServerPortalApplicationSCIMConfig",
    "McpServerPortalApplicationSCIMConfigAuthentication",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
]


class SelfHostedApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Required[ApplicationType]
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

    allow_iframe: bool
    """Enables loading application content in an iFrame."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
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

    mfa_config: SelfHostedApplicationMfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    name: str
    """The name of the application."""

    oauth_configuration: SelfHostedApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: SequenceNotStr[SelfHostedApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    read_service_tokens_from_header: str
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
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

    self_hosted_domains: SequenceNotStr[SelfHostedDomains]
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
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: bool
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class SelfHostedApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

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


class SelfHostedApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


SelfHostedApplicationDestination: TypeAlias = Union[
    SelfHostedApplicationDestinationPublicDestination,
    SelfHostedApplicationDestinationPrivateDestination,
    SelfHostedApplicationDestinationViaMcpServerPortalDestination,
]


class SelfHostedApplicationMfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class SelfHostedApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class SelfHostedApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class SelfHostedApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: SelfHostedApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: SelfHostedApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class SelfHostedApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SelfHostedApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class SelfHostedApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: SelfHostedApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class SelfHostedApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: SelfHostedApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: SelfHostedApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

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

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    logo_url: str
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: str
    """The name of the application."""

    policies: SequenceNotStr[SaaSApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    saas_app: SaaSApplicationSaaSApp

    scim_config: SaaSApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: ApplicationType
    """The application type."""


class SaaSApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SaaSApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class SaaSApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: SaaSApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class SaaSApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: SaaSApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: SaaSApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

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

    type: Required[
        Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
            "proxy_endpoint",
        ]
    ]
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

    allow_iframe: bool
    """Enables loading application content in an iFrame."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
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

    mfa_config: BrowserSSHApplicationMfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    name: str
    """The name of the application."""

    oauth_configuration: BrowserSSHApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: SequenceNotStr[BrowserSSHApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    read_service_tokens_from_header: str
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
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

    self_hosted_domains: SequenceNotStr[SelfHostedDomains]
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
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: bool
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class BrowserSSHApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

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


class BrowserSSHApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


BrowserSSHApplicationDestination: TypeAlias = Union[
    BrowserSSHApplicationDestinationPublicDestination,
    BrowserSSHApplicationDestinationPrivateDestination,
    BrowserSSHApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserSSHApplicationMfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserSSHApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class BrowserSSHApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserSSHApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: BrowserSSHApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: BrowserSSHApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class BrowserSSHApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserSSHApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserSSHApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: BrowserSSHApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserSSHApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: BrowserSSHApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: BrowserSSHApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

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

    type: Required[
        Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
            "proxy_endpoint",
        ]
    ]
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

    allow_iframe: bool
    """Enables loading application content in an iFrame."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
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

    mfa_config: BrowserVNCApplicationMfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    name: str
    """The name of the application."""

    oauth_configuration: BrowserVNCApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: SequenceNotStr[BrowserVNCApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    read_service_tokens_from_header: str
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
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

    self_hosted_domains: SequenceNotStr[SelfHostedDomains]
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
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: bool
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class BrowserVNCApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

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


class BrowserVNCApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


BrowserVNCApplicationDestination: TypeAlias = Union[
    BrowserVNCApplicationDestinationPublicDestination,
    BrowserVNCApplicationDestinationPrivateDestination,
    BrowserVNCApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserVNCApplicationMfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserVNCApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class BrowserVNCApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserVNCApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: BrowserVNCApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: BrowserVNCApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class BrowserVNCApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserVNCApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserVNCApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: BrowserVNCApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserVNCApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: BrowserVNCApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: BrowserVNCApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

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
    type: Required[
        Literal[
            "self_hosted",
            "saas",
            "ssh",
            "vnc",
            "app_launcher",
            "warp",
            "biso",
            "bookmark",
            "dash_sso",
            "infrastructure",
            "rdp",
            "mcp",
            "mcp_portal",
            "proxy_endpoint",
        ]
    ]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    footer_links: Iterable[AppLauncherApplicationFooterLink]
    """The links in the App Launcher footer."""

    header_bg_color: str
    """The background color of the App Launcher header."""

    landing_page_design: AppLauncherApplicationLandingPageDesign
    """The design of the App Launcher landing page shown to users when they log in."""

    policies: SequenceNotStr[AppLauncherApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_app_launcher_login_page: bool
    """Determines when to skip the App Launcher landing page."""


class AppLauncherApplicationFooterLink(TypedDict, total=False):
    name: Required[str]
    """The hypertext in the footer link."""

    url: Required[str]
    """the hyperlink in the footer link."""


class AppLauncherApplicationLandingPageDesign(TypedDict, total=False):
    """The design of the App Launcher landing page shown to users when they log in."""

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
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class AppLauncherApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class AppLauncherApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: AppLauncherApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class AppLauncherApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: AppLauncherApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: AppLauncherApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


class DeviceEnrollmentPermissionsApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    policies: SequenceNotStr[DeviceEnrollmentPermissionsApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class DeviceEnrollmentPermissionsApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: DeviceEnrollmentPermissionsApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: DeviceEnrollmentPermissionsApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


class BrowserIsolationPermissionsApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    policies: SequenceNotStr[BrowserIsolationPermissionsApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserIsolationPermissionsApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
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

    connection_rules: BrowserIsolationPermissionsApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: BrowserIsolationPermissionsApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


class GatewayIdentityProxyEndpointApplication(TypedDict, total=False):
    type: Required[ApplicationType]
    """The application type."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    domain: str
    """
    The proxy endpoint domain in the format: 10 alphanumeric characters followed by
    .proxy.cloudflare-gateway.com
    """

    name: str
    """The name of the application."""

    policies: SequenceNotStr[GatewayIdentityProxyEndpointApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class GatewayIdentityProxyEndpointApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class GatewayIdentityProxyEndpointApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class GatewayIdentityProxyEndpointApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: GatewayIdentityProxyEndpointApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: GatewayIdentityProxyEndpointApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


GatewayIdentityProxyEndpointApplicationPolicy: TypeAlias = Union[
    GatewayIdentityProxyEndpointApplicationPolicyAccessAppPolicyLink,
    str,
    GatewayIdentityProxyEndpointApplicationPolicyUnionMember2,
]


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

    policies: SequenceNotStr[BookmarkApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: ApplicationType
    """The application type."""


class BookmarkApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BookmarkApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BookmarkApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: BookmarkApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BookmarkApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BookmarkApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: BookmarkApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: BookmarkApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


BookmarkApplicationPolicy: TypeAlias = Union[
    BookmarkApplicationPolicyAccessAppPolicyLink, str, BookmarkApplicationPolicyUnionMember2
]


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

    protocol: Required[Literal["SSH"]]
    """The communication protocol your application secures."""

    target_attributes: Required[Dict[str, SequenceNotStr[str]]]
    """Contains a map of target attribute keys to target attribute values."""


class InfrastructureApplicationPolicyConnectionRulesSSH(TypedDict, total=False):
    """
    The SSH-specific rules that define how users may connect to the targets secured by your application.
    """

    usernames: Required[SequenceNotStr[str]]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: bool
    """Enables using Identity Provider email alias as SSH username."""


class InfrastructureApplicationPolicyConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to the targets secured by your application.
    """

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


class BrowserRDPApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    target_criteria: Required[Iterable[BrowserRDPApplicationTargetCriterion]]

    type: Required[ApplicationType]
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

    allow_iframe: bool
    """Enables loading application content in an iFrame."""

    allowed_idps: SequenceNotStr[AllowedIdPs]
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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[BrowserRDPApplicationDestination]
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

    mfa_config: BrowserRDPApplicationMfaConfig
    """Configures multi-factor authentication (MFA) settings."""

    name: str
    """The name of the application."""

    oauth_configuration: BrowserRDPApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: bool
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: SequenceNotStr[BrowserRDPApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    read_service_tokens_from_header: str
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserRDPApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: SequenceNotStr[SelfHostedDomains]
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
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: bool
    """Enables automatic authentication through cloudflared."""

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: bool
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class BrowserRDPApplicationTargetCriterion(TypedDict, total=False):
    port: Required[int]
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Required[Literal["RDP"]]
    """The communication protocol your application secures."""

    target_attributes: Required[Dict[str, SequenceNotStr[str]]]
    """Contains a map of target attribute keys to target attribute values."""


class BrowserRDPApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserRDPApplicationDestinationPrivateDestination(TypedDict, total=False):
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


class BrowserRDPApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


BrowserRDPApplicationDestination: TypeAlias = Union[
    BrowserRDPApplicationDestinationPublicDestination,
    BrowserRDPApplicationDestinationPrivateDestination,
    BrowserRDPApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserRDPApplicationMfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserRDPApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class BrowserRDPApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserRDPApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: BrowserRDPApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: BrowserRDPApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class BrowserRDPApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserRDPApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserRDPApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: BrowserRDPApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserRDPApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserRDPApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: BrowserRDPApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: BrowserRDPApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


BrowserRDPApplicationPolicy: TypeAlias = Union[
    BrowserRDPApplicationPolicyAccessAppPolicyLink, str, BrowserRDPApplicationPolicyUnionMember2
]


class BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


class BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserRDPApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserRDPApplicationSCIMConfig(TypedDict, total=False):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserRDPApplicationSCIMConfigAuthentication
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


class McpServerApplication(TypedDict, total=False):
    type: Required[ApplicationType]
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

    allowed_idps: SequenceNotStr[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[McpServerApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
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

    oauth_configuration: McpServerApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    policies: SequenceNotStr[McpServerApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: McpServerApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class McpServerApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class McpServerApplicationDestinationPrivateDestination(TypedDict, total=False):
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


class McpServerApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


McpServerApplicationDestination: TypeAlias = Union[
    McpServerApplicationDestinationPublicDestination,
    McpServerApplicationDestinationPrivateDestination,
    McpServerApplicationDestinationViaMcpServerPortalDestination,
]


class McpServerApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class McpServerApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class McpServerApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: McpServerApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: McpServerApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class McpServerApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class McpServerApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class McpServerApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: McpServerApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class McpServerApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class McpServerApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: McpServerApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: McpServerApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


McpServerApplicationPolicy: TypeAlias = Union[
    McpServerApplicationPolicyAccessAppPolicyLink, str, McpServerApplicationPolicyUnionMember2
]


class McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


class McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

McpServerApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class McpServerApplicationSCIMConfig(TypedDict, total=False):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: McpServerApplicationSCIMConfigAuthentication
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


class McpServerPortalApplication(TypedDict, total=False):
    type: Required[ApplicationType]
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

    allowed_idps: SequenceNotStr[AllowedIdPs]
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

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

    custom_pages: SequenceNotStr[str]
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Iterable[McpServerPortalApplicationDestination]
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
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

    oauth_configuration: McpServerPortalApplicationOAuthConfiguration
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: bool
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    policies: SequenceNotStr[McpServerPortalApplicationPolicy]
    """
    The policies that Access applies to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application. Reusable and inline policies are mutually
    exclusive.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: McpServerPortalApplicationSCIMConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    tags: SequenceNotStr[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class McpServerPortalApplicationDestinationPublicDestination(TypedDict, total=False):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Literal["public"]

    uri: str
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class McpServerPortalApplicationDestinationPrivateDestination(TypedDict, total=False):
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


class McpServerPortalApplicationDestinationViaMcpServerPortalDestination(TypedDict, total=False):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: str
    """The MCP server id configured in ai-controls."""

    type: Literal["via_mcp_server_portal"]


McpServerPortalApplicationDestination: TypeAlias = Union[
    McpServerPortalApplicationDestinationPublicDestination,
    McpServerPortalApplicationDestinationPrivateDestination,
    McpServerPortalApplicationDestinationViaMcpServerPortalDestination,
]


class McpServerPortalApplicationOAuthConfigurationDynamicClientRegistration(TypedDict, total=False):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: bool
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: bool
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: SequenceNotStr[str]
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: bool
    """Whether dynamic client registration is enabled."""


class McpServerPortalApplicationOAuthConfigurationGrant(TypedDict, total=False):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: str
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: str
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class McpServerPortalApplicationOAuthConfiguration(TypedDict, total=False):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: McpServerPortalApplicationOAuthConfigurationDynamicClientRegistration
    """Settings for OAuth dynamic client registration."""

    enabled: bool
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: McpServerPortalApplicationOAuthConfigurationGrant
    """Settings for OAuth grant behavior."""


class McpServerPortalApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    """A JSON that links a reusable policy to an application."""

    id: str
    """The UUID of the policy"""

    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class McpServerPortalApplicationPolicyUnionMember2ConnectionRulesRDP(TypedDict, total=False):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: List[Literal["text"]]
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class McpServerPortalApplicationPolicyUnionMember2ConnectionRules(TypedDict, total=False):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: McpServerPortalApplicationPolicyUnionMember2ConnectionRulesRDP
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class McpServerPortalApplicationPolicyUnionMember2MfaConfig(TypedDict, total=False):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: List[Literal["totp", "biometrics", "security_key"]]
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: bool
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: str
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class McpServerPortalApplicationPolicyUnionMember2(TypedDict, total=False):
    id: str
    """The UUID of the policy"""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: McpServerPortalApplicationPolicyUnionMember2ConnectionRules
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    isolation_required: bool
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: McpServerPortalApplicationPolicyUnionMember2MfaConfig
    """Configures multi-factor authentication (MFA) settings."""

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


McpServerPortalApplicationPolicy: TypeAlias = Union[
    McpServerPortalApplicationPolicyAccessAppPolicyLink, str, McpServerPortalApplicationPolicyUnionMember2
]


class McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


class McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    TypedDict, total=False
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

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


McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

McpServerPortalApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasicParam,
    SCIMConfigAuthenticationOAuthBearerTokenParam,
    SCIMConfigAuthenticationOauth2Param,
    McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    Iterable[McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class McpServerPortalApplicationSCIMConfig(TypedDict, total=False):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: McpServerPortalApplicationSCIMConfigAuthentication
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
    GatewayIdentityProxyEndpointApplication,
    BookmarkApplication,
    InfrastructureApplication,
    BrowserRDPApplication,
    McpServerApplication,
    McpServerPortalApplication,
]
