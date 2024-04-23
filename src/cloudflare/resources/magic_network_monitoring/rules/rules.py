# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from .advertisements import (
    Advertisements,
    AsyncAdvertisements,
    AdvertisementsWithRawResponse,
    AsyncAdvertisementsWithRawResponse,
    AdvertisementsWithStreamingResponse,
    AsyncAdvertisementsWithStreamingResponse,
)
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.magic_network_monitoring import (
    rule_edit_params,
    rule_create_params,
    rule_delete_params,
    rule_update_params,
)
from ....types.magic_network_monitoring.magic_network_monitoring_rule import MagicNetworkMonitoringRule

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def advertisements(self) -> Advertisements:
        return Advertisements(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(body, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def update(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=maybe_transform(body, rule_update_params.RuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Optional[MagicNetworkMonitoringRule]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page=SyncSinglePage[Optional[MagicNetworkMonitoringRule]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MagicNetworkMonitoringRule,
        )

    def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=maybe_transform(body, rule_delete_params.RuleDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=maybe_transform(body, rule_edit_params.RuleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )


class AsyncRules(AsyncAPIResource):
    @cached_property
    def advertisements(self) -> AsyncAdvertisements:
        return AsyncAdvertisements(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(body, rule_create_params.RuleCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def update(
        self,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
        """
        Update network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._put(
            f"/accounts/{account_id}/mnm/rules",
            body=await async_maybe_transform(body, rule_update_params.RuleUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    def list(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Optional[MagicNetworkMonitoringRule], AsyncSinglePage[Optional[MagicNetworkMonitoringRule]]]:
        """
        Lists network monitoring rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/mnm/rules",
            page=AsyncSinglePage[Optional[MagicNetworkMonitoringRule]],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=MagicNetworkMonitoringRule,
        )

    async def delete(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=await async_maybe_transform(body, rule_delete_params.RuleDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def edit(
        self,
        rule_id: str,
        *,
        account_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            body=await async_maybe_transform(body, rule_edit_params.RuleEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )

    async def get(
        self,
        rule_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MagicNetworkMonitoringRule]:
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
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not rule_id:
            raise ValueError(f"Expected a non-empty value for `rule_id` but received {rule_id!r}")
        return await self._get(
            f"/accounts/{account_id}/mnm/rules/{rule_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MagicNetworkMonitoringRule]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MagicNetworkMonitoringRule]], ResultWrapper[MagicNetworkMonitoringRule]),
        )


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
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
    def advertisements(self) -> AdvertisementsWithRawResponse:
        return AdvertisementsWithRawResponse(self._rules.advertisements)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
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
    def advertisements(self) -> AsyncAdvertisementsWithRawResponse:
        return AsyncAdvertisementsWithRawResponse(self._rules.advertisements)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
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
    def advertisements(self) -> AdvertisementsWithStreamingResponse:
        return AdvertisementsWithStreamingResponse(self._rules.advertisements)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
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
    def advertisements(self) -> AsyncAdvertisementsWithStreamingResponse:
        return AsyncAdvertisementsWithStreamingResponse(self._rules.advertisements)
