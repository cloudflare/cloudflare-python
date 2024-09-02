# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, TypeAlias

from .access_rule_ip_configuration_param import AccessRuleIPConfigurationParam

from .ipv6_configuration_param import IPV6ConfigurationParam

from .access_rule_cidr_configuration_param import AccessRuleCIDRConfigurationParam

from .asn_configuration_param import ASNConfigurationParam

from .country_configuration_param import CountryConfigurationParam

from typing import Union

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

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


Configuration: TypeAlias = Union[
    AccessRuleIPConfigurationParam,
    IPV6ConfigurationParam,
    AccessRuleCIDRConfigurationParam,
    ASNConfigurationParam,
    CountryConfigurationParam,
]
