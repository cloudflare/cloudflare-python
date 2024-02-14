# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["IpsecTunnelDeleteResponse"]


class IpsecTunnelDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_ipsec_tunnel: Optional[object] = None
