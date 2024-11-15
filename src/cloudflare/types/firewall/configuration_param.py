# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .lockdown_ip_configuration_param import LockdownIPConfigurationParam
from .lockdown_cidr_configuration_param import LockdownCIDRConfigurationParam

__all__ = ["ConfigurationParam", "ConfigurationParamItem"]

ConfigurationParamItem: TypeAlias = Union[LockdownIPConfigurationParam, LockdownCIDRConfigurationParam]

ConfigurationParam: TypeAlias = List[ConfigurationParamItem]
