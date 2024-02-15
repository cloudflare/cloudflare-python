# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ServiceListResponse", "ServiceListResponseItem"]


class ServiceListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Name of a service running on the Cloudflare network"""


ServiceListResponse = List[ServiceListResponseItem]
