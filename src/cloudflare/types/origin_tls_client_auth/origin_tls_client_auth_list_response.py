# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .zone_authenticated_origin_pull import ZoneAuthenticatedOriginPull

__all__ = ["OriginTLSClientAuthListResponse"]


class OriginTLSClientAuthListResponse(ZoneAuthenticatedOriginPull):
    id: Optional[str] = None  # type: ignore
    """Identifier"""

    certificate: Optional[str] = None  # type: ignore
    """The zone's leaf certificate."""

    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""

    private_key: Optional[str] = None
    """The zone's private key."""
