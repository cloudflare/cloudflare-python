# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ..._response import BinaryAPIResponse, AsyncBinaryAPIResponse, to_custom_raw_response_wrapper, async_to_custom_raw_response_wrapper, to_custom_streamed_response_wrapper, StreamedBinaryAPIResponse, async_to_custom_streamed_response_wrapper, AsyncStreamedBinaryAPIResponse

from ..._base_client import make_request_options

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params

__all__ = ["DownloadResource", "AsyncDownloadResource"]

class DownloadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadResourceWithRawResponse:
        return DownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadResourceWithStreamingResponse:
        return DownloadResourceWithStreamingResponse(self)

    def get(self,
    pcap_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> BinaryAPIResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not pcap_id:
          raise ValueError(
            f'Expected a non-empty value for `pcap_id` but received {pcap_id!r}'
          )
        extra_headers = {"Accept": "application/vnd.tcpdump.pcap", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/pcaps/{pcap_id}/download",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BinaryAPIResponse,
        )

class AsyncDownloadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadResourceWithRawResponse:
        return AsyncDownloadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadResourceWithStreamingResponse:
        return AsyncDownloadResourceWithStreamingResponse(self)

    async def get(self,
    pcap_id: str,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncBinaryAPIResponse:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        if not pcap_id:
          raise ValueError(
            f'Expected a non-empty value for `pcap_id` but received {pcap_id!r}'
          )
        extra_headers = {"Accept": "application/vnd.tcpdump.pcap", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/pcaps/{pcap_id}/download",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AsyncBinaryAPIResponse,
        )

class DownloadResourceWithRawResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

        self.get = to_custom_raw_response_wrapper(
            download.get,
            BinaryAPIResponse,
        )

class AsyncDownloadResourceWithRawResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

        self.get = async_to_custom_raw_response_wrapper(
            download.get,
            AsyncBinaryAPIResponse,
        )

class DownloadResourceWithStreamingResponse:
    def __init__(self, download: DownloadResource) -> None:
        self._download = download

        self.get = to_custom_streamed_response_wrapper(
            download.get,
            StreamedBinaryAPIResponse,
        )

class AsyncDownloadResourceWithStreamingResponse:
    def __init__(self, download: AsyncDownloadResource) -> None:
        self._download = download

        self.get = async_to_custom_streamed_response_wrapper(
            download.get,
            AsyncStreamedBinaryAPIResponse,
        )