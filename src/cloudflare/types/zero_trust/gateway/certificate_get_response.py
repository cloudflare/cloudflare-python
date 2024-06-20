# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CertificateGetResponse"]


class CertificateGetResponse(BaseModel):
    id: Optional[str] = None
    """Certificate UUID tag."""

    binding_status: Optional[Literal["pending_deployment", "active", "pending_deletion", "inactive"]] = None
    """The deployment status of the certificate on Cloudflare's edge."""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Use this certificate for Gateway TLS interception"""

    expires_on: Optional[datetime] = None

    type: Optional[Literal["custom", "gateway_managed"]] = None
    """The type of certificate, either BYO-PKI (custom) or Gateway-managed."""

    updated_at: Optional[datetime] = None

    uploaded_on: Optional[datetime] = None
