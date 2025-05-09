# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Defines the Account ID."""

    ips: Required[List[str]]
    """Defines a list of IP addresses or CIDR blocks to scan.

    The maximum number of total IP addresses allowed is 5000.
    """

    frequency: float
    """Defines the number of days between each scan (0 = One-off scan)."""

    ports: List[str]
    """Defines a list of ports to scan.

    Valid values are:"default", "all", or a comma-separated list of ports or range
    of ports (e.g. ["1-80", "443"]). "default" scans the 100 most commonly open
    ports.
    """
