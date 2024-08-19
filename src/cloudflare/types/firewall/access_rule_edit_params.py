# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .asn_configuration_param import ASNConfigurationParam
from .ipv6_configuration_param import IPV6ConfigurationParam
from .country_configuration_param import CountryConfigurationParam
from .access_rule_ip_configuration_param import AccessRuleIPConfigurationParam
from .access_rule_cidr_configuration_param import AccessRuleCIDRConfigurationParam

__all__ = ["AccessRuleEditParams", "Configuration"]


class AccessRuleEditParams(TypedDict, total=False):
    configuration: Required[Configuration]
    """The rule configuration."""

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    notes: str
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """


Configuration: TypeAlias = Union[
    AccessRuleIPConfigurationParam,
    IPV6ConfigurationParam,
    AccessRuleCIDRConfigurationParam,
    ASNConfigurationParam,
    CountryConfigurationParam,
]
