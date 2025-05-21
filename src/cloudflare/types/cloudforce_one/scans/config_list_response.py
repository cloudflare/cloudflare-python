# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ConfigListResponse"]


class ConfigListResponse(BaseModel):
    id: str
    """Defines the Config ID."""

    account_id: str

    frequency: float
    """Defines the number of days between each scan (0 = One-off scan)."""

    ips: List[str]
    """Defines a list of IP addresses or CIDR blocks to scan.

    The maximum number of total IP addresses allowed is 5000.
    """

    ports: List[str]
    """Defines a list of ports to scan.

    Valid values are:"default", "all", or a comma-separated list of ports or range
    of ports (e.g. ["1-80", "443"]). "default" scans the 100 most commonly open
    ports.
    """
