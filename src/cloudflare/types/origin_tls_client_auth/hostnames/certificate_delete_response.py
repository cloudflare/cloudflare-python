# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["CertificateDeleteResponse"]


class CertificateDeleteResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The hostname certificate."""

    expires_on: Optional[datetime] = None
    """The date when the certificate expires."""

    issuer: Optional[str] = None
    """The certificate authority that issued the certificate."""

    serial_number: Optional[str] = None
    """The serial number on the uploaded certificate."""

    signature: Optional[str] = None
    """The type of hash used for the certificate."""

    status: Optional[
        Literal[
            "initializing",
            "pending_deployment",
            "pending_deletion",
            "active",
            "deleted",
            "deployment_timed_out",
            "deletion_timed_out",
        ]
    ] = None
    """Status of the certificate or the association."""

    uploaded_on: Optional[datetime] = None
    """The time when the certificate was uploaded."""
