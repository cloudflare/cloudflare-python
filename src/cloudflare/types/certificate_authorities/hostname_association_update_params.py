# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["HostnameAssociationUpdateParams"]


class HostnameAssociationUpdateParams(TypedDict, total=False):
    hostnames: List[str]

    mtls_certificate_id: str
    """
    The UUID for a certificate that was uploaded to the mTLS Certificate Management
    endpoint. If no mtls_certificate_id is given, the hostnames will be associated
    to your active Cloudflare Managed CA.
    """
