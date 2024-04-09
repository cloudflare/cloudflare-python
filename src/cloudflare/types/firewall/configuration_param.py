# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union

from .ip_configuration_param import IPConfigurationParam
from .cidr_configuration_param import CIDRConfigurationParam

__all__ = ["ConfigurationParam"]

ConfigurationParam = Union[IPConfigurationParam, CIDRConfigurationParam]
