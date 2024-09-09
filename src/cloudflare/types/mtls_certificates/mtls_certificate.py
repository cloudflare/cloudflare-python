# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MTLSCertificate"]


class MTLSCertificate(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    ca: Optional[bool] = None
    """Indicates whether the certificate is a CA or leaf certificate."""

    certificates: Optional[str] = None
    """The uploaded root CA certificate."""

    expires_on: Optional[datetime] = None
    """When the certificate expires."""

    issuer: Optional[str] = None
    """The certificate authority that issued the certificate."""

    name: Optional[str] = None
    """Optional unique name for the certificate. Only used for human readability."""

    serial_number: Optional[str] = None
    """The certificate serial number."""

    signature: Optional[str] = None
    """The type of hash used for the certificate."""

    uploaded_on: Optional[datetime] = None
    """This is the time the certificate was uploaded."""
