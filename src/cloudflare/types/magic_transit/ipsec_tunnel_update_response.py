# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IPSECTunnelUpdateResponse"]


class IPSECTunnelUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_ipsec_tunnel: Optional[object] = None
