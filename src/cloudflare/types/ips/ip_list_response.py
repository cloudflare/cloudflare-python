# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .ips import IPs
from .jdcloud_ips import JDCloudIPs

__all__ = ["IPListResponse"]

IPListResponse = Union[IPs, JDCloudIPs]
