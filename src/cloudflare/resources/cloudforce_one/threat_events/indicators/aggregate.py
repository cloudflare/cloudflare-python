# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cloudforce_one.threat_events.indicators import aggregate_list_params
from .....types.cloudforce_one.threat_events.indicators.aggregate_list_response import AggregateListResponse

__all__ = ["AggregateResource", "AsyncAggregateResource"]


class AggregateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AggregateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AggregateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AggregateResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        aggregate_by: str,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        event_date_after: str | Omit = omit,
        event_date_before: str | Omit = omit,
        limit: float | Omit = omit,
        measure: Literal["indicators", "relationships"] | Omit = omit,
        tag_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateListResponse:
        """
        Aggregate threat indicators by one or more columns (e.g., indicatorType, value)
        across datasets. Returns top-N groups ordered by count.

        Args:
          account_id: Account ID.

          aggregate_by: Column(s) to aggregate by - single column or comma-separated list (e.g.,
              'indicatorType', 'value', 'indicatorType,value')

          created_after: Filter indicators created after this date (ISO 8601 format, e.g., '2024-01-01')

          created_before: Filter indicators created before this date (ISO 8601 format, e.g., '2024-12-31')

          dataset_ids: Dataset ID(s) to filter by. Can be a single dataset ID or comma-separated list.
              If not provided, aggregates across all accessible datasets

          event_date_after: For measure=relationships: only count event links whose eventDate is on/after
              this date (ISO 8601). Use to bound 'top indicator' to recent activity.

          event_date_before: For measure=relationships: only count event links whose eventDate is on/before
              this date (ISO 8601).

          limit: Maximum number of aggregation results to return (1-100)

          measure: What to count per group: 'indicators' (catalog rows, default) or 'relationships'
              (linked events per indicator). Use 'relationships' for 'top indicator by event
              activity'.

          tag_uuid: Scope to indicators associated with this tag/actor UUID. Combine with
              measure=relationships for 'top indicator for an actor'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicators/aggregate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aggregate_by": aggregate_by,
                        "created_after": created_after,
                        "created_before": created_before,
                        "dataset_ids": dataset_ids,
                        "event_date_after": event_date_after,
                        "event_date_before": event_date_before,
                        "limit": limit,
                        "measure": measure,
                        "tag_uuid": tag_uuid,
                    },
                    aggregate_list_params.AggregateListParams,
                ),
            ),
            cast_to=AggregateListResponse,
        )


class AsyncAggregateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAggregateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAggregateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAggregateResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        aggregate_by: str,
        created_after: str | Omit = omit,
        created_before: str | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        event_date_after: str | Omit = omit,
        event_date_before: str | Omit = omit,
        limit: float | Omit = omit,
        measure: Literal["indicators", "relationships"] | Omit = omit,
        tag_uuid: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateListResponse:
        """
        Aggregate threat indicators by one or more columns (e.g., indicatorType, value)
        across datasets. Returns top-N groups ordered by count.

        Args:
          account_id: Account ID.

          aggregate_by: Column(s) to aggregate by - single column or comma-separated list (e.g.,
              'indicatorType', 'value', 'indicatorType,value')

          created_after: Filter indicators created after this date (ISO 8601 format, e.g., '2024-01-01')

          created_before: Filter indicators created before this date (ISO 8601 format, e.g., '2024-12-31')

          dataset_ids: Dataset ID(s) to filter by. Can be a single dataset ID or comma-separated list.
              If not provided, aggregates across all accessible datasets

          event_date_after: For measure=relationships: only count event links whose eventDate is on/after
              this date (ISO 8601). Use to bound 'top indicator' to recent activity.

          event_date_before: For measure=relationships: only count event links whose eventDate is on/before
              this date (ISO 8601).

          limit: Maximum number of aggregation results to return (1-100)

          measure: What to count per group: 'indicators' (catalog rows, default) or 'relationships'
              (linked events per indicator). Use 'relationships' for 'top indicator by event
              activity'.

          tag_uuid: Scope to indicators associated with this tag/actor UUID. Combine with
              measure=relationships for 'top indicator for an actor'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicators/aggregate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aggregate_by": aggregate_by,
                        "created_after": created_after,
                        "created_before": created_before,
                        "dataset_ids": dataset_ids,
                        "event_date_after": event_date_after,
                        "event_date_before": event_date_before,
                        "limit": limit,
                        "measure": measure,
                        "tag_uuid": tag_uuid,
                    },
                    aggregate_list_params.AggregateListParams,
                ),
            ),
            cast_to=AggregateListResponse,
        )


class AggregateResourceWithRawResponse:
    def __init__(self, aggregate: AggregateResource) -> None:
        self._aggregate = aggregate

        self.list = to_raw_response_wrapper(
            aggregate.list,
        )


class AsyncAggregateResourceWithRawResponse:
    def __init__(self, aggregate: AsyncAggregateResource) -> None:
        self._aggregate = aggregate

        self.list = async_to_raw_response_wrapper(
            aggregate.list,
        )


class AggregateResourceWithStreamingResponse:
    def __init__(self, aggregate: AggregateResource) -> None:
        self._aggregate = aggregate

        self.list = to_streamed_response_wrapper(
            aggregate.list,
        )


class AsyncAggregateResourceWithStreamingResponse:
    def __init__(self, aggregate: AsyncAggregateResource) -> None:
        self._aggregate = aggregate

        self.list = async_to_streamed_response_wrapper(
            aggregate.list,
        )
