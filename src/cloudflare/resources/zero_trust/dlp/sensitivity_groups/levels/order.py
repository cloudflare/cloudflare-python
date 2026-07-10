# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ......_types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import make_request_options
from ......types.zero_trust.dlp.sensitivity_groups.levels import order_update_params
from ......types.zero_trust.dlp.sensitivity_groups.levels.order_get_response import OrderGetResponse
from ......types.zero_trust.dlp.sensitivity_groups.levels.order_update_response import OrderUpdateResponse

__all__ = ["OrderResource", "AsyncOrderResource"]


class OrderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OrderResourceWithStreamingResponse(self)

    def update(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        level_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OrderUpdateResponse]:
        """
        Updates the order of sensitivity levels in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=maybe_transform({"level_ids": level_ids}, order_update_params.OrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderUpdateResponse]], ResultWrapper[OrderUpdateResponse]),
        )

    def get(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OrderGetResponse]:
        """
        Gets the current order of sensitivity levels in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderGetResponse]], ResultWrapper[OrderGetResponse]),
        )


class AsyncOrderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOrderResourceWithStreamingResponse(self)

    async def update(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        level_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OrderUpdateResponse]:
        """
        Updates the order of sensitivity levels in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return await self._put(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            body=await async_maybe_transform({"level_ids": level_ids}, order_update_params.OrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderUpdateResponse]], ResultWrapper[OrderUpdateResponse]),
        )

    async def get(
        self,
        sensitivity_group_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[OrderGetResponse]:
        """
        Gets the current order of sensitivity levels in a group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not sensitivity_group_id:
            raise ValueError(
                f"Expected a non-empty value for `sensitivity_group_id` but received {sensitivity_group_id!r}"
            )
        return await self._get(
            path_template(
                "/accounts/{account_id}/dlp/sensitivity_groups/{sensitivity_group_id}/level_order",
                account_id=account_id,
                sensitivity_group_id=sensitivity_group_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OrderGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OrderGetResponse]], ResultWrapper[OrderGetResponse]),
        )


class OrderResourceWithRawResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.update = to_raw_response_wrapper(
            order.update,
        )
        self.get = to_raw_response_wrapper(
            order.get,
        )


class AsyncOrderResourceWithRawResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.update = async_to_raw_response_wrapper(
            order.update,
        )
        self.get = async_to_raw_response_wrapper(
            order.get,
        )


class OrderResourceWithStreamingResponse:
    def __init__(self, order: OrderResource) -> None:
        self._order = order

        self.update = to_streamed_response_wrapper(
            order.update,
        )
        self.get = to_streamed_response_wrapper(
            order.get,
        )


class AsyncOrderResourceWithStreamingResponse:
    def __init__(self, order: AsyncOrderResource) -> None:
        self._order = order

        self.update = async_to_streamed_response_wrapper(
            order.update,
        )
        self.get = async_to_streamed_response_wrapper(
            order.get,
        )
