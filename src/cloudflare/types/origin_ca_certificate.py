# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["OriginCACertificate"]


class OriginCACertificate(BaseModel):
    csr: str
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: List[object]
    """
    Array of hostnames or wildcard names (e.g., \\**.example.com) bound to the
    certificate.
    """

    request_type: Literal["origin-rsa", "origin-ecc", "keyless-certificate"]
    """
    Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
    or "keyless-certificate" (for Keyless SSL servers).
    """

    requested_validity: Literal[7, 30, 90, 365, 730, 1095, 5475]
    """The number of days for which the certificate should be valid."""

    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The Origin CA certificate. Will be newline-encoded."""

    expires_on: Optional[datetime] = None
    """When the certificate will expire."""
