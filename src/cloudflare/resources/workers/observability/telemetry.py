# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
          datasets: Leave this empty to use the default datasets

          filters: Apply filters to narrow key discovery. Supports nested groups via kind: 'group'.
              Maximum nesting depth is 4.

          key_needle: If the user suggests a key, use this to narrow down the list of keys returned.
              Make sure matchCase is false to avoid case sensitivity issues.

          limit: Advanced usage: set limit=1000+ to retrieve comprehensive key options without
              needing additional filtering.

          needle: Search for a specific substring in any of the events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/telemetry/keys", account_id=account_id),
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
        view: Literal["traces", "events", "calculations", "invocations", "requests", "agents"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryResponse:
        """Run a temporary or saved query.

        Args:
          query_id: Identifier for the query.

        When parameters are omitted, this ID is used to load a
              previously saved query's parameters. When providing parameters inline, pass any
              identifier (e.g. an ad-hoc ID).

          timeframe: Timeframe for the query using Unix timestamps in milliseconds. Narrower
              timeframes produce faster responses and more specific results.

          chart: When true, includes time-series data in the response.

          compare: When true, includes a comparison dataset from the previous time period of equal
              length.

          dry: When true, executes the query without persisting the results. Useful for
              validation or previewing.

          granularity: Number of time-series buckets. Only used when view is 'calculations'. Omit to
              let the system auto-detect an appropriate granularity.

          ignore_series: When true, omits time-series data from the response and returns only aggregated
              values. Reduces response size when series are not needed.

          limit: Maximum number of events to return when view is 'events'. Also controls the
              number of group-by rows when view is 'calculations'.

          offset: Cursor for pagination in event, trace, and invocation views. Pass the
              $metadata.id of the last returned item to fetch the next page.

          offset_by: Numeric offset for paginating grouped/pattern results (top-N lists). Use
              together with limit. Not used by cursor-based pagination.

          offset_direction: Pagination direction: 'next' for forward, 'prev' for backward.

          parameters: Query parameters defining what data to retrieve — filters, calculations,
              group-bys, and ordering. In practice this should always be provided for ad-hoc
              queries. Only omit when executing a previously saved query by queryId. Use the
              keys and values endpoints to discover available fields before building filters.

          view: Controls the shape of the response. 'events': individual log lines matching the
              query. 'calculations': aggregated metrics (count, avg, p99, etc.) with optional
              group-by breakdowns and time-series. 'invocations': events grouped by request
              ID. 'traces': distributed trace summaries. 'agents': Durable Object agent
              summaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/workers/observability/telemetry/query", account_id=account_id),
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
        List unique values found in your events.

        Args:
          datasets: Leave this empty to use the default datasets

          filters: Apply filters before listing values. Supports nested groups via kind: 'group'.
              Maximum nesting depth is 4.

          needle: Full-text search expression to match events containing the specified text or
              pattern.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/telemetry/values", account_id=account_id),
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
          datasets: Leave this empty to use the default datasets

          filters: Apply filters to narrow key discovery. Supports nested groups via kind: 'group'.
              Maximum nesting depth is 4.

          key_needle: If the user suggests a key, use this to narrow down the list of keys returned.
              Make sure matchCase is false to avoid case sensitivity issues.

          limit: Advanced usage: set limit=1000+ to retrieve comprehensive key options without
              needing additional filtering.

          needle: Search for a specific substring in any of the events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/telemetry/keys", account_id=account_id),
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
        view: Literal["traces", "events", "calculations", "invocations", "requests", "agents"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TelemetryQueryResponse:
        """Run a temporary or saved query.

        Args:
          query_id: Identifier for the query.

        When parameters are omitted, this ID is used to load a
              previously saved query's parameters. When providing parameters inline, pass any
              identifier (e.g. an ad-hoc ID).

          timeframe: Timeframe for the query using Unix timestamps in milliseconds. Narrower
              timeframes produce faster responses and more specific results.

          chart: When true, includes time-series data in the response.

          compare: When true, includes a comparison dataset from the previous time period of equal
              length.

          dry: When true, executes the query without persisting the results. Useful for
              validation or previewing.

          granularity: Number of time-series buckets. Only used when view is 'calculations'. Omit to
              let the system auto-detect an appropriate granularity.

          ignore_series: When true, omits time-series data from the response and returns only aggregated
              values. Reduces response size when series are not needed.

          limit: Maximum number of events to return when view is 'events'. Also controls the
              number of group-by rows when view is 'calculations'.

          offset: Cursor for pagination in event, trace, and invocation views. Pass the
              $metadata.id of the last returned item to fetch the next page.

          offset_by: Numeric offset for paginating grouped/pattern results (top-N lists). Use
              together with limit. Not used by cursor-based pagination.

          offset_direction: Pagination direction: 'next' for forward, 'prev' for backward.

          parameters: Query parameters defining what data to retrieve — filters, calculations,
              group-bys, and ordering. In practice this should always be provided for ad-hoc
              queries. Only omit when executing a previously saved query by queryId. Use the
              keys and values endpoints to discover available fields before building filters.

          view: Controls the shape of the response. 'events': individual log lines matching the
              query. 'calculations': aggregated metrics (count, avg, p99, etc.) with optional
              group-by breakdowns and time-series. 'invocations': events grouped by request
              ID. 'traces': distributed trace summaries. 'agents': Durable Object agent
              summaries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/workers/observability/telemetry/query", account_id=account_id),
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
        List unique values found in your events.

        Args:
          datasets: Leave this empty to use the default datasets

          filters: Apply filters before listing values. Supports nested groups via kind: 'group'.
              Maximum nesting depth is 4.

          needle: Full-text search expression to match events containing the specified text or
              pattern.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/workers/observability/telemetry/values", account_id=account_id),
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
