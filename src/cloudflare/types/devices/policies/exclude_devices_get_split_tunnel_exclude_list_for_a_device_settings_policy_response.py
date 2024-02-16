# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = [
    "ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse",
    "ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponseItem",
]


class ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponseItem(BaseModel):
    address: str
    """The address in CIDR format to exclude from the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: str
    """A description of the Split Tunnel item, displayed in the client UI."""

    host: Optional[str] = None
    """The domain name to exclude from the tunnel.

    If `host` is present, `address` must not be present.
    """


ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponse = List[
    ExcludeDevicesGetSplitTunnelExcludeListForADeviceSettingsPolicyResponseItem
]
