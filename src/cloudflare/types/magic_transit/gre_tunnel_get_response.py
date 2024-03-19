# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GRETunnelGetResponse"]


class GRETunnelGetResponse(BaseModel):
    gre_tunnel: Optional[object] = None
