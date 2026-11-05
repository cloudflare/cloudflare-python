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
    "VersionGetResponse",
    "UnionMember0",
    "UnionMember0Rule",
    "UnionMember0RuleBlockRule",
    "UnionMember0RuleChallengeRule",
    "UnionMember0RuleChallengeRuleExposedCredentialCheck",
    "UnionMember0RuleChallengeRuleRatelimit",
    "UnionMember0RuleResponseCompressionRule",
    "UnionMember0RuleDDoSDynamicRule",
    "UnionMember0RuleExecuteRule",
    "UnionMember0RuleForceConnectionCloseRule",
    "UnionMember0RuleJavaScriptChallengeRule",
    "UnionMember0RuleJavaScriptChallengeRuleExposedCredentialCheck",
    "UnionMember0RuleJavaScriptChallengeRuleRatelimit",
    "UnionMember0RuleLogRule",
    "UnionMember0RuleLogCustomFieldRule",
    "UnionMember0RuleManagedChallengeRule",
    "UnionMember0RuleRedirectRule",
    "UnionMember0RuleRewriteRule",
    "UnionMember0RuleRouteRule",
    "UnionMember0RuleScoreRule",
    "UnionMember0RuleServeErrorRule",
    "UnionMember0RuleSetCacheControlRule",
    "UnionMember0RuleSetCacheControlRuleActionParameters",
    "UnionMember0RuleSetCacheControlRuleActionParametersImmutable",
    "UnionMember0RuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMaxAge",
    "UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidate",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstand",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoCache",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoStore",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoTransform",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersPrivate",
    "UnionMember0RuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidate",
    "UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersPublic",
    "UnionMember0RuleSetCacheControlRuleActionParametersPublicSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersSMaxage",
    "UnionMember0RuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleIfError",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "UnionMember0RuleSetCacheControlRuleExposedCredentialCheck",
    "UnionMember0RuleSetCacheControlRuleRatelimit",
    "UnionMember0RuleSetCacheSettingsRule",
    "UnionMember0RuleSetCacheTagsRule",
    "UnionMember0RuleSetCacheTagsRuleActionParameters",
    "UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "UnionMember0RuleSetCacheTagsRuleExposedCredentialCheck",
    "UnionMember0RuleSetCacheTagsRuleRatelimit",
    "UnionMember0RuleSetConfigurationRule",
    "UnionMember0RuleSkipRule",
    "UnionMember0RuleTransformResponseHTMLRule",
    "UnionMember0RuleTransformResponseHTMLRuleActionParameters",
    "UnionMember0RuleTransformResponseHTMLRuleExposedCredentialCheck",
    "UnionMember0RuleTransformResponseHTMLRuleRatelimit",
    "UnionMember1",
    "UnionMember1Rule",
    "UnionMember1RuleBlockRule",
    "UnionMember1RuleChallengeRule",
    "UnionMember1RuleChallengeRuleExposedCredentialCheck",
    "UnionMember1RuleChallengeRuleRatelimit",
    "UnionMember1RuleResponseCompressionRule",
    "UnionMember1RuleDDoSDynamicRule",
    "UnionMember1RuleExecuteRule",
    "UnionMember1RuleForceConnectionCloseRule",
    "UnionMember1RuleJavaScriptChallengeRule",
    "UnionMember1RuleJavaScriptChallengeRuleExposedCredentialCheck",
    "UnionMember1RuleJavaScriptChallengeRuleRatelimit",
    "UnionMember1RuleLogRule",
    "UnionMember1RuleLogCustomFieldRule",
    "UnionMember1RuleManagedChallengeRule",
    "UnionMember1RuleRedirectRule",
    "UnionMember1RuleRewriteRule",
    "UnionMember1RuleRouteRule",
    "UnionMember1RuleScoreRule",
    "UnionMember1RuleServeErrorRule",
    "UnionMember1RuleSetCacheControlRule",
    "UnionMember1RuleSetCacheControlRuleActionParameters",
    "UnionMember1RuleSetCacheControlRuleActionParametersImmutable",
    "UnionMember1RuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMaxAge",
    "UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidate",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstand",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoCache",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoStore",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoTransform",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersPrivate",
    "UnionMember1RuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidate",
    "UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersPublic",
    "UnionMember1RuleSetCacheControlRuleActionParametersPublicSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersSMaxage",
    "UnionMember1RuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleIfError",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "UnionMember1RuleSetCacheControlRuleExposedCredentialCheck",
    "UnionMember1RuleSetCacheControlRuleRatelimit",
    "UnionMember1RuleSetCacheSettingsRule",
    "UnionMember1RuleSetCacheTagsRule",
    "UnionMember1RuleSetCacheTagsRuleActionParameters",
    "UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "UnionMember1RuleSetCacheTagsRuleExposedCredentialCheck",
    "UnionMember1RuleSetCacheTagsRuleRatelimit",
    "UnionMember1RuleSetConfigurationRule",
    "UnionMember1RuleSkipRule",
    "UnionMember1RuleTransformResponseHTMLRule",
    "UnionMember1RuleTransformResponseHTMLRuleActionParameters",
    "UnionMember1RuleTransformResponseHTMLRuleExposedCredentialCheck",
    "UnionMember1RuleTransformResponseHTMLRuleRatelimit",
    "UnionMember2",
    "UnionMember2Rule",
    "UnionMember2RuleBlockRule",
    "UnionMember2RuleChallengeRule",
    "UnionMember2RuleChallengeRuleExposedCredentialCheck",
    "UnionMember2RuleChallengeRuleRatelimit",
    "UnionMember2RuleResponseCompressionRule",
    "UnionMember2RuleDDoSDynamicRule",
    "UnionMember2RuleExecuteRule",
    "UnionMember2RuleForceConnectionCloseRule",
    "UnionMember2RuleJavaScriptChallengeRule",
    "UnionMember2RuleJavaScriptChallengeRuleExposedCredentialCheck",
    "UnionMember2RuleJavaScriptChallengeRuleRatelimit",
    "UnionMember2RuleLogRule",
    "UnionMember2RuleLogCustomFieldRule",
    "UnionMember2RuleManagedChallengeRule",
    "UnionMember2RuleRedirectRule",
    "UnionMember2RuleRewriteRule",
    "UnionMember2RuleRouteRule",
    "UnionMember2RuleScoreRule",
    "UnionMember2RuleServeErrorRule",
    "UnionMember2RuleSetCacheControlRule",
    "UnionMember2RuleSetCacheControlRuleActionParameters",
    "UnionMember2RuleSetCacheControlRuleActionParametersImmutable",
    "UnionMember2RuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMaxAge",
    "UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidate",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstand",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoCache",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoStore",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoTransform",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersPrivate",
    "UnionMember2RuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidate",
    "UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersPublic",
    "UnionMember2RuleSetCacheControlRuleActionParametersPublicSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersSMaxage",
    "UnionMember2RuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleIfError",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "UnionMember2RuleSetCacheControlRuleExposedCredentialCheck",
    "UnionMember2RuleSetCacheControlRuleRatelimit",
    "UnionMember2RuleSetCacheSettingsRule",
    "UnionMember2RuleSetCacheTagsRule",
    "UnionMember2RuleSetCacheTagsRuleActionParameters",
    "UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "UnionMember2RuleSetCacheTagsRuleExposedCredentialCheck",
    "UnionMember2RuleSetCacheTagsRuleRatelimit",
    "UnionMember2RuleSetConfigurationRule",
    "UnionMember2RuleSkipRule",
    "UnionMember2RuleTransformResponseHTMLRule",
    "UnionMember2RuleTransformResponseHTMLRuleActionParameters",
    "UnionMember2RuleTransformResponseHTMLRuleExposedCredentialCheck",
    "UnionMember2RuleTransformResponseHTMLRuleRatelimit",
    "UnionMember3",
    "UnionMember3Rule",
    "UnionMember3RuleBlockRule",
    "UnionMember3RuleChallengeRule",
    "UnionMember3RuleChallengeRuleExposedCredentialCheck",
    "UnionMember3RuleChallengeRuleRatelimit",
    "UnionMember3RuleResponseCompressionRule",
    "UnionMember3RuleDDoSDynamicRule",
    "UnionMember3RuleExecuteRule",
    "UnionMember3RuleForceConnectionCloseRule",
    "UnionMember3RuleJavaScriptChallengeRule",
    "UnionMember3RuleJavaScriptChallengeRuleExposedCredentialCheck",
    "UnionMember3RuleJavaScriptChallengeRuleRatelimit",
    "UnionMember3RuleLogRule",
    "UnionMember3RuleLogCustomFieldRule",
    "UnionMember3RuleManagedChallengeRule",
    "UnionMember3RuleRedirectRule",
    "UnionMember3RuleRewriteRule",
    "UnionMember3RuleRouteRule",
    "UnionMember3RuleScoreRule",
    "UnionMember3RuleServeErrorRule",
    "UnionMember3RuleSetCacheControlRule",
    "UnionMember3RuleSetCacheControlRuleActionParameters",
    "UnionMember3RuleSetCacheControlRuleActionParametersImmutable",
    "UnionMember3RuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMaxAge",
    "UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidate",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstand",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoCache",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoStore",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoTransform",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersPrivate",
    "UnionMember3RuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidate",
    "UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersPublic",
    "UnionMember3RuleSetCacheControlRuleActionParametersPublicSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersSMaxage",
    "UnionMember3RuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleIfError",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "UnionMember3RuleSetCacheControlRuleExposedCredentialCheck",
    "UnionMember3RuleSetCacheControlRuleRatelimit",
    "UnionMember3RuleSetCacheSettingsRule",
    "UnionMember3RuleSetCacheTagsRule",
    "UnionMember3RuleSetCacheTagsRuleActionParameters",
    "UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "UnionMember3RuleSetCacheTagsRuleExposedCredentialCheck",
    "UnionMember3RuleSetCacheTagsRuleRatelimit",
    "UnionMember3RuleSetConfigurationRule",
    "UnionMember3RuleSkipRule",
    "UnionMember3RuleTransformResponseHTMLRule",
    "UnionMember3RuleTransformResponseHTMLRuleActionParameters",
    "UnionMember3RuleTransformResponseHTMLRuleExposedCredentialCheck",
    "UnionMember3RuleTransformResponseHTMLRuleRatelimit",
    "UnionMember4",
    "UnionMember4Rule",
    "UnionMember4RuleBlockRule",
    "UnionMember4RuleChallengeRule",
    "UnionMember4RuleChallengeRuleExposedCredentialCheck",
    "UnionMember4RuleChallengeRuleRatelimit",
    "UnionMember4RuleResponseCompressionRule",
    "UnionMember4RuleDDoSDynamicRule",
    "UnionMember4RuleExecuteRule",
    "UnionMember4RuleForceConnectionCloseRule",
    "UnionMember4RuleJavaScriptChallengeRule",
    "UnionMember4RuleJavaScriptChallengeRuleExposedCredentialCheck",
    "UnionMember4RuleJavaScriptChallengeRuleRatelimit",
    "UnionMember4RuleLogRule",
    "UnionMember4RuleLogCustomFieldRule",
    "UnionMember4RuleManagedChallengeRule",
    "UnionMember4RuleRedirectRule",
    "UnionMember4RuleRewriteRule",
    "UnionMember4RuleRouteRule",
    "UnionMember4RuleScoreRule",
    "UnionMember4RuleServeErrorRule",
    "UnionMember4RuleSetCacheControlRule",
    "UnionMember4RuleSetCacheControlRuleActionParameters",
    "UnionMember4RuleSetCacheControlRuleActionParametersImmutable",
    "UnionMember4RuleSetCacheControlRuleActionParametersImmutableSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersImmutableRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMaxAge",
    "UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidate",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstand",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoCache",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoCacheSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoStore",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoStoreSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoTransform",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoTransformSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersPrivate",
    "UnionMember4RuleSetCacheControlRuleActionParametersPrivateSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersPrivateRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidate",
    "UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersPublic",
    "UnionMember4RuleSetCacheControlRuleActionParametersPublicSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersPublicRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersSMaxage",
    "UnionMember4RuleSetCacheControlRuleActionParametersSMaxageSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleIfError",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidate",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective",
    "UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective",
    "UnionMember4RuleSetCacheControlRuleExposedCredentialCheck",
    "UnionMember4RuleSetCacheControlRuleRatelimit",
    "UnionMember4RuleSetCacheSettingsRule",
    "UnionMember4RuleSetCacheTagsRule",
    "UnionMember4RuleSetCacheTagsRuleActionParameters",
    "UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsValues",
    "UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression",
    "UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues",
    "UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression",
    "UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsValues",
    "UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression",
    "UnionMember4RuleSetCacheTagsRuleExposedCredentialCheck",
    "UnionMember4RuleSetCacheTagsRuleRatelimit",
    "UnionMember4RuleSetConfigurationRule",
    "UnionMember4RuleSkipRule",
    "UnionMember4RuleTransformResponseHTMLRule",
    "UnionMember4RuleTransformResponseHTMLRuleActionParameters",
    "UnionMember4RuleTransformResponseHTMLRuleExposedCredentialCheck",
    "UnionMember4RuleTransformResponseHTMLRuleRatelimit",
]


class UnionMember0RuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember0RuleChallengeRuleRatelimit(BaseModel):
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


class UnionMember0RuleChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember0RuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember0RuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember0RuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember0RuleJavaScriptChallengeRuleRatelimit(BaseModel):
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


class UnionMember0RuleJavaScriptChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember0RuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember0RuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember0RuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersImmutableSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class UnionMember0RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class UnionMember0RuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersPrivateSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersPublicSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class UnionMember0RuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[UnionMember0RuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[UnionMember0RuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[UnionMember0RuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[UnionMember0RuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[UnionMember0RuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[UnionMember0RuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[UnionMember0RuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[UnionMember0RuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[UnionMember0RuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[UnionMember0RuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[UnionMember0RuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[UnionMember0RuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[UnionMember0RuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class UnionMember0RuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember0RuleSetCacheControlRuleRatelimit(BaseModel):
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


class UnionMember0RuleSetCacheControlRule(BaseModel):
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

    action_parameters: Optional[UnionMember0RuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember0RuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember0RuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember0RuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


UnionMember0RuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    UnionMember0RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    UnionMember0RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    UnionMember0RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class UnionMember0RuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember0RuleSetCacheTagsRuleRatelimit(BaseModel):
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


class UnionMember0RuleSetCacheTagsRule(BaseModel):
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

    action_parameters: Optional[UnionMember0RuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember0RuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember0RuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember0RuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember0RuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class UnionMember0RuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember0RuleTransformResponseHTMLRuleRatelimit(BaseModel):
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


class UnionMember0RuleTransformResponseHTMLRule(BaseModel):
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

    action_parameters: Optional[UnionMember0RuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember0RuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember0RuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


UnionMember0Rule: TypeAlias = Union[
    UnionMember0RuleBlockRule,
    UnionMember0RuleChallengeRule,
    UnionMember0RuleResponseCompressionRule,
    UnionMember0RuleDDoSDynamicRule,
    UnionMember0RuleExecuteRule,
    UnionMember0RuleForceConnectionCloseRule,
    UnionMember0RuleJavaScriptChallengeRule,
    UnionMember0RuleLogRule,
    UnionMember0RuleLogCustomFieldRule,
    UnionMember0RuleManagedChallengeRule,
    UnionMember0RuleRedirectRule,
    UnionMember0RuleRewriteRule,
    UnionMember0RuleRouteRule,
    UnionMember0RuleScoreRule,
    UnionMember0RuleServeErrorRule,
    UnionMember0RuleSetCacheControlRule,
    UnionMember0RuleSetCacheSettingsRule,
    UnionMember0RuleSetCacheTagsRule,
    UnionMember0RuleSetConfigurationRule,
    UnionMember0RuleSkipRule,
    UnionMember0RuleTransformResponseHTMLRule,
]


class UnionMember0(BaseModel):
    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""

    rules: Optional[List[UnionMember0Rule]] = None
    """The list of rules in the ruleset."""

    version: Optional[str] = None
    """The version of the ruleset."""


class UnionMember1RuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember1RuleChallengeRuleRatelimit(BaseModel):
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


class UnionMember1RuleChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember1RuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember1RuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember1RuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember1RuleJavaScriptChallengeRuleRatelimit(BaseModel):
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


class UnionMember1RuleJavaScriptChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember1RuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember1RuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember1RuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersImmutableSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class UnionMember1RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class UnionMember1RuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersPrivateSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersPublicSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class UnionMember1RuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[UnionMember1RuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[UnionMember1RuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[UnionMember1RuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[UnionMember1RuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[UnionMember1RuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[UnionMember1RuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[UnionMember1RuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[UnionMember1RuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[UnionMember1RuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[UnionMember1RuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[UnionMember1RuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[UnionMember1RuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[UnionMember1RuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class UnionMember1RuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember1RuleSetCacheControlRuleRatelimit(BaseModel):
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


class UnionMember1RuleSetCacheControlRule(BaseModel):
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

    action_parameters: Optional[UnionMember1RuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember1RuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember1RuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember1RuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


UnionMember1RuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    UnionMember1RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    UnionMember1RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    UnionMember1RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class UnionMember1RuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember1RuleSetCacheTagsRuleRatelimit(BaseModel):
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


class UnionMember1RuleSetCacheTagsRule(BaseModel):
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

    action_parameters: Optional[UnionMember1RuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember1RuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember1RuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember1RuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember1RuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class UnionMember1RuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember1RuleTransformResponseHTMLRuleRatelimit(BaseModel):
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


class UnionMember1RuleTransformResponseHTMLRule(BaseModel):
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

    action_parameters: Optional[UnionMember1RuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember1RuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember1RuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


UnionMember1Rule: TypeAlias = Union[
    UnionMember1RuleBlockRule,
    UnionMember1RuleChallengeRule,
    UnionMember1RuleResponseCompressionRule,
    UnionMember1RuleDDoSDynamicRule,
    UnionMember1RuleExecuteRule,
    UnionMember1RuleForceConnectionCloseRule,
    UnionMember1RuleJavaScriptChallengeRule,
    UnionMember1RuleLogRule,
    UnionMember1RuleLogCustomFieldRule,
    UnionMember1RuleManagedChallengeRule,
    UnionMember1RuleRedirectRule,
    UnionMember1RuleRewriteRule,
    UnionMember1RuleRouteRule,
    UnionMember1RuleScoreRule,
    UnionMember1RuleServeErrorRule,
    UnionMember1RuleSetCacheControlRule,
    UnionMember1RuleSetCacheSettingsRule,
    UnionMember1RuleSetCacheTagsRule,
    UnionMember1RuleSetConfigurationRule,
    UnionMember1RuleSkipRule,
    UnionMember1RuleTransformResponseHTMLRule,
]


class UnionMember1(BaseModel):
    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""

    rules: Optional[List[UnionMember1Rule]] = None
    """The list of rules in the ruleset."""

    version: Optional[str] = None
    """The version of the ruleset."""


class UnionMember2RuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember2RuleChallengeRuleRatelimit(BaseModel):
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


class UnionMember2RuleChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember2RuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember2RuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember2RuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember2RuleJavaScriptChallengeRuleRatelimit(BaseModel):
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


class UnionMember2RuleJavaScriptChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember2RuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember2RuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember2RuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersImmutableSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class UnionMember2RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class UnionMember2RuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersPrivateSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersPublicSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class UnionMember2RuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[UnionMember2RuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[UnionMember2RuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[UnionMember2RuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[UnionMember2RuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[UnionMember2RuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[UnionMember2RuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[UnionMember2RuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[UnionMember2RuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[UnionMember2RuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[UnionMember2RuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[UnionMember2RuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[UnionMember2RuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[UnionMember2RuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class UnionMember2RuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember2RuleSetCacheControlRuleRatelimit(BaseModel):
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


class UnionMember2RuleSetCacheControlRule(BaseModel):
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

    action_parameters: Optional[UnionMember2RuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember2RuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember2RuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember2RuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


UnionMember2RuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    UnionMember2RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    UnionMember2RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    UnionMember2RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class UnionMember2RuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember2RuleSetCacheTagsRuleRatelimit(BaseModel):
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


class UnionMember2RuleSetCacheTagsRule(BaseModel):
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

    action_parameters: Optional[UnionMember2RuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember2RuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember2RuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember2RuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember2RuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class UnionMember2RuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember2RuleTransformResponseHTMLRuleRatelimit(BaseModel):
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


class UnionMember2RuleTransformResponseHTMLRule(BaseModel):
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

    action_parameters: Optional[UnionMember2RuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember2RuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember2RuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


UnionMember2Rule: TypeAlias = Union[
    UnionMember2RuleBlockRule,
    UnionMember2RuleChallengeRule,
    UnionMember2RuleResponseCompressionRule,
    UnionMember2RuleDDoSDynamicRule,
    UnionMember2RuleExecuteRule,
    UnionMember2RuleForceConnectionCloseRule,
    UnionMember2RuleJavaScriptChallengeRule,
    UnionMember2RuleLogRule,
    UnionMember2RuleLogCustomFieldRule,
    UnionMember2RuleManagedChallengeRule,
    UnionMember2RuleRedirectRule,
    UnionMember2RuleRewriteRule,
    UnionMember2RuleRouteRule,
    UnionMember2RuleScoreRule,
    UnionMember2RuleServeErrorRule,
    UnionMember2RuleSetCacheControlRule,
    UnionMember2RuleSetCacheSettingsRule,
    UnionMember2RuleSetCacheTagsRule,
    UnionMember2RuleSetConfigurationRule,
    UnionMember2RuleSkipRule,
    UnionMember2RuleTransformResponseHTMLRule,
]


class UnionMember2(BaseModel):
    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""

    rules: Optional[List[UnionMember2Rule]] = None
    """The list of rules in the ruleset."""

    version: Optional[str] = None
    """The version of the ruleset."""


class UnionMember3RuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember3RuleChallengeRuleRatelimit(BaseModel):
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


class UnionMember3RuleChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember3RuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember3RuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember3RuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember3RuleJavaScriptChallengeRuleRatelimit(BaseModel):
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


class UnionMember3RuleJavaScriptChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember3RuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember3RuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember3RuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersImmutableSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class UnionMember3RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class UnionMember3RuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersPrivateSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersPublicSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class UnionMember3RuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[UnionMember3RuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[UnionMember3RuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[UnionMember3RuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[UnionMember3RuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[UnionMember3RuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[UnionMember3RuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[UnionMember3RuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[UnionMember3RuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[UnionMember3RuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[UnionMember3RuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[UnionMember3RuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[UnionMember3RuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[UnionMember3RuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class UnionMember3RuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember3RuleSetCacheControlRuleRatelimit(BaseModel):
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


class UnionMember3RuleSetCacheControlRule(BaseModel):
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

    action_parameters: Optional[UnionMember3RuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember3RuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember3RuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember3RuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


UnionMember3RuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    UnionMember3RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    UnionMember3RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    UnionMember3RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class UnionMember3RuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember3RuleSetCacheTagsRuleRatelimit(BaseModel):
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


class UnionMember3RuleSetCacheTagsRule(BaseModel):
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

    action_parameters: Optional[UnionMember3RuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember3RuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember3RuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember3RuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember3RuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class UnionMember3RuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember3RuleTransformResponseHTMLRuleRatelimit(BaseModel):
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


class UnionMember3RuleTransformResponseHTMLRule(BaseModel):
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

    action_parameters: Optional[UnionMember3RuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember3RuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember3RuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


UnionMember3Rule: TypeAlias = Union[
    UnionMember3RuleBlockRule,
    UnionMember3RuleChallengeRule,
    UnionMember3RuleResponseCompressionRule,
    UnionMember3RuleDDoSDynamicRule,
    UnionMember3RuleExecuteRule,
    UnionMember3RuleForceConnectionCloseRule,
    UnionMember3RuleJavaScriptChallengeRule,
    UnionMember3RuleLogRule,
    UnionMember3RuleLogCustomFieldRule,
    UnionMember3RuleManagedChallengeRule,
    UnionMember3RuleRedirectRule,
    UnionMember3RuleRewriteRule,
    UnionMember3RuleRouteRule,
    UnionMember3RuleScoreRule,
    UnionMember3RuleServeErrorRule,
    UnionMember3RuleSetCacheControlRule,
    UnionMember3RuleSetCacheSettingsRule,
    UnionMember3RuleSetCacheTagsRule,
    UnionMember3RuleSetConfigurationRule,
    UnionMember3RuleSkipRule,
    UnionMember3RuleTransformResponseHTMLRule,
]


class UnionMember3(BaseModel):
    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""

    rules: Optional[List[UnionMember3Rule]] = None
    """The list of rules in the ruleset."""

    version: Optional[str] = None
    """The version of the ruleset."""


class UnionMember4RuleBlockRule(BlockRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember4RuleChallengeRuleRatelimit(BaseModel):
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


class UnionMember4RuleChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember4RuleChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember4RuleChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember4RuleResponseCompressionRule(CompressResponseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleDDoSDynamicRule(DDoSDynamicRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleExecuteRule(ExecuteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleForceConnectionCloseRule(ForceConnectionCloseRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleJavaScriptChallengeRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember4RuleJavaScriptChallengeRuleRatelimit(BaseModel):
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


class UnionMember4RuleJavaScriptChallengeRule(BaseModel):
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

    exposed_credential_check: Optional[UnionMember4RuleJavaScriptChallengeRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember4RuleJavaScriptChallengeRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember4RuleLogRule(LogRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleLogCustomFieldRule(LogCustomFieldRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleManagedChallengeRule(ManagedChallengeRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleRedirectRule(RedirectRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleRewriteRule(RewriteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleRouteRule(RouteRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleScoreRule(ScoreRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleServeErrorRule(ServeErrorRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleSetCacheControlRuleActionParametersImmutableSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersImmutableRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersImmutable: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersImmutableSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersImmutableRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersMaxAge: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersMaxAgeRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidate: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidateRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstand: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstandRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersNoCacheSetDirective(BaseModel):
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


class UnionMember4RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersNoCache: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersNoCacheSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersNoCacheRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersNoStoreSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersNoStore: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersNoStoreSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersNoStoreRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersNoTransformSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersNoTransform: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersNoTransformSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersNoTransformRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersPrivateSetDirective(BaseModel):
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


class UnionMember4RuleSetCacheControlRuleActionParametersPrivateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersPrivate: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersPrivateSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersPrivateRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidate: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidateRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersPublicSetDirective(BaseModel):
    """Set the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersPublicRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersPublic: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersPublicSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersPublicRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersSMaxageSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersSMaxage: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersSMaxageSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersSMaxageRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersStaleIfError: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersStaleIfErrorRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective(BaseModel):
    """Set the directive with a duration value in seconds."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    value: int
    """The duration value in seconds for the directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


class UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective(BaseModel):
    """Remove the directive."""

    operation: Literal["set", "remove"]
    """The operation to perform on the cache-control directive."""

    cloudflare_only: Optional[bool] = None
    """Whether the directive should only be applied to the Cloudflare CDN cache."""


UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidate: TypeAlias = Union[
    UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateSetDirective,
    UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidateRemoveDirective,
]


class UnionMember4RuleSetCacheControlRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    immutable: Optional[UnionMember4RuleSetCacheControlRuleActionParametersImmutable] = None
    """A cache-control directive configuration."""

    max_age: Optional[UnionMember4RuleSetCacheControlRuleActionParametersMaxAge] = FieldInfo(
        alias="max-age", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    must_revalidate: Optional[UnionMember4RuleSetCacheControlRuleActionParametersMustRevalidate] = FieldInfo(
        alias="must-revalidate", default=None
    )
    """A cache-control directive configuration."""

    must_understand: Optional[UnionMember4RuleSetCacheControlRuleActionParametersMustUnderstand] = FieldInfo(
        alias="must-understand", default=None
    )
    """A cache-control directive configuration."""

    no_cache: Optional[UnionMember4RuleSetCacheControlRuleActionParametersNoCache] = FieldInfo(
        alias="no-cache", default=None
    )
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    no_store: Optional[UnionMember4RuleSetCacheControlRuleActionParametersNoStore] = FieldInfo(
        alias="no-store", default=None
    )
    """A cache-control directive configuration."""

    no_transform: Optional[UnionMember4RuleSetCacheControlRuleActionParametersNoTransform] = FieldInfo(
        alias="no-transform", default=None
    )
    """A cache-control directive configuration."""

    private: Optional[UnionMember4RuleSetCacheControlRuleActionParametersPrivate] = None
    """
    A cache-control directive configuration that accepts optional qualifiers (header
    names).
    """

    proxy_revalidate: Optional[UnionMember4RuleSetCacheControlRuleActionParametersProxyRevalidate] = FieldInfo(
        alias="proxy-revalidate", default=None
    )
    """A cache-control directive configuration."""

    public: Optional[UnionMember4RuleSetCacheControlRuleActionParametersPublic] = None
    """A cache-control directive configuration."""

    s_maxage: Optional[UnionMember4RuleSetCacheControlRuleActionParametersSMaxage] = FieldInfo(
        alias="s-maxage", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_if_error: Optional[UnionMember4RuleSetCacheControlRuleActionParametersStaleIfError] = FieldInfo(
        alias="stale-if-error", default=None
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """

    stale_while_revalidate: Optional[UnionMember4RuleSetCacheControlRuleActionParametersStaleWhileRevalidate] = (
        FieldInfo(alias="stale-while-revalidate", default=None)
    )
    """
    A cache-control directive configuration that accepts a duration value in
    seconds.
    """


class UnionMember4RuleSetCacheControlRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember4RuleSetCacheControlRuleRatelimit(BaseModel):
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


class UnionMember4RuleSetCacheControlRule(BaseModel):
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

    action_parameters: Optional[UnionMember4RuleSetCacheControlRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember4RuleSetCacheControlRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember4RuleSetCacheControlRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember4RuleSetCacheSettingsRule(SetCacheSettingsRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsValues(BaseModel):
    """Add cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression(BaseModel):
    """Add cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues(BaseModel):
    """Remove cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression(BaseModel):
    """Remove cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


class UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsValues(BaseModel):
    """Set cache tags using a list of values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""

    values: List[str]
    """A list of cache tag values."""


class UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression(BaseModel):
    """Set cache tags using an expression."""

    expression: str
    """An expression that evaluates to an array of cache tag values."""

    operation: Literal["add", "remove", "set"]
    """The operation to perform on the cache tags."""


UnionMember4RuleSetCacheTagsRuleActionParameters: TypeAlias = Union[
    UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsValues,
    UnionMember4RuleSetCacheTagsRuleActionParametersAddCacheTagsExpression,
    UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsValues,
    UnionMember4RuleSetCacheTagsRuleActionParametersRemoveCacheTagsExpression,
    UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsValues,
    UnionMember4RuleSetCacheTagsRuleActionParametersSetCacheTagsExpression,
]


class UnionMember4RuleSetCacheTagsRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember4RuleSetCacheTagsRuleRatelimit(BaseModel):
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


class UnionMember4RuleSetCacheTagsRule(BaseModel):
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

    action_parameters: Optional[UnionMember4RuleSetCacheTagsRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember4RuleSetCacheTagsRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember4RuleSetCacheTagsRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


class UnionMember4RuleSetConfigurationRule(SetConfigRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleSkipRule(SkipRule):
    id: str  # type: ignore

    action: str  # type: ignore

    enabled: bool  # type: ignore

    expression: str  # type: ignore

    ref: str  # type: ignore


class UnionMember4RuleTransformResponseHTMLRuleActionParameters(BaseModel):
    """The parameters configuring the rule's action."""

    link_maze: object
    """Enables the link maze transformation on the response."""


class UnionMember4RuleTransformResponseHTMLRuleExposedCredentialCheck(BaseModel):
    """Configuration for exposed credential checking."""

    password_expression: str
    """An expression that selects the password used in the credentials check."""

    username_expression: str
    """An expression that selects the user ID used in the credentials check."""


class UnionMember4RuleTransformResponseHTMLRuleRatelimit(BaseModel):
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


class UnionMember4RuleTransformResponseHTMLRule(BaseModel):
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

    action_parameters: Optional[UnionMember4RuleTransformResponseHTMLRuleActionParameters] = None
    """The parameters configuring the rule's action."""

    categories: Optional[List[str]] = None
    """The categories of the rule."""

    description: Optional[str] = None
    """An informative description of the rule."""

    exposed_credential_check: Optional[UnionMember4RuleTransformResponseHTMLRuleExposedCredentialCheck] = None
    """Configuration for exposed credential checking."""

    logging: Optional[Logging] = None
    """An object configuring the rule's logging behavior."""

    ratelimit: Optional[UnionMember4RuleTransformResponseHTMLRuleRatelimit] = None
    """An object configuring the rule's rate limit behavior."""


UnionMember4Rule: TypeAlias = Union[
    UnionMember4RuleBlockRule,
    UnionMember4RuleChallengeRule,
    UnionMember4RuleResponseCompressionRule,
    UnionMember4RuleDDoSDynamicRule,
    UnionMember4RuleExecuteRule,
    UnionMember4RuleForceConnectionCloseRule,
    UnionMember4RuleJavaScriptChallengeRule,
    UnionMember4RuleLogRule,
    UnionMember4RuleLogCustomFieldRule,
    UnionMember4RuleManagedChallengeRule,
    UnionMember4RuleRedirectRule,
    UnionMember4RuleRewriteRule,
    UnionMember4RuleRouteRule,
    UnionMember4RuleScoreRule,
    UnionMember4RuleServeErrorRule,
    UnionMember4RuleSetCacheControlRule,
    UnionMember4RuleSetCacheSettingsRule,
    UnionMember4RuleSetCacheTagsRule,
    UnionMember4RuleSetConfigurationRule,
    UnionMember4RuleSkipRule,
    UnionMember4RuleTransformResponseHTMLRule,
]


class UnionMember4(BaseModel):
    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    kind: Optional[Kind] = None
    """The kind of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    name: Optional[str] = None
    """The human-readable name of the ruleset."""

    phase: Optional[Phase] = None
    """The phase of the ruleset."""

    rules: Optional[List[UnionMember4Rule]] = None
    """The list of rules in the ruleset."""

    version: Optional[str] = None
    """The version of the ruleset."""


VersionGetResponse: TypeAlias = Union[Optional[UnionMember0], UnionMember1, UnionMember2, UnionMember3, UnionMember4]
