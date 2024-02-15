# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GreTunnelDeleteResponse"]


class GreTunnelDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_gre_tunnel: Optional[object] = None
