# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .hostname_association import HostnameAssociation

__all__ = ["HostnameAssociationUpdateParams"]


class HostnameAssociationUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hostnames: List[HostnameAssociation]

    mtls_certificate_id: str
    """
    The UUID for a certificate that was uploaded to the mTLS Certificate Management
    endpoint. If no mtls_certificate_id is given, the hostnames will be associated
    to your active Cloudflare Managed CA.
    """
