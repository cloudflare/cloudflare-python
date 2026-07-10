# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.ai_gateway.billing import spending_limit_create_params
from ....types.ai_gateway.billing.spending_limit_get_response import SpendingLimitGetResponse

__all__ = ["SpendingLimitResource", "AsyncSpendingLimitResource"]


class SpendingLimitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpendingLimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SpendingLimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpendingLimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SpendingLimitResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        account_id: str,
        amount: int,
        duration: Literal["daily", "weekly", "monthly"],
        strategy: Literal["fixed", "sliding"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deprecated: spending limits can no longer be created, enabled, or modified and
        this endpoint always responds 403. Use the new AI Gateway spend limits instead:
        https://developers.cloudflare.com/ai-gateway/features/spend-limits/. Existing
        limits can be removed via DELETE /spending-limit.

        Args:
          amount: Spending limit amount in cents (min 100).

          duration: Spending limit duration.

          strategy: Spending limit strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            body=maybe_transform(
                {
                    "amount": amount,
                    "duration": duration,
                    "strategy": strategy,
                },
                spending_limit_create_params.SpendingLimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Remove the spending limit for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendingLimitGetResponse:
        """
        Retrieve the current spending limit configuration for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendingLimitGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendingLimitGetResponse], ResultWrapper[SpendingLimitGetResponse]),
        )


class AsyncSpendingLimitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpendingLimitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpendingLimitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpendingLimitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSpendingLimitResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        duration: Literal["daily", "weekly", "monthly"],
        strategy: Literal["fixed", "sliding"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deprecated: spending limits can no longer be created, enabled, or modified and
        this endpoint always responds 403. Use the new AI Gateway spend limits instead:
        https://developers.cloudflare.com/ai-gateway/features/spend-limits/. Existing
        limits can be removed via DELETE /spending-limit.

        Args:
          amount: Spending limit amount in cents (min 100).

          duration: Spending limit duration.

          strategy: Spending limit strategy.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "duration": duration,
                    "strategy": strategy,
                },
                spending_limit_create_params.SpendingLimitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Remove the spending limit for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[object]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpendingLimitGetResponse:
        """
        Retrieve the current spending limit configuration for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/ai-gateway/billing/spending-limit", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SpendingLimitGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SpendingLimitGetResponse], ResultWrapper[SpendingLimitGetResponse]),
        )


class SpendingLimitResourceWithRawResponse:
    def __init__(self, spending_limit: SpendingLimitResource) -> None:
        self._spending_limit = spending_limit

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                spending_limit.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_raw_response_wrapper(
            spending_limit.delete,
        )
        self.get = to_raw_response_wrapper(
            spending_limit.get,
        )


class AsyncSpendingLimitResourceWithRawResponse:
    def __init__(self, spending_limit: AsyncSpendingLimitResource) -> None:
        self._spending_limit = spending_limit

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                spending_limit.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_raw_response_wrapper(
            spending_limit.delete,
        )
        self.get = async_to_raw_response_wrapper(
            spending_limit.get,
        )


class SpendingLimitResourceWithStreamingResponse:
    def __init__(self, spending_limit: SpendingLimitResource) -> None:
        self._spending_limit = spending_limit

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                spending_limit.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_streamed_response_wrapper(
            spending_limit.delete,
        )
        self.get = to_streamed_response_wrapper(
            spending_limit.get,
        )


class AsyncSpendingLimitResourceWithStreamingResponse:
    def __init__(self, spending_limit: AsyncSpendingLimitResource) -> None:
        self._spending_limit = spending_limit

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                spending_limit.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_streamed_response_wrapper(
            spending_limit.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            spending_limit.get,
        )
