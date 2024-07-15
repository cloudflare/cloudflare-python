# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PrioritizeUpdateParams", "Certificate"]


class PrioritizeUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    certificates: Required[Iterable[Certificate]]
    """Array of ordered certificates."""


class Certificate(TypedDict, total=False):
    id: str
    """Identifier"""

    priority: float
    """The order/priority in which the certificate will be used in a request.

    The higher priority will break ties across overlapping 'legacy_custom'
    certificates, but 'legacy_custom' certificates will always supercede
    'sni_custom' certificates.
    """
