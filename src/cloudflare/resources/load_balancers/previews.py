# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.user.load_balancers import LoadBalancingPreviewResult

__all__ = ["Previews", "AsyncPreviews"]


class Previews(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self)

    def get(
        self,
        preview_id: object,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPreviewResult:
        """
        Get the result of a previous preview operation using the provided preview_id.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPreviewResult], ResultWrapper[LoadBalancingPreviewResult]),
        )


class AsyncPreviews(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self)

    async def get(
        self,
        preview_id: object,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoadBalancingPreviewResult:
        """
        Get the result of a previous preview operation using the provided preview_id.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPreviewResult], ResultWrapper[LoadBalancingPreviewResult]),
        )


class PreviewsWithRawResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.get = to_raw_response_wrapper(
            previews.get,
        )


class AsyncPreviewsWithRawResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.get = async_to_raw_response_wrapper(
            previews.get,
        )


class PreviewsWithStreamingResponse:
    def __init__(self, previews: Previews) -> None:
        self._previews = previews

        self.get = to_streamed_response_wrapper(
            previews.get,
        )


class AsyncPreviewsWithStreamingResponse:
    def __init__(self, previews: AsyncPreviews) -> None:
        self._previews = previews

        self.get = async_to_streamed_response_wrapper(
            previews.get,
        )
