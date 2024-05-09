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
    "SaaSApplication",
    "SaaSApplicationPolicy",
    "SaaSApplicationPolicyAccessAppPolicyLink",
    "SaaSApplicationPolicyUnionMember2",
    "SaaSApplicationSaaSApp",
    "SaaSApplicationSaaSAppAccessOIDCSaaSApp",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaimsSource",
    "SaaSApplicationSaaSAppAccessOIDCSaaSAppRefreshTokenOptions",
    "BrowserSSHApplication",
    "BrowserSSHApplicationPolicy",
    "BrowserSSHApplicationPolicyAccessAppPolicyLink",
    "BrowserSSHApplicationPolicyUnionMember2",
    "BrowserVncApplication",
    "BrowserVncApplicationPolicy",
    "BrowserVncApplicationPolicyAccessAppPolicyLink",
    "BrowserVncApplicationPolicyUnionMember2",
    "AppLauncherApplication",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationPolicyAccessAppPolicyLink",
    "AppLauncherApplicationPolicyUnionMember2",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink",
    "DeviceEnrollmentPermissionsApplicationPolicyUnionMember2",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationPolicy",
    "BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink",
    "BrowserIsolationPermissionsApplicationPolicyUnionMember2",
    "AccessBookmarkProps",
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
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


class SaaSApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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


class SaaSApplicationSaaSAppAccessOIDCSaaSAppCustomClaims(TypedDict, total=False):
    name: str
    """The name of the claim."""

    name_by_idp: Dict[str, str]
    """A mapping from IdP ID to claim name."""

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
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class AppLauncherApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class DeviceEnrollmentPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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

    session_duration: str
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """


class BrowserIsolationPermissionsApplicationPolicyAccessAppPolicyLink(TypedDict, total=False):
    id: str
    """The ID of the Access policy."""

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

    id: str
    """The ID of the Access policy."""

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


class AccessBookmarkProps(TypedDict, total=False):
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

    tags: List[str]
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: str
    """The application type."""


ApplicationUpdateParams = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVncApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    AccessBookmarkProps,
]
