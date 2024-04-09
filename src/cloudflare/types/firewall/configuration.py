# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .lockdown_ip_configuration import LockdownIPConfiguration
from .lockdown_cidr_configuration import LockdownCIDRConfiguration

__all__ = ["Configuration"]

Configuration = Union[LockdownIPConfiguration, LockdownCIDRConfiguration]
