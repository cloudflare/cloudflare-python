# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TLSCertificatesAndHostnamesAssociationObject"]


class TLSCertificatesAndHostnamesAssociationObject(BaseModel):
    service: Optional[str] = None
    """The service using the certificate."""

    status: Optional[str] = None
    """Certificate deployment status for the given service."""
