# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AuthenticatedOriginPull"]


class AuthenticatedOriginPull(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    cert_id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The hostname certificate."""

    enabled: Optional[bool] = None
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    hostname: Optional[str] = None
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """

    private_key: Optional[str] = None
    """The hostname certificate's private key."""
