# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from ..ssl.certificate_pack_request_type import CertificatePackRequestType
from ..ssl.certificate_pack_request_validity import CertificatePackRequestValidity

__all__ = ["OriginCACertificateCreateParams"]


class OriginCACertificateCreateParams(TypedDict, total=False):
    csr: str
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: Iterable[object]
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
