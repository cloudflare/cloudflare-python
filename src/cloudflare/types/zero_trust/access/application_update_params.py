# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .allowed_idps import AllowedIdPs
from .application_type import ApplicationType
from ..access_rule_param import AccessRuleParam
from .cors_headers_param import CORSHeadersParam
from .saml_saas_app_param import SAMLSaaSAppParam
from .self_hosted_domains import SelfHostedDomains
from .applications.approval_group_param import ApprovalGroupParam

__all__ = [
    "ApplicationUpdateParams",
    "SelfHostedApplication",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationPolicyAccessAppPolicyLink",
    "SelfHostedApplicationPolicyUnionMember2",
    "SelfHostedApplicationScimConfig",
    "SelfHostedApplicationScimConfigAuthentication",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "SelfHostedApplicationScimConfigMapping",
    "SelfHostedApplicationScimConfigMappingOperations",
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationPolicyAccessAppPolicyLink",
    "SaaSApplicationPolicyUnionMember2",
    "SaaSApplicationSaaSApp",
    "SaaSApplicationSaaSAppAccessOIDCSaaSApp",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions",
    "SaaSApplicationScimConfig",
    "SaaSApplicationScimConfigAuthentication",
    "SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "SaaSApplicationScimConfigMapping",
    "SaaSApplicationScimConfigMappingOperations",
    "BrowserSSHApplication",
    "BrowserSSHApplicationPolicy",
    "BrowserSSHApplicationPolicyAccessAppPolicyLink",
    "BrowserSSHApplicationPolicyUnionMember2",
    "BrowserSSHApplicationScimConfig",
    "BrowserSSHApplicationScimConfigAuthentication",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BrowserSSHApplicationScimConfigMapping",
    "BrowserSSHApplicationScimConfigMappingOperations",
    "BrowserVncApplication",
    "BrowserVncApplicationPolicy",
    "BrowserVncApplicationPolicyAccessAppPolicyLink",
    "BrowserVncApplicationPolicyUnionMember2",
    "BrowserVncApplicationScimConfig",
    "BrowserVncApplicationScimConfigAuthentication",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BrowserVncApplicationScimConfigMapping",
    "BrowserVncApplicationScimConfigMappingOperations",
    "AppLauncherApplication",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationPolicyAccessAppPolicyLink",
    "AppLauncherApplicationPolicyUnionMember2",
    "AppLauncherApplicationScimConfig",
    "AppLauncherApplicationScimConfigAuthentication",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "AppLauncherApplicationScimConfigMapping",
    "AppLauncherApplicationScimConfigMappingOperations",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2",
    "DeviceEnrollmentPermissionsApplicationScimConfig",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthentication",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "DeviceEnrollmentPermissionsApplicationScimConfigMapping",
    "DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2",
    "BrowserIsolationPermissionsApplicationScimConfig",
    "BrowserIsolationPermissionsApplicationScimConfigAuthentication",
    "BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BrowserIsolationPermissionsApplicationScimConfigMapping",
    "BrowserIsolationPermissionsApplicationScimConfigMappingOperations",
    "BookmarkApplication",
    "BookmarkApplicationScimConfig",
    "BookmarkApplicationScimConfigAuthentication",
    "BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BookmarkApplicationScimConfigMapping",
    "BookmarkApplicationScimConfigMappingOperations",
]


class SelfHostedApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
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
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: SelfHostedApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of domains that Access will secure."""

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


class SelfHostedApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SelfHostedApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


SelfHostedApplicationPolicy = Union[
    SelfHostedApplicationPolicyAccessAppPolicyLink, str, SelfHostedApplicationPolicyUnionMember2
]


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


SelfHostedApplicationScimConfigAuthentication = Union[
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class SelfHostedApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SelfHostedApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: SelfHostedApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class SelfHostedApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: SelfHostedApplicationScimConfigAuthentication
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

    mappings: Iterable[SelfHostedApplicationScimConfigMapping]
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
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    saas_app: SaaSApplicationSaaSApp

    scim_config: SaaSApplicationScimConfig
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
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SaaSApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


SaaSApplicationPolicy = Union[SaaSApplicationPolicyAccessAppPolicyLink, str, SaaSApplicationPolicyUnionMember2]


class SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource(TypedDict, total=False):
    name: str
    """The name of the IdP claim."""

    name_by_idp: Dict[str, str]
    """A mapping from IdP ID to claim name."""


class SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims(TypedDict, total=False):
    name: str
    """The name of the claim."""

    required: bool
    """If the claim is required when building an OIDC token."""

    scope: Literal["groups", "profile", "email", "openid"]
    """The scope of the claim."""

    source: SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource


class SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions(TypedDict, total=False):
    lifetime: str
    """How long a refresh token will be valid for after creation.

    Valid units are m,h,d. Must be longer than 1m.
    """


class SaaSApplicationSaaSAppAccessOIDCSaaSApp(TypedDict, total=False):
    allow_pkce_without_client_secret: bool
    """
    If client secret should be required on the token endpoint when
    authorization_code_with_pkce grant is used.
    """

    app_launcher_url: str
    """The URL where this applications tile redirects users"""

    auth_type: Literal["saml", "oidc"]
    """Identifier of the authentication protocol used for the saas app.

    Required for OIDC.
    """

    client_id: str
    """The application client id"""

    client_secret: str
    """The application client secret, only returned on POST request."""

    custom_claims: SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims

    grant_types: List[Literal["authorization_code", "authorization_code_with_pkce", "refresh_tokens"]]
    """The OIDC flows supported by this application"""

    group_filter_regex: str
    """A regex to filter Cloudflare groups returned in ID token and userinfo endpoint"""

    public_key: str
    """The Access public certificate that will be used to verify your identity."""

    redirect_uris: List[str]
    """
    The permitted URL's for Cloudflare to return Authorization codes and Access/ID
    tokens
    """

    refresh_token_options: SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions

    scopes: List[Literal["openid", "groups", "email", "profile"]]
    """
    Define the user information shared with access, "offline_access" scope will be
    automatically enabled if refresh tokens are enabled
    """


SaaSApplicationSaaSApp = Union[SAMLSaaSAppParam, SaaSApplicationSaaSAppAccessOIDCSaaSApp]


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(TypedDict, total=False):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


SaaSApplicationScimConfigAuthentication = Union[
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class SaaSApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SaaSApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: SaaSApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class SaaSApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: SaaSApplicationScimConfigAuthentication
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

    mappings: Iterable[SaaSApplicationScimConfigMapping]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserSSHApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
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
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserSSHApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of domains that Access will secure."""

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


class BrowserSSHApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserSSHApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserSSHApplicationPolicy = Union[
    BrowserSSHApplicationPolicyAccessAppPolicyLink, str, BrowserSSHApplicationPolicyUnionMember2
]


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserSSHApplicationScimConfigAuthentication = Union[
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserSSHApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserSSHApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: BrowserSSHApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserSSHApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserSSHApplicationScimConfigAuthentication
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

    mappings: Iterable[BrowserSSHApplicationScimConfigMapping]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserVncApplication(TypedDict, total=False):
    domain: Required[str]
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
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

    policies: List[BrowserVncApplicationPolicy]
    """
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    same_site_cookie_attribute: str
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: BrowserVncApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: List[SelfHostedDomains]
    """List of domains that Access will secure."""

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


class BrowserVncApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserVncApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserVncApplicationPolicy = Union[
    BrowserVncApplicationPolicyAccessAppPolicyLink, str, BrowserVncApplicationPolicyUnionMember2
]


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserVncApplicationScimConfigAuthentication = Union[
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserVncApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserVncApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: BrowserVncApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserVncApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserVncApplicationScimConfigAuthentication
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

    mappings: Iterable[BrowserVncApplicationScimConfigMapping]
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

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    policies: List[AppLauncherApplicationPolicy]
    """
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: AppLauncherApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class AppLauncherApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class AppLauncherApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


AppLauncherApplicationPolicy = Union[
    AppLauncherApplicationPolicyAccessAppPolicyLink, str, AppLauncherApplicationPolicyUnionMember2
]


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


AppLauncherApplicationScimConfigAuthentication = Union[
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class AppLauncherApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class AppLauncherApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: AppLauncherApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class AppLauncherApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: AppLauncherApplicationScimConfigAuthentication
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

    mappings: Iterable[AppLauncherApplicationScimConfigMapping]
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

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    policies: List[DeviceEnrollmentPermissionsApplicationPolicy]
    """
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: DeviceEnrollmentPermissionsApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class DeviceEnrollmentPermissionsApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


DeviceEnrollmentPermissionsApplicationPolicy = Union[
    DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink,
    str,
    DeviceEnrollmentPermissionsApplicationPolicyUnionMember2,
]


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(
    TypedDict, total=False
):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(
    TypedDict, total=False
):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


DeviceEnrollmentPermissionsApplicationScimConfigAuthentication = Union[
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class DeviceEnrollmentPermissionsApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class DeviceEnrollmentPermissionsApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: DeviceEnrollmentPermissionsApplicationScimConfigAuthentication
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

    mappings: Iterable[DeviceEnrollmentPermissionsApplicationScimConfigMapping]
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

    auto_redirect_to_identity: bool
    """When set to `true`, users skip the identity provider selection step during
    login.

    You must specify only one identity provider in allowed_idps.
    """

    policies: List[BrowserIsolationPermissionsApplicationPolicy]
    """
    The policies that will apply to the application, in ascending order of
    precedence. Items can reference existing policies or create new policies
    exclusive to the application.
    """

    scim_config: BrowserIsolationPermissionsApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    precedence: int
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserIsolationPermissionsApplicationPolicyUnionMember2(TypedDict, total=False):
    decision: Required[Literal["allow", "deny", "non_identity", "bypass"]]
    """The action Access will take if a user matches this policy."""

    include: Required[Iterable[AccessRuleParam]]
    """Rules evaluated with an OR logical operator.

    A user needs to meet only one of the Include rules.
    """

    name: Required[str]
    """The name of the Access policy."""

    approval_groups: Iterable[ApprovalGroupParam]
    """Administrators who can approve a temporary authentication request."""

    approval_required: bool
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    exclude: Iterable[AccessRuleParam]
    """Rules evaluated with a NOT logical operator.

    To match the policy, a user cannot meet any of the Exclude rules.
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

    require: Iterable[AccessRuleParam]
    """Rules evaluated with an AND logical operator.

    To match the policy, a user must meet all of the Require rules.
    """

    session_duration: str
    """The amount of time that tokens issued for the application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


BrowserIsolationPermissionsApplicationPolicy = Union[
    BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink,
    str,
    BrowserIsolationPermissionsApplicationPolicyUnionMember2,
]


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(
    TypedDict, total=False
):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    TypedDict, total=False
):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(
    TypedDict, total=False
):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserIsolationPermissionsApplicationScimConfigAuthentication = Union[
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserIsolationPermissionsApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserIsolationPermissionsApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: BrowserIsolationPermissionsApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserIsolationPermissionsApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BrowserIsolationPermissionsApplicationScimConfigAuthentication
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

    mappings: Iterable[BrowserIsolationPermissionsApplicationScimConfigMapping]
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

    scim_config: BookmarkApplicationScimConfig
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(TypedDict, total=False):
    password: Required[str]
    """Password used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["httpbasic"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: Required[str]
    """User name used to authenticate with the remote SCIM service."""


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(TypedDict, total=False):
    token: Required[str]
    """Token used to authenticate with the remote SCIM service."""

    scheme: Required[Literal["oauthbearertoken"]]
    """The authentication scheme to use when making SCIM requests to this application."""


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(TypedDict, total=False):
    authorization_url: Required[str]
    """URL used to generate the auth code used during token generation."""

    client_id: Required[str]
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: Required[str]
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Required[Literal["oauth2"]]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: Required[str]
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: List[str]
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BookmarkApplicationScimConfigAuthentication = Union[
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BookmarkApplicationScimConfigMappingOperations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BookmarkApplicationScimConfigMapping(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: BookmarkApplicationScimConfigMappingOperations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BookmarkApplicationScimConfig(TypedDict, total=False):
    idp_uid: Required[str]
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: Required[str]
    """The base URI for the application's SCIM-compatible API."""

    authentication: BookmarkApplicationScimConfigAuthentication
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

    mappings: Iterable[BookmarkApplicationScimConfigMapping]
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


ApplicationUpdateParams = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVncApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    BookmarkApplication,
]
