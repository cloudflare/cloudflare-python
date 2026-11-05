# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .kind import Kind
from .phase import Phase
from .logging import Logging
from .log_rule import LogRule
from ..._models import BaseModel
from .skip_rule import SkipRule
from .block_rule import BlockRule
from .route_rule import RouteRule
from .score_rule import ScoreRule
from .execute_rule import ExecuteRule
from .rewrite_rule import RewriteRule
from .redirect_rule import RedirectRule
from .set_config_rule import SetConfigRule
from .serve_error_rule import ServeErrorRule
from .ddos_dynamic_rule import DDoSDynamicRule
from .log_custom_field_rule import LogCustomFieldRule
from .compress_response_rule import CompressResponseRule
from .managed_challenge_rule import ManagedChallengeRule
from .set_cache_settings_rule import SetCacheSettingsRule
from .force_connection_close_rule import ForceConnectionCloseRule

__all__ = [
    "RuleDeleteResponse",
    "Ruleset",
    "RulesetRule",
    "RulesetRuleBlockRule",
    "RulesetRuleChallengeRule",
    "RulesetRuleChallengeRuleExposedCredentialCheck",
    "RulesetRuleChallengeRuleRatelimit",
    "RulesetRuleResponseCompressionRule",
    "RulesetRuleDDoSDynamicRule",
    "RulesetRuleExecuteRule",
    "RulesetRuleForceConnectionCloseRule",
    "RulesetRuleJavaScriptChallengeRule",
    "RulesetRuleJavaScriptChallengeRuleExposedCredentialCheck",
    "RulesetRuleJavaScriptChallengeRuleRatelimit",
    "RulesetRuleLogRule",
    "RulesetRuleLogCustomFieldRule",
    "RulesetRuleManagedChallengeRule",
    "RulesetRuleRedirectRule",
    "RulesetRuleRewriteRule",
    "RulesetRuleRouteRule",
    "RulesetRuleScoreRule",
    "RulesetRuleServeErrorRule",
    "RulesetRuleSetCacheControlRule",
    "RulesetRuleSetCacheControlRuleActionParameters",
    "RulesetRuleSetCacheControlRuleActionParametersImmutable",
    "RulesetRuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMaxAge",
    "RulesetRuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMustRevalidate",
    "RulesetRuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMustUnderstand",
    "RulesetRuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoCache",
    "RulesetRuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoStore",
    "RulesetRuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoTransform",
    "RulesetRuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersPrivate",
    "RulesetRuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersProxyRevalidate",
    "RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersPublic",
    "RulesetRuleSetCacheControlRuleActionParametersPublicSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersSMaxage",
    "RulesetRuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersStaleIfError",
    "RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "RulesetRuleSetCacheControlRuleExposedCredentialCheck",
    "RulesetRuleSetCacheControlRuleRatelimit",
    "RulesetRuleSetCacheSettingsRule",
    "RulesetRuleSetCacheTagsRule",
    "RulesetRuleSetCacheTagsRuleActionParameters",
    "RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "RulesetRuleSetCacheTagsRuleExposedCredentialCheck",
    "RulesetRuleSetCacheTagsRuleRatelimit",
    "RulesetRuleSetConfigurationRule",
    "RulesetRuleSkipRule",
    "RulesetRuleTransformResponseHTMLRule",
    "RulesetRuleTransformResponseHTMLRuleActionParameters",
    "RulesetRuleTransformResponseHTMLRuleExposedCredentialCheck",
    "RulesetRuleTransformResponseHTMLRuleRatelimit",
]


class RulesetRuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleChallengeRuleRatelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RulesetRuleChallengeRule(BaseModel):
    id: str
    """The unique ID of the rule."""

    action: Literal["challenge"]
    """The action to perform when the rule matches."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""

    version: str
    """The version of the rule."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[RulesetRuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class RulesetRuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleJavaScriptChallengeRuleRatelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RulesetRuleJavaScriptChallengeRule(BaseModel):
    id: str
    """The unique ID of the rule."""

    action: Literal["js_challenge"]
    """The action to perform when the rule matches."""

    enabled: bool
    """Whether the rule should be executed."""

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""

    version: str
    """The version of the rule."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[RulesetRuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class RulesetRuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersImmutableSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
    """Set the directive with optional qualifiers."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""

    qualifiers: Optional[List[str]] = None
    """
    Optional list of header names to qualify the directive (e.g., for "private" or
    "no-cache" directives).
    """


class RulesetRuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
    """Set the directive with optional qualifiers."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""

    qualifiers: Optional[List[str]] = None
    """
    Optional list of header names to qualify the directive (e.g., for "private" or
    "no-cache" directives).
    """


class RulesetRuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersPrivateSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersPublicSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class RulesetRuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[RulesetRuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[RulesetRuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(alias="max-age", default=None)
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[RulesetRuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[RulesetRuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[RulesetRuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[RulesetRuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[RulesetRuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[RulesetRuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[RulesetRuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[RulesetRuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[RulesetRuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[RulesetRuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[RulesetRuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = FieldInfo(
        alias="stale-while-revalidate", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class RulesetRuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleSetCacheControlRuleRatelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RulesetRuleSetCacheControlRule(BaseModel):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_control"]
    """The action to perform when the rule matches."""

    enabled: bool

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""

    version: str
    """The version of the rule."""

    action_parameters: Optional[RulesetRuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[RulesetRuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class RulesetRuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


RulesetRuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    RulesetRuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    RulesetRuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    RulesetRuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class RulesetRuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleSetCacheTagsRuleRatelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RulesetRuleSetCacheTagsRule(BaseModel):
    id: str
    """The unique ID of the rule."""

    action: Literal["set_cache_tags"]
    """The action to perform when the rule matches."""

    enabled: bool

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""

    version: str
    """The version of the rule."""

    action_parameters: Optional[RulesetRuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[RulesetRuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class RulesetRuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class RulesetRuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class RulesetRuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleTransformResponseHTMLRuleRatelimit(BaseModel):
    """An object configuring the rule's rate limit behavior."""

    characteristics: List[str]
    """
    Characteristics of the request on which the rate limit counter will be
    incremented.
    """

    period: int
    """Period in seconds over which the counter is being incremented."""

    counting_expression: Optional[str] = None
    """An expression that defines when the rate limit counter should be incremented.

    It defaults to the same as the rule's expression.
    """

    mitigation_timeout: Optional[int] = None
    """
    Period of time in seconds after which the action will be disabled following its
    first execution.
    """

    requests_per_period: Optional[int] = None
    """
    The threshold of requests per period after which the action will be executed for
    the first time.
    """

    requests_to_origin: Optional[bool] = None
    """Whether counting is only performed when an origin is reached."""

    score_per_period: Optional[int] = None
    """
    The score threshold per period for which the action will be executed the first
    time.
    """

    score_response_header_name: Optional[str] = None
    """
    A response header name provided by the origin, which contains the score to
    increment rate limit counter with.
    """


class RulesetRuleTransformResponseHTMLRule(BaseModel):
    id: str
    """The unique ID of the rule."""

    action: Literal["transform_response_html"]
    """The action to perform when the rule matches."""

    enabled: bool

    expression: str
    """The expression defining which traffic will match the rule."""

    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    ref: str
    """The reference of the rule (the rule's ID by default)."""

    version: str
    """The version of the rule."""

    action_parameters: Optional[RulesetRuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[RulesetRuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


RulesetRule: TypeAlias = Union[
    RulesetRuleBlockRule,
    RulesetRuleChallengeRule,
    RulesetRuleResponseCompressionRule,
    RulesetRuleDDoSDynamicRule,
    RulesetRuleExecuteRule,
    RulesetRuleForceConnectionCloseRule,
    RulesetRuleJavaScriptChallengeRule,
    RulesetRuleLogRule,
    RulesetRuleLogCustomFieldRule,
    RulesetRuleManagedChallengeRule,
    RulesetRuleRedirectRule,
    RulesetRuleRewriteRule,
    RulesetRuleRouteRule,
    RulesetRuleScoreRule,
    RulesetRuleServeErrorRule,
    RulesetRuleSetCacheControlRule,
    RulesetRuleSetCacheSettingsRule,
    RulesetRuleSetCacheTagsRule,
    RulesetRuleSetConfigurationRule,
    RulesetRuleSkipRule,
    RulesetRuleTransformResponseHTMLRule,
]


class Ruleset(BaseModel):
    """A ruleset object."""

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

    rules: List[RulesetRule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""


RuleDeleteResponse: TypeAlias = Union[List[object], str, float, bool, Ruleset, Optional[object], Optional[object]]
