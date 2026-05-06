# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.ai_gateway.billing import topup_create_params, topup_status_params
from .....types.ai_gateway.billing.topup_create_response import TopupCreateResponse
from .....types.ai_gateway.billing.topup_status_response import TopupStatusResponse

__all__ = ["TopupResource", "AsyncTopupResource"]


class TopupResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TopupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TopupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupCreateResponse:
        """
        Create a credit top-up via Stripe PaymentIntent for the given account.

        Args:
          amount: Top-up amount in cents (min 1000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup", account_id=account_id),
            body=maybe_transform({"amount": amount}, topup_create_params.TopupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TopupCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopupCreateResponse], ResultWrapper[TopupCreateResponse]),
        )

    def status(
        self,
        *,
        account_id: str,
        payment_intent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupStatusResponse:
        """
        Get the payment processing status of a top-up by its invoice ID.

        Args:
          payment_intent_id: Stripe invoice ID to check status for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/status", account_id=account_id),
            body=maybe_transform({"payment_intent_id": payment_intent_id}, topup_status_params.TopupStatusParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TopupStatusResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopupStatusResponse], ResultWrapper[TopupStatusResponse]),
        )


class AsyncTopupResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTopupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupCreateResponse:
        """
        Create a credit top-up via Stripe PaymentIntent for the given account.

        Args:
          amount: Top-up amount in cents (min 1000).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup", account_id=account_id),
            body=await async_maybe_transform({"amount": amount}, topup_create_params.TopupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TopupCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopupCreateResponse], ResultWrapper[TopupCreateResponse]),
        )

    async def status(
        self,
        *,
        account_id: str,
        payment_intent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TopupStatusResponse:
        """
        Get the payment processing status of a top-up by its invoice ID.

        Args:
          payment_intent_id: Stripe invoice ID to check status for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/ai-gateway/billing/topup/status", account_id=account_id),
            body=await async_maybe_transform(
                {"payment_intent_id": payment_intent_id}, topup_status_params.TopupStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TopupStatusResponse]._unwrapper,
            ),
            cast_to=cast(Type[TopupStatusResponse], ResultWrapper[TopupStatusResponse]),
        )


class TopupResourceWithRawResponse:
    def __init__(self, topup: TopupResource) -> None:
        self._topup = topup

        self.create = to_raw_response_wrapper(
            topup.create,
        )
        self.status = to_raw_response_wrapper(
            topup.status,
        )

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._topup.config)


class AsyncTopupResourceWithRawResponse:
    def __init__(self, topup: AsyncTopupResource) -> None:
        self._topup = topup

        self.create = async_to_raw_response_wrapper(
            topup.create,
        )
        self.status = async_to_raw_response_wrapper(
            topup.status,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._topup.config)


class TopupResourceWithStreamingResponse:
    def __init__(self, topup: TopupResource) -> None:
        self._topup = topup

        self.create = to_streamed_response_wrapper(
            topup.create,
        )
        self.status = to_streamed_response_wrapper(
            topup.status,
        )

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._topup.config)


class AsyncTopupResourceWithStreamingResponse:
    def __init__(self, topup: AsyncTopupResource) -> None:
        self._topup = topup

        self.create = async_to_streamed_response_wrapper(
            topup.create,
        )
        self.status = async_to_streamed_response_wrapper(
            topup.status,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._topup.config)
