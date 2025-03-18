# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ConfigEditParams"]


class ConfigEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

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
