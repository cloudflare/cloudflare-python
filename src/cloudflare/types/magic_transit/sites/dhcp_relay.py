# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["DHCPRelay"]


class DHCPRelay(BaseModel):
    server_addresses: Optional[List[str]] = None
    """List of DHCP server IPs."""
