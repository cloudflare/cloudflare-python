# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "AccessApps",
    "SelfHostedApplication",
    "SelfHostedApplicationCorsHeaders",
    "SaaSApplication",
    "SaaSApplicationSaasApp",
    "SaaSApplicationSaasAppAccessSamlSaasApp",
    "SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributes",
    "SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributesSource",
    "SaaSApplicationSaasAppAccessOidcSaasApp",
    "BrowserSSHApplication",
    "BrowserSSHApplicationCorsHeaders",
    "BrowserVncApplication",
    "BrowserVncApplicationCorsHeaders",
    "AppLauncherApplication",
    "DeviceEnrollmentPermissionsApplication",
    "BrowserIsolationPermissionsApplication",
    "BookmarkApplication",
]


class SelfHostedApplicationCorsHeaders(BaseModel):
    allow_all_headers: Optional[bool] = None
    """Allows all HTTP request headers."""

    allow_all_methods: Optional[bool] = None
    """Allows all HTTP request methods."""

    allow_all_origins: Optional[bool] = None
    """Allows all origins."""

    allow_credentials: Optional[bool] = None
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Optional[List[object]] = None
    """Allowed HTTP request headers."""

    allowed_methods: Optional[
        List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    ] = None
    """Allowed HTTP request methods."""

    allowed_origins: Optional[List[object]] = None
    """Allowed origins."""

    max_age: Optional[float] = None
    """The maximum number of seconds the results of a preflight request can be cached."""


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

    allowed_idps: Optional[List[str]] = None
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

    cors_headers: Optional[SelfHostedApplicationCorsHeaders] = None

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

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: Optional[List[str]] = None
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


class SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributesSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP attribute."""


class SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributes(BaseModel):
    name: Optional[str] = None
    """The name of the attribute."""

    name_format: Optional[
        Literal[
            "urn:oasis:names:tc:SAML:2.0:attrname-format:unspecified",
            "urn:oasis:names:tc:SAML:2.0:attrname-format:basic",
            "urn:oasis:names:tc:SAML:2.0:attrname-format:uri",
        ]
    ] = None
    """A globally unique name for an identity or service provider."""

    source: Optional[SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributesSource] = None


class SaaSApplicationSaasAppAccessSamlSaasApp(BaseModel):
    auth_type: Optional[Literal["saml", "oidc"]] = None
    """Optional identifier indicating the authentication protocol used for the saas
    app.

    Required for OIDC. Default if unset is "saml"
    """

    consumer_service_url: Optional[str] = None
    """
    The service provider's endpoint that is responsible for receiving and parsing a
    SAML assertion.
    """

    created_at: Optional[datetime] = None

    custom_attributes: Optional[SaaSApplicationSaasAppAccessSamlSaasAppCustomAttributes] = None

    default_relay_state: Optional[str] = None
    """
    The URL that the user will be redirected to after a successful login for IDP
    initiated logins.
    """

    idp_entity_id: Optional[str] = None
    """The unique identifier for your SaaS application."""

    name_id_format: Optional[Literal["id", "email"]] = None
    """The format of the name identifier sent to the SaaS application."""

    name_id_transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms an application's
    user identities into a NameID value for its SAML assertion. This expression
    should evaluate to a singular string. The output of this expression can override
    the `name_id_format` setting.
    """

    public_key: Optional[str] = None
    """The Access public certificate that will be used to verify your identity."""

    saml_attribute_transform_jsonata: Optional[str] = None
    """
    A [JSONata] (https://jsonata.org/) expression that transforms an application's
    user identities into attribute assertions in the SAML response. The expression
    can transform id, email, name, and groups values. It can also transform fields
    listed in the saml_attributes or oidc_fields of the identity provider used to
    authenticate. The output of this expression must be a JSON object.
    """

    sp_entity_id: Optional[str] = None
    """A globally unique name for an identity or service provider."""

    sso_endpoint: Optional[str] = None
    """The endpoint where your SaaS application will send login requests."""

    updated_at: Optional[datetime] = None


class SaaSApplicationSaasAppAccessOidcSaasApp(BaseModel):
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

    grant_types: Optional[List[Literal["authorization_code", "authorization_code_with_pkce"]]] = None
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

    scopes: Optional[List[Literal["openid", "groups", "email", "profile"]]] = None
    """Define the user information shared with access"""

    updated_at: Optional[datetime] = None


SaaSApplicationSaasApp = Union[SaaSApplicationSaasAppAccessSamlSaasApp, SaaSApplicationSaasAppAccessOidcSaasApp]


class SaaSApplication(BaseModel):
    id: Optional[str] = None
    """UUID"""

    allowed_idps: Optional[List[str]] = None
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

    saas_app: Optional[SaaSApplicationSaasApp] = None

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[str] = None
    """The application type."""

    updated_at: Optional[datetime] = None


class BrowserSSHApplicationCorsHeaders(BaseModel):
    allow_all_headers: Optional[bool] = None
    """Allows all HTTP request headers."""

    allow_all_methods: Optional[bool] = None
    """Allows all HTTP request methods."""

    allow_all_origins: Optional[bool] = None
    """Allows all origins."""

    allow_credentials: Optional[bool] = None
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Optional[List[object]] = None
    """Allowed HTTP request headers."""

    allowed_methods: Optional[
        List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    ] = None
    """Allowed HTTP request methods."""

    allowed_origins: Optional[List[object]] = None
    """Allowed origins."""

    max_age: Optional[float] = None
    """The maximum number of seconds the results of a preflight request can be cached."""


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

    allowed_idps: Optional[List[str]] = None
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

    cors_headers: Optional[BrowserSSHApplicationCorsHeaders] = None

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

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: Optional[List[str]] = None
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


class BrowserVncApplicationCorsHeaders(BaseModel):
    allow_all_headers: Optional[bool] = None
    """Allows all HTTP request headers."""

    allow_all_methods: Optional[bool] = None
    """Allows all HTTP request methods."""

    allow_all_origins: Optional[bool] = None
    """Allows all origins."""

    allow_credentials: Optional[bool] = None
    """
    When set to `true`, includes credentials (cookies, authorization headers, or TLS
    client certificates) with requests.
    """

    allowed_headers: Optional[List[object]] = None
    """Allowed HTTP request headers."""

    allowed_methods: Optional[
        List[Literal["GET", "POST", "HEAD", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]]
    ] = None
    """Allowed HTTP request methods."""

    allowed_origins: Optional[List[object]] = None
    """Allowed origins."""

    max_age: Optional[float] = None
    """The maximum number of seconds the results of a preflight request can be cached."""


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

    allowed_idps: Optional[List[str]] = None
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

    cors_headers: Optional[BrowserVncApplicationCorsHeaders] = None

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

    path_cookie_attribute: Optional[bool] = None
    """Enables cookie paths to scope an application's JWT to the application path.

    If disabled, the JWT will scope to the hostname by default
    """

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    self_hosted_domains: Optional[List[str]] = None
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


class AppLauncherApplication(BaseModel):
    type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
    """The application type."""

    id: Optional[str] = None
    """UUID"""

    allowed_idps: Optional[List[str]] = None
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

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class DeviceEnrollmentPermissionsApplication(BaseModel):
    type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
    """The application type."""

    id: Optional[str] = None
    """UUID"""

    allowed_idps: Optional[List[str]] = None
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

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BrowserIsolationPermissionsApplication(BaseModel):
    type: Literal["self_hosted", "saas", "ssh", "vnc", "app_launcher", "warp", "biso", "bookmark", "dash_sso"]
    """The application type."""

    id: Optional[str] = None
    """UUID"""

    allowed_idps: Optional[List[str]] = None
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

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    updated_at: Optional[datetime] = None


class BookmarkApplication(BaseModel):
    id: Optional[str] = None
    """UUID"""

    app_launcher_visible: Optional[object] = None

    aud: Optional[str] = None
    """Audience tag."""

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The URL or domain of the bookmark."""

    logo_url: Optional[str] = None
    """The image URL for the logo shown in the App Launcher dashboard."""

    name: Optional[str] = None
    """The name of the application."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    type: Optional[str] = None
    """The application type."""

    updated_at: Optional[datetime] = None


AccessApps = Union[
    SelfHostedApplication,
    SaaSApplication,
    BrowserSSHApplication,
    BrowserVncApplication,
    AppLauncherApplication,
    DeviceEnrollmentPermissionsApplication,
    BrowserIsolationPermissionsApplication,
    BookmarkApplication,
]
