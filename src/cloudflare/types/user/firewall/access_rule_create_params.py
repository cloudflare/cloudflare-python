# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from ...firewall import (
    IPConfigurationParam,
    ASNConfigurationParam,
    CIDRConfigurationParam,
    IPV6ConfigurationParam,
    CountryConfigurationParam,
)

__all__ = ["AccessRuleCreateParams", "Configuration"]


class AccessRuleCreateParams(TypedDict, total=False):
    configuration: Required[Configuration]
    """The rule configuration."""

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""

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
