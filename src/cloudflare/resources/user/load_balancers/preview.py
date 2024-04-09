# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ....types.user.load_balancers import Preview

__all__ = ["PreviewResource", "AsyncPreviewResource"]


class PreviewResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewResourceWithRawResponse:
        return PreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewResourceWithStreamingResponse:
        return PreviewResourceWithStreamingResponse(self)

    def get(
        self,
        preview_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Preview:
        """
        Get the result of a previous preview operation using the provided preview_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return self._get(
            f"/user/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Preview], ResultWrapper[Preview]),
        )


class AsyncPreviewResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewResourceWithRawResponse:
        return AsyncPreviewResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewResourceWithStreamingResponse:
        return AsyncPreviewResourceWithStreamingResponse(self)

    async def get(
        self,
        preview_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Preview:
        """
        Get the result of a previous preview operation using the provided preview_id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return await self._get(
            f"/user/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Preview], ResultWrapper[Preview]),
        )


class PreviewResourceWithRawResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.get = to_raw_response_wrapper(
            preview.get,
        )


class AsyncPreviewResourceWithRawResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.get = async_to_raw_response_wrapper(
            preview.get,
        )


class PreviewResourceWithStreamingResponse:
    def __init__(self, preview: PreviewResource) -> None:
        self._preview = preview

        self.get = to_streamed_response_wrapper(
            preview.get,
        )


class AsyncPreviewResourceWithStreamingResponse:
    def __init__(self, preview: AsyncPreviewResource) -> None:
        self._preview = preview

        self.get = async_to_streamed_response_wrapper(
            preview.get,
        )
