# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .scim_config_authentication_http_basic import SCIMConfigAuthenticationHTTPBasic

from .scim_config_authentication_oauth_bearer_token import SCIMConfigAuthenticationOAuthBearerToken

from .scim_config_authentication_oauth2 import SCIMConfigAuthenticationOauth2

from typing_extensions import TypeAlias

from ...._models import BaseModel

from typing import Optional, List

from .scim_config_mapping import SCIMConfigMapping

from .allowed_idps import AllowedIdPs

from .cors_headers import CORSHeaders

from datetime import datetime

from .application_policy import ApplicationPolicy

from .self_hosted_domains import SelfHostedDomains

from .saml_saas_app import SAMLSaaSApp

from .oidc_saas_app import OIDCSaaSApp

from .application_type import ApplicationType

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ApplicationCreateResponse", "SelfHostedApplication", "SelfHostedApplicationSCIMConfig", "SelfHostedApplicationSCIMConfigAuthentication", "SaaSApplication", "SaaSApplicationSaaSApp", "SaaSApplicationSCIMConfig", "SaaSApplicationSCIMConfigAuthentication", "BrowserSSHApplication", "BrowserSSHApplicationSCIMConfig", "BrowserSSHApplicationSCIMConfigAuthentication", "BrowserVNCApplication", "BrowserVNCApplicationSCIMConfig", "BrowserVNCApplicationSCIMConfigAuthentication", "AppLauncherApplication", "AppLauncherApplicationFooterLink", "AppLauncherApplicationLandingPageDesign", "AppLauncherApplicationSCIMConfig", "AppLauncherApplicationSCIMConfigAuthentication", "DeviceEnrollmentPermissionsApplication", "DeviceEnrollmentPermissionsApplicationFooterLink", "DeviceEnrollmentPermissionsApplicationLandingPageDesign", "DeviceEnrollmentPermissionsApplicationSCIMConfig", "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication", "BrowserIsolationPermissionsApplication", "BrowserIsolationPermissionsApplicationFooterLink", "BrowserIsolationPermissionsApplicationLandingPageDesign", "BrowserIsolationPermissionsApplicationSCIMConfig", "BrowserIsolationPermissionsApplicationSCIMConfigAuthentication", "BookmarkApplication", "BookmarkApplicationSCIMConfig", "BookmarkApplicationSCIMConfigAuthentication"]

SelfHostedApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    policies: Optional[List[ApplicationPolicy]] = None

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

SaaSApplicationSaaSApp: TypeAlias = Union[SAMLSaaSApp, OIDCSaaSApp]

SaaSApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    policies: Optional[List[ApplicationPolicy]] = None

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

BrowserSSHApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    policies: Optional[List[ApplicationPolicy]] = None

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

BrowserVNCApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

class BrowserVNCApplicationSCIMConfig(BaseModel):
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

    policies: Optional[List[ApplicationPolicy]] = None

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

class AppLauncherApplicationFooterLink(BaseModel):
    name: str
    """The hypertext in the footer link."""

    url: str
    """the hyperlink in the footer link."""

class AppLauncherApplicationLandingPageDesign(BaseModel):
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

AppLauncherApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    footer_links: Optional[List[AppLauncherApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[AppLauncherApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[ApplicationPolicy]] = None

    scim_config: Optional[AppLauncherApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: Optional[bool] = None
    """Determines when to skip the App Launcher landing page."""

    updated_at: Optional[datetime] = None

class DeviceEnrollmentPermissionsApplicationFooterLink(BaseModel):
    name: str
    """The hypertext in the footer link."""

    url: str
    """the hyperlink in the footer link."""

class DeviceEnrollmentPermissionsApplicationLandingPageDesign(BaseModel):
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

DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    footer_links: Optional[List[DeviceEnrollmentPermissionsApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[DeviceEnrollmentPermissionsApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[ApplicationPolicy]] = None

    scim_config: Optional[DeviceEnrollmentPermissionsApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: Optional[bool] = None
    """Determines when to skip the App Launcher landing page."""

    updated_at: Optional[datetime] = None

class BrowserIsolationPermissionsApplicationFooterLink(BaseModel):
    name: str
    """The hypertext in the footer link."""

    url: str
    """the hyperlink in the footer link."""

class BrowserIsolationPermissionsApplicationLandingPageDesign(BaseModel):
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

BrowserIsolationPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

    created_at: Optional[datetime] = None

    domain: Optional[str] = None
    """The primary hostname and path that Access will secure.

    If the app is visible in the App Launcher dashboard, this is the domain that
    will be displayed.
    """

    footer_links: Optional[List[BrowserIsolationPermissionsApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[BrowserIsolationPermissionsApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[ApplicationPolicy]] = None

    scim_config: Optional[BrowserIsolationPermissionsApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    session_duration: Optional[str] = None
    """The amount of time that tokens issued for this application will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h.
    """

    skip_app_launcher_login_page: Optional[bool] = None
    """Determines when to skip the App Launcher landing page."""

    updated_at: Optional[datetime] = None

BookmarkApplicationSCIMConfigAuthentication: TypeAlias = Union[SCIMConfigAuthenticationHTTPBasic, SCIMConfigAuthenticationOAuthBearerToken, SCIMConfigAuthenticationOauth2]

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

ApplicationCreateResponse: TypeAlias = Union[SelfHostedApplication, SaaSApplication, BrowserSSHApplication, BrowserVNCApplication, AppLauncherApplication, DeviceEnrollmentPermissionsApplication, BrowserIsolationPermissionsApplication, BookmarkApplication]