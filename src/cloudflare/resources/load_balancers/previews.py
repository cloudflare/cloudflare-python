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
from ..._base_client import make_request_options
from ...types.load_balancers.preview_get_response import PreviewGetResponse

__all__ = ["PreviewsResource", "AsyncPreviewsResource"]


class PreviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PreviewsResourceWithStreamingResponse(self)

    def get(
        self,
        preview_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
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
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )


class AsyncPreviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPreviewsResourceWithStreamingResponse(self)

    async def get(
        self,
        preview_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PreviewGetResponse:
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
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/preview/{preview_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PreviewGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[PreviewGetResponse], ResultWrapper[PreviewGetResponse]),
        )


class PreviewsResourceWithRawResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.get = to_raw_response_wrapper(
            previews.get,
        )


class AsyncPreviewsResourceWithRawResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.get = async_to_raw_response_wrapper(
            previews.get,
        )


class PreviewsResourceWithStreamingResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.get = to_streamed_response_wrapper(
            previews.get,
        )


class AsyncPreviewsResourceWithStreamingResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.get = async_to_streamed_response_wrapper(
            previews.get,
        )
