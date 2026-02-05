# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.rulesets import rule_edit_params, rule_create_params
from ...types.rulesets.logging_param import LoggingParam
from ...types.rulesets.rule_edit_response import RuleEditResponse
from ...types.rulesets.rule_create_response import RuleCreateResponse
from ...types.rulesets.rule_delete_response import RuleDeleteResponse

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RulesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"] | Omit = omit,
        action_parameters: rule_create_params.BlockRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.BlockRulePosition | Omit = omit,
        ratelimit: rule_create_params.BlockRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.ChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["compress_response"] | Omit = omit,
        action_parameters: rule_create_params.ResponseCompressionRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ResponseCompressionRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ResponseCompressionRulePosition | Omit = omit,
        ratelimit: rule_create_params.ResponseCompressionRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["ddos_dynamic"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.DDoSDynamicRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.DDoSDynamicRulePosition | Omit = omit,
        ratelimit: rule_create_params.DDoSDynamicRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["execute"] | Omit = omit,
        action_parameters: rule_create_params.ExecuteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ExecuteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ExecuteRulePosition | Omit = omit,
        ratelimit: rule_create_params.ExecuteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["force_connection_close"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ForceConnectionCloseRulePosition | Omit = omit,
        ratelimit: rule_create_params.ForceConnectionCloseRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["js_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.JavaScriptChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.JavaScriptChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.JavaScriptChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.LogRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.LogRulePosition | Omit = omit,
        ratelimit: rule_create_params.LogRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log_custom_field"] | Omit = omit,
        action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.LogCustomFieldRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.LogCustomFieldRulePosition | Omit = omit,
        ratelimit: rule_create_params.LogCustomFieldRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["managed_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ManagedChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ManagedChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.ManagedChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["redirect"] | Omit = omit,
        action_parameters: rule_create_params.RedirectRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RedirectRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RedirectRulePosition | Omit = omit,
        ratelimit: rule_create_params.RedirectRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["rewrite"] | Omit = omit,
        action_parameters: rule_create_params.RewriteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RewriteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RewriteRulePosition | Omit = omit,
        ratelimit: rule_create_params.RewriteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["route"] | Omit = omit,
        action_parameters: rule_create_params.RouteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RouteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RouteRulePosition | Omit = omit,
        ratelimit: rule_create_params.RouteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["score"] | Omit = omit,
        action_parameters: rule_create_params.ScoreRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ScoreRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ScoreRulePosition | Omit = omit,
        ratelimit: rule_create_params.ScoreRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["serve_error"] | Omit = omit,
        action_parameters: rule_create_params.ServeErrorRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ServeErrorRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ServeErrorRulePosition | Omit = omit,
        ratelimit: rule_create_params.ServeErrorRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_cache_settings"] | Omit = omit,
        action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SetCacheSettingsRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SetCacheSettingsRulePosition | Omit = omit,
        ratelimit: rule_create_params.SetCacheSettingsRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_config"] | Omit = omit,
        action_parameters: rule_create_params.SetConfigurationRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SetConfigurationRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SetConfigurationRulePosition | Omit = omit,
        ratelimit: rule_create_params.SetConfigurationRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["skip"] | Omit = omit,
        action_parameters: rule_create_params.SkipRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SkipRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SkipRulePosition | Omit = omit,
        ratelimit: rule_create_params.SkipRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["ddos_dynamic"]
        | Literal["execute"]
        | Literal["force_connection_close"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["log_custom_field"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_cache_settings"]
        | Literal["set_config"]
        | Literal["skip"]
        | Omit = omit,
        action_parameters: rule_create_params.BlockRuleActionParameters
        | object
        | rule_create_params.ResponseCompressionRuleActionParameters
        | rule_create_params.ExecuteRuleActionParameters
        | rule_create_params.LogCustomFieldRuleActionParameters
        | rule_create_params.RedirectRuleActionParameters
        | rule_create_params.RewriteRuleActionParameters
        | rule_create_params.RouteRuleActionParameters
        | rule_create_params.ScoreRuleActionParameters
        | rule_create_params.ServeErrorRuleActionParameters
        | rule_create_params.SetCacheSettingsRuleActionParameters
        | rule_create_params.SetConfigurationRuleActionParameters
        | rule_create_params.SkipRuleActionParameters
        | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck
        | rule_create_params.ChallengeRuleExposedCredentialCheck
        | rule_create_params.ResponseCompressionRuleExposedCredentialCheck
        | rule_create_params.DDoSDynamicRuleExposedCredentialCheck
        | rule_create_params.ExecuteRuleExposedCredentialCheck
        | rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck
        | rule_create_params.JavaScriptChallengeRuleExposedCredentialCheck
        | rule_create_params.LogRuleExposedCredentialCheck
        | rule_create_params.LogCustomFieldRuleExposedCredentialCheck
        | rule_create_params.ManagedChallengeRuleExposedCredentialCheck
        | rule_create_params.RedirectRuleExposedCredentialCheck
        | rule_create_params.RewriteRuleExposedCredentialCheck
        | rule_create_params.RouteRuleExposedCredentialCheck
        | rule_create_params.ScoreRuleExposedCredentialCheck
        | rule_create_params.ServeErrorRuleExposedCredentialCheck
        | rule_create_params.SetCacheSettingsRuleExposedCredentialCheck
        | rule_create_params.SetConfigurationRuleExposedCredentialCheck
        | rule_create_params.SkipRuleExposedCredentialCheck
        | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.BlockRulePosition
        | rule_create_params.ChallengeRulePosition
        | rule_create_params.ResponseCompressionRulePosition
        | rule_create_params.DDoSDynamicRulePosition
        | rule_create_params.ExecuteRulePosition
        | rule_create_params.ForceConnectionCloseRulePosition
        | rule_create_params.JavaScriptChallengeRulePosition
        | rule_create_params.LogRulePosition
        | rule_create_params.LogCustomFieldRulePosition
        | rule_create_params.ManagedChallengeRulePosition
        | rule_create_params.RedirectRulePosition
        | rule_create_params.RewriteRulePosition
        | rule_create_params.RouteRulePosition
        | rule_create_params.ScoreRulePosition
        | rule_create_params.ServeErrorRulePosition
        | rule_create_params.SetCacheSettingsRulePosition
        | rule_create_params.SetConfigurationRulePosition
        | rule_create_params.SkipRulePosition
        | Omit = omit,
        ratelimit: rule_create_params.BlockRuleRatelimit
        | rule_create_params.ChallengeRuleRatelimit
        | rule_create_params.ResponseCompressionRuleRatelimit
        | rule_create_params.DDoSDynamicRuleRatelimit
        | rule_create_params.ExecuteRuleRatelimit
        | rule_create_params.ForceConnectionCloseRuleRatelimit
        | rule_create_params.JavaScriptChallengeRuleRatelimit
        | rule_create_params.LogRuleRatelimit
        | rule_create_params.LogCustomFieldRuleRatelimit
        | rule_create_params.ManagedChallengeRuleRatelimit
        | rule_create_params.RedirectRuleRatelimit
        | rule_create_params.RewriteRuleRatelimit
        | rule_create_params.RouteRuleRatelimit
        | rule_create_params.ScoreRuleRatelimit
        | rule_create_params.ServeErrorRuleRatelimit
        | rule_create_params.SetCacheSettingsRuleRatelimit
        | rule_create_params.SetConfigurationRuleRatelimit
        | rule_create_params.SkipRuleRatelimit
        | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "exposed_credential_check": exposed_credential_check,
                    "expression": expression,
                    "logging": logging,
                    "position": position,
                    "ratelimit": ratelimit,
                    "ref": ref,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleCreateResponse], ResultWrapper[RuleCreateResponse]),
        )

    def delete(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteResponse:
        """
        Deletes an existing rule from an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"] | Omit = omit,
        action_parameters: rule_edit_params.BlockRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.BlockRulePosition | Omit = omit,
        ratelimit: rule_edit_params.BlockRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["compress_response"] | Omit = omit,
        action_parameters: rule_edit_params.ResponseCompressionRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ResponseCompressionRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ResponseCompressionRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ResponseCompressionRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["ddos_dynamic"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.DDoSDynamicRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.DDoSDynamicRulePosition | Omit = omit,
        ratelimit: rule_edit_params.DDoSDynamicRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["execute"] | Omit = omit,
        action_parameters: rule_edit_params.ExecuteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ExecuteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ExecuteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ExecuteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["force_connection_close"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ForceConnectionCloseRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ForceConnectionCloseRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["js_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.JavaScriptChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.JavaScriptChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.JavaScriptChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.LogRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.LogRulePosition | Omit = omit,
        ratelimit: rule_edit_params.LogRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log_custom_field"] | Omit = omit,
        action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.LogCustomFieldRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.LogCustomFieldRulePosition | Omit = omit,
        ratelimit: rule_edit_params.LogCustomFieldRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["managed_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ManagedChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ManagedChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ManagedChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["redirect"] | Omit = omit,
        action_parameters: rule_edit_params.RedirectRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RedirectRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RedirectRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RedirectRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["rewrite"] | Omit = omit,
        action_parameters: rule_edit_params.RewriteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RewriteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RewriteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RewriteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["route"] | Omit = omit,
        action_parameters: rule_edit_params.RouteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RouteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RouteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RouteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["score"] | Omit = omit,
        action_parameters: rule_edit_params.ScoreRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ScoreRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ScoreRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ScoreRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["serve_error"] | Omit = omit,
        action_parameters: rule_edit_params.ServeErrorRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ServeErrorRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ServeErrorRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ServeErrorRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_cache_settings"] | Omit = omit,
        action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SetCacheSettingsRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SetCacheSettingsRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_config"] | Omit = omit,
        action_parameters: rule_edit_params.SetConfigurationRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SetConfigurationRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SetConfigurationRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SetConfigurationRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["skip"] | Omit = omit,
        action_parameters: rule_edit_params.SkipRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SkipRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SkipRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SkipRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["ruleset_id"])
    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["ddos_dynamic"]
        | Literal["execute"]
        | Literal["force_connection_close"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["log_custom_field"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_cache_settings"]
        | Literal["set_config"]
        | Literal["skip"]
        | Omit = omit,
        action_parameters: rule_edit_params.BlockRuleActionParameters
        | object
        | rule_edit_params.ResponseCompressionRuleActionParameters
        | rule_edit_params.ExecuteRuleActionParameters
        | rule_edit_params.LogCustomFieldRuleActionParameters
        | rule_edit_params.RedirectRuleActionParameters
        | rule_edit_params.RewriteRuleActionParameters
        | rule_edit_params.RouteRuleActionParameters
        | rule_edit_params.ScoreRuleActionParameters
        | rule_edit_params.ServeErrorRuleActionParameters
        | rule_edit_params.SetCacheSettingsRuleActionParameters
        | rule_edit_params.SetConfigurationRuleActionParameters
        | rule_edit_params.SkipRuleActionParameters
        | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck
        | rule_edit_params.ChallengeRuleExposedCredentialCheck
        | rule_edit_params.ResponseCompressionRuleExposedCredentialCheck
        | rule_edit_params.DDoSDynamicRuleExposedCredentialCheck
        | rule_edit_params.ExecuteRuleExposedCredentialCheck
        | rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck
        | rule_edit_params.JavaScriptChallengeRuleExposedCredentialCheck
        | rule_edit_params.LogRuleExposedCredentialCheck
        | rule_edit_params.LogCustomFieldRuleExposedCredentialCheck
        | rule_edit_params.ManagedChallengeRuleExposedCredentialCheck
        | rule_edit_params.RedirectRuleExposedCredentialCheck
        | rule_edit_params.RewriteRuleExposedCredentialCheck
        | rule_edit_params.RouteRuleExposedCredentialCheck
        | rule_edit_params.ScoreRuleExposedCredentialCheck
        | rule_edit_params.ServeErrorRuleExposedCredentialCheck
        | rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck
        | rule_edit_params.SetConfigurationRuleExposedCredentialCheck
        | rule_edit_params.SkipRuleExposedCredentialCheck
        | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.BlockRulePosition
        | rule_edit_params.ChallengeRulePosition
        | rule_edit_params.ResponseCompressionRulePosition
        | rule_edit_params.DDoSDynamicRulePosition
        | rule_edit_params.ExecuteRulePosition
        | rule_edit_params.ForceConnectionCloseRulePosition
        | rule_edit_params.JavaScriptChallengeRulePosition
        | rule_edit_params.LogRulePosition
        | rule_edit_params.LogCustomFieldRulePosition
        | rule_edit_params.ManagedChallengeRulePosition
        | rule_edit_params.RedirectRulePosition
        | rule_edit_params.RewriteRulePosition
        | rule_edit_params.RouteRulePosition
        | rule_edit_params.ScoreRulePosition
        | rule_edit_params.ServeErrorRulePosition
        | rule_edit_params.SetCacheSettingsRulePosition
        | rule_edit_params.SetConfigurationRulePosition
        | rule_edit_params.SkipRulePosition
        | Omit = omit,
        ratelimit: rule_edit_params.BlockRuleRatelimit
        | rule_edit_params.ChallengeRuleRatelimit
        | rule_edit_params.ResponseCompressionRuleRatelimit
        | rule_edit_params.DDoSDynamicRuleRatelimit
        | rule_edit_params.ExecuteRuleRatelimit
        | rule_edit_params.ForceConnectionCloseRuleRatelimit
        | rule_edit_params.JavaScriptChallengeRuleRatelimit
        | rule_edit_params.LogRuleRatelimit
        | rule_edit_params.LogCustomFieldRuleRatelimit
        | rule_edit_params.ManagedChallengeRuleRatelimit
        | rule_edit_params.RedirectRuleRatelimit
        | rule_edit_params.RewriteRuleRatelimit
        | rule_edit_params.RouteRuleRatelimit
        | rule_edit_params.ScoreRuleRatelimit
        | rule_edit_params.ServeErrorRuleRatelimit
        | rule_edit_params.SetCacheSettingsRuleRatelimit
        | rule_edit_params.SetConfigurationRuleRatelimit
        | rule_edit_params.SkipRuleRatelimit
        | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "exposed_credential_check": exposed_credential_check,
                    "expression": expression,
                    "logging": logging,
                    "position": position,
                    "ratelimit": ratelimit,
                    "ref": ref,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleEditResponse], ResultWrapper[RuleEditResponse]),
        )


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRulesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"] | Omit = omit,
        action_parameters: rule_create_params.BlockRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.BlockRulePosition | Omit = omit,
        ratelimit: rule_create_params.BlockRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.ChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["compress_response"] | Omit = omit,
        action_parameters: rule_create_params.ResponseCompressionRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ResponseCompressionRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ResponseCompressionRulePosition | Omit = omit,
        ratelimit: rule_create_params.ResponseCompressionRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["ddos_dynamic"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.DDoSDynamicRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.DDoSDynamicRulePosition | Omit = omit,
        ratelimit: rule_create_params.DDoSDynamicRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["execute"] | Omit = omit,
        action_parameters: rule_create_params.ExecuteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ExecuteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ExecuteRulePosition | Omit = omit,
        ratelimit: rule_create_params.ExecuteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["force_connection_close"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ForceConnectionCloseRulePosition | Omit = omit,
        ratelimit: rule_create_params.ForceConnectionCloseRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["js_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.JavaScriptChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.JavaScriptChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.JavaScriptChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.LogRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.LogRulePosition | Omit = omit,
        ratelimit: rule_create_params.LogRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log_custom_field"] | Omit = omit,
        action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.LogCustomFieldRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.LogCustomFieldRulePosition | Omit = omit,
        ratelimit: rule_create_params.LogCustomFieldRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["managed_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ManagedChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ManagedChallengeRulePosition | Omit = omit,
        ratelimit: rule_create_params.ManagedChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["redirect"] | Omit = omit,
        action_parameters: rule_create_params.RedirectRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RedirectRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RedirectRulePosition | Omit = omit,
        ratelimit: rule_create_params.RedirectRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["rewrite"] | Omit = omit,
        action_parameters: rule_create_params.RewriteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RewriteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RewriteRulePosition | Omit = omit,
        ratelimit: rule_create_params.RewriteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["route"] | Omit = omit,
        action_parameters: rule_create_params.RouteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.RouteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.RouteRulePosition | Omit = omit,
        ratelimit: rule_create_params.RouteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["score"] | Omit = omit,
        action_parameters: rule_create_params.ScoreRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ScoreRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ScoreRulePosition | Omit = omit,
        ratelimit: rule_create_params.ScoreRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["serve_error"] | Omit = omit,
        action_parameters: rule_create_params.ServeErrorRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.ServeErrorRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.ServeErrorRulePosition | Omit = omit,
        ratelimit: rule_create_params.ServeErrorRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_cache_settings"] | Omit = omit,
        action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SetCacheSettingsRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SetCacheSettingsRulePosition | Omit = omit,
        ratelimit: rule_create_params.SetCacheSettingsRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_config"] | Omit = omit,
        action_parameters: rule_create_params.SetConfigurationRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SetConfigurationRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SetConfigurationRulePosition | Omit = omit,
        ratelimit: rule_create_params.SetConfigurationRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["skip"] | Omit = omit,
        action_parameters: rule_create_params.SkipRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.SkipRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.SkipRulePosition | Omit = omit,
        ratelimit: rule_create_params.SkipRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["ddos_dynamic"]
        | Literal["execute"]
        | Literal["force_connection_close"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["log_custom_field"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_cache_settings"]
        | Literal["set_config"]
        | Literal["skip"]
        | Omit = omit,
        action_parameters: rule_create_params.BlockRuleActionParameters
        | object
        | rule_create_params.ResponseCompressionRuleActionParameters
        | rule_create_params.ExecuteRuleActionParameters
        | rule_create_params.LogCustomFieldRuleActionParameters
        | rule_create_params.RedirectRuleActionParameters
        | rule_create_params.RewriteRuleActionParameters
        | rule_create_params.RouteRuleActionParameters
        | rule_create_params.ScoreRuleActionParameters
        | rule_create_params.ServeErrorRuleActionParameters
        | rule_create_params.SetCacheSettingsRuleActionParameters
        | rule_create_params.SetConfigurationRuleActionParameters
        | rule_create_params.SkipRuleActionParameters
        | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck
        | rule_create_params.ChallengeRuleExposedCredentialCheck
        | rule_create_params.ResponseCompressionRuleExposedCredentialCheck
        | rule_create_params.DDoSDynamicRuleExposedCredentialCheck
        | rule_create_params.ExecuteRuleExposedCredentialCheck
        | rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck
        | rule_create_params.JavaScriptChallengeRuleExposedCredentialCheck
        | rule_create_params.LogRuleExposedCredentialCheck
        | rule_create_params.LogCustomFieldRuleExposedCredentialCheck
        | rule_create_params.ManagedChallengeRuleExposedCredentialCheck
        | rule_create_params.RedirectRuleExposedCredentialCheck
        | rule_create_params.RewriteRuleExposedCredentialCheck
        | rule_create_params.RouteRuleExposedCredentialCheck
        | rule_create_params.ScoreRuleExposedCredentialCheck
        | rule_create_params.ServeErrorRuleExposedCredentialCheck
        | rule_create_params.SetCacheSettingsRuleExposedCredentialCheck
        | rule_create_params.SetConfigurationRuleExposedCredentialCheck
        | rule_create_params.SkipRuleExposedCredentialCheck
        | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_create_params.BlockRulePosition
        | rule_create_params.ChallengeRulePosition
        | rule_create_params.ResponseCompressionRulePosition
        | rule_create_params.DDoSDynamicRulePosition
        | rule_create_params.ExecuteRulePosition
        | rule_create_params.ForceConnectionCloseRulePosition
        | rule_create_params.JavaScriptChallengeRulePosition
        | rule_create_params.LogRulePosition
        | rule_create_params.LogCustomFieldRulePosition
        | rule_create_params.ManagedChallengeRulePosition
        | rule_create_params.RedirectRulePosition
        | rule_create_params.RewriteRulePosition
        | rule_create_params.RouteRulePosition
        | rule_create_params.ScoreRulePosition
        | rule_create_params.ServeErrorRulePosition
        | rule_create_params.SetCacheSettingsRulePosition
        | rule_create_params.SetConfigurationRulePosition
        | rule_create_params.SkipRulePosition
        | Omit = omit,
        ratelimit: rule_create_params.BlockRuleRatelimit
        | rule_create_params.ChallengeRuleRatelimit
        | rule_create_params.ResponseCompressionRuleRatelimit
        | rule_create_params.DDoSDynamicRuleRatelimit
        | rule_create_params.ExecuteRuleRatelimit
        | rule_create_params.ForceConnectionCloseRuleRatelimit
        | rule_create_params.JavaScriptChallengeRuleRatelimit
        | rule_create_params.LogRuleRatelimit
        | rule_create_params.LogCustomFieldRuleRatelimit
        | rule_create_params.ManagedChallengeRuleRatelimit
        | rule_create_params.RedirectRuleRatelimit
        | rule_create_params.RewriteRuleRatelimit
        | rule_create_params.RouteRuleRatelimit
        | rule_create_params.ScoreRuleRatelimit
        | rule_create_params.ServeErrorRuleRatelimit
        | rule_create_params.SetCacheSettingsRuleRatelimit
        | rule_create_params.SetConfigurationRuleRatelimit
        | rule_create_params.SkipRuleRatelimit
        | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleCreateResponse:
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "exposed_credential_check": exposed_credential_check,
                    "expression": expression,
                    "logging": logging,
                    "position": position,
                    "ratelimit": ratelimit,
                    "ref": ref,
                },
                rule_create_params.RuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleCreateResponse], ResultWrapper[RuleCreateResponse]),
        )

    async def delete(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleDeleteResponse:
        """
        Deletes an existing rule from an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"] | Omit = omit,
        action_parameters: rule_edit_params.BlockRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.BlockRulePosition | Omit = omit,
        ratelimit: rule_edit_params.BlockRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["compress_response"] | Omit = omit,
        action_parameters: rule_edit_params.ResponseCompressionRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ResponseCompressionRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ResponseCompressionRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ResponseCompressionRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["ddos_dynamic"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.DDoSDynamicRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.DDoSDynamicRulePosition | Omit = omit,
        ratelimit: rule_edit_params.DDoSDynamicRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["execute"] | Omit = omit,
        action_parameters: rule_edit_params.ExecuteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ExecuteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ExecuteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ExecuteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["force_connection_close"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ForceConnectionCloseRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ForceConnectionCloseRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["js_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.JavaScriptChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.JavaScriptChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.JavaScriptChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.LogRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.LogRulePosition | Omit = omit,
        ratelimit: rule_edit_params.LogRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["log_custom_field"] | Omit = omit,
        action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.LogCustomFieldRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.LogCustomFieldRulePosition | Omit = omit,
        ratelimit: rule_edit_params.LogCustomFieldRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["managed_challenge"] | Omit = omit,
        action_parameters: object | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ManagedChallengeRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ManagedChallengeRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ManagedChallengeRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["redirect"] | Omit = omit,
        action_parameters: rule_edit_params.RedirectRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RedirectRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RedirectRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RedirectRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["rewrite"] | Omit = omit,
        action_parameters: rule_edit_params.RewriteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RewriteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RewriteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RewriteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["route"] | Omit = omit,
        action_parameters: rule_edit_params.RouteRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.RouteRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.RouteRulePosition | Omit = omit,
        ratelimit: rule_edit_params.RouteRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["score"] | Omit = omit,
        action_parameters: rule_edit_params.ScoreRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ScoreRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ScoreRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ScoreRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["serve_error"] | Omit = omit,
        action_parameters: rule_edit_params.ServeErrorRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.ServeErrorRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.ServeErrorRulePosition | Omit = omit,
        ratelimit: rule_edit_params.ServeErrorRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_cache_settings"] | Omit = omit,
        action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SetCacheSettingsRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SetCacheSettingsRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["set_config"] | Omit = omit,
        action_parameters: rule_edit_params.SetConfigurationRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SetConfigurationRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SetConfigurationRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SetConfigurationRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["skip"] | Omit = omit,
        action_parameters: rule_edit_params.SkipRuleActionParameters | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.SkipRuleExposedCredentialCheck | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.SkipRulePosition | Omit = omit,
        ratelimit: rule_edit_params.SkipRuleRatelimit | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          exposed_credential_check: Configuration for exposed credential checking.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's rate limit behavior.

          ref: The reference of the rule (the rule's ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["ruleset_id"])
    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | Omit = omit,
        zone_id: str | Omit = omit,
        id: str | Omit = omit,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["ddos_dynamic"]
        | Literal["execute"]
        | Literal["force_connection_close"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["log_custom_field"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_cache_settings"]
        | Literal["set_config"]
        | Literal["skip"]
        | Omit = omit,
        action_parameters: rule_edit_params.BlockRuleActionParameters
        | object
        | rule_edit_params.ResponseCompressionRuleActionParameters
        | rule_edit_params.ExecuteRuleActionParameters
        | rule_edit_params.LogCustomFieldRuleActionParameters
        | rule_edit_params.RedirectRuleActionParameters
        | rule_edit_params.RewriteRuleActionParameters
        | rule_edit_params.RouteRuleActionParameters
        | rule_edit_params.ScoreRuleActionParameters
        | rule_edit_params.ServeErrorRuleActionParameters
        | rule_edit_params.SetCacheSettingsRuleActionParameters
        | rule_edit_params.SetConfigurationRuleActionParameters
        | rule_edit_params.SkipRuleActionParameters
        | Omit = omit,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck
        | rule_edit_params.ChallengeRuleExposedCredentialCheck
        | rule_edit_params.ResponseCompressionRuleExposedCredentialCheck
        | rule_edit_params.DDoSDynamicRuleExposedCredentialCheck
        | rule_edit_params.ExecuteRuleExposedCredentialCheck
        | rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck
        | rule_edit_params.JavaScriptChallengeRuleExposedCredentialCheck
        | rule_edit_params.LogRuleExposedCredentialCheck
        | rule_edit_params.LogCustomFieldRuleExposedCredentialCheck
        | rule_edit_params.ManagedChallengeRuleExposedCredentialCheck
        | rule_edit_params.RedirectRuleExposedCredentialCheck
        | rule_edit_params.RewriteRuleExposedCredentialCheck
        | rule_edit_params.RouteRuleExposedCredentialCheck
        | rule_edit_params.ScoreRuleExposedCredentialCheck
        | rule_edit_params.ServeErrorRuleExposedCredentialCheck
        | rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck
        | rule_edit_params.SetConfigurationRuleExposedCredentialCheck
        | rule_edit_params.SkipRuleExposedCredentialCheck
        | Omit = omit,
        expression: str | Omit = omit,
        logging: LoggingParam | Omit = omit,
        position: rule_edit_params.BlockRulePosition
        | rule_edit_params.ChallengeRulePosition
        | rule_edit_params.ResponseCompressionRulePosition
        | rule_edit_params.DDoSDynamicRulePosition
        | rule_edit_params.ExecuteRulePosition
        | rule_edit_params.ForceConnectionCloseRulePosition
        | rule_edit_params.JavaScriptChallengeRulePosition
        | rule_edit_params.LogRulePosition
        | rule_edit_params.LogCustomFieldRulePosition
        | rule_edit_params.ManagedChallengeRulePosition
        | rule_edit_params.RedirectRulePosition
        | rule_edit_params.RewriteRulePosition
        | rule_edit_params.RouteRulePosition
        | rule_edit_params.ScoreRulePosition
        | rule_edit_params.ServeErrorRulePosition
        | rule_edit_params.SetCacheSettingsRulePosition
        | rule_edit_params.SetConfigurationRulePosition
        | rule_edit_params.SkipRulePosition
        | Omit = omit,
        ratelimit: rule_edit_params.BlockRuleRatelimit
        | rule_edit_params.ChallengeRuleRatelimit
        | rule_edit_params.ResponseCompressionRuleRatelimit
        | rule_edit_params.DDoSDynamicRuleRatelimit
        | rule_edit_params.ExecuteRuleRatelimit
        | rule_edit_params.ForceConnectionCloseRuleRatelimit
        | rule_edit_params.JavaScriptChallengeRuleRatelimit
        | rule_edit_params.LogRuleRatelimit
        | rule_edit_params.LogCustomFieldRuleRatelimit
        | rule_edit_params.ManagedChallengeRuleRatelimit
        | rule_edit_params.RedirectRuleRatelimit
        | rule_edit_params.RewriteRuleRatelimit
        | rule_edit_params.RouteRuleRatelimit
        | rule_edit_params.ScoreRuleRatelimit
        | rule_edit_params.ServeErrorRuleRatelimit
        | rule_edit_params.SetCacheSettingsRuleRatelimit
        | rule_edit_params.SetConfigurationRuleRatelimit
        | rule_edit_params.SkipRuleRatelimit
        | Omit = omit,
        ref: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RuleEditResponse:
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "exposed_credential_check": exposed_credential_check,
                    "expression": expression,
                    "logging": logging,
                    "position": position,
                    "ratelimit": ratelimit,
                    "ref": ref,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RuleEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[RuleEditResponse], ResultWrapper[RuleEditResponse]),
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
