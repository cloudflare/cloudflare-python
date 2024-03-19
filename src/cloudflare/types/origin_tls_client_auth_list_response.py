# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["OriginTLSClientAuthListResponse", "OriginTLSClientAuthListResponseItem"]


class OriginTLSClientAuthListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The zone's leaf certificate."""

    enabled: Optional[bool] = None
    """Indicates whether zone-level authenticated origin pulls is enabled."""

    private_key: Optional[str] = None
    """The zone's private key."""


OriginTLSClientAuthListResponse = List[OriginTLSClientAuthListResponseItem]
