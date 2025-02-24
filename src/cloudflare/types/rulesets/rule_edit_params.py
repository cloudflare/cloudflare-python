# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .phase import Phase
from .logging_param import LoggingParam
from .rewrite_uri_part_param import RewriteURIPartParam

__all__ = [
    "RuleEditParams",
    "BlockRule",
    "BlockRuleActionParameters",
    "BlockRuleActionParametersResponse",
    "BlockRuleExposedCredentialCheck",
    "BlockRulePosition",
    "BlockRulePositionBeforePosition",
    "BlockRulePositionAfterPosition",
    "BlockRulePositionIndexPosition",
    "BlockRuleRatelimit",
    "ChallengeRule",
    "ChallengeRuleExposedCredentialCheck",
    "ChallengeRulePosition",
    "ChallengeRulePositionBeforePosition",
    "ChallengeRulePositionAfterPosition",
    "ChallengeRulePositionIndexPosition",
    "ChallengeRuleRatelimit",
    "CompressionRule",
    "CompressionRuleActionParameters",
    "CompressionRuleActionParametersAlgorithm",
    "CompressionRuleExposedCredentialCheck",
    "CompressionRulePosition",
    "CompressionRulePositionBeforePosition",
    "CompressionRulePositionAfterPosition",
    "CompressionRulePositionIndexPosition",
    "CompressionRuleRatelimit",
    "ExecuteRule",
    "ExecuteRuleActionParameters",
    "ExecuteRuleActionParametersMatchedData",
    "ExecuteRuleActionParametersOverrides",
    "ExecuteRuleActionParametersOverridesCategory",
    "ExecuteRuleActionParametersOverridesRule",
    "ExecuteRuleExposedCredentialCheck",
    "ExecuteRulePosition",
    "ExecuteRulePositionBeforePosition",
    "ExecuteRulePositionAfterPosition",
    "ExecuteRulePositionIndexPosition",
    "ExecuteRuleRatelimit",
    "JavascriptChallengeRule",
    "JavascriptChallengeRuleExposedCredentialCheck",
    "JavascriptChallengeRulePosition",
    "JavascriptChallengeRulePositionBeforePosition",
    "JavascriptChallengeRulePositionAfterPosition",
    "JavascriptChallengeRulePositionIndexPosition",
    "JavascriptChallengeRuleRatelimit",
    "LogRule",
    "LogRuleExposedCredentialCheck",
    "LogRulePosition",
    "LogRulePositionBeforePosition",
    "LogRulePositionAfterPosition",
    "LogRulePositionIndexPosition",
    "LogRuleRatelimit",
    "ManagedChallengeRule",
    "ManagedChallengeRuleExposedCredentialCheck",
    "ManagedChallengeRulePosition",
    "ManagedChallengeRulePositionBeforePosition",
    "ManagedChallengeRulePositionAfterPosition",
    "ManagedChallengeRulePositionIndexPosition",
    "ManagedChallengeRuleRatelimit",
    "RedirectRule",
    "RedirectRuleActionParameters",
    "RedirectRuleActionParametersFromList",
    "RedirectRuleActionParametersFromValue",
    "RedirectRuleActionParametersFromValueTargetURL",
    "RedirectRuleActionParametersFromValueTargetURLStaticURLRedirect",
    "RedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect",
    "RedirectRuleExposedCredentialCheck",
    "RedirectRulePosition",
    "RedirectRulePositionBeforePosition",
    "RedirectRulePositionAfterPosition",
    "RedirectRulePositionIndexPosition",
    "RedirectRuleRatelimit",
    "RewriteRule",
    "RewriteRuleActionParameters",
    "RewriteRuleActionParametersHeaders",
    "RewriteRuleActionParametersHeadersRemoveHeader",
    "RewriteRuleActionParametersHeadersStaticHeader",
    "RewriteRuleActionParametersHeadersDynamicHeader",
    "RewriteRuleActionParametersURI",
    "RewriteRuleExposedCredentialCheck",
    "RewriteRulePosition",
    "RewriteRulePositionBeforePosition",
    "RewriteRulePositionAfterPosition",
    "RewriteRulePositionIndexPosition",
    "RewriteRuleRatelimit",
    "OriginRule",
    "OriginRuleActionParameters",
    "OriginRuleActionParametersOrigin",
    "OriginRuleActionParametersSNI",
    "OriginRuleExposedCredentialCheck",
    "OriginRulePosition",
    "OriginRulePositionBeforePosition",
    "OriginRulePositionAfterPosition",
    "OriginRulePositionIndexPosition",
    "OriginRuleRatelimit",
    "ScoreRule",
    "ScoreRuleActionParameters",
    "ScoreRuleExposedCredentialCheck",
    "ScoreRulePosition",
    "ScoreRulePositionBeforePosition",
    "ScoreRulePositionAfterPosition",
    "ScoreRulePositionIndexPosition",
    "ScoreRuleRatelimit",
    "ServeErrorRule",
    "ServeErrorRuleActionParameters",
    "ServeErrorRuleExposedCredentialCheck",
    "ServeErrorRulePosition",
    "ServeErrorRulePositionBeforePosition",
    "ServeErrorRulePositionAfterPosition",
    "ServeErrorRulePositionIndexPosition",
    "ServeErrorRuleRatelimit",
    "SetConfigRule",
    "SetConfigRuleActionParameters",
    "SetConfigRuleActionParametersAutominify",
    "SetConfigRuleExposedCredentialCheck",
    "SetConfigRulePosition",
    "SetConfigRulePositionBeforePosition",
    "SetConfigRulePositionAfterPosition",
    "SetConfigRulePositionIndexPosition",
    "SetConfigRuleRatelimit",
    "SkipRule",
    "SkipRuleActionParameters",
    "SkipRuleExposedCredentialCheck",
    "SkipRulePosition",
    "SkipRulePositionBeforePosition",
    "SkipRulePositionAfterPosition",
    "SkipRulePositionIndexPosition",
    "SkipRuleRatelimit",
    "SetCacheSettingsRule",
    "SetCacheSettingsRuleActionParameters",
    "SetCacheSettingsRuleActionParametersBrowserTTL",
    "SetCacheSettingsRuleActionParametersCacheKey",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKey",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser",
    "SetCacheSettingsRuleActionParametersCacheReserve",
    "SetCacheSettingsRuleActionParametersEdgeTTL",
    "SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL",
    "SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange",
    "SetCacheSettingsRuleActionParametersServeStale",
    "SetCacheSettingsRuleExposedCredentialCheck",
    "SetCacheSettingsRulePosition",
    "SetCacheSettingsRulePositionBeforePosition",
    "SetCacheSettingsRulePositionAfterPosition",
    "SetCacheSettingsRulePositionIndexPosition",
    "SetCacheSettingsRuleRatelimit",
    "LogCustomFieldRule",
    "LogCustomFieldRuleActionParameters",
    "LogCustomFieldRuleActionParametersCookieField",
    "LogCustomFieldRuleActionParametersRawResponseField",
    "LogCustomFieldRuleActionParametersRequestField",
    "LogCustomFieldRuleActionParametersResponseField",
    "LogCustomFieldRuleActionParametersTransformedRequestField",
    "LogCustomFieldRuleExposedCredentialCheck",
    "LogCustomFieldRulePosition",
    "LogCustomFieldRulePositionBeforePosition",
    "LogCustomFieldRulePositionAfterPosition",
    "LogCustomFieldRulePositionIndexPosition",
    "LogCustomFieldRuleRatelimit",
    "DDoSDynamicRule",
    "DDoSDynamicRuleExposedCredentialCheck",
    "DDoSDynamicRulePosition",
    "DDoSDynamicRulePositionBeforePosition",
    "DDoSDynamicRulePositionAfterPosition",
    "DDoSDynamicRulePositionIndexPosition",
    "DDoSDynamicRuleRatelimit",
    "ForceConnectionCloseRule",
    "ForceConnectionCloseRuleExposedCredentialCheck",
    "ForceConnectionCloseRulePosition",
    "ForceConnectionCloseRulePositionBeforePosition",
    "ForceConnectionCloseRulePositionAfterPosition",
    "ForceConnectionCloseRulePositionIndexPosition",
    "ForceConnectionCloseRuleRatelimit",
]


class BlockRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["block"]
    """The action to perform when the rule matches."""

    action_parameters: BlockRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: BlockRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: BlockRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: BlockRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class BlockRuleActionParametersResponse(TypedDict, total=False):
    content: Required[str]
    """The content to return."""

    content_type: Required[str]
    """The type of the content to return."""

    status_code: Required[int]
    """The status code to return."""


class BlockRuleActionParameters(TypedDict, total=False):
    response: BlockRuleActionParametersResponse
    """The response to show when the block is applied."""


class BlockRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class BlockRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class BlockRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class BlockRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


BlockRulePosition: TypeAlias = Union[
    BlockRulePositionBeforePosition, BlockRulePositionAfterPosition, BlockRulePositionIndexPosition
]


class BlockRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ChallengeRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["challenge"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ChallengeRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ChallengeRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ChallengeRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ChallengeRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ChallengeRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ChallengeRulePosition: TypeAlias = Union[
    ChallengeRulePositionBeforePosition, ChallengeRulePositionAfterPosition, ChallengeRulePositionIndexPosition
]


class ChallengeRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class CompressionRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["compress_response"]
    """The action to perform when the rule matches."""

    action_parameters: CompressionRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: CompressionRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: CompressionRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: CompressionRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class CompressionRuleActionParametersAlgorithm(TypedDict, total=False):
    name: Literal["none", "auto", "default", "gzip", "brotli"]
    """Name of compression algorithm to enable."""


class CompressionRuleActionParameters(TypedDict, total=False):
    algorithms: Iterable[CompressionRuleActionParametersAlgorithm]
    """Custom order for compression algorithms."""


class CompressionRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class CompressionRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class CompressionRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class CompressionRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


CompressionRulePosition: TypeAlias = Union[
    CompressionRulePositionBeforePosition, CompressionRulePositionAfterPosition, CompressionRulePositionIndexPosition
]


class CompressionRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ExecuteRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["execute"]
    """The action to perform when the rule matches."""

    action_parameters: ExecuteRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ExecuteRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ExecuteRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ExecuteRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ExecuteRuleActionParametersMatchedData(TypedDict, total=False):
    public_key: Required[str]
    """The public key to encrypt matched data logs with."""


class ExecuteRuleActionParametersOverridesCategory(TypedDict, total=False):
    category: Required[str]
    """The name of the category to override."""

    action: str
    """The action to override rules in the category with."""

    enabled: bool
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for rules in the category."""


class ExecuteRuleActionParametersOverridesRule(TypedDict, total=False):
    id: Required[str]
    """The ID of the rule to override."""

    action: str
    """The action to override the rule with."""

    enabled: bool
    """Whether to enable execution of the rule."""

    score_threshold: int
    """The score threshold to use for the rule."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for the rule."""


class ExecuteRuleActionParametersOverrides(TypedDict, total=False):
    action: str
    """An action to override all rules with.

    This option has lower precedence than rule and category overrides.
    """

    categories: Iterable[ExecuteRuleActionParametersOverridesCategory]
    """A list of category-level overrides.

    This option has the second-highest precedence after rule-level overrides.
    """

    enabled: bool
    """Whether to enable execution of all rules.

    This option has lower precedence than rule and category overrides.
    """

    rules: Iterable[ExecuteRuleActionParametersOverridesRule]
    """A list of rule-level overrides. This option has the highest precedence."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """A sensitivity level to set for all rules.

    This option has lower precedence than rule and category overrides and is only
    applicable for DDoS phases.
    """


class ExecuteRuleActionParameters(TypedDict, total=False):
    id: Required[str]
    """The ID of the ruleset to execute."""

    matched_data: ExecuteRuleActionParametersMatchedData
    """The configuration to use for matched data logging."""

    overrides: ExecuteRuleActionParametersOverrides
    """A set of overrides to apply to the target ruleset."""


class ExecuteRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ExecuteRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ExecuteRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ExecuteRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ExecuteRulePosition: TypeAlias = Union[
    ExecuteRulePositionBeforePosition, ExecuteRulePositionAfterPosition, ExecuteRulePositionIndexPosition
]


class ExecuteRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class JavascriptChallengeRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["js_challenge"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: JavascriptChallengeRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: JavascriptChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: JavascriptChallengeRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class JavascriptChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class JavascriptChallengeRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class JavascriptChallengeRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class JavascriptChallengeRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


JavascriptChallengeRulePosition: TypeAlias = Union[
    JavascriptChallengeRulePositionBeforePosition,
    JavascriptChallengeRulePositionAfterPosition,
    JavascriptChallengeRulePositionIndexPosition,
]


class JavascriptChallengeRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class LogRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["log"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: LogRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: LogRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: LogRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class LogRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class LogRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class LogRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class LogRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


LogRulePosition: TypeAlias = Union[
    LogRulePositionBeforePosition, LogRulePositionAfterPosition, LogRulePositionIndexPosition
]


class LogRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ManagedChallengeRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["managed_challenge"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ManagedChallengeRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ManagedChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ManagedChallengeRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ManagedChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ManagedChallengeRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ManagedChallengeRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ManagedChallengeRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ManagedChallengeRulePosition: TypeAlias = Union[
    ManagedChallengeRulePositionBeforePosition,
    ManagedChallengeRulePositionAfterPosition,
    ManagedChallengeRulePositionIndexPosition,
]


class ManagedChallengeRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class RedirectRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["redirect"]
    """The action to perform when the rule matches."""

    action_parameters: RedirectRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RedirectRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: RedirectRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: RedirectRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RedirectRuleActionParametersFromList(TypedDict, total=False):
    key: str
    """Expression that evaluates to the list lookup key."""

    name: str
    """The name of the list to match against."""


class RedirectRuleActionParametersFromValueTargetURLStaticURLRedirect(TypedDict, total=False):
    value: str
    """The URL to redirect the request to."""


class RedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect(TypedDict, total=False):
    expression: str
    """An expression to evaluate to get the URL to redirect the request to."""


RedirectRuleActionParametersFromValueTargetURL: TypeAlias = Union[
    RedirectRuleActionParametersFromValueTargetURLStaticURLRedirect,
    RedirectRuleActionParametersFromValueTargetURLDynamicURLRedirect,
]


class RedirectRuleActionParametersFromValue(TypedDict, total=False):
    preserve_query_string: bool
    """Keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to be used for the redirect."""

    target_url: RedirectRuleActionParametersFromValueTargetURL
    """The URL to redirect the request to."""


class RedirectRuleActionParameters(TypedDict, total=False):
    from_list: RedirectRuleActionParametersFromList
    """Serve a redirect based on a bulk list lookup."""

    from_value: RedirectRuleActionParametersFromValue
    """Serve a redirect based on the request properties."""


class RedirectRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class RedirectRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class RedirectRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class RedirectRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


RedirectRulePosition: TypeAlias = Union[
    RedirectRulePositionBeforePosition, RedirectRulePositionAfterPosition, RedirectRulePositionIndexPosition
]


class RedirectRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class RewriteRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["rewrite"]
    """The action to perform when the rule matches."""

    action_parameters: RewriteRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RewriteRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: RewriteRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: RewriteRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class RewriteRuleActionParametersHeadersRemoveHeader(TypedDict, total=False):
    operation: Required[Literal["remove"]]


class RewriteRuleActionParametersHeadersStaticHeader(TypedDict, total=False):
    operation: Required[Literal["set"]]

    value: Required[str]
    """Static value for the header."""


class RewriteRuleActionParametersHeadersDynamicHeader(TypedDict, total=False):
    expression: Required[str]
    """Expression for the header value."""

    operation: Required[Literal["set"]]


RewriteRuleActionParametersHeaders: TypeAlias = Union[
    RewriteRuleActionParametersHeadersRemoveHeader,
    RewriteRuleActionParametersHeadersStaticHeader,
    RewriteRuleActionParametersHeadersDynamicHeader,
]


class RewriteRuleActionParametersURI(TypedDict, total=False):
    path: RewriteURIPartParam
    """Path portion rewrite."""

    query: RewriteURIPartParam
    """Query portion rewrite."""


class RewriteRuleActionParameters(TypedDict, total=False):
    headers: Dict[str, RewriteRuleActionParametersHeaders]
    """Map of request headers to modify."""

    uri: RewriteRuleActionParametersURI
    """URI to rewrite the request to."""


class RewriteRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class RewriteRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class RewriteRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class RewriteRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


RewriteRulePosition: TypeAlias = Union[
    RewriteRulePositionBeforePosition, RewriteRulePositionAfterPosition, RewriteRulePositionIndexPosition
]


class RewriteRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class OriginRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["route"]
    """The action to perform when the rule matches."""

    action_parameters: OriginRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: OriginRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: OriginRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: OriginRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class OriginRuleActionParametersOrigin(TypedDict, total=False):
    host: str
    """Override the resolved hostname."""

    port: float
    """Override the destination port."""


class OriginRuleActionParametersSNI(TypedDict, total=False):
    value: Required[str]
    """The SNI override."""


class OriginRuleActionParameters(TypedDict, total=False):
    host_header: str
    """Rewrite the HTTP Host header."""

    origin: OriginRuleActionParametersOrigin
    """Override the IP/TCP destination."""

    sni: OriginRuleActionParametersSNI
    """Override the Server Name Indication (SNI)."""


class OriginRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class OriginRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class OriginRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class OriginRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


OriginRulePosition: TypeAlias = Union[
    OriginRulePositionBeforePosition, OriginRulePositionAfterPosition, OriginRulePositionIndexPosition
]


class OriginRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ScoreRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["score"]
    """The action to perform when the rule matches."""

    action_parameters: ScoreRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ScoreRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ScoreRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ScoreRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ScoreRuleActionParameters(TypedDict, total=False):
    increment: int
    """
    Increment contains the delta to change the score and can be either positive or
    negative.
    """


class ScoreRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ScoreRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ScoreRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ScoreRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ScoreRulePosition: TypeAlias = Union[
    ScoreRulePositionBeforePosition, ScoreRulePositionAfterPosition, ScoreRulePositionIndexPosition
]


class ScoreRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ServeErrorRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["serve_error"]
    """The action to perform when the rule matches."""

    action_parameters: ServeErrorRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ServeErrorRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ServeErrorRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ServeErrorRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ServeErrorRuleActionParameters(TypedDict, total=False):
    content: str
    """Error response content."""

    content_type: Literal["application/json", "text/xml", "text/plain", "text/html"]
    """Content-type header to set with the response."""

    status_code: float
    """The status code to use for the error."""


class ServeErrorRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ServeErrorRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ServeErrorRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ServeErrorRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ServeErrorRulePosition: TypeAlias = Union[
    ServeErrorRulePositionBeforePosition, ServeErrorRulePositionAfterPosition, ServeErrorRulePositionIndexPosition
]


class ServeErrorRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class SetConfigRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["set_config"]
    """The action to perform when the rule matches."""

    action_parameters: SetConfigRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: SetConfigRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SetConfigRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SetConfigRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class SetConfigRuleActionParametersAutominify(TypedDict, total=False):
    css: bool
    """Minify CSS files."""

    html: bool
    """Minify HTML files."""

    js: bool
    """Minify JS files."""


class SetConfigRuleActionParameters(TypedDict, total=False):
    automatic_https_rewrites: bool
    """Turn on or off Automatic HTTPS Rewrites."""

    autominify: SetConfigRuleActionParametersAutominify
    """Select which file extensions to minify automatically."""

    bic: bool
    """Turn on or off Browser Integrity Check."""

    disable_apps: Literal[True]
    """Turn off all active Cloudflare Apps."""

    disable_rum: Literal[True]
    """Turn off Real User Monitoring (RUM)."""

    disable_zaraz: Literal[True]
    """Turn off Zaraz."""

    email_obfuscation: bool
    """Turn on or off Email Obfuscation."""

    fonts: bool
    """Turn on or off Cloudflare Fonts."""

    hotlink_protection: bool
    """Turn on or off the Hotlink Protection."""

    mirage: bool
    """Turn on or off Mirage."""

    opportunistic_encryption: bool
    """Turn on or off Opportunistic Encryption."""

    polish: Literal["off", "lossless", "lossy"]
    """Configure the Polish level."""

    rocket_loader: bool
    """Turn on or off Rocket Loader"""

    security_level: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """Configure the Security Level."""

    server_side_excludes: bool
    """Turn on or off Server Side Excludes."""

    ssl: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """Configure the SSL level."""

    sxg: bool
    """Turn on or off Signed Exchanges (SXG)."""


class SetConfigRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class SetConfigRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SetConfigRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SetConfigRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


SetConfigRulePosition: TypeAlias = Union[
    SetConfigRulePositionBeforePosition, SetConfigRulePositionAfterPosition, SetConfigRulePositionIndexPosition
]


class SetConfigRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class SkipRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["skip"]
    """The action to perform when the rule matches."""

    action_parameters: SkipRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: SkipRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SkipRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SkipRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class SkipRuleActionParameters(TypedDict, total=False):
    phases: List[Phase]
    """A list of phases to skip the execution of.

    This option is incompatible with the ruleset and rulesets options.
    """

    products: List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    """A list of legacy security products to skip the execution of."""

    rules: Dict[str, List[str]]
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Literal["current"]
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets, rules and phases options.
    """

    rulesets: List[str]
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class SkipRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class SkipRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SkipRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SkipRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


SkipRulePosition: TypeAlias = Union[
    SkipRulePositionBeforePosition, SkipRulePositionAfterPosition, SkipRulePositionIndexPosition
]


class SkipRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class SetCacheSettingsRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_settings"]
    """The action to perform when the rule matches."""

    action_parameters: SetCacheSettingsRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: SetCacheSettingsRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SetCacheSettingsRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SetCacheSettingsRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class SetCacheSettingsRuleActionParametersBrowserTTL(TypedDict, total=False):
    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """Determines which browser ttl mode to use."""

    default: int
    """The TTL (in seconds) if you choose override_origin mode."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these cookie names.

    The presence of these cookies is used in building the cache key.
    """

    include: List[str]
    """Include these cookies' names and their values."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader(TypedDict, total=False):
    check_presence: List[str]
    """Checks for the presence of these header names.

    The presence of these headers is used in building the cache key.
    """

    contains: Dict[str, List[str]]
    """
    For each header name and list of values combination, check if the request header
    contains any of the values provided. The presence of the request header and
    whether any of the values provided are contained in the request header value is
    used in building the cache key.
    """

    exclude_origin: bool
    """Whether or not to include the origin header.

    A value of true will exclude the origin header in the cache key.
    """

    include: List[str]
    """Include these headers' names and their values."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost(TypedDict, total=False):
    resolved: bool
    """Use the resolved host in the cache key.

    A value of true will use the resolved host, while a value or false will use the
    original host.
    """


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters(
    TypedDict, total=False
):
    list: List[str]


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters(
    TypedDict, total=False
):
    all: bool
    """Determines whether to include all query string parameters in the cache key."""


SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude: TypeAlias = Union[
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeSomeQueryStringParameters,
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersIncludeAllQueryStringParameters,
]


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters(
    TypedDict, total=False
):
    include: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParametersInclude
    """A list of query string parameters used to build the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters(
    TypedDict, total=False
):
    list: List[str]


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters(
    TypedDict, total=False
):
    all: bool
    """Determines whether to exclude all query string parameters from the cache key."""


SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude: TypeAlias = Union[
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeSomeQueryStringParameters,
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExcludeAllQueryStringParameters,
]


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters(
    TypedDict, total=False
):
    exclude: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParametersExclude
    """A list of query string parameters NOT used to build the cache key.

    All parameters present in the request but missing in this list will be used to
    build the cache key.
    """


SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString: TypeAlias = Union[
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringIncludedQueryStringParameters,
    SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExcludedQueryStringParameters,
]


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser(TypedDict, total=False):
    device_type: bool
    """Use the user agent's device type in the cache key."""

    geo: bool
    """Use the user agents's country in the cache key."""

    lang: bool
    """Use the user agent's language in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKey(TypedDict, total=False):
    cookie: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie
    """The cookies to include in building the cache key."""

    header: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader
    """The header names and values to include in building the cache key."""

    host: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost
    """Whether to use the original host or the resolved host in the cache key."""

    query_string: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString
    """Use the presence of parameters in the query string to build the cache key."""

    user: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser
    """Characteristics of the request user agent used in building the cache key."""


class SetCacheSettingsRuleActionParametersCacheKey(TypedDict, total=False):
    cache_by_device_type: bool
    """Separate cached content based on the visitor’s device type"""

    cache_deception_armor: bool
    """
    Protect from web cache deception attacks while allowing static assets to be
    cached
    """

    custom_key: SetCacheSettingsRuleActionParametersCacheKeyCustomKey
    """
    Customize which components of the request are included or excluded from the
    cache key.
    """

    ignore_query_strings_order: bool
    """
    Treat requests with the same query parameters the same, regardless of the order
    those query parameters are in. A value of true ignores the query strings' order.
    """


class SetCacheSettingsRuleActionParametersCacheReserve(TypedDict, total=False):
    eligible: Required[bool]
    """Determines whether cache reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to cache reserve.
    """

    minimum_file_size: Required[int]
    """The minimum file size eligible for store in cache reserve."""


_SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords = TypedDict(
    "_SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange(
    _SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRangeReservedKeywords, total=False
):
    to: Required[int]
    """response status code upper bound"""


class SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL(TypedDict, total=False):
    value: Required[int]
    """Time to cache a response (in seconds).

    A value of 0 is equivalent to setting the Cache-Control header with the value
    "no-cache". A value of -1 is equivalent to setting Cache-Control header with the
    value of "no-store".
    """

    status_code_range: SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    """The range of status codes used to apply the selected mode."""

    status_code_value: int
    """Set the ttl for responses with this specific status code"""


class SetCacheSettingsRuleActionParametersEdgeTTL(TypedDict, total=False):
    default: Required[int]
    """The TTL (in seconds) if you choose override_origin mode."""

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """edge ttl options"""

    status_code_ttl: Required[Iterable[SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL]]
    """List of single status codes, or status code ranges to apply the selected mode"""


class SetCacheSettingsRuleActionParametersServeStale(TypedDict, total=False):
    disable_stale_while_updating: Required[bool]
    """Defines whether Cloudflare should serve stale content while updating.

    If true, Cloudflare will not serve stale content while getting the latest
    content from the origin.
    """


class SetCacheSettingsRuleActionParameters(TypedDict, total=False):
    additional_cacheable_ports: Iterable[int]
    """List of additional ports that caching can be enabled on."""

    browser_ttl: SetCacheSettingsRuleActionParametersBrowserTTL
    """Specify how long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: bool
    """Mark whether the request’s response from origin is eligible for caching.

    Caching itself will still depend on the cache-control header and your other
    caching configurations.
    """

    cache_key: SetCacheSettingsRuleActionParametersCacheKey
    """
    Define which components of the request are included or excluded from the cache
    key Cloudflare uses to store the response in cache.
    """

    cache_reserve: SetCacheSettingsRuleActionParametersCacheReserve
    """
    Mark whether the request's response from origin is eligible for Cache Reserve
    (requires a Cache Reserve add-on plan).
    """

    edge_ttl: SetCacheSettingsRuleActionParametersEdgeTTL
    """
    TTL (Time to Live) specifies the maximum time to cache a resource in the
    Cloudflare edge network.
    """

    origin_cache_control: bool
    """When enabled, Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: bool
    """Generate Cloudflare error pages from issues sent from the origin server.

    When on, error pages will trigger for issues from the origin
    """

    read_timeout: int
    """
    Define a timeout value between two successive read operations to your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: bool
    """
    Specify whether or not Cloudflare should respect strong ETag (entity tag)
    headers. When off, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: SetCacheSettingsRuleActionParametersServeStale
    """
    Define if Cloudflare should serve stale content while getting the latest content
    from the origin. If on, Cloudflare will not serve stale content while getting
    the latest content from the origin.
    """


class SetCacheSettingsRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class SetCacheSettingsRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SetCacheSettingsRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SetCacheSettingsRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


SetCacheSettingsRulePosition: TypeAlias = Union[
    SetCacheSettingsRulePositionBeforePosition,
    SetCacheSettingsRulePositionAfterPosition,
    SetCacheSettingsRulePositionIndexPosition,
]


class SetCacheSettingsRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class LogCustomFieldRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["log_custom_field"]
    """The action to perform when the rule matches."""

    action_parameters: LogCustomFieldRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: LogCustomFieldRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: LogCustomFieldRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: LogCustomFieldRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class LogCustomFieldRuleActionParametersCookieField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class LogCustomFieldRuleActionParametersRawResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class LogCustomFieldRuleActionParametersRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class LogCustomFieldRuleActionParametersResponseField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class LogCustomFieldRuleActionParametersTransformedRequestField(TypedDict, total=False):
    name: Required[str]
    """The name of the field."""


class LogCustomFieldRuleActionParameters(TypedDict, total=False):
    cookie_fields: Iterable[LogCustomFieldRuleActionParametersCookieField]
    """The cookie fields to log."""

    raw_response_fields: Iterable[LogCustomFieldRuleActionParametersRawResponseField]
    """The raw response fields to log."""

    request_fields: Iterable[LogCustomFieldRuleActionParametersRequestField]
    """The raw request fields to log."""

    response_fields: Iterable[LogCustomFieldRuleActionParametersResponseField]
    """The transformed response fields to log."""

    transformed_request_fields: Iterable[LogCustomFieldRuleActionParametersTransformedRequestField]
    """The transformed request fields to log."""


class LogCustomFieldRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class LogCustomFieldRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class LogCustomFieldRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class LogCustomFieldRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


LogCustomFieldRulePosition: TypeAlias = Union[
    LogCustomFieldRulePositionBeforePosition,
    LogCustomFieldRulePositionAfterPosition,
    LogCustomFieldRulePositionIndexPosition,
]


class LogCustomFieldRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class DDoSDynamicRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["ddos_dynamic"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: DDoSDynamicRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: DDoSDynamicRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: DDoSDynamicRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class DDoSDynamicRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class DDoSDynamicRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class DDoSDynamicRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class DDoSDynamicRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


DDoSDynamicRulePosition: TypeAlias = Union[
    DDoSDynamicRulePositionBeforePosition, DDoSDynamicRulePositionAfterPosition, DDoSDynamicRulePositionIndexPosition
]


class DDoSDynamicRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


class ForceConnectionCloseRule(TypedDict, total=False):
    ruleset_id: Required[str]
    """The unique ID of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["force_connection_close"]
    """The action to perform when the rule matches."""

    action_parameters: object
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ForceConnectionCloseRuleExposedCredentialCheck
    """Configure checks for exposed credentials."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ForceConnectionCloseRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ForceConnectionCloseRuleRatelimit
    """An object configuring the rule's ratelimit behavior."""

    ref: str
    """The reference of the rule (the rule ID by default)."""


class ForceConnectionCloseRuleExposedCredentialCheck(TypedDict, total=False):
    password_expression: Required[str]
    """Expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """Expression that selects the user ID used in the credentials check."""


class ForceConnectionCloseRulePositionBeforePosition(TypedDict, total=False):
    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ForceConnectionCloseRulePositionAfterPosition(TypedDict, total=False):
    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ForceConnectionCloseRulePositionIndexPosition(TypedDict, total=False):
    index: float
    """An index at which to place the rule, where index 1 is the first rule."""


ForceConnectionCloseRulePosition: TypeAlias = Union[
    ForceConnectionCloseRulePositionBeforePosition,
    ForceConnectionCloseRulePositionAfterPosition,
    ForceConnectionCloseRulePositionIndexPosition,
]


class ForceConnectionCloseRuleRatelimit(TypedDict, total=False):
    characteristics: Required[List[str]]
    """
    Characteristics of the request on which the ratelimiter counter will be
    incremented.
    """

    period: Required[Literal[10, 60, 600, 3600]]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """Defines when the ratelimit counter should be incremented.

    It is optional and defaults to the same as the rule's expression.
    """

    mitigation_timeout: int
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: int
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: bool
    """Defines if ratelimit counting is only done when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    The response header name provided by the origin which should contain the score
    to increment ratelimit counter on.
    """


RuleEditParams: TypeAlias = Union[
    BlockRule,
    ChallengeRule,
    CompressionRule,
    ExecuteRule,
    JavascriptChallengeRule,
    LogRule,
    ManagedChallengeRule,
    RedirectRule,
    RewriteRule,
    OriginRule,
    ScoreRule,
    ServeErrorRule,
    SetConfigRule,
    SkipRule,
    SetCacheSettingsRule,
    LogCustomFieldRule,
    DDoSDynamicRule,
    ForceConnectionCloseRule,
]
