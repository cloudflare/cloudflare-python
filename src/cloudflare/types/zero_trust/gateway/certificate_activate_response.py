# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CertificateActivateResponse"]


class CertificateActivateResponse(BaseModel):
    id: Optional[str] = None
    """Identify the certificate with a UUID."""

    binding_status: Optional[Literal["pending_deployment", "available", "pending_deletion", "inactive"]] = None
    """Indicate the read-only deployment status of the certificate on Cloudflare's
    edge.

    Gateway TLS interception can use certificates in the 'available' (previously
    called 'active') state.
    """

    certificate: Optional[str] = None
    """Provide the CA certificate (read-only)."""

    created_at: Optional[datetime] = None

    expires_on: Optional[datetime] = None

    fingerprint: Optional[str] = None
    """Provide the SHA256 fingerprint of the certificate (read-only)."""

    in_use: Optional[bool] = None
    """Indicate whether Gateway TLS interception uses this certificate (read-only).

    You cannot set this value directly. To configure interception, use the Gateway
    configuration setting named `certificate` (read-only).
    """

    issuer_org: Optional[str] = None
    """Indicate the organization that issued the certificate (read-only)."""

    issuer_raw: Optional[str] = None
    """Provide the entire issuer field of the certificate (read-only)."""

    type: Optional[Literal["custom", "gateway_managed"]] = None
    """Indicate the read-only certificate type, BYO-PKI (custom) or Gateway-managed."""

    updated_at: Optional[datetime] = None

    uploaded_on: Optional[datetime] = None
