# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse"]


class HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse(BaseModel):
    hostnames: Optional[List[str]] = None

    mtls_certificate_id: Optional[str] = None
    """
    The UUID for a certificate that was uploaded to the mTLS Certificate Management
    endpoint. If no mtls_certificate_id is given, the hostnames will be associated
    to your active Cloudflare Managed CA.
    """
