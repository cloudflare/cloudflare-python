# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...types import RulesetsRulesetResponse
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
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
from ..._base_client import (
    make_request_options,
)
from ...types.rulesets import rule_edit_params, rule_create_params

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        position: rule_create_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          position: An object configuring where the rule will be placed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=maybe_transform({"position": position}, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
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
    ) -> RulesetsRulesetResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )

    def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        position: rule_edit_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          position: An object configuring where the rule will be placed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=maybe_transform({"position": position}, rule_edit_params.RuleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def create(
        self,
        ruleset_id: str,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        position: rule_create_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          position: An object configuring where the rule will be placed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=await async_maybe_transform({"position": position}, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
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
    ) -> RulesetsRulesetResponse:
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
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )

    async def edit(
        self,
        rule_id: str,
        *,
        ruleset_id: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        position: rule_edit_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RulesetsRulesetResponse:
        """
        Updates an existing rule in an account ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          position: An object configuring where the rule will be placed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
            raise ValueError(f"Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not account_id and not zone_id:
            raise ValueError("You must provide either account_id or zone_id")
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=await async_maybe_transform({"position": position}, rule_edit_params.RuleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[RulesetsRulesetResponse], ResultWrapper[RulesetsRulesetResponse]),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
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


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
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


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
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


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
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
