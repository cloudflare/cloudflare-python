# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..log_rule import LogRule
from ...._models import BaseModel
from ..skip_rule import SkipRule
from ..block_rule import BlockRule
from ..route_rule import RouteRule
from ..score_rule import ScoreRule
from ..execute_rule import ExecuteRule
from ..rewrite_rule import RewriteRule
from ..redirect_rule import RedirectRule
from ..challenge_rule import ChallengeRule
from ..set_config_rule import SetConfigRule
from ..serve_error_rule import ServeErrorRule
from ..js_challenge_rule import JsChallengeRule
from ..compress_response_rule import CompressResponseRule
from ..managed_challenge_rule import ManagedChallengeRule
from ..set_cache_settings_rule import SetCacheSettingsRule

__all__ = ["VersionGetResponse", "Rule"]

Rule = Union[
    BlockRule,
    ChallengeRule,
    CompressResponseRule,
    ExecuteRule,
    JsChallengeRule,
    LogRule,
    ManagedChallengeRule,
    RedirectRule,
    RewriteRule,
    RouteRule,
    ScoreRule,
    ServeErrorRule,
    SetConfigRule,
    SkipRule,
    SetCacheSettingsRule,
]


class VersionGetResponse(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    kind: Literal["managed", "custom", "root", "zone"]
    """The kind of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Literal[
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
    """The phase of the ruleset."""

    rules: List[Rule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""
