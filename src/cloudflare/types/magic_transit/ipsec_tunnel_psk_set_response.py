# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel
from .psk_metadata import PSKMetadata

__all__ = ["IPSECTunnelPSKSetResponse", "SuccessfullyAppliedPSKs"]


class SuccessfullyAppliedPSKs(BaseModel):
    """A successfully applied PSK for an IPsec tunnel."""

    ipsec_id: str
    """The IKE identifier used for this tunnel on the Cloudflare edge."""

    ipsec_tunnel_id: str
    """Identifier"""

    psk: str
    """A randomly generated or provided string for use in the IPsec tunnel."""

    psk_metadata: PSKMetadata
    """The PSK metadata that includes when the PSK was generated."""


class IPSECTunnelPSKSetResponse(BaseModel):
    successfully_applied_psks: Optional[Dict[str, SuccessfullyAppliedPSKs]] = None
    """Map of tunnel IDs to successfully applied PSK details."""

    unapplied_psks: Optional[Dict[str, str]] = None
    """Map of tunnel IDs to failure reasons for PSKs that could not be applied."""
