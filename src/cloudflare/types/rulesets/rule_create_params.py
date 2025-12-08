# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .phase import Phase
from ..._types import SequenceNotStr
from .logging_param import LoggingParam

__all__ = [
    "RuleCreateParams",
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
    "ResponseCompressionRule",
    "ResponseCompressionRuleActionParameters",
    "ResponseCompressionRuleActionParametersAlgorithm",
    "ResponseCompressionRuleExposedCredentialCheck",
    "ResponseCompressionRulePosition",
    "ResponseCompressionRulePositionBeforePosition",
    "ResponseCompressionRulePositionAfterPosition",
    "ResponseCompressionRulePositionIndexPosition",
    "ResponseCompressionRuleRatelimit",
    "DDoSDynamicRule",
    "DDoSDynamicRuleExposedCredentialCheck",
    "DDoSDynamicRulePosition",
    "DDoSDynamicRulePositionBeforePosition",
    "DDoSDynamicRulePositionAfterPosition",
    "DDoSDynamicRulePositionIndexPosition",
    "DDoSDynamicRuleRatelimit",
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
    "ForceConnectionCloseRule",
    "ForceConnectionCloseRuleExposedCredentialCheck",
    "ForceConnectionCloseRulePosition",
    "ForceConnectionCloseRulePositionBeforePosition",
    "ForceConnectionCloseRulePositionAfterPosition",
    "ForceConnectionCloseRulePositionIndexPosition",
    "ForceConnectionCloseRuleRatelimit",
    "JavaScriptChallengeRule",
    "JavaScriptChallengeRuleExposedCredentialCheck",
    "JavaScriptChallengeRulePosition",
    "JavaScriptChallengeRulePositionBeforePosition",
    "JavaScriptChallengeRulePositionAfterPosition",
    "JavaScriptChallengeRulePositionIndexPosition",
    "JavaScriptChallengeRuleRatelimit",
    "LogRule",
    "LogRuleExposedCredentialCheck",
    "LogRulePosition",
    "LogRulePositionBeforePosition",
    "LogRulePositionAfterPosition",
    "LogRulePositionIndexPosition",
    "LogRuleRatelimit",
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
    "RedirectRuleExposedCredentialCheck",
    "RedirectRulePosition",
    "RedirectRulePositionBeforePosition",
    "RedirectRulePositionAfterPosition",
    "RedirectRulePositionIndexPosition",
    "RedirectRuleRatelimit",
    "RewriteRule",
    "RewriteRuleActionParameters",
    "RewriteRuleActionParametersHeaders",
    "RewriteRuleActionParametersHeadersAddStaticHeader",
    "RewriteRuleActionParametersHeadersAddDynamicHeader",
    "RewriteRuleActionParametersHeadersSetStaticHeader",
    "RewriteRuleActionParametersHeadersSetDynamicHeader",
    "RewriteRuleActionParametersHeadersRemoveHeader",
    "RewriteRuleActionParametersURI",
    "RewriteRuleActionParametersURIURIPath",
    "RewriteRuleActionParametersURIURIPathPath",
    "RewriteRuleActionParametersURIURIQuery",
    "RewriteRuleActionParametersURIURIQueryQuery",
    "RewriteRuleExposedCredentialCheck",
    "RewriteRulePosition",
    "RewriteRulePositionBeforePosition",
    "RewriteRulePositionAfterPosition",
    "RewriteRulePositionIndexPosition",
    "RewriteRuleRatelimit",
    "RouteRule",
    "RouteRuleActionParameters",
    "RouteRuleActionParametersOrigin",
    "RouteRuleActionParametersSNI",
    "RouteRuleExposedCredentialCheck",
    "RouteRulePosition",
    "RouteRulePositionBeforePosition",
    "RouteRulePositionAfterPosition",
    "RouteRulePositionIndexPosition",
    "RouteRuleRatelimit",
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
    "ServeErrorRuleActionParametersActionParametersContent",
    "ServeErrorRuleActionParametersActionParametersAsset",
    "ServeErrorRuleExposedCredentialCheck",
    "ServeErrorRulePosition",
    "ServeErrorRulePositionBeforePosition",
    "ServeErrorRulePositionAfterPosition",
    "ServeErrorRulePositionIndexPosition",
    "ServeErrorRuleRatelimit",
    "SetCacheSettingsRule",
    "SetCacheSettingsRuleActionParameters",
    "SetCacheSettingsRuleActionParametersBrowserTTL",
    "SetCacheSettingsRuleActionParametersCacheKey",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKey",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude",
    "SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude",
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
    "SetConfigurationRule",
    "SetConfigurationRuleActionParameters",
    "SetConfigurationRuleActionParametersAutominify",
    "SetConfigurationRuleExposedCredentialCheck",
    "SetConfigurationRulePosition",
    "SetConfigurationRulePositionBeforePosition",
    "SetConfigurationRulePositionAfterPosition",
    "SetConfigurationRulePositionIndexPosition",
    "SetConfigurationRuleRatelimit",
    "SkipRule",
    "SkipRuleActionParameters",
    "SkipRuleExposedCredentialCheck",
    "SkipRulePosition",
    "SkipRulePositionBeforePosition",
    "SkipRulePositionAfterPosition",
    "SkipRulePositionIndexPosition",
    "SkipRuleRatelimit",
]


class BlockRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: BlockRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: BlockRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class BlockRuleActionParametersResponse(TypedDict, total=False):
    """The response to show when the block is applied."""

    content: Required[str]
    """The content to return."""

    content_type: Required[str]
    """The type of the content to return."""

    status_code: Required[int]
    """The status code to return."""


class BlockRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    response: BlockRuleActionParametersResponse
    """The response to show when the block is applied."""


class BlockRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class BlockRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class BlockRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class BlockRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


BlockRulePosition: TypeAlias = Union[
    BlockRulePositionBeforePosition, BlockRulePositionAfterPosition, BlockRulePositionIndexPosition
]


class BlockRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ChallengeRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ChallengeRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ChallengeRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ChallengeRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ChallengeRulePosition: TypeAlias = Union[
    ChallengeRulePositionBeforePosition, ChallengeRulePositionAfterPosition, ChallengeRulePositionIndexPosition
]


class ChallengeRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ResponseCompressionRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["compress_response"]
    """The action to perform when the rule matches."""

    action_parameters: ResponseCompressionRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: ResponseCompressionRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ResponseCompressionRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ResponseCompressionRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ResponseCompressionRuleActionParametersAlgorithm(TypedDict, total=False):
    """Compression algorithm to enable."""

    name: Literal["none", "auto", "default", "gzip", "brotli", "zstd"]
    """Name of the compression algorithm to enable."""


class ResponseCompressionRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    algorithms: Required[Iterable[ResponseCompressionRuleActionParametersAlgorithm]]
    """Custom order for compression algorithms."""


class ResponseCompressionRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ResponseCompressionRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ResponseCompressionRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ResponseCompressionRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ResponseCompressionRulePosition: TypeAlias = Union[
    ResponseCompressionRulePositionBeforePosition,
    ResponseCompressionRulePositionAfterPosition,
    ResponseCompressionRulePositionIndexPosition,
]


class ResponseCompressionRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class DDoSDynamicRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: DDoSDynamicRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: DDoSDynamicRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class DDoSDynamicRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class DDoSDynamicRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class DDoSDynamicRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class DDoSDynamicRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


DDoSDynamicRulePosition: TypeAlias = Union[
    DDoSDynamicRulePositionBeforePosition, DDoSDynamicRulePositionAfterPosition, DDoSDynamicRulePositionIndexPosition
]


class DDoSDynamicRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ExecuteRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ExecuteRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ExecuteRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ExecuteRuleActionParametersMatchedData(TypedDict, total=False):
    """The configuration to use for matched data logging."""

    public_key: Required[str]
    """The public key to encrypt matched data logs with."""


class ExecuteRuleActionParametersOverridesCategory(TypedDict, total=False):
    """A category-level override."""

    category: Required[str]
    """The name of the category to override."""

    action: str
    """The action to override rules in the category with."""

    enabled: bool
    """Whether to enable execution of rules in the category."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for rules in the category.

    This option is only applicable for DDoS phases.
    """


class ExecuteRuleActionParametersOverridesRule(TypedDict, total=False):
    """A rule-level override."""

    id: Required[str]
    """The ID of the rule to override."""

    action: str
    """The action to override the rule with."""

    enabled: bool
    """Whether to enable execution of the rule."""

    score_threshold: int
    """The score threshold to use for the rule."""

    sensitivity_level: Literal["default", "medium", "low", "eoff"]
    """The sensitivity level to use for the rule.

    This option is only applicable for DDoS phases.
    """


class ExecuteRuleActionParametersOverrides(TypedDict, total=False):
    """A set of overrides to apply to the target ruleset."""

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
    """The parameters configuring the rule's action."""

    id: Required[str]
    """The ID of the ruleset to execute."""

    matched_data: ExecuteRuleActionParametersMatchedData
    """The configuration to use for matched data logging."""

    overrides: ExecuteRuleActionParametersOverrides
    """A set of overrides to apply to the target ruleset."""


class ExecuteRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ExecuteRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ExecuteRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ExecuteRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ExecuteRulePosition: TypeAlias = Union[
    ExecuteRulePositionBeforePosition, ExecuteRulePositionAfterPosition, ExecuteRulePositionIndexPosition
]


class ExecuteRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ForceConnectionCloseRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ForceConnectionCloseRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ForceConnectionCloseRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ForceConnectionCloseRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ForceConnectionCloseRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ForceConnectionCloseRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ForceConnectionCloseRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ForceConnectionCloseRulePosition: TypeAlias = Union[
    ForceConnectionCloseRulePositionBeforePosition,
    ForceConnectionCloseRulePositionAfterPosition,
    ForceConnectionCloseRulePositionIndexPosition,
]


class ForceConnectionCloseRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class JavaScriptChallengeRule(TypedDict, total=False):
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

    exposed_credential_check: JavaScriptChallengeRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: JavaScriptChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: JavaScriptChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class JavaScriptChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class JavaScriptChallengeRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class JavaScriptChallengeRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class JavaScriptChallengeRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


JavaScriptChallengeRulePosition: TypeAlias = Union[
    JavaScriptChallengeRulePositionBeforePosition,
    JavaScriptChallengeRulePositionAfterPosition,
    JavaScriptChallengeRulePositionIndexPosition,
]


class JavaScriptChallengeRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class LogRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: LogRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: LogRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class LogRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class LogRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class LogRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class LogRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


LogRulePosition: TypeAlias = Union[
    LogRulePositionBeforePosition, LogRulePositionAfterPosition, LogRulePositionIndexPosition
]


class LogRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class LogCustomFieldRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: LogCustomFieldRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: LogCustomFieldRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class LogCustomFieldRuleActionParametersCookieField(TypedDict, total=False):
    """The cookie field to log."""

    name: Required[str]
    """The name of the cookie."""


class LogCustomFieldRuleActionParametersRawResponseField(TypedDict, total=False):
    """The raw response field to log."""

    name: Required[str]
    """The name of the response header."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class LogCustomFieldRuleActionParametersRequestField(TypedDict, total=False):
    """The raw request field to log."""

    name: Required[str]
    """The name of the header."""


class LogCustomFieldRuleActionParametersResponseField(TypedDict, total=False):
    """The transformed response field to log."""

    name: Required[str]
    """The name of the response header."""

    preserve_duplicates: bool
    """Whether to log duplicate values of the same header."""


class LogCustomFieldRuleActionParametersTransformedRequestField(TypedDict, total=False):
    """The transformed request field to log."""

    name: Required[str]
    """The name of the header."""


class LogCustomFieldRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

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
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class LogCustomFieldRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class LogCustomFieldRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class LogCustomFieldRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


LogCustomFieldRulePosition: TypeAlias = Union[
    LogCustomFieldRulePositionBeforePosition,
    LogCustomFieldRulePositionAfterPosition,
    LogCustomFieldRulePositionIndexPosition,
]


class LogCustomFieldRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ManagedChallengeRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ManagedChallengeRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ManagedChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ManagedChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ManagedChallengeRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ManagedChallengeRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ManagedChallengeRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ManagedChallengeRulePosition: TypeAlias = Union[
    ManagedChallengeRulePositionBeforePosition,
    ManagedChallengeRulePositionAfterPosition,
    ManagedChallengeRulePositionIndexPosition,
]


class ManagedChallengeRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RedirectRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: RedirectRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: RedirectRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RedirectRuleActionParametersFromList(TypedDict, total=False):
    """A redirect based on a bulk list lookup."""

    key: Required[str]
    """An expression that evaluates to the list lookup key."""

    name: Required[str]
    """The name of the list to match against."""


class RedirectRuleActionParametersFromValueTargetURL(TypedDict, total=False):
    """A URL to redirect the request to."""

    expression: str
    """An expression that evaluates to a URL to redirect the request to."""

    value: str
    """A URL to redirect the request to."""


class RedirectRuleActionParametersFromValue(TypedDict, total=False):
    """A redirect based on the request properties."""

    target_url: Required[RedirectRuleActionParametersFromValueTargetURL]
    """A URL to redirect the request to."""

    preserve_query_string: bool
    """Whether to keep the query string of the original request."""

    status_code: Literal[301, 302, 303, 307, 308]
    """The status code to use for the redirect."""


class RedirectRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    from_list: RedirectRuleActionParametersFromList
    """A redirect based on a bulk list lookup."""

    from_value: RedirectRuleActionParametersFromValue
    """A redirect based on the request properties."""


class RedirectRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RedirectRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class RedirectRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class RedirectRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


RedirectRulePosition: TypeAlias = Union[
    RedirectRulePositionBeforePosition, RedirectRulePositionAfterPosition, RedirectRulePositionIndexPosition
]


class RedirectRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RewriteRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: RewriteRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: RewriteRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RewriteRuleActionParametersHeadersAddStaticHeader(TypedDict, total=False):
    """A header with a static value to add."""

    operation: Required[Literal["add"]]
    """The operation to perform on the header."""

    value: Required[str]
    """A static value for the header."""


class RewriteRuleActionParametersHeadersAddDynamicHeader(TypedDict, total=False):
    """A header with a dynamic value to add."""

    expression: Required[str]
    """An expression that evaluates to a value for the header."""

    operation: Required[Literal["add"]]
    """The operation to perform on the header."""


class RewriteRuleActionParametersHeadersSetStaticHeader(TypedDict, total=False):
    """A header with a static value to set."""

    operation: Required[Literal["set"]]
    """The operation to perform on the header."""

    value: Required[str]
    """A static value for the header."""


class RewriteRuleActionParametersHeadersSetDynamicHeader(TypedDict, total=False):
    """A header with a dynamic value to set."""

    expression: Required[str]
    """An expression that evaluates to a value for the header."""

    operation: Required[Literal["set"]]
    """The operation to perform on the header."""


class RewriteRuleActionParametersHeadersRemoveHeader(TypedDict, total=False):
    """A header to remove."""

    operation: Required[Literal["remove"]]
    """The operation to perform on the header."""


RewriteRuleActionParametersHeaders: TypeAlias = Union[
    RewriteRuleActionParametersHeadersAddStaticHeader,
    RewriteRuleActionParametersHeadersAddDynamicHeader,
    RewriteRuleActionParametersHeadersSetStaticHeader,
    RewriteRuleActionParametersHeadersSetDynamicHeader,
    RewriteRuleActionParametersHeadersRemoveHeader,
]


class RewriteRuleActionParametersURIURIPathPath(TypedDict, total=False):
    """A URI path rewrite."""

    expression: str
    """An expression that evaluates to a value to rewrite the URI path to."""

    value: str
    """A value to rewrite the URI path to."""


class RewriteRuleActionParametersURIURIPath(TypedDict, total=False):
    """A URI path rewrite."""

    path: Required[RewriteRuleActionParametersURIURIPathPath]
    """A URI path rewrite."""


class RewriteRuleActionParametersURIURIQueryQuery(TypedDict, total=False):
    """A URI query rewrite."""

    expression: str
    """An expression that evaluates to a value to rewrite the URI query to."""

    value: str
    """A value to rewrite the URI query to."""


class RewriteRuleActionParametersURIURIQuery(TypedDict, total=False):
    """A URI query rewrite."""

    query: Required[RewriteRuleActionParametersURIURIQueryQuery]
    """A URI query rewrite."""


RewriteRuleActionParametersURI: TypeAlias = Union[
    RewriteRuleActionParametersURIURIPath, RewriteRuleActionParametersURIURIQuery
]


class RewriteRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    headers: Dict[str, RewriteRuleActionParametersHeaders]
    """A map of headers to rewrite."""

    uri: RewriteRuleActionParametersURI
    """A URI path rewrite."""


class RewriteRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RewriteRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class RewriteRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class RewriteRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


RewriteRulePosition: TypeAlias = Union[
    RewriteRulePositionBeforePosition, RewriteRulePositionAfterPosition, RewriteRulePositionIndexPosition
]


class RewriteRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RouteRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["route"]
    """The action to perform when the rule matches."""

    action_parameters: RouteRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RouteRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: RouteRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: RouteRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RouteRuleActionParametersOrigin(TypedDict, total=False):
    """An origin to route to."""

    host: str
    """A resolved host to route to."""

    port: int
    """A destination port to route to."""


class RouteRuleActionParametersSNI(TypedDict, total=False):
    """A Server Name Indication (SNI) override."""

    value: Required[str]
    """A value to override the SNI to."""


class RouteRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    host_header: str
    """A value to rewrite the HTTP host header to."""

    origin: RouteRuleActionParametersOrigin
    """An origin to route to."""

    sni: RouteRuleActionParametersSNI
    """A Server Name Indication (SNI) override."""


class RouteRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RouteRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class RouteRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class RouteRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


RouteRulePosition: TypeAlias = Union[
    RouteRulePositionBeforePosition, RouteRulePositionAfterPosition, RouteRulePositionIndexPosition
]


class RouteRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ScoreRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ScoreRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ScoreRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ScoreRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    increment: Required[int]
    """A delta to change the score by, which can be either positive or negative."""


class ScoreRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ScoreRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ScoreRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ScoreRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ScoreRulePosition: TypeAlias = Union[
    ScoreRulePositionBeforePosition, ScoreRulePositionAfterPosition, ScoreRulePositionIndexPosition
]


class ScoreRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class ServeErrorRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: ServeErrorRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: ServeErrorRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class ServeErrorRuleActionParametersActionParametersContent(TypedDict, total=False):
    content: Required[str]
    """The response content."""

    content_type: Literal["application/json", "text/html", "text/plain", "text/xml"]
    """The content type header to set with the error response."""

    status_code: int
    """The status code to use for the error."""


class ServeErrorRuleActionParametersActionParametersAsset(TypedDict, total=False):
    asset_name: Required[str]
    """The name of a custom asset to serve as the error response."""

    content_type: Literal["application/json", "text/html", "text/plain", "text/xml"]
    """The content type header to set with the error response."""

    status_code: int
    """The status code to use for the error."""


ServeErrorRuleActionParameters: TypeAlias = Union[
    ServeErrorRuleActionParametersActionParametersContent, ServeErrorRuleActionParametersActionParametersAsset
]


class ServeErrorRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class ServeErrorRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class ServeErrorRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class ServeErrorRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


ServeErrorRulePosition: TypeAlias = Union[
    ServeErrorRulePositionBeforePosition, ServeErrorRulePositionAfterPosition, ServeErrorRulePositionIndexPosition
]


class ServeErrorRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class SetCacheSettingsRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SetCacheSettingsRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SetCacheSettingsRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class SetCacheSettingsRuleActionParametersBrowserTTL(TypedDict, total=False):
    """How long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high browser TTLs may lead to stale content.
    """

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin", "bypass"]]
    """The browser TTL mode."""

    default: int
    """The browser TTL (in seconds) if you choose the "override_origin" mode."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie(TypedDict, total=False):
    """Which cookies to include in the cache key."""

    check_presence: SequenceNotStr[str]
    """A list of cookies to check for the presence of.

    The presence of these cookies is included in the cache key.
    """

    include: SequenceNotStr[str]
    """A list of cookies to include in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader(TypedDict, total=False):
    """Which headers to include in the cache key."""

    check_presence: SequenceNotStr[str]
    """A list of headers to check for the presence of.

    The presence of these headers is included in the cache key.
    """

    contains: Dict[str, SequenceNotStr[str]]
    """A mapping of header names to a list of values.

    If a header is present in the request and contains any of the values provided,
    its value is included in the cache key.
    """

    exclude_origin: bool
    """Whether to exclude the origin header in the cache key."""

    include: SequenceNotStr[str]
    """A list of headers to include in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost(TypedDict, total=False):
    """How to use the host in the cache key."""

    resolved: bool
    """Whether to use the resolved host in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude(TypedDict, total=False):
    """Which query string parameters to exclude from the cache key."""

    all: Literal[True]
    """Whether to exclude all query string parameters from the cache key."""

    list: SequenceNotStr[str]
    """A list of query string parameters to exclude from the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude(TypedDict, total=False):
    """Which query string parameters to include in the cache key."""

    all: Literal[True]
    """Whether to include all query string parameters in the cache key."""

    list: SequenceNotStr[str]
    """A list of query string parameters to include in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString(TypedDict, total=False):
    """Which query string parameters to include in or exclude from the cache key."""

    exclude: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringExclude
    """Which query string parameters to exclude from the cache key."""

    include: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryStringInclude
    """Which query string parameters to include in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser(TypedDict, total=False):
    """How to use characteristics of the request user agent in the cache key."""

    device_type: bool
    """Whether to use the user agent's device type in the cache key."""

    geo: bool
    """Whether to use the user agents's country in the cache key."""

    lang: bool
    """Whether to use the user agent's language in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKeyCustomKey(TypedDict, total=False):
    """Which components of the request are included or excluded from the cache key."""

    cookie: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyCookie
    """Which cookies to include in the cache key."""

    header: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHeader
    """Which headers to include in the cache key."""

    host: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyHost
    """How to use the host in the cache key."""

    query_string: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyQueryString
    """Which query string parameters to include in or exclude from the cache key."""

    user: SetCacheSettingsRuleActionParametersCacheKeyCustomKeyUser
    """How to use characteristics of the request user agent in the cache key."""


class SetCacheSettingsRuleActionParametersCacheKey(TypedDict, total=False):
    """
    Which components of the request are included in or excluded from the cache key Cloudflare uses to store the response in cache.
    """

    cache_by_device_type: bool
    """Whether to separate cached content based on the visitor's device type."""

    cache_deception_armor: bool
    """
    Whether to protect from web cache deception attacks, while allowing static
    assets to be cached.
    """

    custom_key: SetCacheSettingsRuleActionParametersCacheKeyCustomKey
    """Which components of the request are included or excluded from the cache key."""

    ignore_query_strings_order: bool
    """
    Whether to treat requests with the same query parameters the same, regardless of
    the order those query parameters are in.
    """


class SetCacheSettingsRuleActionParametersCacheReserve(TypedDict, total=False):
    """
    Settings to determine whether the request's response from origin is eligible for Cache Reserve (requires a Cache Reserve add-on plan).
    """

    eligible: Required[bool]
    """Whether Cache Reserve is enabled.

    If this is true and a request meets eligibility criteria, Cloudflare will write
    the resource to Cache Reserve.
    """

    minimum_file_size: int
    """The minimum file size eligible for storage in Cache Reserve."""


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
    """A range of status codes to apply the TTL to."""

    to: int
    """The upper bound of the range."""


class SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL(TypedDict, total=False):
    value: Required[int]
    """The time to cache the response for (in seconds).

    A value of 0 is equivalent to setting the cache control header with the value
    "no-cache". A value of -1 is equivalent to setting the cache control header with
    the value of "no-store".
    """

    status_code: int
    """A single status code to apply the TTL to."""

    status_code_range: SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTLStatusCodeRange
    """A range of status codes to apply the TTL to."""


class SetCacheSettingsRuleActionParametersEdgeTTL(TypedDict, total=False):
    """How long the Cloudflare edge network should cache the response."""

    mode: Required[Literal["respect_origin", "bypass_by_default", "override_origin"]]
    """The edge TTL mode."""

    default: int
    """The edge TTL (in seconds) if you choose the "override_origin" mode."""

    status_code_ttl: Iterable[SetCacheSettingsRuleActionParametersEdgeTTLStatusCodeTTL]
    """A list of TTLs to apply to specific status codes or status code ranges."""


class SetCacheSettingsRuleActionParametersServeStale(TypedDict, total=False):
    """When to serve stale content from cache."""

    disable_stale_while_updating: bool
    """
    Whether Cloudflare should disable serving stale content while getting the latest
    content from the origin.
    """


class SetCacheSettingsRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    additional_cacheable_ports: Iterable[int]
    """A list of additional ports that caching should be enabled on."""

    browser_ttl: SetCacheSettingsRuleActionParametersBrowserTTL
    """How long client browsers should cache the response.

    Cloudflare cache purge will not purge content cached on client browsers, so high
    browser TTLs may lead to stale content.
    """

    cache: bool
    """Whether the request's response from the origin is eligible for caching.

    Caching itself will still depend on the cache control header and your other
    caching configurations.
    """

    cache_key: SetCacheSettingsRuleActionParametersCacheKey
    """
    Which components of the request are included in or excluded from the cache key
    Cloudflare uses to store the response in cache.
    """

    cache_reserve: SetCacheSettingsRuleActionParametersCacheReserve
    """
    Settings to determine whether the request's response from origin is eligible for
    Cache Reserve (requires a Cache Reserve add-on plan).
    """

    edge_ttl: SetCacheSettingsRuleActionParametersEdgeTTL
    """How long the Cloudflare edge network should cache the response."""

    origin_cache_control: bool
    """Whether Cloudflare will aim to strictly adhere to RFC 7234."""

    origin_error_page_passthru: bool
    """Whether to generate Cloudflare error pages for issues from the origin server."""

    read_timeout: int
    """
    A timeout value between two successive read operations to use for your origin
    server. Historically, the timeout value between two read options from Cloudflare
    to an origin server is 100 seconds. If you are attempting to reduce HTTP 524
    errors because of timeouts from an origin server, try increasing this timeout
    value.
    """

    respect_strong_etags: bool
    """Whether Cloudflare should respect strong ETag (entity tag) headers.

    If false, Cloudflare converts strong ETag headers to weak ETag headers.
    """

    serve_stale: SetCacheSettingsRuleActionParametersServeStale
    """When to serve stale content from cache."""


class SetCacheSettingsRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class SetCacheSettingsRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SetCacheSettingsRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SetCacheSettingsRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


SetCacheSettingsRulePosition: TypeAlias = Union[
    SetCacheSettingsRulePositionBeforePosition,
    SetCacheSettingsRulePositionAfterPosition,
    SetCacheSettingsRulePositionIndexPosition,
]


class SetCacheSettingsRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class SetConfigurationRule(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    id: str
    """The unique ID of the rule."""

    action: Literal["set_config"]
    """The action to perform when the rule matches."""

    action_parameters: SetConfigurationRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: SetConfigurationRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SetConfigurationRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SetConfigurationRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class SetConfigurationRuleActionParametersAutominify(TypedDict, total=False):
    """Which file extensions to minify automatically."""

    css: bool
    """Whether to minify CSS files."""

    html: bool
    """Whether to minify HTML files."""

    js: bool
    """Whether to minify JavaScript files."""


class SetConfigurationRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    automatic_https_rewrites: bool
    """Whether to enable Automatic HTTPS Rewrites."""

    autominify: SetConfigurationRuleActionParametersAutominify
    """Which file extensions to minify automatically."""

    bic: bool
    """Whether to enable Browser Integrity Check (BIC)."""

    disable_apps: Literal[True]
    """Whether to disable Cloudflare Apps."""

    disable_pay_per_crawl: Literal[True]
    """Whether to disable Pay Per Crawl."""

    disable_rum: Literal[True]
    """Whether to disable Real User Monitoring (RUM)."""

    disable_zaraz: Literal[True]
    """Whether to disable Zaraz."""

    email_obfuscation: bool
    """Whether to enable Email Obfuscation."""

    fonts: bool
    """Whether to enable Cloudflare Fonts."""

    hotlink_protection: bool
    """Whether to enable Hotlink Protection."""

    mirage: bool
    """Whether to enable Mirage."""

    opportunistic_encryption: bool
    """Whether to enable Opportunistic Encryption."""

    polish: Literal["off", "lossless", "lossy", "webp"]
    """The Polish level to configure."""

    rocket_loader: bool
    """Whether to enable Rocket Loader."""

    security_level: Literal["off", "essentially_off", "low", "medium", "high", "under_attack"]
    """The Security Level to configure."""

    server_side_excludes: bool
    """Whether to enable Server-Side Excludes."""

    ssl: Literal["off", "flexible", "full", "strict", "origin_pull"]
    """The SSL level to configure."""

    sxg: bool
    """Whether to enable Signed Exchanges (SXG)."""


class SetConfigurationRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class SetConfigurationRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SetConfigurationRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SetConfigurationRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


SetConfigurationRulePosition: TypeAlias = Union[
    SetConfigurationRulePositionBeforePosition,
    SetConfigurationRulePositionAfterPosition,
    SetConfigurationRulePositionIndexPosition,
]


class SetConfigurationRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class SkipRule(TypedDict, total=False):
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
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    position: SkipRulePosition
    """An object configuring where the rule will be placed."""

    ratelimit: SkipRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class SkipRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    phase: Literal["current"]
    """A phase to skip the execution of.

    This option is only compatible with the products option.
    """

    phases: List[Phase]
    """A list of phases to skip the execution of.

    This option is incompatible with the rulesets option.
    """

    products: List[Literal["bic", "hot", "rateLimit", "securityLevel", "uaBlock", "waf", "zoneLockdown"]]
    """A list of legacy security products to skip the execution of."""

    rules: Dict[str, SequenceNotStr[str]]
    """
    A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the
    execution of. This option is incompatible with the ruleset option.
    """

    ruleset: Literal["current"]
    """A ruleset to skip the execution of.

    This option is incompatible with the rulesets option.
    """

    rulesets: SequenceNotStr[str]
    """A list of ruleset IDs to skip the execution of.

    This option is incompatible with the ruleset and phases options.
    """


class SkipRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class SkipRulePositionBeforePosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    before: str
    """The ID of another rule to place the rule before.

    An empty value causes the rule to be placed at the top.
    """


class SkipRulePositionAfterPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    after: str
    """The ID of another rule to place the rule after.

    An empty value causes the rule to be placed at the bottom.
    """


class SkipRulePositionIndexPosition(TypedDict, total=False):
    """An object configuring where the rule will be placed."""

    index: int
    """An index at which to place the rule, where index 1 is the first rule."""


SkipRulePosition: TypeAlias = Union[
    SkipRulePositionBeforePosition, SkipRulePositionAfterPosition, SkipRulePositionIndexPosition
]


class SkipRuleRatelimit(TypedDict, total=False):
    """An object configuring the rule's rate limit behavior."""

    characteristics: Required[SequenceNotStr[str]]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: Required[int]
    """Period in seconds over which the counter is being incremented."""

    counting_expression: str
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
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
    """Whether counting is only performed when an origin is reached."""

    score_per_period: int
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: str
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


RuleCreateParams: TypeAlias = Union[
    BlockRule,
    ChallengeRule,
    ResponseCompressionRule,
    DDoSDynamicRule,
    ExecuteRule,
    ForceConnectionCloseRule,
    JavaScriptChallengeRule,
    LogRule,
    LogCustomFieldRule,
    ManagedChallengeRule,
    RedirectRule,
    RewriteRule,
    RouteRule,
    ScoreRule,
    ServeErrorRule,
    SetCacheSettingsRule,
    SetConfigurationRule,
    SkipRule,
]
