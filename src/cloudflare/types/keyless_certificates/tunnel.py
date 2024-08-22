# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Tunnel"]

class Tunnel(BaseModel):
    private_ip: str
    """Private IP of the Key Server Host"""

    vnet_id: str
    """Cloudflare Tunnel Virtual Network ID"""