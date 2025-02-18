# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....._base_client import make_request_options

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
        filename: str,
        *,
        account_id: str,
        command_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Downloads artifacts for an executed command.

        Bulk downloads are not supported

        Args:
          command_id: Unique identifier for a command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not command_id:
            raise ValueError(f"Expected a non-empty value for `command_id` but received {command_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
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
        filename: str,
        *,
        account_id: str,
        command_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Downloads artifacts for an executed command.

        Bulk downloads are not supported

        Args:
          command_id: Unique identifier for a command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not command_id:
            raise ValueError(f"Expected a non-empty value for `command_id` but received {command_id!r}")
        if not filename:
            raise ValueError(f"Expected a non-empty value for `filename` but received {filename!r}")
        extra_headers = {"Accept": "application/zip", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class DownloadsResourceWithRawResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.get = to_custom_raw_response_wrapper(
            downloads.get,
            BinaryAPIResponse,
        )


class AsyncDownloadsResourceWithRawResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.get = async_to_custom_raw_response_wrapper(
            downloads.get,
            AsyncBinaryAPIResponse,
        )


class DownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: DownloadsResource) -> None:
        self._downloads = downloads

        self.get = to_custom_streamed_response_wrapper(
            downloads.get,
            StreamedBinaryAPIResponse,
        )


class AsyncDownloadsResourceWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloadsResource) -> None:
        self._downloads = downloads

        self.get = async_to_custom_streamed_response_wrapper(
            downloads.get,
            AsyncStreamedBinaryAPIResponse,
        )
