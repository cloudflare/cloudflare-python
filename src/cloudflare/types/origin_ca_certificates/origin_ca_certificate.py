# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..ssl.request_validity import RequestValidity
from ..shared.certificate_request_type import CertificateRequestType

__all__ = ["OriginCACertificate"]


class OriginCACertificate(BaseModel):
    csr: str
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: List[str]
    """
    Array of hostnames or wildcard names (e.g., \\**.example.com) bound to the
    certificate.
    """

    request_type: CertificateRequestType
    """
    Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
    or "keyless-certificate" (for Keyless SSL servers).
    """

    requested_validity: RequestValidity
    """The number of days for which the certificate should be valid."""

    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The Origin CA certificate. Will be newline-encoded."""

    expires_on: Optional[str] = None
    """When the certificate will expire."""
