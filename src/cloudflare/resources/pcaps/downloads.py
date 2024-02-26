# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Downloads", "AsyncDownloads"]


class Downloads(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsWithRawResponse:
        return DownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsWithStreamingResponse:
        return DownloadsWithStreamingResponse(self)

    def get(
        self,
        pcap_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """Download PCAP information into a file.

        Response is a binary PCAP file.

        Args:
          account_id: Identifier

          pcap_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pcap_id:
            raise ValueError(f"Expected a non-empty value for `pcap_id` but received {pcap_id!r}")
        extra_headers = {"Accept": "application/vnd.tcpdump.pcap", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/pcaps/{pcap_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncDownloads(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsWithRawResponse:
        return AsyncDownloadsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsWithStreamingResponse:
        return AsyncDownloadsWithStreamingResponse(self)

    async def get(
        self,
        pcap_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """Download PCAP information into a file.

        Response is a binary PCAP file.

        Args:
          account_id: Identifier

          pcap_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pcap_id:
            raise ValueError(f"Expected a non-empty value for `pcap_id` but received {pcap_id!r}")
        extra_headers = {"Accept": "application/vnd.tcpdump.pcap", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/pcaps/{pcap_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class DownloadsWithRawResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.get = to_custom_raw_response_wrapper(
            downloads.get,
            BinaryAPIResponse,
        )


class AsyncDownloadsWithRawResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.get = async_to_custom_raw_response_wrapper(
            downloads.get,
            AsyncBinaryAPIResponse,
        )


class DownloadsWithStreamingResponse:
    def __init__(self, downloads: Downloads) -> None:
        self._downloads = downloads

        self.get = to_custom_streamed_response_wrapper(
            downloads.get,
            StreamedBinaryAPIResponse,
        )


class AsyncDownloadsWithStreamingResponse:
    def __init__(self, downloads: AsyncDownloads) -> None:
        self._downloads = downloads

        self.get = async_to_custom_streamed_response_wrapper(
            downloads.get,
            AsyncStreamedBinaryAPIResponse,
        )
