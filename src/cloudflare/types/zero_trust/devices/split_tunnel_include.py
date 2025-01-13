# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SplitTunnelInclude"]


class SplitTunnelInclude(BaseModel):
    address: str
    """The address in CIDR format to include in the tunnel.

    If address is present, host must not be present.
    """

    description: str
    """A description of the split tunnel item, displayed in the client UI."""

    host: Optional[str] = None
    """The domain name to include in the tunnel.

    If host is present, address must not be present.
    """
