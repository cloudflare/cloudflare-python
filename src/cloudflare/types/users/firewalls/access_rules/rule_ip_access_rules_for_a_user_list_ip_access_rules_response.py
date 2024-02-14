# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ....._models import BaseModel
from .....types import shared

__all__ = [
    "RuleIPAccessRulesForAUserListIPAccessRulesResponse",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItem",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfiguration",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPConfiguration",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPV6Configuration",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCidrConfiguration",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsAsnConfiguration",
    "RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCountryConfiguration",
]


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPConfiguration(BaseModel):
    target: Optional[Literal["ip"]] = None
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the rule.
    """

    value: Optional[str] = None
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPV6Configuration(BaseModel):
    target: Optional[Literal["ip6"]] = None
    """The configuration target.

    You must set the target to `ip6` when specifying an IPv6 address in the rule.
    """

    value: Optional[str] = None
    """The IPv6 address to match."""


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCidrConfiguration(BaseModel):
    target: Optional[Literal["ip_range"]] = None
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    rule.
    """

    value: Optional[str] = None
    """The IP address range to match.

    You can only use prefix lengths `/16` and `/24` for IPv4 ranges, and prefix
    lengths `/32`, `/48`, and `/64` for IPv6 ranges.
    """


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsAsnConfiguration(BaseModel):
    target: Optional[Literal["asn"]] = None
    """The configuration target.

    You must set the target to `asn` when specifying an Autonomous System Number
    (ASN) in the rule.
    """

    value: Optional[str] = None
    """The AS number to match."""


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCountryConfiguration(BaseModel):
    target: Optional[Literal["country"]] = None
    """The configuration target.

    You must set the target to `country` when specifying a country code in the rule.
    """

    value: Optional[str] = None
    """The two-letter ISO-3166-1 alpha-2 code to match.

    For more information, refer to
    [IP Access rules: Parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country).
    """


RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfiguration = Union[
    RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPConfiguration,
    RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsIPV6Configuration,
    RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCidrConfiguration,
    RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsAsnConfiguration,
    RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfigurationLegacyJhsCountryConfiguration,
]


class RuleIPAccessRulesForAUserListIPAccessRulesResponseItem(BaseModel):
    id: str
    """The unique identifier of the IP Access rule."""

    allowed_modes: List[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The available actions that a rule can apply to a matched request."""

    configuration: RuleIPAccessRulesForAUserListIPAccessRulesResponseItemConfiguration
    """The rule configuration."""

    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    created_on: Optional[datetime] = None
    """The timestamp of when the rule was created."""

    modified_on: Optional[datetime] = None
    """The timestamp of when the rule was last modified."""

    notes: Optional[str] = None
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """


RuleIPAccessRulesForAUserListIPAccessRulesResponse = List[RuleIPAccessRulesForAUserListIPAccessRulesResponseItem]
