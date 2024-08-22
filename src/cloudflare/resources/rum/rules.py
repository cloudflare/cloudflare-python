# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.rum.rum_rule import RUMRule

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type, List

from ..._base_client import make_request_options

from ...types.rum.rule_list_response import RuleListResponse

from ...types.rum.rule_delete_response import RuleDeleteResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.rum import rule_create_params
from ...types.rum import rule_update_params
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
    ruleset_id: str,
    *,
    account_id: str,
    host: str | NotGiven = NOT_GIVEN,
    inclusive: bool | NotGiven = NOT_GIVEN,
    is_paused: bool | NotGiven = NOT_GIVEN,
    paths: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RUMRule]:
        """
        Creates a new rule in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          inclusive: Whether the rule includes or excludes traffic from being measured.

          is_paused: Whether the rule is paused or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule",
            body=maybe_transform({
                "host": host,
                "inclusive": inclusive,
                "is_paused": is_paused,
                "paths": paths,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RUMRule]]._unwrapper),
            cast_to=cast(Type[Optional[RUMRule]], ResultWrapper[RUMRule]),
        )

    def update(self,
    rule_id: str,
    *,
    account_id: str,
    ruleset_id: str,
    host: str | NotGiven = NOT_GIVEN,
    inclusive: bool | NotGiven = NOT_GIVEN,
    is_paused: bool | NotGiven = NOT_GIVEN,
    paths: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RUMRule]:
        """
        Updates a rule in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          rule_id: The Web Analytics rule identifier.

          inclusive: Whether the rule includes or excludes traffic from being measured.

          is_paused: Whether the rule is paused or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}",
            body=maybe_transform({
                "host": host,
                "inclusive": inclusive,
                "is_paused": is_paused,
                "paths": paths,
            }, rule_update_params.RuleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RUMRule]]._unwrapper),
            cast_to=cast(Type[Optional[RUMRule]], ResultWrapper[RUMRule]),
        )

    def list(self,
    ruleset_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleListResponse]:
        """
        Lists all the rules in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleListResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleListResponse]], ResultWrapper[RuleListResponse]),
        )

    def delete(self,
    rule_id: str,
    *,
    account_id: str,
    ruleset_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleDeleteResponse]:
        """
        Deletes an existing rule from a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          rule_id: The Web Analytics rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
        )

class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(self,
    ruleset_id: str,
    *,
    account_id: str,
    host: str | NotGiven = NOT_GIVEN,
    inclusive: bool | NotGiven = NOT_GIVEN,
    is_paused: bool | NotGiven = NOT_GIVEN,
    paths: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RUMRule]:
        """
        Creates a new rule in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          inclusive: Whether the rule includes or excludes traffic from being measured.

          is_paused: Whether the rule is paused or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule",
            body=await async_maybe_transform({
                "host": host,
                "inclusive": inclusive,
                "is_paused": is_paused,
                "paths": paths,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RUMRule]]._unwrapper),
            cast_to=cast(Type[Optional[RUMRule]], ResultWrapper[RUMRule]),
        )

    async def update(self,
    rule_id: str,
    *,
    account_id: str,
    ruleset_id: str,
    host: str | NotGiven = NOT_GIVEN,
    inclusive: bool | NotGiven = NOT_GIVEN,
    is_paused: bool | NotGiven = NOT_GIVEN,
    paths: List[str] | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RUMRule]:
        """
        Updates a rule in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          rule_id: The Web Analytics rule identifier.

          inclusive: Whether the rule includes or excludes traffic from being measured.

          is_paused: Whether the rule is paused or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}",
            body=await async_maybe_transform({
                "host": host,
                "inclusive": inclusive,
                "is_paused": is_paused,
                "paths": paths,
            }, rule_update_params.RuleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RUMRule]]._unwrapper),
            cast_to=cast(Type[Optional[RUMRule]], ResultWrapper[RUMRule]),
        )

    async def list(self,
    ruleset_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleListResponse]:
        """
        Lists all the rules in a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rules",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleListResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleListResponse]], ResultWrapper[RuleListResponse]),
        )

    async def delete(self,
    rule_id: str,
    *,
    account_id: str,
    ruleset_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[RuleDeleteResponse]:
        """
        Deletes an existing rule from a Web Analytics ruleset.

        Args:
          account_id: Identifier

          ruleset_id: The Web Analytics ruleset identifier.

          rule_id: The Web Analytics rule identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/rum/v2/{ruleset_id}/rule/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[RuleDeleteResponse]]._unwrapper),
            cast_to=cast(Type[Optional[RuleDeleteResponse]], ResultWrapper[RuleDeleteResponse]),
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
        self.list = to_raw_response_wrapper(
            rules.list,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
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
        self.list = async_to_raw_response_wrapper(
            rules.list,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
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
        self.list = to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
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
        self.list = async_to_streamed_response_wrapper(
            rules.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )