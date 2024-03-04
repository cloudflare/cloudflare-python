# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

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
from ...._base_client import (
    make_request_options,
)
from ....types.user.tokens import value_update_params

__all__ = ["Value", "AsyncValue"]


class Value(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValueWithRawResponse:
        return ValueWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValueWithStreamingResponse:
        return ValueWithStreamingResponse(self)

    def update(
        self,
        token_id: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Roll the token secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/user/tokens/{token_id}/value",
            body=maybe_transform(body, value_update_params.ValueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class AsyncValue(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValueWithRawResponse:
        return AsyncValueWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValueWithStreamingResponse:
        return AsyncValueWithStreamingResponse(self)

    async def update(
        self,
        token_id: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Roll the token secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/user/tokens/{token_id}/value",
            body=await async_maybe_transform(body, value_update_params.ValueUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[str], ResultWrapper[str]),
        )


class ValueWithRawResponse:
    def __init__(self, value: Value) -> None:
        self._value = value

        self.update = to_raw_response_wrapper(
            value.update,
        )


class AsyncValueWithRawResponse:
    def __init__(self, value: AsyncValue) -> None:
        self._value = value

        self.update = async_to_raw_response_wrapper(
            value.update,
        )


class ValueWithStreamingResponse:
    def __init__(self, value: Value) -> None:
        self._value = value

        self.update = to_streamed_response_wrapper(
            value.update,
        )


class AsyncValueWithStreamingResponse:
    def __init__(self, value: AsyncValue) -> None:
        self._value = value

        self.update = async_to_streamed_response_wrapper(
            value.update,
        )
