# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CertificateAsssociation"]


class CertificateAsssociation(BaseModel):
    service: Optional[str] = None
    """The service using the certificate."""

    status: Optional[str] = None
    """Certificate deployment status for the given service."""
