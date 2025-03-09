# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ConfigCreateParams"]


class ConfigCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID"""

    frequency: Required[float]
    """The number of days between each scan (0 = no recurring scans)"""

    ips: Required[List[str]]
    """A list of IP addresses or CIDR blocks to scan.

    The maximum number of total IP addresses allowed is 5000.
    """
