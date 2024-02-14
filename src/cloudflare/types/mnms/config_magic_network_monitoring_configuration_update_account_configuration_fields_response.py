# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse"]


class ConfigMagicNetworkMonitoringConfigurationUpdateAccountConfigurationFieldsResponse(BaseModel):
    default_sampling: float
    """Fallback sampling rate of flow messages being sent in packets per second.

    This should match the packet sampling rate configured on the router.
    """

    name: str
    """The account name."""

    router_ips: List[str]
