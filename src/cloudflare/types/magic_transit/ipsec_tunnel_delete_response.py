# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IPSECTunnelDeleteResponse"]


class IPSECTunnelDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_ipsec_tunnel: Optional[object] = None
