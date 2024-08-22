# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.addressing.regional_hostnames.region_list_response import RegionListResponse

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._base_client import make_request_options, AsyncPaginator

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params

__all__ = ["RegionsResource", "AsyncRegionsResource"]

class RegionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[RegionListResponse]:
        """
        List all Regional Services regions available for use by this account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/regional_hostnames/regions",
            page = SyncSinglePage[RegionListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=RegionListResponse,
        )

class AsyncRegionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[RegionListResponse, AsyncSinglePage[RegionListResponse]]:
        """
        List all Regional Services regions available for use by this account.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
          raise ValueError(
            f'Expected a non-empty value for `account_id` but received {account_id!r}'
          )
        return self._get_api_list(
            f"/accounts/{account_id}/addressing/regional_hostnames/regions",
            page = AsyncSinglePage[RegionListResponse],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=RegionListResponse,
        )

class RegionsResourceWithRawResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_raw_response_wrapper(
            regions.list,
        )

class AsyncRegionsResourceWithRawResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_raw_response_wrapper(
            regions.list,
        )

class RegionsResourceWithStreamingResponse:
    def __init__(self, regions: RegionsResource) -> None:
        self._regions = regions

        self.list = to_streamed_response_wrapper(
            regions.list,
        )

class AsyncRegionsResourceWithStreamingResponse:
    def __init__(self, regions: AsyncRegionsResource) -> None:
        self._regions = regions

        self.list = async_to_streamed_response_wrapper(
            regions.list,
        )