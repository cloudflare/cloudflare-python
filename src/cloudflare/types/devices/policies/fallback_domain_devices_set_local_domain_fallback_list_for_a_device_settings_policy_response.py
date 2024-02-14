# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse",
    "FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem",
]


class FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem(BaseModel):
    suffix: str
    """The domain suffix to match when resolving locally."""

    description: Optional[str] = None
    """A description of the fallback domain, displayed in the client UI."""

    dns_server: Optional[List[object]] = None
    """A list of IP addresses to handle domain resolution."""


FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponse = List[
    FallbackDomainDevicesSetLocalDomainFallbackListForADeviceSettingsPolicyResponseItem
]
