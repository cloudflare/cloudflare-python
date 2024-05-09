# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..access_rule import AccessRule
from .allowed_idps import AllowedIdPs
from .cors_headers import CORSHeaders
from .saml_saas_app import SAMLSaaSApp
from .application_type import ApplicationType
from .self_hosted_domains import SelfHostedDomains
from .applications.approval_group import ApprovalGroup

__all__ = [
    "ApplicationUpdateResponse",
    "SelfHostedApplication",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationScimConfig",
    "SelfHostedApplicationScimConfigAuthentication",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "SelfHostedApplicationScimConfigMapping",
    "SelfHostedApplicationScimConfigMappingOperations",
    "SaaSApplication",
    "SaaSApplicationPolicy",
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
    "BrowserSSHApplicationScimConfig",
    "BrowserSSHApplicationScimConfigAuthentication",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BrowserSSHApplicationScimConfigMapping",
    "BrowserSSHApplicationScimConfigMappingOperations",
    "BrowserVncApplication",
    "BrowserVncApplicationPolicy",
    "BrowserVncApplicationScimConfig",
    "BrowserVncApplicationScimConfigAuthentication",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "BrowserVncApplicationScimConfigMapping",
    "BrowserVncApplicationScimConfigMappingOperations",
    "AppLauncherApplication",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationScimConfig",
    "AppLauncherApplicationScimConfigAuthentication",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "AppLauncherApplicationScimConfigMapping",
    "AppLauncherApplicationScimConfigMappingOperations",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationScimConfig",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthentication",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken",
    "DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2",
    "DeviceEnrollmentPermissionsApplicationScimConfigMapping",
    "DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
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


class SelfHostedApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


SelfHostedApplicationScimConfigAuthentication = Union[
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    SelfHostedApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class SelfHostedApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SelfHostedApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[SelfHostedApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class SelfHostedApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[SelfHostedApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[SelfHostedApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class SelfHostedApplication(BaseModel):
    domain: str
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: str
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

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

    name: Optional[str] = None
    """The name of the application."""

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

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[SelfHostedApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of domains that Access will secure."""

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


class SaaSApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP claim."""


class SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims(BaseModel):
    name: Optional[str] = None
    """The name of the claim."""

    name_by_idp: Optional[Dict[str, str]] = None
    """A mapping from IdP ID to claim name."""

    required: Optional[bool] = None
    """If the claim is required when building an OIDC token."""

    scope: Optional[Literal["groups", "profile", "email", "openid"]] = None
    """The scope of the claim."""

    source: Optional[SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource] = None


class SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions(BaseModel):
    lifetime: Optional[str] = None
    """How long a refresh token will be valid for after creation.

    Valid units are m,h,d. Must be longer than 1m.
    """


class SaaSApplicationSaaSAppAccessOIDCSaaSApp(BaseModel):
    allow_pkce_without_client_secret: Optional[bool] = None
    """
    If client secret should be required on the token endpoint when
    authorization_code_with_pkce grant is used.
    """

    app_launcher_url: Optional[str] = None
    """The URL where this applications tile redirects users"""

    auth_type: Optional[Literal["saml", "oidc"]] = None
    """Identifier of the authentication protocol used for the saas app.

    Required for OIDC.
    """

    client_id: Optional[str] = None
    """The application client id"""

    client_secret: Optional[str] = None
    """The application client secret, only returned on POST request."""

    created_at: Optional[datetime] = None

    custom_claims: Optional[SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims] = None

    grant_types: Optional[List[Literal["authorization_code", "authorization_code_with_pkce", "refresh_tokens"]]] = None
    """The OIDC flows supported by this application"""

    group_filter_regex: Optional[str] = None
    """A regex to filter Cloudflare groups returned in ID token and userinfo endpoint"""

    public_key: Optional[str] = None
    """The Access public certificate that will be used to verify your identity."""

    redirect_uris: Optional[List[str]] = None
    """
    The permitted URL's for Cloudflare to return Authorization codes and Access/ID
    tokens
    """

    refresh_token_options: Optional[SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions] = None

    scopes: Optional[List[Literal["openid", "groups", "email", "profile"]]] = None
    """
    Define the user information shared with access, "offline_access" scope will be
    automatically enabled if refresh tokens are enabled
    """

    updated_at: Optional[datetime] = None


SaaSApplicationSaaSApp = Union[SAMLSaaSApp, SaaSApplicationSaaSAppAccessOIDCSaaSApp]


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


SaaSApplicationScimConfigAuthentication = Union[
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    SaaSApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class SaaSApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SaaSApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[SaaSApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class SaaSApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[SaaSApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[SaaSApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class SaaSApplication(BaseModel):
    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

    custom_pages: Optional[List[str]] = None
    """The custom pages that will be displayed when applicable for this application"""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[SaaSApplicationPolicy]] = None

    saas_app: Optional[SaaSApplicationSaaSApp] = None

    scim_config: Optional[SaaSApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[str] = None
    """The application type."""

    updated_at: Optional[datetime] = None


class BrowserSSHApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserSSHApplicationScimConfigAuthentication = Union[
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserSSHApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserSSHApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserSSHApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[BrowserSSHApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserSSHApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserSSHApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[BrowserSSHApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserSSHApplication(BaseModel):
    domain: str
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: str
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

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

    name: Optional[str] = None
    """The name of the application."""

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

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserSSHApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of domains that Access will secure."""

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


class BrowserVncApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserVncApplicationScimConfigAuthentication = Union[
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserVncApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserVncApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserVncApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[BrowserVncApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserVncApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserVncApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[BrowserVncApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserVncApplication(BaseModel):
    domain: str
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    type: str
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

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

    name: Optional[str] = None
    """The name of the application."""

    options_preflight_bypass: Optional[bool] = None
    """
    Allows options preflight requests to bypass Access authentication and go
    directly to the origin. Cannot turn on if cors_headers is set.
    """

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    policies: Optional[List[BrowserVncApplicationPolicy]] = None

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserVncApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    self_hosted_domains: Optional[List[SelfHostedDomains]] = None
    """List of domains that Access will secure."""

    service_auth_401_redirect: Optional[bool] = None
    """Returns a 401 status code when the request is blocked by a Service Auth policy."""

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


class AppLauncherApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


AppLauncherApplicationScimConfigAuthentication = Union[
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    AppLauncherApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class AppLauncherApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class AppLauncherApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[AppLauncherApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class AppLauncherApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[AppLauncherApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[AppLauncherApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class AppLauncherApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[AppLauncherApplicationPolicy]] = None

    scim_config: Optional[AppLauncherApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class DeviceEnrollmentPermissionsApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    BaseModel
):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


DeviceEnrollmentPermissionsApplicationScimConfigAuthentication = Union[
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    DeviceEnrollmentPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class DeviceEnrollmentPermissionsApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[DeviceEnrollmentPermissionsApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class DeviceEnrollmentPermissionsApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[DeviceEnrollmentPermissionsApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[DeviceEnrollmentPermissionsApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class DeviceEnrollmentPermissionsApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[DeviceEnrollmentPermissionsApplicationPolicy]] = None

    scim_config: Optional[DeviceEnrollmentPermissionsApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserIsolationPermissionsApplicationPolicy(BaseModel):
    id: Optional[str] = None
    """The ID of the Access policy."""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Literal["allow", "deny", "non_identity", "bypass"]] = None
    """The action Access will take if a user matches this policy."""

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

    name: Optional[str] = None
    """The name of the Access policy."""

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


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(
    BaseModel
):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BrowserIsolationPermissionsApplicationScimConfigAuthentication = Union[
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BrowserIsolationPermissionsApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BrowserIsolationPermissionsApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BrowserIsolationPermissionsApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[BrowserIsolationPermissionsApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BrowserIsolationPermissionsApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserIsolationPermissionsApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[BrowserIsolationPermissionsApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BrowserIsolationPermissionsApplication(BaseModel):
    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID"""

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[BrowserIsolationPermissionsApplicationPolicy]] = None

    scim_config: Optional[BrowserIsolationPermissionsApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic(BaseModel):
    password: str
    """Password used to authenticate with the remote SCIM service."""

    scheme: Literal["httpbasic"]
    """The authentication scheme to use when making SCIM requests to this application."""

    user: str
    """User name used to authenticate with the remote SCIM service."""


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken(BaseModel):
    token: str
    """Token used to authenticate with the remote SCIM service."""

    scheme: Literal["oauthbearertoken"]
    """The authentication scheme to use when making SCIM requests to this application."""


class BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2(BaseModel):
    authorization_url: str
    """URL used to generate the auth code used during token generation."""

    client_id: str
    """
    Client ID used to authenticate when generating a token for authenticating with
    the remote SCIM service.
    """

    client_secret: str
    """
    Secret used to authenticate when generating a token for authenticating with the
    remove SCIM service.
    """

    scheme: Literal["oauth2"]
    """The authentication scheme to use when making SCIM requests to this application."""

    token_url: str
    """
    URL used to generate the token used to authenticate with the remote SCIM
    service.
    """

    scopes: Optional[List[str]] = None
    """
    The authorization scopes to request when generating the token used to
    authenticate with the remove SCIM service.
    """


BookmarkApplicationScimConfigAuthentication = Union[
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationHTTPBasic,
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOAuthBearerToken,
    BookmarkApplicationScimConfigAuthenticationAccessScimConfigAuthenticationOauth2,
]


class BookmarkApplicationScimConfigMappingOperations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class BookmarkApplicationScimConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[BookmarkApplicationScimConfigMappingOperations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """


class BookmarkApplicationScimConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BookmarkApplicationScimConfigAuthentication] = None
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

    mappings: Optional[List[BookmarkApplicationScimConfigMapping]] = None
    """
    A list of mappings to apply to SCIM resources before provisioning them in this
    application. These can transform or filter the resources to be provisioned.
    """


class BookmarkApplication(BaseModel):
    id: Optional[str] = None
    """UUID"""

    app_launcher_visible: Optional[bool] = None
    """Displays the application in the App Launcher."""

    aud: Optional[str] = None
    """Audience tag."""

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The URL or domain of the bookmark."""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    scim_config: Optional[BookmarkApplicationScimConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[str] = None
    """The application type."""

    updated_at: Optional[datetime] = None


ApplicationUpdateResponse = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVncApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    BookmarkApplication,
]
