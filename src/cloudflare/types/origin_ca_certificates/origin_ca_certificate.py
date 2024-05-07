# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..ssl.certificate_pack_request_type import CertificatePackRequestType
from ..ssl.certificate_pack_request_validity import CertificatePackRequestValidity

__all__ = ["OriginCACertificate"]


class OriginCACertificate(BaseModel):
    csr: str
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: List[object]
    """
    Array of hostnames or wildcard names (e.g., \\**.example.com) bound to the
    certificate.
    """

    request_type: CertificatePackRequestType
    """
    Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
    or "keyless-certificate" (for Keyless SSL servers).
    """

    requested_validity: CertificatePackRequestValidity
    """The number of days for which the certificate should be valid."""

    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The Origin CA certificate. Will be newline-encoded."""

    expires_on: Optional[datetime] = None
    """When the certificate will expire."""
