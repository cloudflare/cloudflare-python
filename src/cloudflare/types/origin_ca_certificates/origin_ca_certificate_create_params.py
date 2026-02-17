# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from ..ssl.request_validity import RequestValidity
from ..shared.certificate_request_type import CertificateRequestType

__all__ = ["OriginCACertificateCreateParams"]


class OriginCACertificateCreateParams(TypedDict, total=False):
    csr: Required[str]
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    hostnames: Required[SequenceNotStr[str]]
    """
    Array of hostnames or wildcard names bound to the certificate. Hostnames must be
    fully qualified domain names (FQDNs) belonging to zones on your account (e.g.,
    `example.com` or `sub.example.com`). Wildcards are supported only as a `*.`
    prefix for a single level (e.g., `*.example.com`). Double wildcards
    (`*.*.example.com`) and interior wildcards (`foo.*.example.com`) are not
    allowed. The wildcard suffix must be a multi-label domain (`*.example.com` is
    valid, but `*.com` is not). Unicode/IDN hostnames are accepted and automatically
    converted to punycode.
    """

    request_type: Required[CertificateRequestType]
    """
    Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa),
    or "keyless-certificate" (for Keyless SSL servers).
    """

    requested_validity: RequestValidity
    """The number of days for which the certificate should be valid."""
