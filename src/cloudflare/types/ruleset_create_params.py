# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .execute_rule_param import ExecuteRuleParam

__all__ = ["RulesetCreateParams", "Rule"]


class RulesetCreateParams(TypedDict, total=False):
    kind: Required[Literal["managed", "custom", "root", "zone"]]
    """The kind of the ruleset."""

    name: Required[str]
    """The human-readable name of the ruleset."""

    phase: Required[
        Literal[
            "ddos_l4",
            "ddos_l7",
            "http_config_settings",
            "http_custom_errors",
            "http_log_custom_fields",
            "http_ratelimit",
            "http_request_cache_settings",
            "http_request_dynamic_redirect",
            "http_request_firewall_custom",
            "http_request_firewall_managed",
            "http_request_late_transform",
            "http_request_origin",
            "http_request_redirect",
            "http_request_sanitize",
            "http_request_sbfm",
            "http_request_select_configuration",
            "http_request_transform",
            "http_response_compression",
            "http_response_firewall_managed",
            "http_response_headers_transform",
            "magic_transit",
            "magic_transit_ids_managed",
            "magic_transit_managed",
        ]
    ]
    """The phase of the ruleset."""

    rules: Required[Iterable[Rule]]
    """The list of rules in the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""


Rule = Union[BlockRuleParam, ExecuteRuleParam, LogRuleParam, SkipRuleParam]
