# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .decision import Decision
from ...._models import BaseModel
from ..access_rule import AccessRule
from .allowed_idps import AllowedIdPs
from .cors_headers import CORSHeaders
from .oidc_saas_app import OIDCSaaSApp
from .saml_saas_app import SAMLSaaSApp
from .application_type import ApplicationType
from .scim_config_mapping import SCIMConfigMapping
from .self_hosted_domains import SelfHostedDomains
from .applications.approval_group import ApprovalGroup
from .scim_config_authentication_oauth2 import SCIMConfigAuthenticationOauth2
from .scim_config_authentication_http_basic import SCIMConfigAuthenticationHTTPBasic
from .scim_config_authentication_oauth_bearer_token import SCIMConfigAuthenticationOAuthBearerToken

__all__ = [
    "ApplicationCreateResponse",
    "SelfHostedApplication",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationSCIMConfig",
    "SelfHostedApplicationSCIMConfigAuthentication",
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationSaaSApp",
    "SaaSApplicationSCIMConfig",
    "SaaSApplicationSCIMConfigAuthentication",
    "BrowserSSHApplication",
    "BrowserSSHApplicationPolicy",
    "BrowserSSHApplicationSCIMConfig",
    "BrowserSSHApplicationSCIMConfigAuthentication",
    "BrowserVncApplication",
    "BrowserVncApplicationPolicy",
    "BrowserVncApplicationSCIMConfig",
    "BrowserVncApplicationSCIMConfigAuthentication",
    "AppLauncherApplication",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationSCIMConfig",
    "AppLauncherApplicationSCIMConfigAuthentication",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationSCIMConfig",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationSCIMConfig",
    "BrowserIsolationPermissionsApplicationSCIMConfigAuthentication",
    "BookmarkApplication",
    "BookmarkApplicationSCIMConfig",
    "BookmarkApplicationSCIMConfigAuthentication",
]


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

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


SelfHostedApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class SelfHostedApplicationSCIMConfig(BaseModel):
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

    scim_config: Optional[SelfHostedApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


SaaSApplicationSaaSApp = Union[SAMLSaaSApp, OIDCSaaSApp]

SaaSApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class SaaSApplicationSCIMConfig(BaseModel):
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

    scim_config: Optional[SaaSApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


BrowserSSHApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class BrowserSSHApplicationSCIMConfig(BaseModel):
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

    scim_config: Optional[BrowserSSHApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


BrowserVncApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class BrowserVncApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserVncApplicationSCIMConfigAuthentication] = None
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

    scim_config: Optional[BrowserVncApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


AppLauncherApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class AppLauncherApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[AppLauncherApplicationSCIMConfigAuthentication] = None
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

    scim_config: Optional[AppLauncherApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class DeviceEnrollmentPermissionsApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication] = None
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

    scim_config: Optional[DeviceEnrollmentPermissionsApplicationSCIMConfig] = None
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
    """The UUID of the policy"""

    approval_groups: Optional[List[ApprovalGroup]] = None
    """Administrators who can approve a temporary authentication request."""

    approval_required: Optional[bool] = None
    """
    Requires the user to request access from an administrator at the start of each
    session.
    """

    created_at: Optional[datetime] = None

    decision: Optional[Decision] = None
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


BrowserIsolationPermissionsApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class BrowserIsolationPermissionsApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserIsolationPermissionsApplicationSCIMConfigAuthentication] = None
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

    scim_config: Optional[BrowserIsolationPermissionsApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


BookmarkApplicationSCIMConfigAuthentication = Union[
    SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2
]


class BookmarkApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BookmarkApplicationSCIMConfigAuthentication] = None
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

    scim_config: Optional[BookmarkApplicationSCIMConfig] = None
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


ApplicationCreateResponse = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVncApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    BookmarkApplication,
]
