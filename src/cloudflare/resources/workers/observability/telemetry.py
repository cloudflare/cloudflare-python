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
        account_id: str | None = None,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
        account_id: str | None = None,
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
        """
        Run a temporary or saved query.

        Args:
          query_id: Unique identifier for the query to execute

          timeframe: Timeframe for your query using Unix timestamps in milliseconds. Provide from/to
              epoch ms; narrower timeframes provide faster responses and more specific
              results.

          chart: Whether to include timeseties data in the response

          compare: Whether to include comparison data with previous time periods

          dry: Whether to perform a dry run without saving the results of the query. Useful for
              validation

          granularity: This is only used when the view is calculations. Leaving it empty lets Workers
              Observability detect the correct granularity.

          ignore_series: Whether to ignore time-series data in the results and return only aggregated
              values

          limit: Use this limit to cap the number of events returned when the view is events.

          offset: Cursor pagination for event/trace/invocation views. Pass the last item's
              $metadata.id as the next offset.

          offset_by: Numeric offset for pattern results (top-N list). Use with limit to page pattern
              groups; not used by cursor pagination.

          offset_direction: Direction for offset-based pagination (e.g., 'next', 'prev')

          parameters: Optional parameters to pass to the query execution

          view: Examples by view type. Events: show errors for a worker in the last 30 minutes.
              Calculations: p99 of wall time or count by status code. Invocations: find a
              specific request that resulted in a 500.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
        account_id: str | None = None,
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

          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
        account_id: str | None = None,
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
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
        account_id: str | None = None,
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
        """
        Run a temporary or saved query.

        Args:
          query_id: Unique identifier for the query to execute

          timeframe: Timeframe for your query using Unix timestamps in milliseconds. Provide from/to
              epoch ms; narrower timeframes provide faster responses and more specific
              results.

          chart: Whether to include timeseties data in the response

          compare: Whether to include comparison data with previous time periods

          dry: Whether to perform a dry run without saving the results of the query. Useful for
              validation

          granularity: This is only used when the view is calculations. Leaving it empty lets Workers
              Observability detect the correct granularity.

          ignore_series: Whether to ignore time-series data in the results and return only aggregated
              values

          limit: Use this limit to cap the number of events returned when the view is events.

          offset: Cursor pagination for event/trace/invocation views. Pass the last item's
              $metadata.id as the next offset.

          offset_by: Numeric offset for pattern results (top-N list). Use with limit to page pattern
              groups; not used by cursor pagination.

          offset_direction: Direction for offset-based pagination (e.g., 'next', 'prev')

          parameters: Optional parameters to pass to the query execution

          view: Examples by view type. Events: show errors for a worker in the last 30 minutes.
              Calculations: p99 of wall time or count by status code. Invocations: find a
              specific request that resulted in a 500.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
        account_id: str | None = None,
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

          needle: Search for a specific substring in the event.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
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
