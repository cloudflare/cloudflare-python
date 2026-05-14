# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .azure_ad import AzureAD
from ..._models import BaseModel
from .generic_oauth_config import GenericOAuthConfig
from .identity_provider_type import IdentityProviderType
from .identity_provider_scim_config import IdentityProviderSCIMConfig

__all__ = [
    "IdentityProvider",
    "AccessCentrify",
    "AccessCentrifyConfig",
    "AccessCentrifySAMLCertificateSet",
    "AccessCentrifySAMLCertificateSetCurrentCertificate",
    "AccessFacebook",
    "AccessFacebookSAMLCertificateSet",
    "AccessFacebookSAMLCertificateSetCurrentCertificate",
    "AccessGitHub",
    "AccessGitHubSAMLCertificateSet",
    "AccessGitHubSAMLCertificateSetCurrentCertificate",
    "AccessGoogle",
    "AccessGoogleConfig",
    "AccessGoogleSAMLCertificateSet",
    "AccessGoogleSAMLCertificateSetCurrentCertificate",
    "AccessGoogleApps",
    "AccessGoogleAppsConfig",
    "AccessGoogleAppsSAMLCertificateSet",
    "AccessGoogleAppsSAMLCertificateSetCurrentCertificate",
    "AccessLinkedin",
    "AccessLinkedinSAMLCertificateSet",
    "AccessLinkedinSAMLCertificateSetCurrentCertificate",
    "AccessOIDC",
    "AccessOIDCConfig",
    "AccessOIDCSAMLCertificateSet",
    "AccessOIDCSAMLCertificateSetCurrentCertificate",
    "AccessOkta",
    "AccessOktaConfig",
    "AccessOktaSAMLCertificateSet",
    "AccessOktaSAMLCertificateSetCurrentCertificate",
    "AccessOnelogin",
    "AccessOneloginConfig",
    "AccessOneloginSAMLCertificateSet",
    "AccessOneloginSAMLCertificateSetCurrentCertificate",
    "AccessPingone",
    "AccessPingoneConfig",
    "AccessPingoneSAMLCertificateSet",
    "AccessPingoneSAMLCertificateSetCurrentCertificate",
    "AccessSAML",
    "AccessSAMLConfig",
    "AccessSAMLConfigHeaderAttribute",
    "AccessSAMLSAMLCertificateSet",
    "AccessSAMLSAMLCertificateSetCurrentCertificate",
    "AccessYandex",
    "AccessYandexSAMLCertificateSet",
    "AccessYandexSAMLCertificateSetCurrentCertificate",
    "AccessOnetimepin",
    "AccessOnetimepinConfig",
    "AccessOnetimepinSAMLCertificateSet",
    "AccessOnetimepinSAMLCertificateSetCurrentCertificate",
]


class AccessCentrifyConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class AccessCentrifySAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessCentrifySAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessCentrifySAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessCentrify(BaseModel):
    config: AccessCentrifyConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessCentrifySAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessFacebookSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessFacebookSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessFacebookSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessFacebook(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessFacebookSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGitHubSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessGitHubSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessGitHubSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessGitHub(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessGitHubSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""


class AccessGoogleSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessGoogleSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessGoogleSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessGoogle(BaseModel):
    config: AccessGoogleConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessGoogleSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessGoogleAppsConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class AccessGoogleAppsSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessGoogleAppsSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessGoogleAppsSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessGoogleApps(BaseModel):
    config: AccessGoogleAppsConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessGoogleAppsSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessLinkedinSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessLinkedinSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessLinkedinSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessLinkedin(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessLinkedinSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOIDCConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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

    pkce_enabled: Optional[bool] = None
    """Enable Proof Key for Code Exchange (PKCE)"""

    scopes: Optional[List[str]] = None
    """OAuth scopes"""

    token_url: Optional[str] = None
    """The token_endpoint URL of your IdP"""


class AccessOIDCSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessOIDCSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessOIDCSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessOIDC(BaseModel):
    config: AccessOIDCConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessOIDCSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOktaConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class AccessOktaSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessOktaSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessOktaSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessOkta(BaseModel):
    config: AccessOktaConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessOktaSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOneloginConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class AccessOneloginSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessOneloginSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessOneloginSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessOnelogin(BaseModel):
    config: AccessOneloginConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessOneloginSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessPingoneConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class AccessPingoneSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessPingoneSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessPingoneSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessPingone(BaseModel):
    config: AccessPingoneConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessPingoneSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessSAMLConfigHeaderAttribute(BaseModel):
    attribute_name: Optional[str] = None
    """attribute name from the IDP"""

    header_name: Optional[str] = None
    """header that will be added on the request to the origin"""


class AccessSAMLConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    attributes: Optional[List[str]] = None
    """
    A list of SAML attribute names that will be added to your signed JWT token and
    can be used in SAML policy rules.
    """

    email_attribute_name: Optional[str] = None
    """The attribute name for email in the SAML response."""

    enable_encryption: Optional[bool] = None
    """Enable SAML assertion encryption.

    When enabled, the Identity Provider will encrypt SAML assertions using the
    certificate from the assigned certificate set.

    To enable encryption:

    1. Create a certificate set via POST to
       `/identity_providers/{id}/saml_certificate`
    2. Set this field to `true` and include `saml_certificate_set_id` in the PUT
       request
    3. Configure the public certificate in your external Identity Provider

    Note: Requires `saml_certificate_set_id` to be set when `true`.
    """

    header_attributes: Optional[List[AccessSAMLConfigHeaderAttribute]] = None
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


class AccessSAMLSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessSAMLSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessSAMLSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessSAML(BaseModel):
    config: AccessSAMLConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessSAMLSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessYandexSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessYandexSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessYandexSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessYandex(BaseModel):
    config: GenericOAuthConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessYandexSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


class AccessOnetimepinConfig(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    redirect_url: Optional[str] = None


class AccessOnetimepinSAMLCertificateSetCurrentCertificate(BaseModel):
    """The currently active certificate used for encrypting SAML assertions"""

    is_current: bool
    """Indicates whether this is the currently active certificate"""

    not_after: datetime
    """Certificate expiration date.

    Certificates are automatically rotated 30 days before expiration.
    """

    public_certificate: str
    """
    PEM-encoded X.509 certificate containing the public key. Configure this
    certificate in your external SAML Identity Provider to enable encryption.
    """

    uid: str
    """Unique identifier for the certificate"""


class AccessOnetimepinSAMLCertificateSet(BaseModel):
    """
    The SAML encryption certificate set details, including current and previous certificates.
    Only present for SAML identity providers with a certificate set assigned.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[AccessOnetimepinSAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AccessOnetimepin(BaseModel):
    config: AccessOnetimepinConfig
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID."""

    saml_certificate_set: Optional[AccessOnetimepinSAMLCertificateSet] = None
    """
    The SAML encryption certificate set details, including current and previous
    certificates. Only present for SAML identity providers with a certificate set
    assigned.
    """

    saml_certificate_set_id: Optional[str] = None
    """
    The UID of the SAML encryption certificate set assigned to this Identity
    Provider. Only present for SAML identity providers with encryption configured.
    Create a certificate set via POST to
    `/identity_providers/{id}/saml_certificate`.
    """

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """


IdentityProvider: TypeAlias = Union[
    AzureAD,
    AccessCentrify,
    AccessFacebook,
    AccessGitHub,
    AccessGoogle,
    AccessGoogleApps,
    AccessLinkedin,
    AccessOIDC,
    AccessOkta,
    AccessOnelogin,
    AccessPingone,
    AccessSAML,
    AccessYandex,
    AccessOnetimepin,
]
