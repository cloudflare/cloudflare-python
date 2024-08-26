# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.intel.indicator_feeds.download_get_response import DownloadGetResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from typing import cast
from typing import cast

__all__ = ["DownloadsResource", "AsyncDownloadsResource"]

class DownloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self)

    def get(self,
    feed_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DownloadGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get(
            f"/accounts/{account_id}/intel/indicator_feeds/{feed_id}/download",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper),
            cast_to=cast(Type[Optional[DownloadGetResponse]], ResultWrapper[DownloadGetResponse]),
        )

class AsyncDownloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self)

    async def get(self,
    feed_id: int,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[DownloadGetResponse]:
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
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return await self._get(
            f"/accounts/{account_id}/intel/indicator_feeds/{feed_id}/download",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[DownloadGetResponse]]._unwrapper),
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