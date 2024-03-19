# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "IdentityProviderListResponse",
    "IdentityProviderListResponseItem",
    "IdentityProviderListResponseItemAccessAzureAd",
    "IdentityProviderListResponseItemAccessAzureAdConfig",
    "IdentityProviderListResponseItemAccessAzureAdScimConfig",
    "IdentityProviderListResponseItemAccessCentrify",
    "IdentityProviderListResponseItemAccessCentrifyConfig",
    "IdentityProviderListResponseItemAccessCentrifyScimConfig",
    "IdentityProviderListResponseItemAccessFacebook",
    "IdentityProviderListResponseItemAccessFacebookConfig",
    "IdentityProviderListResponseItemAccessFacebookScimConfig",
    "IdentityProviderListResponseItemAccessGitHub",
    "IdentityProviderListResponseItemAccessGitHubConfig",
    "IdentityProviderListResponseItemAccessGitHubScimConfig",
    "IdentityProviderListResponseItemAccessGoogle",
    "IdentityProviderListResponseItemAccessGoogleConfig",
    "IdentityProviderListResponseItemAccessGoogleScimConfig",
    "IdentityProviderListResponseItemAccessGoogleApps",
    "IdentityProviderListResponseItemAccessGoogleAppsConfig",
    "IdentityProviderListResponseItemAccessGoogleAppsScimConfig",
    "IdentityProviderListResponseItemAccessLinkedin",
    "IdentityProviderListResponseItemAccessLinkedinConfig",
    "IdentityProviderListResponseItemAccessLinkedinScimConfig",
    "IdentityProviderListResponseItemAccessOidc",
    "IdentityProviderListResponseItemAccessOidcConfig",
    "IdentityProviderListResponseItemAccessOidcScimConfig",
    "IdentityProviderListResponseItemAccessOkta",
    "IdentityProviderListResponseItemAccessOktaConfig",
    "IdentityProviderListResponseItemAccessOktaScimConfig",
    "IdentityProviderListResponseItemAccessOnelogin",
    "IdentityProviderListResponseItemAccessOneloginConfig",
    "IdentityProviderListResponseItemAccessOneloginScimConfig",
    "IdentityProviderListResponseItemAccessPingone",
    "IdentityProviderListResponseItemAccessPingoneConfig",
    "IdentityProviderListResponseItemAccessPingoneScimConfig",
    "IdentityProviderListResponseItemAccessSaml",
    "IdentityProviderListResponseItemAccessSamlConfig",
    "IdentityProviderListResponseItemAccessSamlConfigHeaderAttribute",
    "IdentityProviderListResponseItemAccessSamlScimConfig",
    "IdentityProviderListResponseItemAccessYandex",
    "IdentityProviderListResponseItemAccessYandexConfig",
    "IdentityProviderListResponseItemAccessYandexScimConfig",
]


class IdentityProviderListResponseItemAccessAzureAdConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    conditional_access_enabled: Optional[bool] = None
    """Should Cloudflare try to load authentication contexts from your account"""

    directory_id: Optional[str] = None
    """Your Azure directory uuid"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    prompt: Optional[Literal["login", "select_account", "none"]] = None
    """Indicates the type of user interaction that is required.

    prompt=login forces the user to enter their credentials on that request,
    negating single-sign on. prompt=none is the opposite. It ensures that the user
    isn't presented with any interactive prompt. If the request can't be completed
    silently by using single-sign on, the Microsoft identity platform returns an
    interaction_required error. prompt=select_account interrupts single sign-on
    providing account selection experience listing all the accounts either in
    session or any remembered account or an option to choose to use a different
    account altogether.
    """

    support_groups: Optional[bool] = None
    """Should Cloudflare try to load groups from your account"""


class IdentityProviderListResponseItemAccessAzureAdScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessAzureAd(BaseModel):
    config: IdentityProviderListResponseItemAccessAzureAdConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessAzureAdScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessCentrifyConfig(BaseModel):
    centrify_account: Optional[str] = None
    """Your centrify account url"""

    centrify_app_id: Optional[str] = None
    """Your centrify app id"""

    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class IdentityProviderListResponseItemAccessCentrifyScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessCentrify(BaseModel):
    config: IdentityProviderListResponseItemAccessCentrifyConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessCentrifyScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessFacebookConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderListResponseItemAccessFacebookScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessFacebook(BaseModel):
    config: IdentityProviderListResponseItemAccessFacebookConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessFacebookScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessGitHubConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderListResponseItemAccessGitHubScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessGitHub(BaseModel):
    config: IdentityProviderListResponseItemAccessGitHubConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessGitHubScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessGoogleConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class IdentityProviderListResponseItemAccessGoogleScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessGoogle(BaseModel):
    config: IdentityProviderListResponseItemAccessGoogleConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessGoogleScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessGoogleAppsConfig(BaseModel):
    apps_domain: Optional[str] = None
    """Your companies TLD"""

    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class IdentityProviderListResponseItemAccessGoogleAppsScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessGoogleApps(BaseModel):
    config: IdentityProviderListResponseItemAccessGoogleAppsConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessGoogleAppsScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessLinkedinConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderListResponseItemAccessLinkedinScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessLinkedin(BaseModel):
    config: IdentityProviderListResponseItemAccessLinkedinConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessLinkedinScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessOidcConfig(BaseModel):
    auth_url: Optional[str] = None
    """The authorization_endpoint URL of your IdP"""

    certs_url: Optional[str] = None
    """The jwks_uri endpoint of your IdP to allow the IdP keys to sign the tokens"""

    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    scopes: Optional[List[str]] = None
    """OAuth scopes"""

    token_url: Optional[str] = None
    """The token_endpoint URL of your IdP"""


class IdentityProviderListResponseItemAccessOidcScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessOidc(BaseModel):
    config: IdentityProviderListResponseItemAccessOidcConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessOidcScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessOktaConfig(BaseModel):
    authorization_server_id: Optional[str] = None
    """Your okta authorization server id"""

    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    okta_account: Optional[str] = None
    """Your okta account url"""


class IdentityProviderListResponseItemAccessOktaScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessOkta(BaseModel):
    config: IdentityProviderListResponseItemAccessOktaConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessOktaScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessOneloginConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    onelogin_account: Optional[str] = None
    """Your OneLogin account url"""


class IdentityProviderListResponseItemAccessOneloginScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessOnelogin(BaseModel):
    config: IdentityProviderListResponseItemAccessOneloginConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessOneloginScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessPingoneConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    ping_env_id: Optional[str] = None
    """Your PingOne environment identifier"""


class IdentityProviderListResponseItemAccessPingoneScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessPingone(BaseModel):
    config: IdentityProviderListResponseItemAccessPingoneConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessPingoneScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessSamlConfigHeaderAttribute(BaseModel):
    attribute_name: Optional[str] = None
    """attribute name from the IDP"""

    header_name: Optional[str] = None
    """header that will be added on the request to the origin"""


class IdentityProviderListResponseItemAccessSamlConfig(BaseModel):
    attributes: Optional[List[str]] = None
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: Optional[str] = None
    """The attribute name for email in the SAML response."""

    header_attributes: Optional[List[IdentityProviderListResponseItemAccessSamlConfigHeaderAttribute]] = None
    """
    Add a list of attribute names that will be returned in the response header from
    the Access callback.
    """

    idp_public_certs: Optional[List[str]] = None
    """X509 certificate to verify the signature in the SAML authentication response"""

    issuer_url: Optional[str] = None
    """IdP Entity ID or Issuer URL"""

    sign_request: Optional[bool] = None
    """Sign the SAML authentication request with Access credentials.

    To verify the signature, use the public key from the Access certs endpoints.
    """

    sso_target_url: Optional[str] = None
    """URL to send the SAML authentication requests to"""


class IdentityProviderListResponseItemAccessSamlScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessSaml(BaseModel):
    config: IdentityProviderListResponseItemAccessSamlConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessSamlScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderListResponseItemAccessYandexConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderListResponseItemAccessYandexScimConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class IdentityProviderListResponseItemAccessYandex(BaseModel):
    config: IdentityProviderListResponseItemAccessYandexConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: Literal[
        "onetimepin",
        "azureAD",
        "saml",
        "centrify",
        "facebook",
        "github",
        "google-apps",
        "google",
        "linkedin",
        "oidc",
        "okta",
        "onelogin",
        "pingone",
        "yandex",
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderListResponseItemAccessYandexScimConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


IdentityProviderListResponseItem = Union[
    IdentityProviderListResponseItemAccessAzureAd,
    IdentityProviderListResponseItemAccessCentrify,
    IdentityProviderListResponseItemAccessFacebook,
    IdentityProviderListResponseItemAccessGitHub,
    IdentityProviderListResponseItemAccessGoogle,
    IdentityProviderListResponseItemAccessGoogleApps,
    IdentityProviderListResponseItemAccessLinkedin,
    IdentityProviderListResponseItemAccessOidc,
    IdentityProviderListResponseItemAccessOkta,
    IdentityProviderListResponseItemAccessOnelogin,
    IdentityProviderListResponseItemAccessPingone,
    IdentityProviderListResponseItemAccessSaml,
    IdentityProviderListResponseItemAccessYandex,
]

IdentityProviderListResponse = List[IdentityProviderListResponseItem]
