# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .lockdown_ip_configuration import LockdownIPConfiguration
from .lockdown_cidr_configuration import LockdownCIDRConfiguration

__all__ = ["Configuration", "ConfigurationItem"]

ConfigurationItem: TypeAlias = Union[LockdownIPConfiguration, LockdownCIDRConfiguration]

Configuration: TypeAlias = List[ConfigurationItem]
