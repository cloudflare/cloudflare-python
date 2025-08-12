# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CertificateCreateResponse"]


class CertificateCreateResponse(BaseModel):
    id: Optional[str] = None
    """Certificate UUID tag."""

    binding_status: Optional[Literal["pending_deployment", "available", "pending_deletion", "inactive"]] = None
    """The read only deployment status of the certificate on Cloudflare's edge.

    Certificates in the 'available' (previously called 'active') state may be used
    for Gateway TLS interception.
    """

    certificate: Optional[str] = None
    """The CA certificate(read only)."""

    created_at: Optional[datetime] = None

    expires_on: Optional[datetime] = None

    fingerprint: Optional[str] = None
    """The SHA256 fingerprint of the certificate(read only)."""

    in_use: Optional[bool] = None
    """
    Read-only field that shows whether Gateway TLS interception is using this
    certificate. This value cannot be set directly. To configure the certificate for
    interception, use the Gateway configuration setting named certificate.
    """

    issuer_org: Optional[str] = None
    """The organization that issued the certificate(read only)."""

    issuer_raw: Optional[str] = None
    """The entire issuer field of the certificate(read only)."""

    type: Optional[Literal["custom", "gateway_managed"]] = None
    """The type of certificate, either BYO-PKI (custom) or Gateway-managed(read only)."""

    updated_at: Optional[datetime] = None

    uploaded_on: Optional[datetime] = None
