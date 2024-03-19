# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TLSCertificatesAndHostnamesHostnameAssociation"]


class TLSCertificatesAndHostnamesHostnameAssociation(BaseModel):
    hostnames: Optional[List[str]] = None

    mtls_certificate_id: Optional[str] = None
    """
    The UUID for a certificate that was uploaded to the mTLS Certificate Management
    endpoint. If no mtls_certificate_id is given, the hostnames will be associated
    to your active Cloudflare Managed CA.
    """
