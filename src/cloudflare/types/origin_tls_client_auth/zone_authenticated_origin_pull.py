# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ZoneAuthenticatedOriginPull"]


class ZoneAuthenticatedOriginPull(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The zone's leaf certificate."""

    expires_on: Optional[datetime] = None
    """When the certificate from the authority expires."""

    issuer: Optional[str] = None
    """The certificate authority that issued the certificate."""

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
    """Status of the certificate activation."""

    uploaded_on: Optional[datetime] = None
    """This is the time the certificate was uploaded."""
