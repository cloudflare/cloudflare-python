# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from .types import (
    TypesResource,
    AsyncTypesResource,
    TypesResourceWithRawResponse,
    AsyncTypesResourceWithRawResponse,
    TypesResourceWithStreamingResponse,
    AsyncTypesResourceWithStreamingResponse,
)
from .aggregate import (
    AggregateResource,
    AsyncAggregateResource,
    AggregateResourceWithRawResponse,
    AsyncAggregateResourceWithRawResponse,
    AggregateResourceWithStreamingResponse,
    AsyncAggregateResourceWithStreamingResponse,
)
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
from .by_dataset.by_dataset import (
    ByDatasetResource,
    AsyncByDatasetResource,
    ByDatasetResourceWithRawResponse,
    AsyncByDatasetResourceWithRawResponse,
    ByDatasetResourceWithStreamingResponse,
    AsyncByDatasetResourceWithStreamingResponse,
)
from .....types.cloudforce_one.threat_events import indicator_list_params
from .....types.cloudforce_one.threat_events.indicator_list_response import IndicatorListResponse

__all__ = ["IndicatorsResource", "AsyncIndicatorsResource"]


class IndicatorsResource(SyncAPIResource):
    @cached_property
    def aggregate(self) -> AggregateResource:
        return AggregateResource(self._client)

    @cached_property
    def types(self) -> TypesResource:
        return TypesResource(self._client)

    @cached_property
    def by_dataset(self) -> ByDatasetResource:
        return ByDatasetResource(self._client)

    @cached_property
    def with_raw_response(self) -> IndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IndicatorsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        format: Literal["json", "stix2", "taxii"] | Omit = omit,
        include_tags: bool | Omit = omit,
        include_total_count: bool | Omit = omit,
        indicator_type: str | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_events: SequenceNotStr[str] | Omit = omit,
        related_events_limit: float | Omit = omit,
        search: Iterable[indicator_list_params.Search] | Omit = omit,
        source: Literal["do", "r2catalog"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tag_search: Iterable[indicator_list_params.TagSearch] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """Retrieves a paginated list of indicators across specified datasets.

        Use
        datasetIds=all or datasetIds=\\** to query all datasets for the account. If no
        datasetIds provided, uses the default dataset.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          created_after: Filter indicators created on or after this date. Must use ISO 8601 format (e.g.,
              '2024-01-15T00:00:00Z').

          created_before: Filter indicators created on or before this date. Must use ISO 8601 format
              (e.g., '2024-12-31T23:59:59Z').

          dataset_ids: Dataset IDs to query indicators from (array of UUIDs), or special value 'all' or
              '\\**' to query all datasets. If not provided, uses the default dataset.

          format: Output format for indicator data. 'json' returns the default format, 'stix2'
              returns STIX 2.1 Indicator SDOs, 'taxii' returns a TAXII 2.1 Envelope with
              Content-Type application/taxii+json;version=2.1.

          include_tags: Whether to include full tag details for each indicator. Defaults to true.

          include_total_count: Whether to compute accurate total count via COUNT(\\**). Defaults to false for
              performance. When false, total_count is an approximation.

          name: Filter indicators by value using substring match (LIKE). Legacy alternative to
              structured search.

          related_events: Filter by related event IDs

          related_events_limit: Limit the number of related events returned per indicator. Default: 2. Set to 0
              for none, -1 for all events.

          search: Structured search as a JSON array of {field, op, value} objects. Searchable
              fields: value, indicatorType, uuid. Supports operators: equals, not, contains,
              startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use the 'in' operator
              with an array value to bulk-check up to 100 indicators in a single request, e.g.
              search=[{"field":"value","op":"in","value":["evil.com","bad.org"]}]. Multiple
              conditions are AND'd together. Max 10 conditions per request.

          source: Read backend. 'do' (default) reads Durable Object storage. 'r2catalog' reads R2
              Data Catalog (admin-only, experimental; supports a subset of search fields).

          tags: Filter by tag values or UUIDs. Indicators must have at least one of the
              specified tags (OR logic). Supports both tag UUID and tag value.

          tag_search: Structured tag-metadata filter as a JSON array of {field, op, value} objects.
              Operates against the per-dataset IndicatorTag mirror so you can find indicators
              by tag attributes (origin country, motive, sophistication, priority, etc.)
              without a separate Tags lookup. Common dashboard usage: drill from a country
              into indicators, e.g.
              tagSearch=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Country
              values may be passed as alpha-2, alpha-3, name, or alias (e.g. "iran").
              Operators: equals, not, gt/gte/lt/lte (numeric only),
              contains/like/find/startsWith/endsWith (string only), in. AND-joined across
              entries; combined with `tags`, a matching tag must satisfy both. Max 10 entries
              per request, max 100 values per 'in'. Performance notes: `originCountryISO` uses
              its B-tree index for equals/not/in. `priority` uses its B-tree index for numeric
              comparisons. Other string columns (`actorCategory`, `motive`, etc.) are
              case-insensitive and unindexed; current catalog size makes this a non-issue.
              `endsWith` and `aliasGroupNames` contains/like are leading-wildcard scans and
              slow on large result sets. `aliasGroupNames` matches on the JSON-encoded text,
              so substrings can cross alias boundaries ("apt28" also matches "apt280" when
              both appear in the same tag's alias list).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicators", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache": cache,
                        "created_after": created_after,
                        "created_before": created_before,
                        "dataset_ids": dataset_ids,
                        "format": format,
                        "include_tags": include_tags,
                        "include_total_count": include_total_count,
                        "indicator_type": indicator_type,
                        "name": name,
                        "page": page,
                        "page_size": page_size,
                        "related_events": related_events,
                        "related_events_limit": related_events_limit,
                        "search": search,
                        "source": source,
                        "tags": tags,
                        "tag_search": tag_search,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
            ),
            cast_to=IndicatorListResponse,
        )


class AsyncIndicatorsResource(AsyncAPIResource):
    @cached_property
    def aggregate(self) -> AsyncAggregateResource:
        return AsyncAggregateResource(self._client)

    @cached_property
    def types(self) -> AsyncTypesResource:
        return AsyncTypesResource(self._client)

    @cached_property
    def by_dataset(self) -> AsyncByDatasetResource:
        return AsyncByDatasetResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIndicatorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicatorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIndicatorsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        dataset_ids: SequenceNotStr[str] | Omit = omit,
        format: Literal["json", "stix2", "taxii"] | Omit = omit,
        include_tags: bool | Omit = omit,
        include_total_count: bool | Omit = omit,
        indicator_type: str | Omit = omit,
        name: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        related_events: SequenceNotStr[str] | Omit = omit,
        related_events_limit: float | Omit = omit,
        search: Iterable[indicator_list_params.Search] | Omit = omit,
        source: Literal["do", "r2catalog"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        tag_search: Iterable[indicator_list_params.TagSearch] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IndicatorListResponse:
        """Retrieves a paginated list of indicators across specified datasets.

        Use
        datasetIds=all or datasetIds=\\** to query all datasets for the account. If no
        datasetIds provided, uses the default dataset.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          created_after: Filter indicators created on or after this date. Must use ISO 8601 format (e.g.,
              '2024-01-15T00:00:00Z').

          created_before: Filter indicators created on or before this date. Must use ISO 8601 format
              (e.g., '2024-12-31T23:59:59Z').

          dataset_ids: Dataset IDs to query indicators from (array of UUIDs), or special value 'all' or
              '\\**' to query all datasets. If not provided, uses the default dataset.

          format: Output format for indicator data. 'json' returns the default format, 'stix2'
              returns STIX 2.1 Indicator SDOs, 'taxii' returns a TAXII 2.1 Envelope with
              Content-Type application/taxii+json;version=2.1.

          include_tags: Whether to include full tag details for each indicator. Defaults to true.

          include_total_count: Whether to compute accurate total count via COUNT(\\**). Defaults to false for
              performance. When false, total_count is an approximation.

          name: Filter indicators by value using substring match (LIKE). Legacy alternative to
              structured search.

          related_events: Filter by related event IDs

          related_events_limit: Limit the number of related events returned per indicator. Default: 2. Set to 0
              for none, -1 for all events.

          search: Structured search as a JSON array of {field, op, value} objects. Searchable
              fields: value, indicatorType, uuid. Supports operators: equals, not, contains,
              startsWith, endsWith, gt, lt, gte, lte, like, in, find. Use the 'in' operator
              with an array value to bulk-check up to 100 indicators in a single request, e.g.
              search=[{"field":"value","op":"in","value":["evil.com","bad.org"]}]. Multiple
              conditions are AND'd together. Max 10 conditions per request.

          source: Read backend. 'do' (default) reads Durable Object storage. 'r2catalog' reads R2
              Data Catalog (admin-only, experimental; supports a subset of search fields).

          tags: Filter by tag values or UUIDs. Indicators must have at least one of the
              specified tags (OR logic). Supports both tag UUID and tag value.

          tag_search: Structured tag-metadata filter as a JSON array of {field, op, value} objects.
              Operates against the per-dataset IndicatorTag mirror so you can find indicators
              by tag attributes (origin country, motive, sophistication, priority, etc.)
              without a separate Tags lookup. Common dashboard usage: drill from a country
              into indicators, e.g.
              tagSearch=[{"field":"originCountryISO","op":"in","value":["IR","CN"]}]. Country
              values may be passed as alpha-2, alpha-3, name, or alias (e.g. "iran").
              Operators: equals, not, gt/gte/lt/lte (numeric only),
              contains/like/find/startsWith/endsWith (string only), in. AND-joined across
              entries; combined with `tags`, a matching tag must satisfy both. Max 10 entries
              per request, max 100 values per 'in'. Performance notes: `originCountryISO` uses
              its B-tree index for equals/not/in. `priority` uses its B-tree index for numeric
              comparisons. Other string columns (`actorCategory`, `motive`, etc.) are
              case-insensitive and unindexed; current catalog size makes this a non-issue.
              `endsWith` and `aliasGroupNames` contains/like are leading-wildcard scans and
              slow on large result sets. `aliasGroupNames` matches on the JSON-encoded text,
              so substrings can cross alias boundaries ("apt28" also matches "apt280" when
              both appear in the same tag's alias list).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events/indicators", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cache": cache,
                        "created_after": created_after,
                        "created_before": created_before,
                        "dataset_ids": dataset_ids,
                        "format": format,
                        "include_tags": include_tags,
                        "include_total_count": include_total_count,
                        "indicator_type": indicator_type,
                        "name": name,
                        "page": page,
                        "page_size": page_size,
                        "related_events": related_events,
                        "related_events_limit": related_events_limit,
                        "search": search,
                        "source": source,
                        "tags": tags,
                        "tag_search": tag_search,
                    },
                    indicator_list_params.IndicatorListParams,
                ),
            ),
            cast_to=IndicatorListResponse,
        )


class IndicatorsResourceWithRawResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_raw_response_wrapper(
            indicators.list,
        )

    @cached_property
    def aggregate(self) -> AggregateResourceWithRawResponse:
        return AggregateResourceWithRawResponse(self._indicators.aggregate)

    @cached_property
    def types(self) -> TypesResourceWithRawResponse:
        return TypesResourceWithRawResponse(self._indicators.types)

    @cached_property
    def by_dataset(self) -> ByDatasetResourceWithRawResponse:
        return ByDatasetResourceWithRawResponse(self._indicators.by_dataset)


class AsyncIndicatorsResourceWithRawResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_raw_response_wrapper(
            indicators.list,
        )

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithRawResponse:
        return AsyncAggregateResourceWithRawResponse(self._indicators.aggregate)

    @cached_property
    def types(self) -> AsyncTypesResourceWithRawResponse:
        return AsyncTypesResourceWithRawResponse(self._indicators.types)

    @cached_property
    def by_dataset(self) -> AsyncByDatasetResourceWithRawResponse:
        return AsyncByDatasetResourceWithRawResponse(self._indicators.by_dataset)


class IndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: IndicatorsResource) -> None:
        self._indicators = indicators

        self.list = to_streamed_response_wrapper(
            indicators.list,
        )

    @cached_property
    def aggregate(self) -> AggregateResourceWithStreamingResponse:
        return AggregateResourceWithStreamingResponse(self._indicators.aggregate)

    @cached_property
    def types(self) -> TypesResourceWithStreamingResponse:
        return TypesResourceWithStreamingResponse(self._indicators.types)

    @cached_property
    def by_dataset(self) -> ByDatasetResourceWithStreamingResponse:
        return ByDatasetResourceWithStreamingResponse(self._indicators.by_dataset)


class AsyncIndicatorsResourceWithStreamingResponse:
    def __init__(self, indicators: AsyncIndicatorsResource) -> None:
        self._indicators = indicators

        self.list = async_to_streamed_response_wrapper(
            indicators.list,
        )

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithStreamingResponse:
        return AsyncAggregateResourceWithStreamingResponse(self._indicators.aggregate)

    @cached_property
    def types(self) -> AsyncTypesResourceWithStreamingResponse:
        return AsyncTypesResourceWithStreamingResponse(self._indicators.types)

    @cached_property
    def by_dataset(self) -> AsyncByDatasetResourceWithStreamingResponse:
        return AsyncByDatasetResourceWithStreamingResponse(self._indicators.by_dataset)
