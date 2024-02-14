# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

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
