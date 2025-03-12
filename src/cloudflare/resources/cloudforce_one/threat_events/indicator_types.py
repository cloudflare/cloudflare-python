# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events.indicator_type_list_response import IndicatorTypeListResponse

__all__ = ["IndicatorTypesResource", "AsyncIndicatorTypesResource"]


class IndicatorTypesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndicatorTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IndicatorTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IndicatorTypesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorTypeListResponse:
        """
        Lists all indicator types

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/indicatorTypes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndicatorTypeListResponse,
        )


class AsyncIndicatorTypesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndicatorTypesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicatorTypesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorTypesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIndicatorTypesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndicatorTypeListResponse:
        """
        Lists all indicator types

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/indicatorTypes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndicatorTypeListResponse,
        )


class IndicatorTypesResourceWithRawResponse:
    def __init__(self, indicator_types: IndicatorTypesResource) -> None:
        self._indicator_types = indicator_types

        self.list = to_raw_response_wrapper(
            indicator_types.list,
        )


class AsyncIndicatorTypesResourceWithRawResponse:
    def __init__(self, indicator_types: AsyncIndicatorTypesResource) -> None:
        self._indicator_types = indicator_types

        self.list = async_to_raw_response_wrapper(
            indicator_types.list,
        )


class IndicatorTypesResourceWithStreamingResponse:
    def __init__(self, indicator_types: IndicatorTypesResource) -> None:
        self._indicator_types = indicator_types

        self.list = to_streamed_response_wrapper(
            indicator_types.list,
        )


class AsyncIndicatorTypesResourceWithStreamingResponse:
    def __init__(self, indicator_types: AsyncIndicatorTypesResource) -> None:
        self._indicator_types = indicator_types

        self.list = async_to_streamed_response_wrapper(
            indicator_types.list,
        )
