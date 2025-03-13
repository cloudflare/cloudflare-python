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
from .application_type import ApplicationType
from .application_policy import ApplicationPolicy
from .scim_config_mapping import SCIMConfigMapping
from .self_hosted_domains import SelfHostedDomains
from .applications.access_rule import AccessRule
from .scim_config_authentication_oauth2 import SCIMConfigAuthenticationOauth2
from .scim_config_authentication_http_basic import SCIMConfigAuthenticationHTTPBasic
from .scim_config_authentication_oauth_bearer_token import SCIMConfigAuthenticationOAuthBearerToken

__all__ = [
    "ApplicationUpdateResponse",
    "SelfHostedApplication",
    "SelfHostedApplicationDestination",
    "SelfHostedApplicationDestinationPublicDestination",
    "SelfHostedApplicationDestinationPrivateDestination",
    "SelfHostedApplicationPolicy",
    "SelfHostedApplicationSCIMConfig",
    "SelfHostedApplicationSCIMConfigAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "SaaSApplication",
    "SaaSApplicationPolicy",
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
    "BrowserVNCApplicationSCIMConfig",
    "BrowserVNCApplicationSCIMConfigAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "AppLauncherApplication",
    "AppLauncherApplicationFooterLink",
    "AppLauncherApplicationLandingPageDesign",
    "AppLauncherApplicationPolicy",
    "AppLauncherApplicationSCIMConfig",
    "AppLauncherApplicationSCIMConfigAuthentication",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "DeviceEnrollmentPermissionsApplication",
    "DeviceEnrollmentPermissionsApplicationFooterLink",
    "DeviceEnrollmentPermissionsApplicationLandingPageDesign",
    "DeviceEnrollmentPermissionsApplicationPolicy",
    "DeviceEnrollmentPermissionsApplicationSCIMConfig",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserIsolationPermissionsApplication",
    "BrowserIsolationPermissionsApplicationFooterLink",
    "BrowserIsolationPermissionsApplicationLandingPageDesign",
    "BrowserIsolationPermissionsApplicationPolicy",
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
    "InfrastructureApplicationSCIMConfig",
    "InfrastructureApplicationSCIMConfigAuthentication",
    "InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserRdpApplication",
    "BrowserRdpApplicationTargetCriterion",
    "BrowserRdpApplicationDestination",
    "BrowserRdpApplicationDestinationPublicDestination",
    "BrowserRdpApplicationDestinationPrivateDestination",
    "BrowserRdpApplicationPolicy",
    "BrowserRdpApplicationSCIMConfig",
    "BrowserRdpApplicationSCIMConfigAuthentication",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication",
    "BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken",
]


class SelfHostedApplicationDestinationPublicDestination(BaseModel):
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


SelfHostedApplicationDestination: TypeAlias = Union[
    SelfHostedApplicationDestinationPublicDestination, SelfHostedApplicationDestinationPrivateDestination
]


class SelfHostedApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class SelfHostedApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


class SaaSApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


SaaSApplicationSaaSApp: TypeAlias = Union[SAMLSaaSApp, OIDCSaaSApp]


class SaaSApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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


class BrowserSSHApplicationDestinationPublicDestination(BaseModel):
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


BrowserSSHApplicationDestination: TypeAlias = Union[
    BrowserSSHApplicationDestinationPublicDestination, BrowserSSHApplicationDestinationPrivateDestination
]


class BrowserSSHApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserSSHApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


class BrowserVNCApplicationDestinationPublicDestination(BaseModel):
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


BrowserVNCApplicationDestination: TypeAlias = Union[
    BrowserVNCApplicationDestinationPublicDestination, BrowserVNCApplicationDestinationPrivateDestination
]


class BrowserVNCApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserVNCApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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

    policies: Optional[List[BrowserVNCApplicationPolicy]] = None

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


class AppLauncherApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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


class AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

AppLauncherApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[AppLauncherApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
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


class DeviceEnrollmentPermissionsApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


class DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

DeviceEnrollmentPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[DeviceEnrollmentPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
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
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    footer_links: Optional[List[DeviceEnrollmentPermissionsApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[DeviceEnrollmentPermissionsApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

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


class BrowserIsolationPermissionsApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


class BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserIsolationPermissionsApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BrowserIsolationPermissionsApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
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
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    footer_links: Optional[List[BrowserIsolationPermissionsApplicationFooterLink]] = None
    """The links in the App Launcher footer."""

    header_bg_color: Optional[str] = None
    """The background color of the App Launcher header."""

    landing_page_design: Optional[BrowserIsolationPermissionsApplicationLandingPageDesign] = None
    """The design of the App Launcher landing page shown to users when they log in."""

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

    skip_app_launcher_login_page: Optional[bool] = None
    """Determines when to skip the App Launcher landing page."""

    updated_at: Optional[datetime] = None


class BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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


class BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BookmarkApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BookmarkApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
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


class InfrastructureApplicationTargetCriterion(BaseModel):
    port: int
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Literal["ssh"]
    """The communication protocol your application secures."""

    target_attributes: Dict[str, List[str]]
    """Contains a map of target attribute keys to target attribute values."""


class InfrastructureApplicationPolicyConnectionRulesSSH(BaseModel):
    usernames: List[str]
    """Contains the Unix usernames that may be used when connecting over SSH."""

    allow_email_alias: Optional[bool] = None
    """Enables using Identity Provider email alias as SSH username."""


class InfrastructureApplicationPolicyConnectionRules(BaseModel):
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


class InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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


class InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

InfrastructureApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[InfrastructureApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class InfrastructureApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[InfrastructureApplicationSCIMConfigAuthentication] = None
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


class InfrastructureApplication(BaseModel):
    target_criteria: List[InfrastructureApplicationTargetCriterion]

    type: ApplicationType
    """The application type."""

    id: Optional[str] = None
    """UUID"""

    aud: Optional[str] = None
    """Audience tag."""

    created_at: Optional[datetime] = None

    name: Optional[str] = None
    """The name of the application."""

    policies: Optional[List[InfrastructureApplicationPolicy]] = None

    scim_config: Optional[InfrastructureApplicationSCIMConfig] = None
    """Configuration for provisioning to this application via SCIM.

    This is currently in closed beta.
    """

    updated_at: Optional[datetime] = None


class BrowserRdpApplicationTargetCriterion(BaseModel):
    port: int
    """The port that the targets use for the chosen communication protocol.

    A port cannot be assigned to multiple protocols.
    """

    protocol: Literal["ssh"]
    """The communication protocol your application secures."""

    target_attributes: Dict[str, List[str]]
    """Contains a map of target attribute keys to target attribute values."""


class BrowserRdpApplicationDestinationPublicDestination(BaseModel):
    type: Optional[Literal["public"]] = None

    uri: Optional[str] = None
    """The URI of the destination.

    Public destinations' URIs can include a domain and path with
    [wildcards](https://developers.cloudflare.com/cloudflare-one/policies/access/app-paths/).
    """


class BrowserRdpApplicationDestinationPrivateDestination(BaseModel):
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


BrowserRdpApplicationDestination: TypeAlias = Union[
    BrowserRdpApplicationDestinationPublicDestination, BrowserRdpApplicationDestinationPrivateDestination
]


class BrowserRdpApplicationPolicy(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """


class BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(BaseModel):
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


class BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken(
    BaseModel
):
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


BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
]

BrowserRdpApplicationSCIMConfigAuthentication: TypeAlias = Union[
    SCIMConfigAuthenticationHTTPBasic,
    SCIMConfigAuthenticationOAuthBearerToken,
    SCIMConfigAuthenticationOauth2,
    BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigAuthenticationAccessServiceToken,
    List[BrowserRdpApplicationSCIMConfigAuthenticationAccessSCIMConfigMultiAuthentication],
]


class BrowserRdpApplicationSCIMConfig(BaseModel):
    idp_uid: str
    """
    The UID of the IdP to use as the source for SCIM resources to provision to this
    application.
    """

    remote_uri: str
    """The base URI for the application's SCIM-compatible API."""

    authentication: Optional[BrowserRdpApplicationSCIMConfigAuthentication] = None
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


class BrowserRdpApplication(BaseModel):
    domain: str
    """The primary hostname and path secured by Access.

    This domain will be displayed if the app is visible in the App Launcher.
    """

    target_criteria: List[BrowserRdpApplicationTargetCriterion]

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

    destinations: Optional[List[BrowserRdpApplicationDestination]] = None
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

    policies: Optional[List[BrowserRdpApplicationPolicy]] = None

    same_site_cookie_attribute: Optional[str] = None
    """
    Sets the SameSite cookie setting, which provides increased security against CSRF
    attacks.
    """

    scim_config: Optional[BrowserRdpApplicationSCIMConfig] = None
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
    ms, s, m, h.
    """

    skip_interstitial: Optional[bool] = None
    """Enables automatic authentication through cloudflared."""

    tags: Optional[List[str]] = None
    """The tags you want assigned to an application.

    Tags are used to filter applications in the App Launcher dashboard.
    """

    updated_at: Optional[datetime] = None


ApplicationUpdateResponse: TypeAlias = Union[
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
