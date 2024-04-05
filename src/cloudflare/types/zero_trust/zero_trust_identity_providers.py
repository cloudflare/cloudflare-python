# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional

from .azure_ad import AzureAd
from ..._models import BaseModel
from .generic_oauth_config import GenericOAuthConfig
from .unnamed_schema_ref_9ab84e842cdf571c8f3898648bcdabcb import UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
from .unnamed_schema_ref_dd86d8b7ea73283da7b160ed3f86cae1 import UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1

__all__ = [
    "ZeroTrustIdentityProviders",
    "AccessCentrify",
    "AccessCentrifyConfig",
    "AccessFacebook",
    "AccessGitHub",
    "AccessGoogle",
    "AccessGoogleConfig",
    "AccessGoogleApps",
    "AccessGoogleAppsConfig",
    "AccessLinkedin",
    "AccessOidc",
    "AccessOidcConfig",
    "AccessOkta",
    "AccessOktaConfig",
    "AccessOnelogin",
    "AccessOneloginConfig",
    "AccessPingone",
    "AccessPingoneConfig",
    "AccessSaml",
    "AccessSamlConfig",
    "AccessSamlConfigHeaderAttribute",
    "AccessYandex",
    "AccessOnetimepin",
]


class AccessCentrifyConfig(BaseModel):
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


class AccessCentrify(BaseModel):
    config: AccessCentrifyConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessFacebook(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGitHub(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleConfig(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class AccessGoogle(BaseModel):
    config: AccessGoogleConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleAppsConfig(BaseModel):
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


class AccessGoogleApps(BaseModel):
    config: AccessGoogleAppsConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessLinkedin(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOidcConfig(BaseModel):
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


class AccessOidc(BaseModel):
    config: AccessOidcConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOktaConfig(BaseModel):
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


class AccessOkta(BaseModel):
    config: AccessOktaConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOneloginConfig(BaseModel):
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


class AccessOnelogin(BaseModel):
    config: AccessOneloginConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessPingoneConfig(BaseModel):
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


class AccessPingone(BaseModel):
    config: AccessPingoneConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessSamlConfigHeaderAttribute(BaseModel):
    attribute_name: Optional[str] = None
    """attribute name from the IDP"""

    header_name: Optional[str] = None
    """header that will be added on the request to the origin"""


class AccessSamlConfig(BaseModel):
    attributes: Optional[List[str]] = None
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: Optional[str] = None
    """The attribute name for email in the SAML response."""

    header_attributes: Optional[List[AccessSamlConfigHeaderAttribute]] = None
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


class AccessSaml(BaseModel):
    config: AccessSamlConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessYandex(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOnetimepin(BaseModel):
    config: object
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: UnnamedSchemaRef9ab84e842cdf571c8f3898648bcdabcb
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[UnnamedSchemaRefDd86d8b7ea73283da7b160ed3f86cae1] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


ZeroTrustIdentityProviders = Union[
    AzureAd,
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
