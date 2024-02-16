# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse",
    "FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem",
]


class FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem(BaseModel):
    suffix: str
    """The domain suffix to match when resolving locally."""

    description: Optional[str] = None
    """A description of the fallback domain, displayed in the client UI."""

    dns_server: Optional[List[object]] = None
    """A list of IP addresses to handle domain resolution."""


FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponse = List[
    FallbackDomainDevicesGetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem
]
