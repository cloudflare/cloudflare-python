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
    "PhaseGetResponse",
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


class RuleRulesetsChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsChallengeRuleRatelimit(BaseModel):
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


class RuleRulesetsChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[RuleRulesetsChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsJSChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsJSChallengeRuleRatelimit(BaseModel):
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


class RuleRulesetsJSChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[RuleRulesetsJSChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsJSChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersImmutableSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMaxAgeSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class RuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoCacheSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoStoreSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersNoTransformSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class RuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersPrivateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersPublicSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersSMaxageSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class RuleRulesetsSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[RuleRulesetsSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[RuleRulesetsSetCacheControlRuleActionParametersMaxAge] = FieldInfo(alias="max-age", default=None)
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[RuleRulesetsSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[RuleRulesetsSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[RuleRulesetsSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[RuleRulesetsSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[RuleRulesetsSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[RuleRulesetsSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[RuleRulesetsSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[RuleRulesetsSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[RuleRulesetsSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[RuleRulesetsSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[RuleRulesetsSetCacheControlRuleActionParametersStaleWhileRevalidate] = FieldInfo(
        alias="stale-while-revalidate", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class RuleRulesetsSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsSetCacheControlRuleRatelimit(BaseModel):
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


class RuleRulesetsSetCacheControlRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_control"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RuleRulesetsSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


class RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


RuleRulesetsSetCacheTagsRuleActionParameters: TypeAlias = Union[
    RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsValues,
    RuleRulesetsSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class RuleRulesetsSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class RuleRulesetsSetCacheTagsRuleRatelimit(BaseModel):
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


class RuleRulesetsSetCacheTagsRule(BaseModel):
    last_updated: datetime
    """The timestamp of when the rule was last modified."""

    version: str
    """The version of the rule."""

    id: Optional[str] = None
    """The unique ID of the rule."""

    action: Optional[Literal["set_cache_tags"]] = None
    """The action to perform when the rule matches."""

    action_parameters: Optional[RuleRulesetsSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    enabled: Optional[bool] = None
    """Whether the rule should be executed."""

    exposed_credential_check: Optional[RuleRulesetsSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    expression: Optional[str] = None
    """The expression defining which traffic will match the rule."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[RuleRulesetsSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""

    ref: Optional[str] = None
    """The reference of the rule (the rule's ID by default)."""


Rule: TypeAlias = Annotated[
    Union[
        BlockRule,
        RuleRulesetsChallengeRule,
        CompressResponseRule,
        DDoSDynamicRule,
        ExecuteRule,
        ForceConnectionCloseRule,
        RuleRulesetsJSChallengeRule,
        LogRule,
        LogCustomFieldRule,
        ManagedChallengeRule,
        RedirectRule,
        RewriteRule,
        RouteRule,
        ScoreRule,
        ServeErrorRule,
        RuleRulesetsSetCacheControlRule,
        SetCacheSettingsRule,
        RuleRulesetsSetCacheTagsRule,
        SetConfigRule,
        SkipRule,
    ],
    PropertyInfo(discriminator="action"),
]


class PhaseGetResponse(BaseModel):
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

    rules: List[Rule]
    """The list of rules in the ruleset."""

    version: str
    """The version of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""
