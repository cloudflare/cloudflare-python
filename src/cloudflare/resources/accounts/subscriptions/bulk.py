# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import make_request_options
from ....types.accounts.subscriptions import bulk_create_params
from ....types.shared_params.subscription import Subscription
from ....types.accounts.subscriptions.bulk_create_response import BulkCreateResponse

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        idemp_key: str | Omit = omit,
        coupon_code: str | Omit = omit,
        payment_hold_id: int | Omit = omit,
        subscriptions: Iterable[Subscription] | Omit = omit,
        user_is_on_session: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """
        Creates multiple subscriptions for an account in a single request.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/bulk/subscriptions", account_id=account_id),
            body=maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "payment_hold_id": payment_hold_id,
                    "subscriptions": subscriptions,
                    "user_is_on_session": user_is_on_session,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"idemp_key": idemp_key}, bulk_create_params.BulkCreateParams),
                post_parser=ResultWrapper[BulkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkCreateResponse], ResultWrapper[BulkCreateResponse]),
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        idemp_key: str | Omit = omit,
        coupon_code: str | Omit = omit,
        payment_hold_id: int | Omit = omit,
        subscriptions: Iterable[Subscription] | Omit = omit,
        user_is_on_session: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkCreateResponse:
        """
        Creates multiple subscriptions for an account in a single request.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/bulk/subscriptions", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "coupon_code": coupon_code,
                    "payment_hold_id": payment_hold_id,
                    "subscriptions": subscriptions,
                    "user_is_on_session": user_is_on_session,
                },
                bulk_create_params.BulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"idemp_key": idemp_key}, bulk_create_params.BulkCreateParams),
                post_parser=ResultWrapper[BulkCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[BulkCreateResponse], ResultWrapper[BulkCreateResponse]),
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_raw_response_wrapper(
            bulk.create,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_raw_response_wrapper(
            bulk.create,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.create = to_streamed_response_wrapper(
            bulk.create,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.create = async_to_streamed_response_wrapper(
            bulk.create,
        )
