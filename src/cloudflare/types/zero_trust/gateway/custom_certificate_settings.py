# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CustomCertificateSettings"]


class CustomCertificateSettings(BaseModel):
    enabled: bool
    """Enable use of custom certificate authority for signing Gateway traffic."""

    id: Optional[str] = None
    """UUID of certificate (ID from MTLS certificate store)."""

    binding_status: Optional[str] = None
    """Certificate status (internal)."""

    updated_at: Optional[datetime] = None
