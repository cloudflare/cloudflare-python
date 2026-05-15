# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomTrustStore"]


class CustomTrustStore(BaseModel):
    id: str
    """Identifier."""

    certificate: str
    """The root CA certificate in PEM format.

    Only root CA certificates are accepted; intermediate and leaf certificates are
    not supported.
    """

    expires_on: datetime
    """When the certificate expires."""

    issuer: str
    """The certificate authority that issued the certificate."""

    signature: str
    """The type of hash used for the certificate."""

    status: Literal["initializing", "pending_deployment", "active", "pending_deletion", "deleted", "expired"]
    """Status of the zone's custom SSL."""

    updated_at: datetime
    """When the certificate was last modified."""

    uploaded_on: datetime
    """When the certificate was uploaded to Cloudflare."""
