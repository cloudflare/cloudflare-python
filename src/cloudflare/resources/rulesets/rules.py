# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.CompressionRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.CompressionRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.CompressionRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.CompressionRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ExecuteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ExecuteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ExecuteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.JavascriptChallengeRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.JavascriptChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.JavascriptChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.LogRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.LogRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.LogRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ManagedChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ManagedChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ManagedChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["redirect"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.RedirectRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.RedirectRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.RedirectRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.RewriteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.RewriteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.RewriteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["route"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.OriginRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.OriginRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.OriginRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.OriginRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["score"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ScoreRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ScoreRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ScoreRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ServeErrorRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ServeErrorRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ServeErrorRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_config"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SetConfigRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SetConfigRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SetConfigRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SkipRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SkipRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SkipRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SetCacheSettingsRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SetCacheSettingsRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SetCacheSettingsRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.LogCustomFieldRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.LogCustomFieldRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.LogCustomFieldRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.DDoSDynamicRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.DDoSDynamicRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.DDoSDynamicRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ForceConnectionCloseRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ForceConnectionCloseRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["execute"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_config"]
        | Literal["skip"]
        | Literal["set_cache_settings"]
        | Literal["log_custom_field"]
        | Literal["ddos_dynamic"]
        | Literal["force_connection_close"]
        | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.BlockRuleActionParameters
        | object
        | rule_create_params.CompressionRuleActionParameters
        | rule_create_params.ExecuteRuleActionParameters
        | rule_create_params.RedirectRuleActionParameters
        | rule_create_params.RewriteRuleActionParameters
        | rule_create_params.OriginRuleActionParameters
        | rule_create_params.ScoreRuleActionParameters
        | rule_create_params.ServeErrorRuleActionParameters
        | rule_create_params.SetConfigRuleActionParameters
        | rule_create_params.SkipRuleActionParameters
        | rule_create_params.SetCacheSettingsRuleActionParameters
        | rule_create_params.LogCustomFieldRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.CompressionRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.CompressionRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.CompressionRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.CompressionRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ExecuteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ExecuteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ExecuteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.JavascriptChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.JavascriptChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.JavascriptChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.LogRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.LogRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.LogRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ManagedChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ManagedChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ManagedChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["redirect"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.RedirectRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.RedirectRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.RedirectRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.RewriteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.RewriteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.RewriteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["route"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.OriginRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.OriginRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.OriginRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.OriginRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["score"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ScoreRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ScoreRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ScoreRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ServeErrorRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ServeErrorRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ServeErrorRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_config"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SetConfigRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SetConfigRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SetConfigRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SkipRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SkipRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SkipRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SetCacheSettingsRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SetCacheSettingsRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.LogCustomFieldRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.LogCustomFieldRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.LogCustomFieldRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.DDoSDynamicRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.DDoSDynamicRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.DDoSDynamicRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ForceConnectionCloseRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ForceConnectionCloseRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["execute"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_config"]
        | Literal["skip"]
        | Literal["set_cache_settings"]
        | Literal["log_custom_field"]
        | Literal["ddos_dynamic"]
        | Literal["force_connection_close"]
        | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.BlockRuleActionParameters
        | object
        | rule_edit_params.CompressionRuleActionParameters
        | rule_edit_params.ExecuteRuleActionParameters
        | rule_edit_params.RedirectRuleActionParameters
        | rule_edit_params.RewriteRuleActionParameters
        | rule_edit_params.OriginRuleActionParameters
        | rule_edit_params.ScoreRuleActionParameters
        | rule_edit_params.ServeErrorRuleActionParameters
        | rule_edit_params.SetConfigRuleActionParameters
        | rule_edit_params.SkipRuleActionParameters
        | rule_edit_params.SetCacheSettingsRuleActionParameters
        | rule_edit_params.LogCustomFieldRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.CompressionRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.CompressionRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.CompressionRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.CompressionRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ExecuteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ExecuteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ExecuteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.JavascriptChallengeRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.JavascriptChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.JavascriptChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.LogRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.LogRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.LogRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ManagedChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ManagedChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ManagedChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["redirect"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.RedirectRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.RedirectRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.RedirectRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.RewriteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.RewriteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.RewriteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["route"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.OriginRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.OriginRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.OriginRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.OriginRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["score"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ScoreRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ScoreRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ScoreRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ServeErrorRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ServeErrorRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ServeErrorRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_config"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SetConfigRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SetConfigRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SetConfigRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SkipRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SkipRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SkipRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.SetCacheSettingsRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.SetCacheSettingsRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.SetCacheSettingsRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.LogCustomFieldRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.LogCustomFieldRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.LogCustomFieldRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.DDoSDynamicRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.DDoSDynamicRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.DDoSDynamicRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.ForceConnectionCloseRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.ForceConnectionCloseRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.ForceConnectionCloseRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["execute"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_config"]
        | Literal["skip"]
        | Literal["set_cache_settings"]
        | Literal["log_custom_field"]
        | Literal["ddos_dynamic"]
        | Literal["force_connection_close"]
        | NotGiven = NOT_GIVEN,
        action_parameters: rule_create_params.BlockRuleActionParameters
        | object
        | rule_create_params.CompressionRuleActionParameters
        | rule_create_params.ExecuteRuleActionParameters
        | rule_create_params.RedirectRuleActionParameters
        | rule_create_params.RewriteRuleActionParameters
        | rule_create_params.OriginRuleActionParameters
        | rule_create_params.ScoreRuleActionParameters
        | rule_create_params.ServeErrorRuleActionParameters
        | rule_create_params.SetConfigRuleActionParameters
        | rule_create_params.SkipRuleActionParameters
        | rule_create_params.SetCacheSettingsRuleActionParameters
        | rule_create_params.LogCustomFieldRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_create_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_create_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_create_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.CompressionRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.CompressionRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.CompressionRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.CompressionRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ExecuteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ExecuteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ExecuteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.JavascriptChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.JavascriptChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.JavascriptChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.LogRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.LogRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.LogRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ManagedChallengeRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ManagedChallengeRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ManagedChallengeRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["redirect"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.RedirectRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.RedirectRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.RedirectRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.RewriteRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.RewriteRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.RewriteRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["route"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.OriginRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.OriginRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.OriginRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.OriginRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["score"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ScoreRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ScoreRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ScoreRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ServeErrorRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ServeErrorRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ServeErrorRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_config"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SetConfigRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SetConfigRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SetConfigRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SkipRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SkipRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SkipRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.SetCacheSettingsRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.SetCacheSettingsRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.SetCacheSettingsRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.LogCustomFieldRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.LogCustomFieldRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.LogCustomFieldRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.DDoSDynamicRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.DDoSDynamicRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.DDoSDynamicRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.ForceConnectionCloseRuleExposedCredentialCheck
        | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.ForceConnectionCloseRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.ForceConnectionCloseRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          exposed_credential_check: Configure checks for exposed credentials.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          position: An object configuring where the rule will be placed.

          ratelimit: An object configuring the rule's ratelimit behavior.

          ref: The reference of the rule (the rule ID by default).

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
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"]
        | Literal["challenge"]
        | Literal["compress_response"]
        | Literal["execute"]
        | Literal["js_challenge"]
        | Literal["log"]
        | Literal["managed_challenge"]
        | Literal["redirect"]
        | Literal["rewrite"]
        | Literal["route"]
        | Literal["score"]
        | Literal["serve_error"]
        | Literal["set_config"]
        | Literal["skip"]
        | Literal["set_cache_settings"]
        | Literal["log_custom_field"]
        | Literal["ddos_dynamic"]
        | Literal["force_connection_close"]
        | NotGiven = NOT_GIVEN,
        action_parameters: rule_edit_params.BlockRuleActionParameters
        | object
        | rule_edit_params.CompressionRuleActionParameters
        | rule_edit_params.ExecuteRuleActionParameters
        | rule_edit_params.RedirectRuleActionParameters
        | rule_edit_params.RewriteRuleActionParameters
        | rule_edit_params.OriginRuleActionParameters
        | rule_edit_params.ScoreRuleActionParameters
        | rule_edit_params.ServeErrorRuleActionParameters
        | rule_edit_params.SetConfigRuleActionParameters
        | rule_edit_params.SkipRuleActionParameters
        | rule_edit_params.SetCacheSettingsRuleActionParameters
        | rule_edit_params.LogCustomFieldRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        exposed_credential_check: rule_edit_params.BlockRuleExposedCredentialCheck | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: LoggingParam | NotGiven = NOT_GIVEN,
        position: rule_edit_params.BlockRulePosition | NotGiven = NOT_GIVEN,
        ratelimit: rule_edit_params.BlockRuleRatelimit | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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
