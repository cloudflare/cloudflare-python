# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..authenticated_origin_pull import AuthenticatedOriginPull

__all__ = ["CertificateListResponse"]


class CertificateListResponse(AuthenticatedOriginPull):
    id: Optional[str] = None
    """Identifier"""

    cert_id: Optional[str] = None  # type: ignore
    """Identifier"""

    certificate: Optional[str] = None  # type: ignore
    """The hostname certificate."""

    enabled: Optional[bool] = None  # type: ignore
    """Indicates whether hostname-level authenticated origin pulls is enabled.

    A null value voids the association.
    """

    hostname: Optional[str] = None  # type: ignore
    """
    The hostname on the origin for which the client certificate uploaded will be
    used.
    """

    private_key: Optional[str] = None
    """The hostname certificate's private key."""
