# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CustomCertificateSettings"]


class CustomCertificateSettings(BaseModel):
    """Specify custom certificate settings for BYO-PKI.

    This field is deprecated; use `certificate` instead.
    """

    enabled: Optional[bool] = None
    """
    Specify whether to enable a custom certificate authority for signing Gateway
    traffic.
    """

    id: Optional[str] = None
    """Specify the UUID of the certificate (ID from MTLS certificate store)."""

    binding_status: Optional[str] = None
    """Indicate the internal certificate status."""

    updated_at: Optional[datetime] = None
