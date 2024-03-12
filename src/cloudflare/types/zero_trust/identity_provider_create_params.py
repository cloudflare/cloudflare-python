# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IdentityProviderCreateParams", "Config", "ConfigHeaderAttribute", "ScimConfig"]


class IdentityProviderCreateParams(TypedDict, total=False):
    config: Required[Config]

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

    scim_config: ScimConfig


class ConfigHeaderAttribute(TypedDict, total=False):
    attribute_name: str
    """attribute name from the IDP"""

    header_name: str
    """header that will be added on the request to the origin"""


class Config(TypedDict, total=False):
    apps_domain: str
    """Your companies TLD"""

    attributes: List[str]
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    auth_url: str
    """The authorization_endpoint URL of your IdP"""

    authorization_server_id: str
    """Your okta authorization server id"""

    centrify_account: str
    """Your centrify account url"""

    centrify_app_id: str
    """Your centrify app id"""

    certs_url: str
    """The jwks_uri endpoint of your IdP to allow the IdP keys to sign the tokens"""

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

    email_attribute_name: str
    """The attribute name for email in the SAML response."""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    header_attributes: Iterable[ConfigHeaderAttribute]
    """
    Add a list of attribute names that will be returned in the response header from
    the Access callback.
    """

    idp_public_certs: List[str]
    """X509 certificate to verify the signature in the SAML authentication response"""

    issuer_url: str
    """IdP Entity ID or Issuer URL"""

    okta_account: str
    """Your okta account url"""

    onelogin_account: str
    """Your OneLogin account url"""

    ping_env_id: str
    """Your PingOne environment identifier"""

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

    scopes: List[str]
    """OAuth scopes"""

    sign_request: bool
    """Sign the SAML authentication request with Access credentials.

    To verify the signature, use the public key from the Access certs endpoints.
    """

    sso_target_url: str
    """URL to send the SAML authentication requests to"""

    support_groups: bool
    """Should Cloudflare try to load groups from your account"""

    token_url: str
    """The token_endpoint URL of your IdP"""


class ScimConfig(TypedDict, total=False):
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
