# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.zero_trust.risk_scoring import summary_get_params
from ....types.zero_trust.risk_scoring.summary_get_response import SummaryGetResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        return SummaryResourceWithStreamingResponse(self)

    def get(
        self,
        account_identifier: str,
        *,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        order_by: Literal["timestamp", "event_count", "max_risk_level"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryGetResponse:
        """
        Get risk score info for all users in the account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    summary_get_params.SummaryGetParams,
                ),
                post_parser=ResultWrapper[SummaryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryGetResponse], ResultWrapper[SummaryGetResponse]),
        )


class AsyncSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def get(
        self,
        account_identifier: str,
        *,
        direction: Literal["desc", "asc"] | NotGiven = NOT_GIVEN,
        order_by: Literal["timestamp", "event_count", "max_risk_level"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SummaryGetResponse:
        """
        Get risk score info for all users in the account

        Args:
          account_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_identifier:
            raise ValueError(f"Expected a non-empty value for `account_identifier` but received {account_identifier!r}")
        return await self._get(
            f"/accounts/{account_identifier}/zt_risk_scoring/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "order_by": order_by,
                        "page": page,
                        "per_page": per_page,
                    },
                    summary_get_params.SummaryGetParams,
                ),
                post_parser=ResultWrapper[SummaryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SummaryGetResponse], ResultWrapper[SummaryGetResponse]),
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
