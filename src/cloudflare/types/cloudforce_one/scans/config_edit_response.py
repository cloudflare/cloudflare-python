# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["ConfigEditResponse"]


class ConfigEditResponse(BaseModel):
    id: str
    """Config ID"""

    account_id: str

    frequency: float
    """The number of days between each scan (0 = no recurring scans)."""

    ips: List[str]
    """A list of IP addresses or CIDR blocks to scan.

    The maximum number of total IP addresses allowed is 5000.
    """

    ports: List[str]
    """A list of ports to scan.

    Allowed values:"default", "all", or a comma-separated list of ports or range of
    ports (e.g. ["1-80", "443"]). Default will scan the 100 most commonly open
    ports.
    """
