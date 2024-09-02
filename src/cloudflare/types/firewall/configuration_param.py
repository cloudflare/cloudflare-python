# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .lockdown_ip_configuration_param import LockdownIPConfigurationParam

from .lockdown_cidr_configuration_param import LockdownCIDRConfigurationParam

from typing_extensions import TypeAlias

from typing import Union

__all__ = ["ConfigurationParam"]

ConfigurationParam: TypeAlias = Union[LockdownIPConfigurationParam, LockdownCIDRConfigurationParam]
