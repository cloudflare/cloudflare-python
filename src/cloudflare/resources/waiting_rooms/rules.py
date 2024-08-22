# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.waiting_rooms.rule_create_response import RuleCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, Iterable

from ..._base_client import make_request_options

from typing_extensions import Literal

from ...types.waiting_rooms.rule_update_response import RuleUpdateResponse

from ...types.waiting_rooms.rule_delete_response import RuleDeleteResponse

from ...types.waiting_rooms.rule_edit_response import RuleEditResponse

from ...types.waiting_rooms.rule_get_response import RuleGetResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.waiting_rooms import rule_update_params, rule_edit_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.waiting_rooms import rule_create_params
from ...types.waiting_rooms import rule_update_params
from ...types.waiting_rooms import rule_edit_params
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

__all__ = ["RulesResource", "AsyncRulesResource"]

class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)

    def create(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    action: Literal["bypass_waiting_room"],
    expression: str,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleCreateResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_id: Identifier

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return self._post(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform({
                "action": action,
                "expression": expression,
                "description": description,
                "enabled": enabled,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    def update(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    body: Iterable[rule_update_params.Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            body=maybe_transform(body, Iterable[rule_update_params.Body]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    def delete(self,
    rule_id: str,
    *,
    zone_id: str,
    waiting_room_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleDeleteResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    def edit(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleEditResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            body=maybe_transform({
                "action": action,
                "expression": expression,
                "description": description,
                "enabled": enabled,
                "position": position,
            }, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleEditResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleEditResponse]], ResultWrapper[RuleEditResponse]),
        )

    def get(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
        )

class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    action: Literal["bypass_waiting_room"],
    expression: str,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleCreateResponse]:
        """Only available for the Waiting Room Advanced subscription.

        Creates a rule for a
        waiting room.

        Args:
          zone_id: Identifier

          action: The action to take when the expression matches.

          expression: Criteria defining when there is a match for the current rule.

          description: The description of the rule.

          enabled: When set to true, the rule is enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return await self._post(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            body=await async_maybe_transform({
                "action": action,
                "expression": expression,
                "description": description,
                "enabled": enabled,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleCreateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleCreateResponse]], ResultWrapper[RuleCreateResponse]),
        )

    async def update(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    body: Iterable[rule_update_params.Body],
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleUpdateResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return await self._put(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            body=await async_maybe_transform(body, Iterable[rule_update_params.Body]),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleUpdateResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleUpdateResponse]], ResultWrapper[RuleUpdateResponse]),
        )

    async def delete(self,
    rule_id: str,
    *,
    zone_id: str,
    waiting_room_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleDeleteResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._delete(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

    async def edit(self,
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
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleEditResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._patch(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules/{rule_id}",
            body=await async_maybe_transform({
                "action": action,
                "expression": expression,
                "description": description,
                "enabled": enabled,
                "position": position,
            }, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleEditResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleEditResponse]], ResultWrapper[RuleEditResponse]),
        )

    async def get(self,
    waiting_room_id: str,
    *,
    zone_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `zone_id` but received {zone_id!r}'
          )
        if not waiting_room_id:
          raise ValueError(
            f'Expected a non-empty value for `waiting_room_id` but received {waiting_room_id!r}'
          )
        return await self._get(
            f"/zones/{zone_id}/waiting_rooms/{waiting_room_id}/rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleGetResponse]], ResultWrapper[RuleGetResponse]),
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