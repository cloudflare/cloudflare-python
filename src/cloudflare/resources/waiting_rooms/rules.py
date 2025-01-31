# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.waiting_rooms import rule_edit_params, rule_create_params, rule_update_params
from ...types.waiting_rooms.waiting_room_rule import WaitingRoomRule

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

    def create(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        rules: rule_create_params.Rules,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoomRule]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=SyncSinglePage[WaitingRoomRule],
            body=maybe_transform(rules, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="post",
        )

    def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        rules: Iterable[rule_update_params.Rule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoomRule]:
        """Only available for the Waiting Room Advanced subscription.

        Replaces all rules
        for a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=SyncSinglePage[WaitingRoomRule],
            body=maybe_transform(rules, Iterable[rule_update_params.Rule]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="put",
        )

    def delete(
        self,
        rule_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoomRule]:
        """
        Deletes a rule for a waiting room.

        Args:
          zone_id: Identifier

          rule_id: The ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            page=SyncSinglePage[WaitingRoomRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="delete",
        )

    def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        position: rule_edit_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoomRule]:
        """
        Patches a rule for a waiting room.

        Args:
          zone_id: Identifier

          rule_id: The ID of the rule.

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          position: Reorder the position of a rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            page=SyncSinglePage[WaitingRoomRule],
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                    "position": position,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="patch",
        )

    def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[WaitingRoomRule]:
        """
        Lists rules for a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=SyncSinglePage[WaitingRoomRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
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

    def create(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        rules: rule_create_params.Rules,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoomRule, AsyncSinglePage[WaitingRoomRule]]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=AsyncSinglePage[WaitingRoomRule],
            body=maybe_transform(rules, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="post",
        )

    def update(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        rules: Iterable[rule_update_params.Rule],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoomRule, AsyncSinglePage[WaitingRoomRule]]:
        """Only available for the Waiting Room Advanced subscription.

        Replaces all rules
        for a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=AsyncSinglePage[WaitingRoomRule],
            body=maybe_transform(rules, Iterable[rule_update_params.Rule]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="put",
        )

    def delete(
        self,
        rule_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoomRule, AsyncSinglePage[WaitingRoomRule]]:
        """
        Deletes a rule for a waiting room.

        Args:
          zone_id: Identifier

          rule_id: The ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            page=AsyncSinglePage[WaitingRoomRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="delete",
        )

    def edit(
        self,
        rule_id: str,
        *,
        zone_id: str,
        waiting_room_id: str,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        position: rule_edit_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoomRule, AsyncSinglePage[WaitingRoomRule]]:
        """
        Patches a rule for a waiting room.

        Args:
          zone_id: Identifier

          rule_id: The ID of the rule.

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          position: Reorder the position of a rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            page=AsyncSinglePage[WaitingRoomRule],
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                    "position": position,
                },
                rule_edit_params.RuleEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
            method="patch",
        )

    def get(
        self,
        waiting_room_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[WaitingRoomRule, AsyncSinglePage[WaitingRoomRule]]:
        """
        Lists rules for a waiting room.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not waiting_room_id:
            raise ValueError(f"Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            page=AsyncSinglePage[WaitingRoomRule],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=WaitingRoomRule,
        )


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.update = to_raw_response_wrapper(
            rules.update,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.update = async_to_raw_response_wrapper(
            rules.update,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.update = to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.update = async_to_streamed_response_wrapper(
            rules.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )
