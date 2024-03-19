# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "AccessRuleCreateParams",
    "Configuration",
    "ConfigurationLegacyJhsIPConfiguration",
    "ConfigurationLegacyJhsIPV6Configuration",
    "ConfigurationLegacyJhsCIDRConfiguration",
    "ConfigurationLegacyJhsASNConfiguration",
    "ConfigurationLegacyJhsCountryConfiguration",
]


class AccessRuleCreateParams(TypedDict, total=False):
    configuration: Required[Configuration]
    """The rule configuration."""

    mode: Required[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The action to apply to a matched request."""

    notes: str
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """


class ConfigurationLegacyJhsIPConfiguration(TypedDict, total=False):
    target: Literal["ip"]
    """The configuration target.

    You must set the target to `ip` when specifying an IP address in the rule.
    """

    value: str
    """The IP address to match.

    This address will be compared to the IP address of incoming requests.
    """


class ConfigurationLegacyJhsIPV6Configuration(TypedDict, total=False):
    target: Literal["ip6"]
    """The configuration target.

    You must set the target to `ip6` when specifying an IPv6 address in the rule.
    """

    value: str
    """The IPv6 address to match."""


class ConfigurationLegacyJhsCIDRConfiguration(TypedDict, total=False):
    target: Literal["ip_range"]
    """The configuration target.

    You must set the target to `ip_range` when specifying an IP address range in the
    rule.
    """

    value: str
    """The IP address range to match.

    You can only use prefix lengths `/16` and `/24` for IPv4 ranges, and prefix
    lengths `/32`, `/48`, and `/64` for IPv6 ranges.
    """


class ConfigurationLegacyJhsASNConfiguration(TypedDict, total=False):
    target: Literal["asn"]
    """The configuration target.

    You must set the target to `asn` when specifying an Autonomous System Number
    (ASN) in the rule.
    """

    value: str
    """The AS number to match."""


class ConfigurationLegacyJhsCountryConfiguration(TypedDict, total=False):
    target: Literal["country"]
    """The configuration target.

    You must set the target to `country` when specifying a country code in the rule.
    """

    value: str
    """The two-letter ISO-3166-1 alpha-2 code to match.

    For more information, refer to
    [IP Access rules: Parameters](https://developers.cloudflare.com/waf/tools/ip-access-rules/parameters/#country).
    """


Configuration = Union[
    ConfigurationLegacyJhsIPConfiguration,
    ConfigurationLegacyJhsIPV6Configuration,
    ConfigurationLegacyJhsCIDRConfiguration,
    ConfigurationLegacyJhsASNConfiguration,
    ConfigurationLegacyJhsCountryConfiguration,
]
