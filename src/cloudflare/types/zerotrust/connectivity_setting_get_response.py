# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConnectivitySettingGetResponse"]


class ConnectivitySettingGetResponse(BaseModel):
    icmp_proxy_enabled: Optional[bool] = None
    """A flag to enable the ICMP proxy for the account network."""

    offramp_warp_enabled: Optional[bool] = None
    """A flag to enable WARP to WARP traffic."""
