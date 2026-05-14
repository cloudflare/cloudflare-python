# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SAMLCertificateGetResponse", "CurrentCertificate"]


class CurrentCertificate(BaseModel):
    """The current active certificate"""

    is_current: bool
    """Indicates whether the certificate can be used for IdP configuration."""

    not_after: datetime
    """Certificate expiration date"""

    public_certificate: str
    """The public certificate in PEM format"""

    uid: str
    """Unique identifier for the certificate"""


class SAMLCertificateGetResponse(BaseModel):
    created_at: datetime
    """When the certificate set was created"""

    uid: str
    """Unique identifier for the certificate set"""

    updated_at: datetime
    """When the certificate set was last updated"""

    current_certificate: Optional[CurrentCertificate] = None
    """The current active certificate"""

    previous_certificate: Optional[object] = None
    """The previous certificate (maintained during rotation period).

    May be null when no rotation has occurred. Mirrors the structure of
    `saml_certificate`.
    """
