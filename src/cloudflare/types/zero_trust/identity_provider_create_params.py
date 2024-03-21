# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "IdentityProviderCreateParams",
    "AccessAzureAd",
    "AccessAzureAdConfig",
    "AccessAzureAdScimConfig",
    "AccessCentrify",
    "AccessCentrifyConfig",
    "AccessCentrifyScimConfig",
    "AccessFacebook",
    "AccessFacebookConfig",
    "AccessFacebookScimConfig",
    "AccessGitHub",
    "AccessGitHubConfig",
    "AccessGitHubScimConfig",
    "AccessGoogle",
    "AccessGoogleConfig",
    "AccessGoogleScimConfig",
    "AccessGoogleApps",
    "AccessGoogleAppsConfig",
    "AccessGoogleAppsScimConfig",
    "AccessLinkedin",
    "AccessLinkedinConfig",
    "AccessLinkedinScimConfig",
    "AccessOidc",
    "AccessOidcConfig",
    "AccessOidcScimConfig",
    "AccessOkta",
    "AccessOktaConfig",
    "AccessOktaScimConfig",
    "AccessOnelogin",
    "AccessOneloginConfig",
    "AccessOneloginScimConfig",
    "AccessPingone",
    "AccessPingoneConfig",
    "AccessPingoneScimConfig",
    "AccessSaml",
    "AccessSamlConfig",
    "AccessSamlConfigHeaderAttribute",
    "AccessSamlScimConfig",
    "AccessYandex",
    "AccessYandexConfig",
    "AccessYandexScimConfig",
    "AccessOnetimepin",
    "AccessOnetimepinScimConfig",
]


class AccessAzureAd(TypedDict, total=False):
    config: Required[AccessAzureAdConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessAzureAdScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessAzureAdConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    conditional_access_enabled: bool
    """Should Cloudflare try to load authentication contexts from your account"""

    directory_id: str
    """Your Azure directory uuid"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    prompt: Literal["login", "select_account", "none"]
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

    support_groups: bool
    """Should Cloudflare try to load groups from your account"""


class AccessAzureAdScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessCentrify(TypedDict, total=False):
    config: Required[AccessCentrifyConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessCentrifyScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessCentrifyConfig(TypedDict, total=False):
    centrify_account: str
    """Your centrify account url"""

    centrify_app_id: str
    """Your centrify app id"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessCentrifyScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessFacebook(TypedDict, total=False):
    config: Required[AccessFacebookConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessFacebookScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessFacebookConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessFacebookScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessGitHub(TypedDict, total=False):
    config: Required[AccessGitHubConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessGitHubScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGitHubConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessGitHubScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessGoogle(TypedDict, total=False):
    config: Required[AccessGoogleConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessGoogleScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessGoogleScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessGoogleApps(TypedDict, total=False):
    config: Required[AccessGoogleAppsConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessGoogleAppsScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleAppsConfig(TypedDict, total=False):
    apps_domain: str
    """Your companies TLD"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""


class AccessGoogleAppsScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessLinkedin(TypedDict, total=False):
    config: Required[AccessLinkedinConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessLinkedinScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessLinkedinConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessLinkedinScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessOidc(TypedDict, total=False):
    config: Required[AccessOidcConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessOidcScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOidcConfig(TypedDict, total=False):
    auth_url: str
    """The authorization_endpoint URL of your IdP"""

    certs_url: str
    """The jwks_uri endpoint of your IdP to allow the IdP keys to sign the tokens"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    scopes: List[str]
    """OAuth scopes"""

    token_url: str
    """The token_endpoint URL of your IdP"""


class AccessOidcScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessOkta(TypedDict, total=False):
    config: Required[AccessOktaConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessOktaScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOktaConfig(TypedDict, total=False):
    authorization_server_id: str
    """Your okta authorization server id"""

    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    okta_account: str
    """Your okta account url"""


class AccessOktaScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessOnelogin(TypedDict, total=False):
    config: Required[AccessOneloginConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessOneloginScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOneloginConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    onelogin_account: str
    """Your OneLogin account url"""


class AccessOneloginScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessPingone(TypedDict, total=False):
    config: Required[AccessPingoneConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessPingoneScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessPingoneConfig(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    ping_env_id: str
    """Your PingOne environment identifier"""


class AccessPingoneScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessSaml(TypedDict, total=False):
    config: Required[AccessSamlConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessSamlScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessSamlConfigHeaderAttribute(TypedDict, total=False):
    attribute_name: str
    """attribute name from the IDP"""

    header_name: str
    """header that will be added on the request to the origin"""


class AccessSamlConfig(TypedDict, total=False):
    attributes: List[str]
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: str
    """The attribute name for email in the SAML response."""

    header_attributes: Iterable[AccessSamlConfigHeaderAttribute]
    """
    Add a list of attribute names that will be returned in the response header from
    the Access callback.
    """

    idp_public_certs: List[str]
    """X509 certificate to verify the signature in the SAML authentication response"""

    issuer_url: str
    """IdP Entity ID or Issuer URL"""

    sign_request: bool
    """Sign the SAML authentication request with Access credentials.

    To verify the signature, use the public key from the Access certs endpoints.
    """

    sso_target_url: str
    """URL to send the SAML authentication requests to"""


class AccessSamlScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessYandex(TypedDict, total=False):
    config: Required[AccessYandexConfig]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessYandexScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessYandexConfig(TypedDict, total=False):
    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""


class AccessYandexScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


class AccessOnetimepin(TypedDict, total=False):
    config: Required[object]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[
        Literal[
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
    ]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_config: AccessOnetimepinScimConfig
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOnetimepinScimConfig(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """


IdentityProviderCreateParams = Union[
    AccessAzureAd,
    AccessCentrify,
    AccessFacebook,
    AccessGitHub,
    AccessGoogle,
    AccessGoogleApps,
    AccessLinkedin,
    AccessOidc,
    AccessOkta,
    AccessOnelogin,
    AccessPingone,
    AccessSaml,
    AccessYandex,
    AccessOnetimepin,
]
