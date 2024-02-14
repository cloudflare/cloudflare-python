# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItem",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAd",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrify",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebook",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHub",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogle",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleApps",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedin",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidc",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOkta",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOnelogin",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingone",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSaml",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfigHeaderAttribute",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlScimConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandex",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexConfig",
    "IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexScimConfig",
]


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdConfig(BaseModel):
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

    support_groups: Optional[bool] = None
    """Should Cloudflare try to load groups from your account"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAd(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAdScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrify(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrifyScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebook(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebookScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHub(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHubScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogle(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsScimConfig(
    BaseModel
):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleApps(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleAppsScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedin(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedinScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidc(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidcScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOkta(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOktaScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOnelogin(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOneloginScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingone(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingoneScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfigHeaderAttribute(
    BaseModel
):
    attribute_name: Optional[str] = None
    """attribute name from the IDP"""

    header_name: Optional[str] = None
    """header that will be added on the request to the origin"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfig(BaseModel):
    attributes: Optional[List[str]] = None
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: Optional[str] = None
    """The attribute name for email in the SAML response."""

    header_attributes: Optional[
        List[
            IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfigHeaderAttribute
        ]
    ] = None
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSaml(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSamlScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexConfig(BaseModel):
    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexScimConfig(BaseModel):
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


class IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandex(BaseModel):
    config: IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexConfig
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

    scim_config: Optional[
        IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandexScimConfig
    ] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItem = Union[
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessAzureAd,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessCentrify,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessFacebook,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGitHub,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogle,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessGoogleApps,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessLinkedin,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOidc,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOkta,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessOnelogin,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessPingone,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessSaml,
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItemAccessYandex,
]

IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponse = List[
    IdentityProviderAccessIdentityProvidersListAccessIdentityProvidersResponseItem
]
