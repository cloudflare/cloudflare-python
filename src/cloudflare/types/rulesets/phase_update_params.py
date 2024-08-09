# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .route_rule_param import RouteRuleParam
from .score_rule_param import ScoreRuleParam
from .execute_rule_param import ExecuteRuleParam
from .rewrite_rule_param import RewriteRuleParam
from .redirect_rule_param import RedirectRuleParam
from .challenge_rule_param import ChallengeRuleParam
from .set_config_rule_param import SetConfigRuleParam
from .serve_error_rule_param import ServeErrorRuleParam
from .ddos_dynamic_rule_param import DDoSDynamicRuleParam
from .js_challenge_rule_param import JSChallengeRuleParam
from .log_custom_field_rule_param import LogCustomFieldRuleParam
from .compress_response_rule_param import CompressResponseRuleParam
from .managed_challenge_rule_param import ManagedChallengeRuleParam
from .set_cache_settings_rule_param import SetCacheSettingsRuleParam
from .force_connection_close_rule_param import ForceConnectionCloseRuleParam

__all__ = ["PhaseUpdateParams", "Rule"]


class PhaseUpdateParams(TypedDict, total=False):
    rules: Required[Iterable[Rule]]
    """The list of rules in the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""

    name: str
    """The human-readable name of the ruleset."""


Rule: TypeAlias = Union[
    BlockRuleParam,
    ChallengeRuleParam,
    CompressResponseRuleParam,
    ExecuteRuleParam,
    JSChallengeRuleParam,
    LogRuleParam,
    ManagedChallengeRuleParam,
    RedirectRuleParam,
    RewriteRuleParam,
    RouteRuleParam,
    ScoreRuleParam,
    ServeErrorRuleParam,
    SetConfigRuleParam,
    SkipRuleParam,
    SetCacheSettingsRuleParam,
    LogCustomFieldRuleParam,
    DDoSDynamicRuleParam,
    ForceConnectionCloseRuleParam,
]
