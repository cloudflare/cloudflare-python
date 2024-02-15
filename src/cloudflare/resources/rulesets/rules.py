# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.rulesets import (
    RuleDeleteResponse,
    RuleUpdateResponse,
    RuleAccountRulesetsCreateAnAccountRulesetRuleResponse,
    rule_update_params,
    rule_account_rulesets_create_an_account_ruleset_rule_params,
)

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    @overload
    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsBlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsBlockRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsExecuteRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsLogRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsSkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsSkipRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
    )
    def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | Literal["execute"] | Literal["log"] | Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsBlockRuleActionParameters
        | rule_update_params.RulesetsExecuteRuleActionParameters
        | object
        | rule_update_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsBlockRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            f"/{account_id}/{ruleset_id}/rulesets/{rule_id}/rules/:rule_id",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "logging": logging,
                    "ref": ref,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleUpdateResponse], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(
        self,
        rule_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
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
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsLogRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
    )
    def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | Literal["execute"] | Literal["log"] | Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleActionParameters
        | rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleActionParameters
        | object
        | rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "logging": logging,
                    "ref": ref,
                },
                rule_account_rulesets_create_an_account_ruleset_rule_params.RuleAccountRulesetsCreateAnAccountRulesetRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RuleAccountRulesetsCreateAnAccountRulesetRuleResponse],
                ResultWrapper[RuleAccountRulesetsCreateAnAccountRulesetRuleResponse],
            ),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    @overload
    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsBlockRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsBlockRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsExecuteRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsLogRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsSkipRuleActionParameters | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsSkipRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          account_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
        ["account_id", "ruleset_id"],
    )
    async def update(
        self,
        rule_id: str,
        *,
        account_id: str,
        ruleset_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | Literal["execute"] | Literal["log"] | Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_update_params.RulesetsBlockRuleActionParameters
        | rule_update_params.RulesetsExecuteRuleActionParameters
        | object
        | rule_update_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_update_params.RulesetsBlockRuleLogging | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleUpdateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            f"/{account_id}/{ruleset_id}/rulesets/{rule_id}/rules/:rule_id",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "logging": logging,
                    "ref": ref,
                },
                rule_update_params.RuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleUpdateResponse], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(
        self,
        rule_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        ruleset_id: str,
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
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    async def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["execute"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["log"] | NotGiven = NOT_GIVEN,
        action_parameters: object | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsLogRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          account_or_zone_id: The unique ID of the account.

          ruleset_id: The unique ID of the ruleset.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
        ["account_or_zone", "account_or_zone_id"],
    )
    async def account_rulesets_create_an_account_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        action: Literal["block"] | Literal["execute"] | Literal["log"] | Literal["skip"] | NotGiven = NOT_GIVEN,
        action_parameters: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleActionParameters
        | rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsExecuteRuleActionParameters
        | object
        | rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsSkipRuleActionParameters
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        expression: str | NotGiven = NOT_GIVEN,
        logging: rule_account_rulesets_create_an_account_ruleset_rule_params.RulesetsBlockRuleLogging
        | NotGiven = NOT_GIVEN,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuleAccountRulesetsCreateAnAccountRulesetRuleResponse:
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=maybe_transform(
                {
                    "id": id,
                    "action": action,
                    "action_parameters": action_parameters,
                    "description": description,
                    "enabled": enabled,
                    "expression": expression,
                    "logging": logging,
                    "ref": ref,
                },
                rule_account_rulesets_create_an_account_ruleset_rule_params.RuleAccountRulesetsCreateAnAccountRulesetRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[RuleAccountRulesetsCreateAnAccountRulesetRuleResponse],
                ResultWrapper[RuleAccountRulesetsCreateAnAccountRulesetRuleResponse],
            ),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.account_rulesets_create_an_account_ruleset_rule = to_raw_response_wrapper(
            rules.account_rulesets_create_an_account_ruleset_rule,
        )


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.account_rulesets_create_an_account_ruleset_rule = async_to_raw_response_wrapper(
            rules.account_rulesets_create_an_account_ruleset_rule,
        )


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.account_rulesets_create_an_account_ruleset_rule = to_streamed_response_wrapper(
            rules.account_rulesets_create_an_account_ruleset_rule,
        )


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.account_rulesets_create_an_account_ruleset_rule = async_to_streamed_response_wrapper(
            rules.account_rulesets_create_an_account_ruleset_rule,
        )
