# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IpsecTunnelDeleteResponse"]


class IpsecTunnelDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_ipsec_tunnel: Optional[object] = None
