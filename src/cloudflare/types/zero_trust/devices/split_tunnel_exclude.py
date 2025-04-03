# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["SplitTunnelExclude", "TeamsDevicesExcludeSplitTunnelWithAddress", "TeamsDevicesExcludeSplitTunnelWithHost"]


class TeamsDevicesExcludeSplitTunnelWithAddress(BaseModel):
    address: str
    """The address in CIDR format to exclude from the tunnel.

    If `address` is present, `host` must not be present.
    """

    description: Optional[str] = None
    """A description of the Split Tunnel item, displayed in the client UI."""


class TeamsDevicesExcludeSplitTunnelWithHost(BaseModel):
    host: str
    """The domain name to exclude from the tunnel.

    If `host` is present, `address` must not be present.
    """

    description: Optional[str] = None
    """A description of the Split Tunnel item, displayed in the client UI."""


SplitTunnelExclude: TypeAlias = Union[TeamsDevicesExcludeSplitTunnelWithAddress, TeamsDevicesExcludeSplitTunnelWithHost]
