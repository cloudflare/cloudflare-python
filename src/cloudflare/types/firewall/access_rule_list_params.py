# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccessRuleListParams", "Configuration"]


class AccessRuleListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    configuration: Configuration

    direction: Literal["asc", "desc"]
    """Defines the direction used to sort returned rules."""

    match: Literal["any", "all"]
    """Defines the search requirements.

    When set to `all`, all the search requirements must match. When set to `any`,
    only one of the search requirements has to match.
    """

    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    notes: str
    """
    Defines the string to search for in the notes of existing IP Access rules.
    Notes: For example, the string 'attack' would match IP Access rules with notes
    'Attack 26/02' and 'Attack 27/02'. The search is case insensitive.
    """

    order: Literal["configuration.target", "configuration.value", "mode"]
    """Defines the field used to sort returned rules."""

    page: float
    """Defines the requested page within paginated list of results."""

    per_page: float
    """Defines the maximum number of results requested."""


class Configuration(TypedDict, total=False):
    target: Literal["ip", "ip_range", "asn", "country"]
    """Defines the target to search in existing rules."""

    value: str
    """
    Defines the target value to search for in existing rules: an IP address, an IP
    address range, or a country code, depending on the provided
    `configuration.target`. Notes: You can search for a single IPv4 address, an IP
    address range with a subnet of '/16' or '/24', or a two-letter ISO-3166-1
    alpha-2 country code.
    """
