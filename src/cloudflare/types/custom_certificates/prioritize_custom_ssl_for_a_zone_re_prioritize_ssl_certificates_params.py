# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesParams", "Certificate"]


class PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesParams(TypedDict, total=False):
    certificates: Required[Iterable[Certificate]]
    """Array of ordered certificates."""


class Certificate(TypedDict, total=False):
    priority: float
    """The order/priority in which the certificate will be used in a request.

    The higher priority will break ties across overlapping 'legacy_custom'
    certificates, but 'legacy_custom' certificates will always supercede
    'sni_custom' certificates.
    """
