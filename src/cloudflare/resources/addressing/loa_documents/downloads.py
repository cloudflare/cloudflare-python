# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    async_to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    StreamedBinaryAPIResponse,
    async_to_custom_streamed_response_wrapper,
    AsyncStreamedBinaryAPIResponse,
)

from ...._base_client import make_request_options

from typing import Optional

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params

__all__ = ["DownloadsResource", "AsyncDownloadsResource"]


class DownloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DownloadsResourceWithRawResponse:
        return DownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DownloadsResourceWithStreamingResponse:
        return DownloadsResourceWithStreamingResponse(self)

    def get(
        self,
        loa_document_id: Optional[str],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Download specified LOA document under the account.

        Args:
          account_id: Identifier

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not loa_document_id:
            raise ValueError(f"Expected a non-empty value for `loa_document_id` but received {loa_document_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncDownloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDownloadsResourceWithRawResponse:
        return AsyncDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDownloadsResourceWithStreamingResponse:
        return AsyncDownloadsResourceWithStreamingResponse(self)

    async def get(
        self,
        loa_document_id: Optional[str],
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Download specified LOA document under the account.

        Args:
          account_id: Identifier

          loa_document_id: Identifier for the uploaded LOA document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not loa_document_id:
            raise ValueError(f"Expected a non-empty value for `loa_document_id` but received {loa_document_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download",
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
