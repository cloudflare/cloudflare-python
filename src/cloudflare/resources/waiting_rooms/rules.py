# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.waiting_rooms import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleWaitingRoomCreateWaitingRoomRuleResponse,
    RuleWaitingRoomListWaitingRoomRulesResponse,
    RuleWaitingRoomReplaceWaitingRoomRulesResponse,
    rule_update_params,
    rule_waiting_room_replace_waiting_room_rules_params,
)

from typing import Type, Optional, Iterable

from typing_extensions import Literal

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.waiting_rooms import rule_update_params
from ...types.waiting_rooms import rule_waiting_room_create_waiting_room_rule_params
from ...types.waiting_rooms import rule_waiting_room_replace_waiting_room_rules_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def update(
        self,
        rule_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        position: rule_update_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Patches a rule for a waiting room.

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                    "position": position,
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
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(
        self,
        rule_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes a rule for a waiting room.

        Args:
          zone_identifier: Identifier

          rule_id: The ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def waiting_room_create_waiting_room_rule(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_identifier: Identifier

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                },
                rule_waiting_room_create_waiting_room_rule_params.RuleWaitingRoomCreateWaitingRoomRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse]],
                ResultWrapper[RuleWaitingRoomCreateWaitingRoomRuleResponse],
            ),
        )

    def waiting_room_list_waiting_room_rules(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomListWaitingRoomRulesResponse]:
        """
        Lists rules for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomListWaitingRoomRulesResponse]],
                ResultWrapper[RuleWaitingRoomListWaitingRoomRulesResponse],
            ),
        )

    def waiting_room_replace_waiting_room_rules(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        body: Iterable[rule_waiting_room_replace_waiting_room_rules_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Replaces all rules
        for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._put(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform(
                body, rule_waiting_room_replace_waiting_room_rules_params.RuleWaitingRoomReplaceWaitingRoomRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse]],
                ResultWrapper[RuleWaitingRoomReplaceWaitingRoomRulesResponse],
            ),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def update(
        self,
        rule_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        position: rule_update_params.Position | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleUpdateResponse]:
        """
        Patches a rule for a waiting room.

        Args:
          zone_identifier: Identifier

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
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                    "position": position,
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
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(
        self,
        rule_id: str,
        *,
        zone_identifier: str,
        waiting_room_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleDeleteResponse]:
        """
        Deletes a rule for a waiting room.

        Args:
          zone_identifier: Identifier

          rule_id: The ID of the rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def waiting_room_create_waiting_room_rule(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        action: Literal["bypass_waiting_room"],
        expression: str,
        description: str | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_identifier: Identifier

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform(
                {
                    "action": action,
                    "expression": expression,
                    "description": description,
                    "enabled": enabled,
                },
                rule_waiting_room_create_waiting_room_rule_params.RuleWaitingRoomCreateWaitingRoomRuleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomCreateWaitingRoomRuleResponse]],
                ResultWrapper[RuleWaitingRoomCreateWaitingRoomRuleResponse],
            ),
        )

    async def waiting_room_list_waiting_room_rules(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomListWaitingRoomRulesResponse]:
        """
        Lists rules for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomListWaitingRoomRulesResponse]],
                ResultWrapper[RuleWaitingRoomListWaitingRoomRulesResponse],
            ),
        )

    async def waiting_room_replace_waiting_room_rules(
        self,
        waiting_room_id: object,
        *,
        zone_identifier: str,
        body: Iterable[rule_waiting_room_replace_waiting_room_rules_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Replaces all rules
        for a waiting room.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._put(
            f"/zones/{zone_identifier}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform(
                body, rule_waiting_room_replace_waiting_room_rules_params.RuleWaitingRoomReplaceWaitingRoomRulesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[RuleWaitingRoomReplaceWaitingRoomRulesResponse]],
                ResultWrapper[RuleWaitingRoomReplaceWaitingRoomRulesResponse],
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
        self.waiting_room_create_waiting_room_rule = to_raw_response_wrapper(
            rules.waiting_room_create_waiting_room_rule,
        )
        self.waiting_room_list_waiting_room_rules = to_raw_response_wrapper(
            rules.waiting_room_list_waiting_room_rules,
        )
        self.waiting_room_replace_waiting_room_rules = to_raw_response_wrapper(
            rules.waiting_room_replace_waiting_room_rules,
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
        self.waiting_room_create_waiting_room_rule = async_to_raw_response_wrapper(
            rules.waiting_room_create_waiting_room_rule,
        )
        self.waiting_room_list_waiting_room_rules = async_to_raw_response_wrapper(
            rules.waiting_room_list_waiting_room_rules,
        )
        self.waiting_room_replace_waiting_room_rules = async_to_raw_response_wrapper(
            rules.waiting_room_replace_waiting_room_rules,
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
        self.waiting_room_create_waiting_room_rule = to_streamed_response_wrapper(
            rules.waiting_room_create_waiting_room_rule,
        )
        self.waiting_room_list_waiting_room_rules = to_streamed_response_wrapper(
            rules.waiting_room_list_waiting_room_rules,
        )
        self.waiting_room_replace_waiting_room_rules = to_streamed_response_wrapper(
            rules.waiting_room_replace_waiting_room_rules,
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
        self.waiting_room_create_waiting_room_rule = async_to_streamed_response_wrapper(
            rules.waiting_room_create_waiting_room_rule,
        )
        self.waiting_room_list_waiting_room_rules = async_to_streamed_response_wrapper(
            rules.waiting_room_list_waiting_room_rules,
        )
        self.waiting_room_replace_waiting_room_rules = async_to_streamed_response_wrapper(
            rules.waiting_room_replace_waiting_room_rules,
        )
