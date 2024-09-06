# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ips import IPs

from .jdcloud_ips import JDCloudIPs

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IPListResponse"]

IPListResponse: TypeAlias = Union[IPs, JDCloudIPs]
