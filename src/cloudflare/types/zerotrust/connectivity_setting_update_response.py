# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ConnectivitySettingUpdateResponse"]


class ConnectivitySettingUpdateResponse(BaseModel):
    icmp_proxy_enabled: Optional[bool] = None
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: Optional[bool] = None
    """A flag to enable WARP to WARP traffic."""
