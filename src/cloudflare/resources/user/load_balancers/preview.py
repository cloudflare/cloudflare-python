# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.user.load_balancers import LoadBalancingPreviewResult

__all__ = ["Preview", "AsyncPreview"]


class Preview(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewWithRawResponse:
        return PreviewWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewWithStreamingResponse:
        return PreviewWithStreamingResponse(self)

    def get(
        self,
        preview_id: object,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/user/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPreviewResult], ResultWrapper[LoadBalancingPreviewResult]),
        )


class AsyncPreview(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewWithRawResponse:
        return AsyncPreviewWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewWithStreamingResponse:
        return AsyncPreviewWithStreamingResponse(self)

    async def get(
        self,
        preview_id: object,
        *,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/user/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[LoadBalancingPreviewResult], ResultWrapper[LoadBalancingPreviewResult]),
        )


class PreviewWithRawResponse:
    def __init__(self, preview: Preview) -> None:
        self._preview = preview

        self.get = to_raw_response_wrapper(
            preview.get,
        )


class AsyncPreviewWithRawResponse:
    def __init__(self, preview: AsyncPreview) -> None:
        self._preview = preview

        self.get = async_to_raw_response_wrapper(
            preview.get,
        )


class PreviewWithStreamingResponse:
    def __init__(self, preview: Preview) -> None:
        self._preview = preview

        self.get = to_streamed_response_wrapper(
            preview.get,
        )


class AsyncPreviewWithStreamingResponse:
    def __init__(self, preview: AsyncPreview) -> None:
        self._preview = preview

        self.get = async_to_streamed_response_wrapper(
            preview.get,
        )
