# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Literal

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["CertificateOriginCaCreateCertificateParams"]


class CertificateOriginCaCreateCertificateParams(TypedDict, total=False):
    csr: str
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: Iterable[object]
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
