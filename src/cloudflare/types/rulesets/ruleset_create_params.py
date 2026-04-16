# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .kind import Kind
from .phase import Phase
from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .logging_param import LoggingParam
from .log_rule_param import LogRuleParam
from .skip_rule_param import SkipRuleParam
from .block_rule_param import BlockRuleParam
from .route_rule_param import RouteRuleParam
from .score_rule_param import ScoreRuleParam
from .execute_rule_param import ExecuteRuleParam
from .rewrite_rule_param import RewriteRuleParam
from .redirect_rule_param import RedirectRuleParam
from .set_config_rule_param import SetConfigRuleParam
from .serve_error_rule_param import ServeErrorRuleParam
from .ddos_dynamic_rule_param import DDoSDynamicRuleParam
from .log_custom_field_rule_param import LogCustomFieldRuleParam
from .compress_response_rule_param import CompressResponseRuleParam
from .managed_challenge_rule_param import ManagedChallengeRuleParam
from .set_cache_settings_rule_param import SetCacheSettingsRuleParam
from .force_connection_close_rule_param import ForceConnectionCloseRuleParam

__all__ = [
    "RulesetCreateParams",
    "Rule",
    "RuleRulesetsChallengeRule",
    "RuleRulesetsChallengeRuleExposedCredentialCheck",
    "RuleRulesetsChallengeRuleRatelimit",
    "RuleRulesetsJSChallengeRule",
    "RuleRulesetsJSChallengeRuleExposedCredentialCheck",
    "RuleRulesetsJSChallengeRuleRatelimit",
    "RuleRulesetsSetCacheControlRule",
    "RuleRulesetsSetCacheControlRuleActionParameters",
    "RuleRulesetsSetCacheControlRuleActionParametersImmutable",
    "RuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMaxAge",
    "RuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMustRevalidate",
    "RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMustUnderstand",
    "RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoCache",
    "RuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoStore",
    "RuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoTransform",
    "RuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersPrivate",
    "RuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate",
    "RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersPublic",
    "RuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersSMaxage",
    "RuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleIfError",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "RuleRulesetsSetCacheControlRuleExposedCredentialCheck",
    "RuleRulesetsSetCacheControlRuleRatelimit",
    "RuleRulesetsSetCacheTagsRule",
    "RuleRulesetsSetCacheTagsRuleActionParameters",
    "RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "RuleRulesetsSetCacheTagsRuleExposedCredentialCheck",
    "RuleRulesetsSetCacheTagsRuleRatelimit",
]


class RulesetCreateParams(TypedDict, total=False):
    kind: Required[Kind]
    """The kind of the ruleset."""

    name: Required[str]
    """The human-readable name of the ruleset."""

    phase: Required[Phase]
    """The phase of the ruleset."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """An informative description of the ruleset."""

    rules: Iterable[Rule]
    """The list of rules in the ruleset."""


class RuleRulesetsChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsChallengeRuleRatelimit(TypedDict, total=False):
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


class RuleRulesetsChallengeRule(TypedDict, total=False):
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

    exposed_credential_check: RuleRulesetsChallengeRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsJSChallengeRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsJSChallengeRuleRatelimit(TypedDict, total=False):
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


class RuleRulesetsJSChallengeRule(TypedDict, total=False):
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

    exposed_credential_check: RuleRulesetsJSChallengeRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsJSChallengeRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective(TypedDict, total=False):
    """Set the directive with a duration value in seconds."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    value: Required[int]
    """The duration value in seconds for the directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective(TypedDict, total=False):
    """Set the directive with optional qualifiers."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""

    qualifiers: SequenceNotStr[str]
    """
    Optional list of header names to qualify the directive (e.g., for "private" or
    "no-cache" directives).
    """


class RuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective(TypedDict, total=False):
    """Set the directive with optional qualifiers."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""

    qualifiers: SequenceNotStr[str]
    """
    Optional list of header names to qualify the directive (e.g., for "private" or
    "no-cache" directives).
    """


class RuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective(TypedDict, total=False):
    """Set the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective(TypedDict, total=False):
    """Set the directive with a duration value in seconds."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    value: Required[int]
    """The duration value in seconds for the directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective(TypedDict, total=False):
    """Set the directive with a duration value in seconds."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    value: Required[int]
    """The duration value in seconds for the directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(TypedDict, total=False):
    """Set the directive with a duration value in seconds."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    value: Required[int]
    """The duration value in seconds for the directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(TypedDict, total=False):
    """Remove the directive."""

    operation: Required[Literal["set", "remove"]]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: bool
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParameters(TypedDict, total=False):
    """The parameters configuring the rule's action."""

    immutable: RuleRulesetsSetCacheControlRuleActionParametersImmutable
    """A cache-control directive configuration."""

    max_age: Annotated[RuleRulesetsSetCacheControlRuleActionParametersMaxAge, PropertyInfo(alias="max-age")]
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersMustRevalidate, PropertyInfo(alias="must-revalidate")
    ]
    """A cache-control directive configuration."""

    must_understand: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersMustUnderstand, PropertyInfo(alias="must-understand")
    ]
    """A cache-control directive configuration."""

    no_cache: Annotated[RuleRulesetsSetCacheControlRuleActionParametersNoCache, PropertyInfo(alias="no-cache")]
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Annotated[RuleRulesetsSetCacheControlRuleActionParametersNoStore, PropertyInfo(alias="no-store")]
    """A cache-control directive configuration."""

    no_transform: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersNoTransform, PropertyInfo(alias="no-transform")
    ]
    """A cache-control directive configuration."""

    private: RuleRulesetsSetCacheControlRuleActionParametersPrivate
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate, PropertyInfo(alias="proxy-revalidate")
    ]
    """A cache-control directive configuration."""

    public: RuleRulesetsSetCacheControlRuleActionParametersPublic
    """A cache-control directive configuration."""

    s_maxage: Annotated[RuleRulesetsSetCacheControlRuleActionParametersSMaxage, PropertyInfo(alias="s-maxage")]
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersStaleIfError, PropertyInfo(alias="stale-if-error")
    ]
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Annotated[
        RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate,
        PropertyInfo(alias="stale-while-revalidate"),
    ]
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class RuleRulesetsSetCacheControlRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsSetCacheControlRuleRatelimit(TypedDict, total=False):
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


class RuleRulesetsSetCacheControlRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_control"]
    """The action to perform when the rule matches."""

    action_parameters: RuleRulesetsSetCacheControlRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RuleRulesetsSetCacheControlRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsSetCacheControlRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues(TypedDict, total=False):
    """Add cache tags using a list of values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""

    values: Required[SequenceNotStr[str]]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression(TypedDict, total=False):
    """Add cache tags using an expression."""

    expression: Required[str]
    """An expression that evaluates to an array of cache tag values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""


class RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues(TypedDict, total=False):
    """Remove cache tags using a list of values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""

    values: Required[SequenceNotStr[str]]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(TypedDict, total=False):
    """Remove cache tags using an expression."""

    expression: Required[str]
    """An expression that evaluates to an array of cache tag values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""


class RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues(TypedDict, total=False):
    """Set cache tags using a list of values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""

    values: Required[SequenceNotStr[str]]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression(TypedDict, total=False):
    """Set cache tags using an expression."""

    expression: Required[str]
    """An expression that evaluates to an array of cache tag values."""

    operation: Required[Literal["add", "remove", "set"]]
    """The operation to perform on the cache tags."""


RuleRulesetsSetCacheTagsRuleActionParameters: TypeAlias = Union[
    RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class RuleRulesetsSetCacheTagsRuleExposedCredentialCheck(TypedDict, total=False):
    """Configuration for exposed credential checking."""

    password_expression: Required[str]
    """An expression that selects the password used in the credentials check."""

    username_expression: Required[str]
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsSetCacheTagsRuleRatelimit(TypedDict, total=False):
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


class RuleRulesetsSetCacheTagsRule(TypedDict, total=False):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_tags"]
    """The action to perform when the rule matches."""

    action_parameters: RuleRulesetsSetCacheTagsRuleActionParameters
    """The parameters configuring the rule's action."""

    description: str
    """An informative description of the rule."""

    enabled: bool
    """Whether the rule should be executed."""

    exposed_credential_check: RuleRulesetsSetCacheTagsRuleExposedCredentialCheck
    """Configuration for exposed credential checking."""

    expression: str
    """The expression defining which traffic will match the rule."""

    logging: LoggingParam
    """An object configuring the rule's logging behavior."""

    ratelimit: RuleRulesetsSetCacheTagsRuleRatelimit
    """An object configuring the rule's rate limit behavior."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""


Rule: TypeAlias = Union[
    BlockRuleParam,
    RuleRulesetsChallengeRule,
    CompressResponseRuleParam,
    DDoSDynamicRuleParam,
    ExecuteRuleParam,
    ForceConnectionCloseRuleParam,
    RuleRulesetsJSChallengeRule,
    LogRuleParam,
    LogCustomFieldRuleParam,
    ManagedChallengeRuleParam,
    RedirectRuleParam,
    RewriteRuleParam,
    RouteRuleParam,
    ScoreRuleParam,
    ServeErrorRuleParam,
    RuleRulesetsSetCacheControlRule,
    SetCacheSettingsRuleParam,
    RuleRulesetsSetCacheTagsRule,
    SetConfigRuleParam,
    SkipRuleParam,
]
