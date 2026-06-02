# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .identity_provider_type import IdentityProviderType
from .identity_provider_scim_config import IdentityProviderSCIMConfig

__all__ = ["AzureAD", "Config", "SAMLCertificateSet", "SAMLCertificateSetCurrentCertificate"]


class Config(BaseModel):
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

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


class SAMLCertificateSetCurrentCertificate(BaseModel):
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


class SAMLCertificateSet(BaseModel):
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

    current_certificate: Optional[SAMLCertificateSetCurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """


class AzureAD(BaseModel):
    config: Config
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

    read_only: Optional[bool] = None
    """
    Indicates that the identity provider is immutable and cannot be updated or
    deleted via the API.
    """

    saml_certificate_set: Optional[SAMLCertificateSet] = None
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
