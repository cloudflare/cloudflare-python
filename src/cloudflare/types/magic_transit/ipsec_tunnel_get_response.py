# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IPSECTunnelGetResponse"]


class IPSECTunnelGetResponse(BaseModel):
    ipsec_tunnel: Optional[object] = None
