# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.intel.sinkhole import Sinkhole

from ...pagination import SyncSinglePage, AsyncSinglePage

from ..._base_client import make_request_options, AsyncPaginator

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params

__all__ = ["SinkholesResource", "AsyncSinkholesResource"]

class SinkholesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SinkholesResourceWithRawResponse:
        return SinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SinkholesResourceWithStreamingResponse:
        return SinkholesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SyncSinglePage[Sinkhole]:
        """
        List sinkholes owned by this account

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
            f"/accounts/{account_id}/intel/sinkholes",
            page = SyncSinglePage[Sinkhole],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Sinkhole,
        )

class AsyncSinkholesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSinkholesResourceWithRawResponse:
        return AsyncSinkholesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSinkholesResourceWithStreamingResponse:
        return AsyncSinkholesResourceWithStreamingResponse(self)

    def list(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> AsyncPaginator[Sinkhole, AsyncSinglePage[Sinkhole]]:
        """
        List sinkholes owned by this account

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
            f"/accounts/{account_id}/intel/sinkholes",
            page = AsyncSinglePage[Sinkhole],
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            model=Sinkhole,
        )

class SinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = to_raw_response_wrapper(
            sinkholes.list,
        )

class AsyncSinkholesResourceWithRawResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_raw_response_wrapper(
            sinkholes.list,
        )

class SinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: SinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = to_streamed_response_wrapper(
            sinkholes.list,
        )

class AsyncSinkholesResourceWithStreamingResponse:
    def __init__(self, sinkholes: AsyncSinkholesResource) -> None:
        self._sinkholes = sinkholes

        self.list = async_to_streamed_response_wrapper(
            sinkholes.list,
        )