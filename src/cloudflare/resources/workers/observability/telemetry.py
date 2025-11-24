# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workers.observability import telemetry_keys_params, telemetry_query_params, telemetry_values_params
from ....types.workers.observability.telemetry_keys_response import TelemetryKeysResponse
from ....types.workers.observability.telemetry_query_response import TelemetryQueryResponse
from ....types.workers.observability.telemetry_values_response import TelemetryValuesResponse

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)

    def keys(
        self,
        *,
        account_id: str,
        datasets: SequenceNotStr[str] | Omit = omit,
        filters: Iterable[telemetry_keys_params.Filter] | Omit = omit,
        from_: float | Omit = omit,
        key_needle: telemetry_keys_params.KeyNeedle | Omit = omit,
        limit: float | Omit = omit,
        needle: telemetry_keys_params.Needle | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TelemetryKeysResponse]:
        """
        List all the keys in your telemetry events.

        Args:
          key_needle: Search for a specific substring in the keys.

          needle: Search for a specific substring in any of the events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/keys",
            page=SyncSinglePage[TelemetryKeysResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "filters": filters,
                    "from_": from_,
                    "key_needle": key_needle,
                    "limit": limit,
                    "needle": needle,
                    "to": to,
                },
                telemetry_keys_params.TelemetryKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TelemetryKeysResponse,
            method="post",
        )

    def query(
        self,
        *,
        account_id: str,
        query_id: str,
        timeframe: telemetry_query_params.Timeframe,
        chart: bool | Omit = omit,
        compare: bool | Omit = omit,
        dry: bool | Omit = omit,
        granularity: float | Omit = omit,
        ignore_series: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: str | Omit = omit,
        offset_by: float | Omit = omit,
        offset_direction: str | Omit = omit,
        parameters: telemetry_query_params.Parameters | Omit = omit,
        pattern_type: Literal["message", "error"] | Omit = omit,
        view: Literal["traces", "events", "calculations", "invocations", "requests", "patterns"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryResponse:
        """
        Runs a temporary or saved query

        Args:
          query_id: Unique identifier for the query to execute

          timeframe: Time range for the query execution

          chart: Whether to include timeseties data in the response

          compare: Whether to include comparison data with previous time periods

          dry: Whether to perform a dry run without saving the results of the query. Useful for
              validation

          granularity: Time granularity for aggregating results (in milliseconds). Controls the
              bucketing of time-series data

          ignore_series: Whether to ignore time-series data in the results and return only aggregated
              values

          limit: Maximum number of events to return.

          offset: Cursor for pagination to retrieve the next set of results

          offset_by: Number of events to skip for pagination. Used in conjunction with offset

          offset_direction: Direction for offset-based pagination (e.g., 'next', 'prev')

          parameters: Optional parameters to pass to the query execution

          pattern_type: Type of pattern to search for when using pattern-based views

          view: View type for presenting the query results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/workers/observability/telemetry/query",
            body=maybe_transform(
                {
                    "query_id": query_id,
                    "timeframe": timeframe,
                    "chart": chart,
                    "compare": compare,
                    "dry": dry,
                    "granularity": granularity,
                    "ignore_series": ignore_series,
                    "limit": limit,
                    "offset": offset,
                    "offset_by": offset_by,
                    "offset_direction": offset_direction,
                    "parameters": parameters,
                    "pattern_type": pattern_type,
                    "view": view,
                },
                telemetry_query_params.TelemetryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TelemetryQueryResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryResponse], ResultWrapper[TelemetryQueryResponse]),
        )

    def values(
        self,
        *,
        account_id: str,
        datasets: SequenceNotStr[str],
        key: str,
        timeframe: telemetry_values_params.Timeframe,
        type: Literal["string", "boolean", "number"],
        filters: Iterable[telemetry_values_params.Filter] | Omit = omit,
        limit: float | Omit = omit,
        needle: telemetry_values_params.Needle | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[TelemetryValuesResponse]:
        """
        List unique values found in your events

        Args:
          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/values",
            page=SyncSinglePage[TelemetryValuesResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "key": key,
                    "timeframe": timeframe,
                    "type": type,
                    "filters": filters,
                    "limit": limit,
                    "needle": needle,
                },
                telemetry_values_params.TelemetryValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TelemetryValuesResponse,
            method="post",
        )


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)

    def keys(
        self,
        *,
        account_id: str,
        datasets: SequenceNotStr[str] | Omit = omit,
        filters: Iterable[telemetry_keys_params.Filter] | Omit = omit,
        from_: float | Omit = omit,
        key_needle: telemetry_keys_params.KeyNeedle | Omit = omit,
        limit: float | Omit = omit,
        needle: telemetry_keys_params.Needle | Omit = omit,
        to: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TelemetryKeysResponse, AsyncSinglePage[TelemetryKeysResponse]]:
        """
        List all the keys in your telemetry events.

        Args:
          key_needle: Search for a specific substring in the keys.

          needle: Search for a specific substring in any of the events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/keys",
            page=AsyncSinglePage[TelemetryKeysResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "filters": filters,
                    "from_": from_,
                    "key_needle": key_needle,
                    "limit": limit,
                    "needle": needle,
                    "to": to,
                },
                telemetry_keys_params.TelemetryKeysParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TelemetryKeysResponse,
            method="post",
        )

    async def query(
        self,
        *,
        account_id: str,
        query_id: str,
        timeframe: telemetry_query_params.Timeframe,
        chart: bool | Omit = omit,
        compare: bool | Omit = omit,
        dry: bool | Omit = omit,
        granularity: float | Omit = omit,
        ignore_series: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: str | Omit = omit,
        offset_by: float | Omit = omit,
        offset_direction: str | Omit = omit,
        parameters: telemetry_query_params.Parameters | Omit = omit,
        pattern_type: Literal["message", "error"] | Omit = omit,
        view: Literal["traces", "events", "calculations", "invocations", "requests", "patterns"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryResponse:
        """
        Runs a temporary or saved query

        Args:
          query_id: Unique identifier for the query to execute

          timeframe: Time range for the query execution

          chart: Whether to include timeseties data in the response

          compare: Whether to include comparison data with previous time periods

          dry: Whether to perform a dry run without saving the results of the query. Useful for
              validation

          granularity: Time granularity for aggregating results (in milliseconds). Controls the
              bucketing of time-series data

          ignore_series: Whether to ignore time-series data in the results and return only aggregated
              values

          limit: Maximum number of events to return.

          offset: Cursor for pagination to retrieve the next set of results

          offset_by: Number of events to skip for pagination. Used in conjunction with offset

          offset_direction: Direction for offset-based pagination (e.g., 'next', 'prev')

          parameters: Optional parameters to pass to the query execution

          pattern_type: Type of pattern to search for when using pattern-based views

          view: View type for presenting the query results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/observability/telemetry/query",
            body=await async_maybe_transform(
                {
                    "query_id": query_id,
                    "timeframe": timeframe,
                    "chart": chart,
                    "compare": compare,
                    "dry": dry,
                    "granularity": granularity,
                    "ignore_series": ignore_series,
                    "limit": limit,
                    "offset": offset,
                    "offset_by": offset_by,
                    "offset_direction": offset_direction,
                    "parameters": parameters,
                    "pattern_type": pattern_type,
                    "view": view,
                },
                telemetry_query_params.TelemetryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TelemetryQueryResponse]._unwrapper,
            ),
            cast_to=cast(Type[TelemetryQueryResponse], ResultWrapper[TelemetryQueryResponse]),
        )

    def values(
        self,
        *,
        account_id: str,
        datasets: SequenceNotStr[str],
        key: str,
        timeframe: telemetry_values_params.Timeframe,
        type: Literal["string", "boolean", "number"],
        filters: Iterable[telemetry_values_params.Filter] | Omit = omit,
        limit: float | Omit = omit,
        needle: telemetry_values_params.Needle | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TelemetryValuesResponse, AsyncSinglePage[TelemetryValuesResponse]]:
        """
        List unique values found in your events

        Args:
          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/workers/observability/telemetry/values",
            page=AsyncSinglePage[TelemetryValuesResponse],
            body=maybe_transform(
                {
                    "datasets": datasets,
                    "key": key,
                    "timeframe": timeframe,
                    "type": type,
                    "filters": filters,
                    "limit": limit,
                    "needle": needle,
                },
                telemetry_values_params.TelemetryValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=TelemetryValuesResponse,
            method="post",
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.keys = to_raw_response_wrapper(
            telemetry.keys,
        )
        self.query = to_raw_response_wrapper(
            telemetry.query,
        )
        self.values = to_raw_response_wrapper(
            telemetry.values,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.keys = async_to_raw_response_wrapper(
            telemetry.keys,
        )
        self.query = async_to_raw_response_wrapper(
            telemetry.query,
        )
        self.values = async_to_raw_response_wrapper(
            telemetry.values,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.keys = to_streamed_response_wrapper(
            telemetry.keys,
        )
        self.query = to_streamed_response_wrapper(
            telemetry.query,
        )
        self.values = to_streamed_response_wrapper(
            telemetry.values,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.keys = async_to_streamed_response_wrapper(
            telemetry.keys,
        )
        self.query = async_to_streamed_response_wrapper(
            telemetry.query,
        )
        self.values = async_to_streamed_response_wrapper(
            telemetry.values,
        )
