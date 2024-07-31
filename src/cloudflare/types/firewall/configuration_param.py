# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .lockdown_ip_configuration_param import LockdownIPConfigurationParam
from .lockdown_cidr_configuration_param import LockdownCIDRConfigurationParam

__all__ = ["ConfigurationParam"]

ConfigurationParam = Union[LockdownIPConfigurationParam, LockdownCIDRConfigurationParam]
