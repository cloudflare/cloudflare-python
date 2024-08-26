# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from typing import List

from ..shared.certificate_request_type import CertificateRequestType

from ..ssl.request_validity import RequestValidity

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["OriginCACertificateCreateParams"]

class OriginCACertificateCreateParams(TypedDict, total=False):
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