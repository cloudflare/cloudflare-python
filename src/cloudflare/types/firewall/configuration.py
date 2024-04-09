# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .ip_configuration import IPConfiguration
from .cidr_configuration import CIDRConfiguration

__all__ = ["Configuration"]

Configuration = Union[IPConfiguration, CIDRConfiguration]
