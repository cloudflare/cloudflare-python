# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SAMLCertificateCreateResponse", "CurrentCertificate"]


class CurrentCertificate(BaseModel):
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


class SAMLCertificateCreateResponse(BaseModel):
    """
    A SAML encryption certificate set containing current and optionally previous certificates for encryption key rotation.
    """

    created_at: datetime
    """Timestamp when the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """Timestamp when the certificate set was last updated (e.g., during rotation)"""

    current_certificate: Optional[CurrentCertificate] = None
    """The currently active certificate used for encrypting SAML assertions"""

    previous_certificate: Optional[object] = None
    """The previous certificate, maintained during rotation to ensure continuity.

    Null if no rotation has occurred. Mirrors the structure of `saml_certificate`.
    """
