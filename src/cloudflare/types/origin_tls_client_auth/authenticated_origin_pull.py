# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthenticatedOriginPull"]


class AuthenticatedOriginPull(BaseModel):
    cert_id: Optional[str] = None
    """Identifier"""

    cert_status: Optional[
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

    cert_updated_at: Optional[datetime] = None
    """The time when the certificate was updated."""

    cert_uploaded_on: Optional[datetime] = None
    """The time when the certificate was uploaded."""

    certificate: Optional[str] = None
    """The hostname certificate."""

    created_at: Optional[datetime] = None
    """The time when the certificate was created."""

    enabled: Optional[bool] = None
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    expires_on: Optional[datetime] = None
    """The date when the certificate expires."""

    hostname: Optional[str] = None
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """

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

    updated_at: Optional[datetime] = None
    """The time when the certificate was updated."""
