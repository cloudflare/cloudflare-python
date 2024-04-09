# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .ip_configuration_param import IPConfigurationParam
from .asn_configuration_param import ASNConfigurationParam
from .cidr_configuration_param import CIDRConfigurationParam
from .ipv6_configuration_param import IPV6ConfigurationParam
from .country_configuration_param import CountryConfigurationParam

__all__ = ["AccessRuleCreateParams", "Configuration"]


class AccessRuleCreateParams(TypedDict, total=False):
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


Configuration = Union[
    IPConfigurationParam,
    IPV6ConfigurationParam,
    CIDRConfigurationParam,
    ASNConfigurationParam,
    CountryConfigurationParam,
]
