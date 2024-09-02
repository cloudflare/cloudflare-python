# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ConnectivitySettingEditResponse"]


class ConnectivitySettingEditResponse(BaseModel):
    icmp_proxy_enabled: Optional[bool] = None
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: Optional[bool] = None
    """A flag to enable WARP to WARP traffic."""
