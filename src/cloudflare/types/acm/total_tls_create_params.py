# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from .certificate_authority import CertificateAuthority

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

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