# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.cloudforce_one.threat_events import aggregate_list_params
from ....types.cloudforce_one.threat_events.aggregate_list_response import AggregateListResponse

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
        dataset_id: SequenceNotStr[str] | Omit = omit,
        end_date: str | Omit = omit,
        group_by_date: bool | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateListResponse:
        """
        Aggregate threat events by one or more columns (e.g., attacker, targetIndustry)
        with optional date filtering and daily grouping. Supports multi-dimensional
        aggregation for cross-analysis.

        Args:
          account_id: Account ID.

          aggregate_by: Column(s) to aggregate by - single column or comma-separated list (e.g.,
              'attacker', 'targetIndustry', 'attacker,targetIndustry')

          dataset_id: Dataset ID(s) to filter by. Can be a single dataset ID, comma-separated list, or
              array. If not provided, uses default dataset

          end_date: End date for filtering (ISO 8601 format, e.g., '2024-12-31')

          group_by_date: Whether to group results by date (daily aggregation)

          limit: Maximum number of results to return

          start_date: Start date for filtering (ISO 8601 format, e.g., '2024-01-01')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/aggregate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aggregate_by": aggregate_by,
                        "dataset_id": dataset_id,
                        "end_date": end_date,
                        "group_by_date": group_by_date,
                        "limit": limit,
                        "start_date": start_date,
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
        dataset_id: SequenceNotStr[str] | Omit = omit,
        end_date: str | Omit = omit,
        group_by_date: bool | Omit = omit,
        limit: float | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AggregateListResponse:
        """
        Aggregate threat events by one or more columns (e.g., attacker, targetIndustry)
        with optional date filtering and daily grouping. Supports multi-dimensional
        aggregation for cross-analysis.

        Args:
          account_id: Account ID.

          aggregate_by: Column(s) to aggregate by - single column or comma-separated list (e.g.,
              'attacker', 'targetIndustry', 'attacker,targetIndustry')

          dataset_id: Dataset ID(s) to filter by. Can be a single dataset ID, comma-separated list, or
              array. If not provided, uses default dataset

          end_date: End date for filtering (ISO 8601 format, e.g., '2024-12-31')

          group_by_date: Whether to group results by date (daily aggregation)

          limit: Maximum number of results to return

          start_date: Start date for filtering (ISO 8601 format, e.g., '2024-01-01')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/aggregate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aggregate_by": aggregate_by,
                        "dataset_id": dataset_id,
                        "end_date": end_date,
                        "group_by_date": group_by_date,
                        "limit": limit,
                        "start_date": start_date,
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
