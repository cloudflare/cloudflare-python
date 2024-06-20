# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .psk_metadata import PSKMetadata

__all__ = ["IPSECTunnelPSKGenerateResponse"]


class IPSECTunnelPSKGenerateResponse(BaseModel):
    ipsec_tunnel_id: Optional[str] = None
    """Identifier"""

    psk: Optional[str] = None
    """A randomly generated or provided string for use in the IPsec tunnel."""

    psk_metadata: Optional[PSKMetadata] = None
    """The PSK metadata that includes when the PSK was generated."""
