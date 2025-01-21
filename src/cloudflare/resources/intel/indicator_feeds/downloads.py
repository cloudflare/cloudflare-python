# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

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
from ...._base_client import make_request_options
from ....types.intel.indicator_feeds.download_get_response import DownloadGetResponse

__all__ = ["DownloadsResource", "AsyncDownloadsResource"]


class DownloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DownloadsResourceWithStreamingResponse(self)

    def get(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DownloadGetResponse]:
        """
        Download indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/intel/indicator_feeds/{feed_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DownloadGetResponse]], ResultWrapper[DownloadGetResponse]),
        )


class AsyncDownloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDownloadsResourceWithStreamingResponse(self)

    async def get(
        self,
        feed_id: int,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[DownloadGetResponse]:
        """
        Download indicator feed data

        Args:
          account_id: Identifier

          feed_id: Indicator feed ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/intel/indicator_feeds/{feed_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[DownloadGetResponse]], ResultWrapper[DownloadGetResponse]),
        )


class DownloadsResourceWithRawResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.get = to_raw_response_wrapper(
            downloads.get,
        )


class AsyncDownloadsResourceWithRawResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.get = async_to_raw_response_wrapper(
            downloads.get,
        )


class DownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.get = to_streamed_response_wrapper(
            downloads.get,
        )


class AsyncDownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.get = async_to_streamed_response_wrapper(
            downloads.get,
        )
