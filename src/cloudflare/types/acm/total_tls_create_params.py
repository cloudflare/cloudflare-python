# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .certificate_authority import CertificateAuthority

__all__ = ["TotalTLSCreateParams"]


class TotalTLSCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    enabled: Required[bool]
    """
    If enabled, Total TLS will order a hostname specific TLS certificate for any
    proxied A, AAAA, or CNAME record in your zone.
    """

    certificate_authority: CertificateAuthority
    """The Certificate Authority that Total TLS certificates will be issued through."""
