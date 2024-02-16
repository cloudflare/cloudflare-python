# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse", "PskMetadata"]


class PskMetadata(BaseModel):
    last_generated_on: Optional[datetime] = None
    """The date and time the tunnel was last modified."""


class PskGenerateMagicIPsecTunnelsGeneratePreSharedKeyPskForIPsecTunnelsResponse(BaseModel):
    ipsec_tunnel_id: Optional[str] = None
    """Identifier"""

    psk: Optional[str] = None
    """A randomly generated or provided string for use in the IPsec tunnel."""

    psk_metadata: Optional[PskMetadata] = None
    """The PSK metadata that includes when the PSK was generated."""
