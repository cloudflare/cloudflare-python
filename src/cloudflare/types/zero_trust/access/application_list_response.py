# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .decision import Decision
from ...._models import BaseModel
from .allowed_idps import AllowedIdPs
from .cors_headers import CORSHeaders
from .oidc_saas_app import OIDCSaaSApp
from .saml_saas_app import SAMLSaaSApp
from .approval_group import ApprovalGroup
from .application_type import ApplicationType
from .scim_config_mapping import SCIMConfigMapping
from .self_hosted_domains import SelfHostedDomains
from .applications.access_rule import AccessRule
from .scim_config_authentication_oauth2 import SCIMConfigAuthenticationOauth2
from .scim_config_authentication_http_basic import SCIMConfigAuthenticationHTTPBasic
from .scim_config_authentication_oauth_bearer_token import SCIMConfigAuthenticationOAuthBearerToken

__all__ = [
    "ApplicationListResponse",
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
    "SelfHostedApplicationPolicyConnectionRules",
    "SelfHostedApplicationPolicyConnectionRulesRDP",
    "SelfHostedApplicationPolicyMfaConfig",
    "SelfHostedApplicationSCIMConfig",
    "SelfHostedApplicationSCIMConfigAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationPolicyConnectionRules",
    "SaaSApplicationPolicyConnectionRulesRDP",
    "SaaSApplicationPolicyMfaConfig",
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
    "BrowserSSHApplicationPolicyConnectionRules",
    "BrowserSSHApplicationPolicyConnectionRulesRDP",
    "BrowserSSHApplicationPolicyMfaConfig",
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
    "BrowserVNCApplicationPolicyConnectionRules",
    "BrowserVNCApplicationPolicyConnectionRulesRDP",
    "BrowserVNCApplicationPolicyMfaConfig",
    "BrowserVNCApplicationSCIMConfig",
    "BrowserVNCApplicationSCIMConfigAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "AppLauncherApplication",
    "AppLauncherApplicationFooterLink",
    "AppLauncherApplicationLandingPageDesign",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationPolicyConnectionRules",
    "AppLauncherApplicationPolicyConnectionRulesRDP",
    "AppLauncherApplicationPolicyMfaConfig",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationPolicyConnectionRules",
    "DeviceEnrollmentPermissionsApplicationPolicyConnectionRulesRDP",
    "DeviceEnrollmentPermissionsApplicationPolicyMfaConfig",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationPolicyConnectionRules",
    "BrowserIsolationPermissionsApplicationPolicyConnectionRulesRDP",
    "BrowserIsolationPermissionsApplicationPolicyMfaConfig",
    "GatewayIdentityProxyEndpointApplication",
    "GatewayIdentityProxyEndpointApplicationPolicy",
    "GatewayIdentityProxyEndpointApplicationPolicyConnectionRules",
    "GatewayIdentityProxyEndpointApplicationPolicyConnectionRulesRDP",
    "GatewayIdentityProxyEndpointApplicationPolicyMfaConfig",
    "BookmarkApplication",
    "BookmarkApplicationPolicy",
    "BookmarkApplicationPolicyConnectionRules",
    "BookmarkApplicationPolicyConnectionRulesRDP",
    "BookmarkApplicationPolicyMfaConfig",
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
    "BrowserRDPApplicationPolicyConnectionRules",
    "BrowserRDPApplicationPolicyConnectionRulesRDP",
    "BrowserRDPApplicationPolicyMfaConfig",
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
    "McpServerApplicationPolicyConnectionRules",
    "McpServerApplicationPolicyConnectionRulesRDP",
    "McpServerApplicationPolicyMfaConfig",
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
    "McpServerPortalApplicationPolicyConnectionRules",
    "McpServerPortalApplicationPolicyConnectionRulesRDP",
    "McpServerPortalApplicationPolicyMfaConfig",
    "McpServerPortalApplicationSCIMConfig",
    "McpServerPortalApplicationSCIMConfigAuthentication",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
]


class SelfHostedApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class SelfHostedApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class SelfHostedApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


SelfHostedApplicationDestination: TypeAlias = Union[
    SelfHostedApplicationDestinationPublicDestination,
    SelfHostedApplicationDestinationPrivateDestination,
    SelfHostedApplicationDestinationViaMcpServerPortalDestination,
]


class SelfHostedApplicationMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class SelfHostedApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class SelfHostedApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class SelfHostedApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[SelfHostedApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[SelfHostedApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class SelfHostedApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class SelfHostedApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[SelfHostedApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class SelfHostedApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class SelfHostedApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[SelfHostedApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[SelfHostedApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

SelfHostedApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class SelfHostedApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[SelfHostedApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class SelfHostedApplication(BaseModel):
    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allow_iframe: Optional[bool] = None
    """Enables loading application content in an iFrame."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Optional[CORSHeaders] = None

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[SelfHostedApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: Optional[bool] = None
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    mfa_config: Optional[SelfHostedApplicationMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[SelfHostedApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: Optional[List[SelfHostedApplicationPolicy]] = None

    read_service_tokens_from_header: Optional[str] = None
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[SelfHostedApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: Optional[bool] = None
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class SaaSApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class SaaSApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[SaaSApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class SaaSApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class SaaSApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[SaaSApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[SaaSApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


SaaSApplicationSaaSApp: TypeAlias = Union[SAMLSaaSApp, OIDCSaaSApp]


class SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

SaaSApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class SaaSApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[SaaSApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class SaaSApplication(BaseModel):
    id: Optional[str] = None
    """UUID."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[SaaSApplicationPolicy]] = None

    saas_app: Optional[SaaSApplicationSaaSApp] = None

    scim_config: Optional[SaaSApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[ApplicationType] = None
    """The application type."""


class BrowserSSHApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserSSHApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class BrowserSSHApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


BrowserSSHApplicationDestination: TypeAlias = Union[
    BrowserSSHApplicationDestinationPublicDestination,
    BrowserSSHApplicationDestinationPrivateDestination,
    BrowserSSHApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserSSHApplicationMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserSSHApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class BrowserSSHApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserSSHApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[BrowserSSHApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[BrowserSSHApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class BrowserSSHApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserSSHApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[BrowserSSHApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserSSHApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserSSHApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[BrowserSSHApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[BrowserSSHApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserSSHApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserSSHApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserSSHApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserSSHApplication(BaseModel):
    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Literal[
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
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allow_iframe: Optional[bool] = None
    """Enables loading application content in an iFrame."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Optional[CORSHeaders] = None

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[BrowserSSHApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: Optional[bool] = None
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    mfa_config: Optional[BrowserSSHApplicationMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[BrowserSSHApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: Optional[List[BrowserSSHApplicationPolicy]] = None

    read_service_tokens_from_header: Optional[str] = None
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserSSHApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: Optional[bool] = None
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class BrowserVNCApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserVNCApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class BrowserVNCApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


BrowserVNCApplicationDestination: TypeAlias = Union[
    BrowserVNCApplicationDestinationPublicDestination,
    BrowserVNCApplicationDestinationPrivateDestination,
    BrowserVNCApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserVNCApplicationMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserVNCApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class BrowserVNCApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserVNCApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[BrowserVNCApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[BrowserVNCApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class BrowserVNCApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserVNCApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[BrowserVNCApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserVNCApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserVNCApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[BrowserVNCApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[BrowserVNCApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserVNCApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserVNCApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserVNCApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserVNCApplication(BaseModel):
    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    type: Literal[
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
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allow_iframe: Optional[bool] = None
    """Enables loading application content in an iFrame."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Optional[CORSHeaders] = None

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[BrowserVNCApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: Optional[bool] = None
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    mfa_config: Optional[BrowserVNCApplicationMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[BrowserVNCApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: Optional[List[BrowserVNCApplicationPolicy]] = None

    read_service_tokens_from_header: Optional[str] = None
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserVNCApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: Optional[bool] = None
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class AppLauncherApplicationFooterLink(BaseModel):
    name: str
    """The hypertext in the footer link."""

    url: str
    """the hyperlink in the footer link."""


class AppLauncherApplicationLandingPageDesign(BaseModel):
    """The design of the App Launcher landing page shown to users when they log in."""

    button_color: Optional[str] = None
    """The background color of the log in button on the landing page."""

    button_text_color: Optional[str] = None
    """The color of the text in the log in button on the landing page."""

    image_url: Optional[str] = None
    """The URL of the image shown on the landing page."""

    message: Optional[str] = None
    """The message shown on the landing page."""

    title: Optional[str] = None
    """The title shown on the landing page."""


class AppLauncherApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class AppLauncherApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[AppLauncherApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class AppLauncherApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class AppLauncherApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[AppLauncherApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[AppLauncherApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class AppLauncherApplication(BaseModel):
    type: Literal[
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
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_logo_url: Optional[str] = None
    """The image URL of the logo shown in the App Launcher header."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    bg_color: Optional[str] = None
    """The background color of the App Launcher page."""

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    domain: Optional[str] = None
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    footer_links: Optional[List[AppLauncherApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[AppLauncherApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[AppLauncherApplicationPolicy]] = None

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_app_launcher_login_page: Optional[bool] = None
    """Determines when to skip the App Launcher landing page."""


class DeviceEnrollmentPermissionsApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class DeviceEnrollmentPermissionsApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[DeviceEnrollmentPermissionsApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class DeviceEnrollmentPermissionsApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class DeviceEnrollmentPermissionsApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[DeviceEnrollmentPermissionsApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[DeviceEnrollmentPermissionsApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class DeviceEnrollmentPermissionsApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    domain: Optional[str] = None
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[DeviceEnrollmentPermissionsApplicationPolicy]] = None

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class BrowserIsolationPermissionsApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserIsolationPermissionsApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[BrowserIsolationPermissionsApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserIsolationPermissionsApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserIsolationPermissionsApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[BrowserIsolationPermissionsApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[BrowserIsolationPermissionsApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserIsolationPermissionsApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    domain: Optional[str] = None
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[BrowserIsolationPermissionsApplicationPolicy]] = None

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class GatewayIdentityProxyEndpointApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class GatewayIdentityProxyEndpointApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[GatewayIdentityProxyEndpointApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class GatewayIdentityProxyEndpointApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class GatewayIdentityProxyEndpointApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[GatewayIdentityProxyEndpointApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[GatewayIdentityProxyEndpointApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class GatewayIdentityProxyEndpointApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    domain: Optional[str] = None
    """
    The proxy endpoint domain in the format: 10 alphanumeric characters followed by
    .proxy.cloudflare-gateway.com
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[GatewayIdentityProxyEndpointApplicationPolicy]] = None

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """


class BookmarkApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BookmarkApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[BookmarkApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BookmarkApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BookmarkApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[BookmarkApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[BookmarkApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BookmarkApplication(BaseModel):
    id: Optional[str] = None
    """UUID."""

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    domain: Optional[str] = None
    """The URL or domain of the bookmark."""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[BookmarkApplicationPolicy]] = None

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[ApplicationType] = None
    """The application type."""


class InfrastructureApplicationTargetCriterion(BaseModel):
    port: int
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Literal["SSH"]
    """The communication protocol your application secures."""

    target_attributes: Dict[str, List[str]]
    """Contains a map of target attribute keys to target attribute values."""


class InfrastructureApplicationPolicyConnectionRulesSSH(BaseModel):
    """
    The SSH-specific rules that define how users may connect to the targets secured by your application.
    """

    usernames: List[str]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: Optional[bool] = None
    """Enables using Identity Provider email alias as SSH username."""


class InfrastructureApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to the targets secured by your application.
    """

    ssh: Optional[InfrastructureApplicationPolicyConnectionRulesSSH] = None
    """
    The SSH-specific rules that define how users may connect to the targets secured
    by your application.
    """


class InfrastructureApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    connection_rules: Optional[InfrastructureApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to the targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Optional[str] = None
    """The name of the Access policy."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    updated_at: Optional[datetime] = None


class InfrastructureApplication(BaseModel):
    target_criteria: List[InfrastructureApplicationTargetCriterion]

    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    aud: Optional[str] = None
    """Audience tag."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[InfrastructureApplicationPolicy]] = None


class BrowserRDPApplicationTargetCriterion(BaseModel):
    port: int
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Literal["RDP"]
    """The communication protocol your application secures."""

    target_attributes: Dict[str, List[str]]
    """Contains a map of target attribute keys to target attribute values."""


class BrowserRDPApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserRDPApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class BrowserRDPApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


BrowserRDPApplicationDestination: TypeAlias = Union[
    BrowserRDPApplicationDestinationPublicDestination,
    BrowserRDPApplicationDestinationPrivateDestination,
    BrowserRDPApplicationDestinationViaMcpServerPortalDestination,
]


class BrowserRDPApplicationMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserRDPApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class BrowserRDPApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class BrowserRDPApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[BrowserRDPApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[BrowserRDPApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class BrowserRDPApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class BrowserRDPApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[BrowserRDPApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class BrowserRDPApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class BrowserRDPApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[BrowserRDPApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[BrowserRDPApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserRDPApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BrowserRDPApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserRDPApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserRDPApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserRDPApplication(BaseModel):
    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    target_criteria: List[BrowserRDPApplicationTargetCriterion]

    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allow_iframe: Optional[bool] = None
    """Enables loading application content in an iFrame."""

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    cors_headers: Optional[CORSHeaders] = None

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[BrowserRDPApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    enable_binding_cookie: Optional[bool] = None
    """
    Enables the binding cookie, which increases security against compromised
    authorization tokens and CSRF attacks.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    mfa_config: Optional[BrowserRDPApplicationMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[BrowserRDPApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: Optional[List[BrowserRDPApplicationPolicy]] = None

    read_service_tokens_from_header: Optional[str] = None
    """
    Allows matching Access Service Tokens passed HTTP in a single header with this
    name. This works as an alternative to the (CF-Access-Client-Id,
    CF-Access-Client-Secret) pair of headers. The header value will be interpreted
    as a json object similar to: { "cf-access-client-id":
    "88bf3b6d86161464f6509f7219099e57.access.example.com",
    "cf-access-client-secret":
    "bdd31cbc4dec990953e39163fbbb194c93313ca9f0a6e420346af9d326b1d2a5" }
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserRDPApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of public domains that Access will secure.

    This field is deprecated in favor of `destinations` and will be supported until
    **November 21, 2025.** If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    use_clientless_isolation_app_launcher_url: Optional[bool] = None
    """
    Determines if users can access this application via a clientless browser
    isolation URL. This allows users to access private domains without connecting to
    Gateway. The option requires Clientless Browser Isolation to be set up with
    policies that allow users of this application.
    """


class McpServerApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class McpServerApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class McpServerApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


McpServerApplicationDestination: TypeAlias = Union[
    McpServerApplicationDestinationPublicDestination,
    McpServerApplicationDestinationPrivateDestination,
    McpServerApplicationDestinationViaMcpServerPortalDestination,
]


class McpServerApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class McpServerApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class McpServerApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[McpServerApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[McpServerApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class McpServerApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class McpServerApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[McpServerApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class McpServerApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class McpServerApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[McpServerApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[McpServerApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

McpServerApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[McpServerApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class McpServerApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[McpServerApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class McpServerApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[McpServerApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[McpServerApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    policies: Optional[List[McpServerApplicationPolicy]] = None

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[McpServerApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


class McpServerPortalApplicationDestinationPublicDestination(BaseModel):
    """A public hostname that Access will secure.

    Public destinations support sub-domain and path. Wildcard '*' can be used in the definition.
    """

    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class McpServerPortalApplicationDestinationPrivateDestination(BaseModel):
    cidr: Optional[str] = None
    """The CIDR range of the destination. Single IPs will be computed as /32."""

    hostname: Optional[str] = None
    """The hostname of the destination. Matches a valid SNI served by an HTTPS origin."""

    l4_protocol: Optional[Literal["tcp", "udp"]] = None
    """The L4 protocol of the destination.

    When omitted, both UDP and TCP traffic will match.
    """

    port_range: Optional[str] = None
    """The port range of the destination.

    Can be a single port or a range of ports. When omitted, all ports will match.
    """

    type: Optional[Literal["private"]] = None

    vnet_id: Optional[str] = None
    """The VNET ID to match the destination. When omitted, all VNETs will match."""


class McpServerPortalApplicationDestinationViaMcpServerPortalDestination(BaseModel):
    """A MCP server id configured in ai-controls.

    Access will secure the MCP server if accessed through a MCP portal.
    """

    mcp_server_id: Optional[str] = None
    """The MCP server id configured in ai-controls."""

    type: Optional[Literal["via_mcp_server_portal"]] = None


McpServerPortalApplicationDestination: TypeAlias = Union[
    McpServerPortalApplicationDestinationPublicDestination,
    McpServerPortalApplicationDestinationPrivateDestination,
    McpServerPortalApplicationDestinationViaMcpServerPortalDestination,
]


class McpServerPortalApplicationOAuthConfigurationDynamicClientRegistration(BaseModel):
    """Settings for OAuth dynamic client registration."""

    allow_any_on_localhost: Optional[bool] = None
    """Allows any client with redirect URIs on localhost."""

    allow_any_on_loopback: Optional[bool] = None
    """Allows any client with redirect URIs on 127.0.0.1."""

    allowed_uris: Optional[List[str]] = None
    """The URIs that are allowed as redirect URIs for dynamically registered clients.

    Must use the `https` protocol. Paths may end in `/*` to match all sub-paths.
    """

    enabled: Optional[bool] = None
    """Whether dynamic client registration is enabled."""


class McpServerPortalApplicationOAuthConfigurationGrant(BaseModel):
    """Settings for OAuth grant behavior."""

    access_token_lifetime: Optional[str] = None
    """The lifetime of the access token.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """

    session_duration: Optional[str] = None
    """The duration of the OAuth session.

    Must be in the format `300ms` or `2h45m`. Valid time units are ns, us (or µs),
    ms, s, m, h.
    """


class McpServerPortalApplicationOAuthConfiguration(BaseModel):
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow controlled by Access. When set, Access will act as the OAuth authorization server for this application. Only compatible with OAuth clients that support [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators for OAuth 2.0). This feature is currently in beta.
    """

    dynamic_client_registration: Optional[McpServerPortalApplicationOAuthConfigurationDynamicClientRegistration] = None
    """Settings for OAuth dynamic client registration."""

    enabled: Optional[bool] = None
    """Whether the OAuth configuration is enabled for this application.

    When set to `false`, Access will not handle OAuth for this application. Defaults
    to `true` if omitted.
    """

    grant: Optional[McpServerPortalApplicationOAuthConfigurationGrant] = None
    """Settings for OAuth grant behavior."""


class McpServerPortalApplicationPolicyConnectionRulesRDP(BaseModel):
    """The RDP-specific rules that define clipboard behavior for RDP connections."""

    allowed_clipboard_local_to_remote_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from local machine to remote RDP session.
    """

    allowed_clipboard_remote_to_local_formats: Optional[List[Literal["text"]]] = None
    """
    Clipboard formats allowed when copying from remote RDP session to local machine.
    """


class McpServerPortalApplicationPolicyConnectionRules(BaseModel):
    """
    The rules that define how users may connect to targets secured by your application.
    """

    rdp: Optional[McpServerPortalApplicationPolicyConnectionRulesRDP] = None
    """The RDP-specific rules that define clipboard behavior for RDP connections."""


class McpServerPortalApplicationPolicyMfaConfig(BaseModel):
    """Configures multi-factor authentication (MFA) settings."""

    allowed_authenticators: Optional[List[Literal["totp", "biometrics", "security_key"]]] = None
    """Lists the MFA methods that users can authenticate with."""

    mfa_disabled: Optional[bool] = None
    """Indicates whether to disable MFA for this resource.

    This option is available at the application and policy level.
    """

    session_duration: Optional[str] = None
    """Defines the duration of an MFA session.

    Must be in minutes (m) or hours (h). Minimum: 0m. Maximum: 720h (30 days).
    Examples:`5m` or `24h`.
    """


class McpServerPortalApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    connection_rules: Optional[McpServerPortalApplicationPolicyConnectionRules] = None
    """
    The rules that define how users may connect to targets secured by your
    application.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
    """The action Access will take if a user matches this policy.

    Infrastructure application policies can only use the Allow action.
    """

    exclude: Optional[List[AccessRule]] = None
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
    """

    include: Optional[List[AccessRule]] = None
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    isolation_required: Optional[bool] = None
    """
    Require this application to be served in an isolated browser for users matching
    this policy. 'Client Web Isolation' must be on for the account in order to use
    this feature.
    """

    mfa_config: Optional[McpServerPortalApplicationPolicyMfaConfig] = None
    """Configures multi-factor authentication (MFA) settings."""

    name: Optional[str] = None
    """The name of the Access policy."""

    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """

    purpose_justification_prompt: Optional[str] = None
    """A custom message that will appear on the purpose justification screen."""

    purpose_justification_required: Optional[bool] = None
    """Require users to enter a justification when they log in to the application."""

    require: Optional[List[AccessRule]] = None
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


class McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
    """
    Attributes for configuring Access Service Token authentication scheme for SCIM provisioning to an application.
    """

    client_id: str
    """
    Client ID of the Access service token used to authenticate with the remote
    service.
    """

    client_secret: str
    """
    Client secret of the Access service token used to authenticate with the remote
    service.
    """

    scheme: Literal["access_service_token"]
    """The authentication scheme to use when making SCIM requests to this application."""


McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

McpServerPortalApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[McpServerPortalApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class McpServerPortalApplicationSCIMConfig(BaseModel):
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[McpServerPortalApplicationSCIMConfigAuthentication] = None
    """
    Attributes for configuring HTTP Basic authentication scheme for SCIM
    provisioning to an application.
    """

    deactivate_on_delete: Optional[bool] = None
    """
    If false, propagates DELETE requests to the target application for SCIM
    resources. If true, sets 'active' to false on the SCIM resource. Note: Some
    targets do not support DELETE operations.
    """

    enabled: Optional[bool] = None
    """Whether SCIM provisioning is turned on for this application."""

    mappings: Optional[List[SCIMConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class McpServerPortalApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID."""

    allow_authenticate_via_warp: Optional[bool] = None
    """
    When set to true, users can authenticate to this application using their WARP
    session. When set to false this application will always require direct IdP
    authentication. This setting always overrides the organization setting for WARP
    authentication.
    """

    allowed_idps: Optional[List[AllowedIdPs]] = None
    """The identity providers your users can select when connecting to this
    application.

    Defaults to all IdPs configured in your account.
    """

    aud: Optional[str] = None
    """Audience tag."""

    auto_redirect_to_identity: Optional[bool] = None
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    custom_deny_message: Optional[str] = None
    """
    The custom error message shown to a user when they are denied access to the
    application.
    """

    custom_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing identity-based rules.
    """

    custom_non_identity_deny_url: Optional[str] = None
    """
    The custom URL a user is redirected to when they are denied access to the
    application when failing non-identity rules.
    """

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    destinations: Optional[List[McpServerPortalApplicationDestination]] = None
    """List of destinations secured by Access.

    This supersedes `self_hosted_domains` to allow for more flexibility in defining
    different types of domains. If `destinations` are provided, then
    `self_hosted_domains` will be ignored.
    """

    domain: Optional[str] = None
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    http_only_cookie_attribute: Optional[bool] = None
    """
    Enables the HttpOnly cookie attribute, which increases security against XSS
    attacks.
    """

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    oauth_configuration: Optional[McpServerPortalApplicationOAuthConfiguration] = None
    """
    **Beta:** Optional configuration for managing an OAuth authorization flow
    controlled by Access. When set, Access will act as the OAuth authorization
    server for this application. Only compatible with OAuth clients that support
    [RFC 8707](https://datatracker.ietf.org/doc/html/rfc8707) (Resource Indicators
    for OAuth 2.0). This feature is currently in beta.
    """

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    policies: Optional[List[McpServerPortalApplicationPolicy]] = None

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[McpServerPortalApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. Note: unsupported for infrastructure type applications.
    """

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """


ApplicationListResponse: TypeAlias = Union[
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
