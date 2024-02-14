# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = ["ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse"]


class ContentListWeb3HostnameIpfsUniversalPathGatewayContentListDetailsResponse(BaseModel):
    action: Optional[Literal["block"]] = None
    """Behavior of the content list."""
