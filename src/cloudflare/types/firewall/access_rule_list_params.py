# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccessRuleListParams", "EgsPagination", "EgsPaginationJson", "Filters"]


class AccessRuleListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    direction: Literal["asc", "desc"]
    """The direction used to sort returned rules."""

    egs_pagination: Annotated[EgsPagination, PropertyInfo(alias="egs-pagination")]

    filters: Filters

    order: Literal["configuration.target", "configuration.value", "mode"]
    """The field used to sort returned rules."""

    page: float
    """Requested page within paginated list of results."""

    per_page: float
    """Maximum number of results requested."""


class EgsPaginationJson(TypedDict, total=False):
    page: float
    """The page number of paginated results."""

    per_page: float
    """The maximum number of results per page.

    You can only set the value to `1` or to a multiple of 5 such as `5`, `10`, `15`,
    or `20`.
    """


class EgsPagination(TypedDict, total=False):
    json: EgsPaginationJson


class Filters(TypedDict, total=False):
    configuration_target: Annotated[
        Literal["ip", "ip_range", "asn", "country"], PropertyInfo(alias="configuration.target")
    ]
    """The target to search in existing rules."""

    configuration_value: Annotated[str, PropertyInfo(alias="configuration.value")]
    """
    The target value to search for in existing rules: an IP address, an IP address
    range, or a country code, depending on the provided `configuration.target`.
    Notes: You can search for a single IPv4 address, an IP address range with a
    subnet of '/16' or '/24', or a two-letter ISO-3166-1 alpha-2 country code.
    """

    match: Literal["any", "all"]
    """When set to `all`, all the search requirements must match.

    When set to `any`, only one of the search requirements has to match.
    """

    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    notes: str
    """
    The string to search for in the notes of existing IP Access rules. Notes: For
    example, the string 'attack' would match IP Access rules with notes 'Attack
    26/02' and 'Attack 27/02'. The search is case insensitive.
    """
