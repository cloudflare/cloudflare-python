# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime

from .kind import Kind
from .phase import Phase
from .log_rule import LogRule
from ..._models import BaseModel
from .skip_rule import SkipRule
from .block_rule import BlockRule
from .route_rule import RouteRule
from .score_rule import ScoreRule
from .execute_rule import ExecuteRule
from .rewrite_rule import RewriteRule
from .redirect_rule import RedirectRule
from .challenge_rule import ChallengeRule
from .set_config_rule import SetConfigRule
from .serve_error_rule import ServeErrorRule
from .js_challenge_rule import JSChallengeRule
from .compress_response_rule import CompressResponseRule
from .managed_challenge_rule import ManagedChallengeRule
from .set_cache_settings_rule import SetCacheSettingsRule

__all__ = ["RulesetUpdateResponse", "Rule"]

Rule = Union[
    BlockRule,
    ChallengeRule,
    CompressResponseRule,
    ExecuteRule,
    JSChallengeRule,
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


class RulesetUpdateResponse(BaseModel):
    id: str
    """The unique ID of the ruleset."""

    kind: Kind
    """The kind of the ruleset."""

    last_updated: datetime
    """The timestamp of when the ruleset was last modified."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Phase
    """The phase of the ruleset."""

    rules: List[Rule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""
