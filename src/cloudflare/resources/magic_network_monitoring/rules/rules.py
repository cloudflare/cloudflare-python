# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .advertisements import AdvertisementsResource, AsyncAdvertisementsResource

from ...._compat import cached_property

from ....types.magic_network_monitoring.magic_network_monitoring_rule import MagicNetworkMonitoringRule

from ...._wrappers import ResultWrapper

from ...._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ...._base_client import make_request_options, AsyncPaginator

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.magic_network_monitoring import rule_create_params
from ....types.magic_network_monitoring import rule_update_params
from ....types.magic_network_monitoring import rule_edit_params
from .advertisements import AdvertisementsResource, AsyncAdvertisementsResource, AdvertisementsResourceWithRawResponse, AsyncAdvertisementsResourceWithRawResponse, AdvertisementsResourceWithStreamingResponse, AsyncAdvertisementsResourceWithStreamingResponse
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
    def advertisements(self) -> AdvertisementsResource:
        return AdvertisementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)

    def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(body, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def update(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(body, rule_update_params.RuleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Optional[MagicNetworkMonitoringRule]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page = SyncSinglePage[Optional[MagicNetworkMonitoringRule]],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=MagicNetworkMonitoringRule,
        )

    def delete(self,
    rule_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Delete a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def edit(self,
    rule_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=maybe_transform(body, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def get(self,
    rule_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        List a single network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResource:
        return AsyncAdvertisementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    async def create(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """Create network monitoring rules for account.

        Currently only supports creating a
        single rule per API request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(body, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def update(self,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(body, rule_update_params.RuleUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Optional[MagicNetworkMonitoringRule], AsyncSinglePage[Optional[MagicNetworkMonitoringRule]]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page = AsyncSinglePage[Optional[MagicNetworkMonitoringRule]],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=MagicNetworkMonitoringRule,
        )

    async def delete(self,
    rule_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Delete a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def edit(self,
    rule_id: str,
    *,
    account_id: str,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update a network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=await async_maybe_transform(body, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def get(self,
    rule_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[MagicNetworkMonitoringRule]:
        """
        List a single network monitoring rule for account.

        Args:
          rule_id: The id of the rule. Must be unique.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
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
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )
        self.get = to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsResourceWithRawResponse:
        return AdvertisementsResourceWithRawResponse(self._rules.advertisements)

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
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )
        self.get = async_to_raw_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResourceWithRawResponse:
        return AsyncAdvertisementsResourceWithRawResponse(self._rules.advertisements)

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
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AdvertisementsResourceWithStreamingResponse:
        return AdvertisementsResourceWithStreamingResponse(self._rules.advertisements)

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
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            rules.get,
        )

    @cached_property
    def advertisements(self) -> AsyncAdvertisementsResourceWithStreamingResponse:
        return AsyncAdvertisementsResourceWithStreamingResponse(self._rules.advertisements)