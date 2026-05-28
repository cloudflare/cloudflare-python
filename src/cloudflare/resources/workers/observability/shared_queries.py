# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...._base_client import make_request_options
from ....types.workers.observability import shared_query_get_params, shared_query_create_params
from ....types.workers.observability.shared_query_get_response import SharedQueryGetResponse
from ....types.workers.observability.shared_query_create_response import SharedQueryCreateResponse

__all__ = ["SharedQueriesResource", "AsyncSharedQueriesResource"]


class SharedQueriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SharedQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SharedQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SharedQueriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        query_id: str,
        timeframe: shared_query_create_params.Timeframe,
        chart: bool | Omit = omit,
        compare: bool | Omit = omit,
        dry: bool | Omit = omit,
        granularity: float | Omit = omit,
        ignore_series: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: str | Omit = omit,
        offset_by: float | Omit = omit,
        offset_direction: str | Omit = omit,
        parameters: shared_query_create_params.Parameters | Omit = omit,
        view: Literal["traces", "events", "calculations", "invocations", "requests", "agents"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedQueryCreateResponse:
        """
        Shared queries store the results of a previously run query, allowing you to
        share the results with others.

        Args:
          query_id: Identifier for the query. When parameters are omitted, this ID is used to load a
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
            path_template("/accounts/{account_id}/workers/observability/shared/query", account_id=account_id),
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
                shared_query_create_params.SharedQueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SharedQueryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SharedQueryCreateResponse], ResultWrapper[SharedQueryCreateResponse]),
        )

    def get(
        self,
        id: str,
        *,
        account_id: str,
        view: Literal["events", "invocations", "calculations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedQueryGetResponse:
        """
        Shared queries store the results of a previously run query, allowing you to
        share the results with others.

        Args:
          id: Specify the ID of the shared query.

          view: Select the view of the query result to return, defaults to events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/workers/observability/shared/query/{id}", account_id=account_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"view": view}, shared_query_get_params.SharedQueryGetParams),
                post_parser=ResultWrapper[SharedQueryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SharedQueryGetResponse], ResultWrapper[SharedQueryGetResponse]),
        )


class AsyncSharedQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSharedQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSharedQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSharedQueriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        query_id: str,
        timeframe: shared_query_create_params.Timeframe,
        chart: bool | Omit = omit,
        compare: bool | Omit = omit,
        dry: bool | Omit = omit,
        granularity: float | Omit = omit,
        ignore_series: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: str | Omit = omit,
        offset_by: float | Omit = omit,
        offset_direction: str | Omit = omit,
        parameters: shared_query_create_params.Parameters | Omit = omit,
        view: Literal["traces", "events", "calculations", "invocations", "requests", "agents"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedQueryCreateResponse:
        """
        Shared queries store the results of a previously run query, allowing you to
        share the results with others.

        Args:
          query_id: Identifier for the query. When parameters are omitted, this ID is used to load a
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
            path_template("/accounts/{account_id}/workers/observability/shared/query", account_id=account_id),
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
                shared_query_create_params.SharedQueryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[SharedQueryCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[SharedQueryCreateResponse], ResultWrapper[SharedQueryCreateResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        account_id: str,
        view: Literal["events", "invocations", "calculations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedQueryGetResponse:
        """
        Shared queries store the results of a previously run query, allowing you to
        share the results with others.

        Args:
          id: Specify the ID of the shared query.

          view: Select the view of the query result to return, defaults to events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/workers/observability/shared/query/{id}", account_id=account_id, id=id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"view": view}, shared_query_get_params.SharedQueryGetParams),
                post_parser=ResultWrapper[SharedQueryGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[SharedQueryGetResponse], ResultWrapper[SharedQueryGetResponse]),
        )


class SharedQueriesResourceWithRawResponse:
    def __init__(self, shared_queries: SharedQueriesResource) -> None:
        self._shared_queries = shared_queries

        self.create = to_raw_response_wrapper(
            shared_queries.create,
        )
        self.get = to_raw_response_wrapper(
            shared_queries.get,
        )


class AsyncSharedQueriesResourceWithRawResponse:
    def __init__(self, shared_queries: AsyncSharedQueriesResource) -> None:
        self._shared_queries = shared_queries

        self.create = async_to_raw_response_wrapper(
            shared_queries.create,
        )
        self.get = async_to_raw_response_wrapper(
            shared_queries.get,
        )


class SharedQueriesResourceWithStreamingResponse:
    def __init__(self, shared_queries: SharedQueriesResource) -> None:
        self._shared_queries = shared_queries

        self.create = to_streamed_response_wrapper(
            shared_queries.create,
        )
        self.get = to_streamed_response_wrapper(
            shared_queries.get,
        )


class AsyncSharedQueriesResourceWithStreamingResponse:
    def __init__(self, shared_queries: AsyncSharedQueriesResource) -> None:
        self._shared_queries = shared_queries

        self.create = async_to_streamed_response_wrapper(
            shared_queries.create,
        )
        self.get = async_to_streamed_response_wrapper(
            shared_queries.get,
        )
