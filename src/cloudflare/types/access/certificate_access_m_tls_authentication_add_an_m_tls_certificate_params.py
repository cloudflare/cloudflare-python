# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams"]


class CertificateAccessMTLSAuthenticationAddAnMTLSCertificateParams(TypedDict, total=False):
    account_or_zone: Required[str]

    certificate: Required[str]
    """The certificate content."""

    name: Required[str]
    """The name of the certificate."""

    associated_hostnames: List[str]
    """The hostnames of the applications that will use this certificate."""
