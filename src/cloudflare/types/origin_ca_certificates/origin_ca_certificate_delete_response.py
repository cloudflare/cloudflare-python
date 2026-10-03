# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["OriginCACertificateDeleteResponse"]


class OriginCACertificateDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The x509 serial number of the Origin CA certificate."""

    revoked_at: Optional[datetime] = None
    """When the certificate was revoked."""
