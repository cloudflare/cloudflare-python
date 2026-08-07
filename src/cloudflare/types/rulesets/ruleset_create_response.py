# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .kind import Kind
from .phase import Phase
from .logging import Logging
from ..._utils import PropertyInfo
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
    "RulesetCreateResponse",
    "Ruleset",
    "RulesetRule",
    "RulesetRuleRulesetsChallengeRule",
    "RulesetRuleRulesetsChallengeRuleExposedCredentialCheck",
    "RulesetRuleRulesetsChallengeRuleRatelimit",
    "RulesetRuleRulesetsJSChallengeRule",
    "RulesetRuleRulesetsJSChallengeRuleExposedCredentialCheck",
    "RulesetRuleRulesetsJSChallengeRuleRatelimit",
    "RulesetRuleRulesetsSetCacheControlRule",
    "RulesetRuleRulesetsSetCacheControlRuleActionParameters",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutable",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAge",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidate",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstand",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCache",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStore",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransform",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivate",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPublic",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxage",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfError",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "RulesetRuleRulesetsSetCacheControlRuleExposedCredentialCheck",
    "RulesetRuleRulesetsSetCacheControlRuleRatelimit",
    "RulesetRuleRulesetsSetCacheTagsRule",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParameters",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "RulesetRuleRulesetsSetCacheTagsRuleExposedCredentialCheck",
    "RulesetRuleRulesetsSetCacheTagsRuleRatelimit",
    "RulesetRuleRulesetsTransformResponseHTMLRule",
    "RulesetRuleRulesetsTransformResponseHTMLRuleActionParameters",
    "RulesetRuleRulesetsTransformResponseHTMLRuleExposedCredentialCheck",
    "RulesetRuleRulesetsTransformResponseHTMLRuleRatelimit",
]


class RulesetRuleRulesetsChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleRulesetsChallengeRuleRatelimit(BaseModel):
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


class RulesetRuleRulesetsChallengeRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["challenge"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RulesetRuleRulesetsChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleRulesetsChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RulesetRuleRulesetsJSChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleRulesetsJSChallengeRuleRatelimit(BaseModel):
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


class RulesetRuleRulesetsJSChallengeRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["js_challenge"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[object] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RulesetRuleRulesetsJSChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleRulesetsJSChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class RulesetRuleRulesetsSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class RulesetRuleRulesetsSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleRulesetsSetCacheControlRuleRatelimit(BaseModel):
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


class RulesetRuleRulesetsSetCacheControlRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_control"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RulesetRuleRulesetsSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RulesetRuleRulesetsSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleRulesetsSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


RulesetRuleRulesetsSetCacheTagsRuleActionParameters: TypeAlias = Union[
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues,
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues,
    RulesetRuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class RulesetRuleRulesetsSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleRulesetsSetCacheTagsRuleRatelimit(BaseModel):
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


class RulesetRuleRulesetsSetCacheTagsRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_tags"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RulesetRuleRulesetsSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RulesetRuleRulesetsSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleRulesetsSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RulesetRuleRulesetsTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class RulesetRuleRulesetsTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RulesetRuleRulesetsTransformResponseHTMLRuleRatelimit(BaseModel):
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


class RulesetRuleRulesetsTransformResponseHTMLRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["transform_response_html"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RulesetRuleRulesetsTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RulesetRuleRulesetsTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RulesetRuleRulesetsTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


RulesetRule: TypeAlias = Annotated[
    Union[
        BlockRule,
        RulesetRuleRulesetsChallengeRule,
        CompressResponseRule,
        DDoSDynamicRule,
        ExecuteRule,
        ForceConnectionCloseRule,
        RulesetRuleRulesetsJSChallengeRule,
        LogRule,
        LogCustomFieldRule,
        ManagedChallengeRule,
        RedirectRule,
        RewriteRule,
        RouteRule,
        ScoreRule,
        ServeErrorRule,
        RulesetRuleRulesetsSetCacheControlRule,
        SetCacheSettingsRule,
        RulesetRuleRulesetsSetCacheTagsRule,
        SetConfigRule,
        SkipRule,
        RulesetRuleRulesetsTransformResponseHTMLRule,
    ],
    PropertyInfo(discriminator="action"),
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


RulesetCreateResponse: TypeAlias = Union[Ruleset, Optional[object]]
