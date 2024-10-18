# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .asn_configuration_param import ASNConfigurationParam
from .ipv6_configuration_param import IPV6ConfigurationParam
from .country_configuration_param import CountryConfigurationParam
from .access_rule_ip_configuration_param import AccessRuleIPConfigurationParam
from .access_rule_cidr_configuration_param import AccessRuleCIDRConfigurationParam

__all__ = ["UARuleCreateParams", "Configuration"]


class UARuleCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    configuration: Required[Configuration]
    """The rule configuration."""

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""


Configuration: TypeAlias = Union[
    AccessRuleIPConfigurationParam,
    IPV6ConfigurationParam,
    AccessRuleCIDRConfigurationParam,
    ASNConfigurationParam,
    CountryConfigurationParam,
]
