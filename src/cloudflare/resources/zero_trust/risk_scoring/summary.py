# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.zero_trust.risk_scoring.summary_get_response import SummaryGetResponse

from ...._base_client import make_request_options

from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params

__all__ = ["SummaryResource", "AsyncSummaryResource"]

class SummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self)

    def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SummaryGetResponse:
        """
        Get risk score info for all users in the account

        Args:
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
            f"/accounts/{account_id}/zt_risk_scoring/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SummaryGetResponse,
        )

class AsyncSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def get(self,
    *,
    account_id: str,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> SummaryGetResponse:
        """
        Get risk score info for all users in the account

        Args:
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
            f"/accounts/{account_id}/zt_risk_scoring/summary",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=SummaryGetResponse,
        )

class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.get = to_raw_response_wrapper(
            summary.get,
        )

class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.get = async_to_raw_response_wrapper(
            summary.get,
        )

class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.get = to_streamed_response_wrapper(
            summary.get,
        )

class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.get = async_to_streamed_response_wrapper(
            summary.get,
        )