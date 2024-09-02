# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from .psk_metadata import PSKMetadata

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPSECTunnelPSKGenerateResponse"]


class IPSECTunnelPSKGenerateResponse(BaseModel):
    ipsec_tunnel_id: Optional[str] = None
    """Identifier"""

    psk: Optional[str] = None
    """A randomly generated or provided string for use in the IPsec tunnel."""

    psk_metadata: Optional[PSKMetadata] = None
    """The PSK metadata that includes when the PSK was generated."""
