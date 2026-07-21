# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from .graph import (
    GraphResource,
    AsyncGraphResource,
    GraphResourceWithRawResponse,
    AsyncGraphResourceWithRawResponse,
    GraphResourceWithStreamingResponse,
    AsyncGraphResourceWithStreamingResponse,
)
from .relate import (
    RelateResource,
    AsyncRelateResource,
    RelateResourceWithRawResponse,
    AsyncRelateResourceWithRawResponse,
    RelateResourceWithStreamingResponse,
    AsyncRelateResourceWithStreamingResponse,
)
from .graphql import (
    GraphqlResource,
    AsyncGraphqlResource,
    GraphqlResourceWithRawResponse,
    AsyncGraphqlResourceWithRawResponse,
    GraphqlResourceWithStreamingResponse,
    AsyncGraphqlResourceWithStreamingResponse,
)
from .queries import (
    QueriesResource,
    AsyncQueriesResource,
    QueriesResourceWithRawResponse,
    AsyncQueriesResourceWithRawResponse,
    QueriesResourceWithStreamingResponse,
    AsyncQueriesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from .aggregate import (
    AggregateResource,
    AsyncAggregateResource,
    AggregateResourceWithRawResponse,
    AsyncAggregateResourceWithRawResponse,
    AggregateResourceWithStreamingResponse,
    AsyncAggregateResourceWithStreamingResponse,
)
from .attackers import (
    AttackersResource,
    AsyncAttackersResource,
    AttackersResourceWithRawResponse,
    AsyncAttackersResourceWithRawResponse,
    AttackersResourceWithStreamingResponse,
    AsyncAttackersResourceWithStreamingResponse,
)
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from .tags.tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .event_tags import (
    EventTagsResource,
    AsyncEventTagsResource,
    EventTagsResourceWithRawResponse,
    AsyncEventTagsResourceWithRawResponse,
    EventTagsResourceWithStreamingResponse,
    AsyncEventTagsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .relationships import (
    RelationshipsResource,
    AsyncRelationshipsResource,
    RelationshipsResourceWithRawResponse,
    AsyncRelationshipsResourceWithRawResponse,
    RelationshipsResourceWithStreamingResponse,
    AsyncRelationshipsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .datasets.datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .categories.categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
from .indicators.indicators import (
    IndicatorsResource,
    AsyncIndicatorsResource,
    IndicatorsResourceWithRawResponse,
    AsyncIndicatorsResourceWithRawResponse,
    IndicatorsResourceWithStreamingResponse,
    AsyncIndicatorsResourceWithStreamingResponse,
)
from ....types.cloudforce_one import (
    threat_event_edit_params,
    threat_event_list_params,
    threat_event_create_params,
    threat_event_bulk_create_params,
    threat_event_bulk_create_relationships_params,
)
from .target_industries.target_industries import (
    TargetIndustriesResource,
    AsyncTargetIndustriesResource,
    TargetIndustriesResourceWithRawResponse,
    AsyncTargetIndustriesResourceWithRawResponse,
    TargetIndustriesResourceWithStreamingResponse,
    AsyncTargetIndustriesResourceWithStreamingResponse,
)
from ....types.cloudforce_one.threat_event_get_response import ThreatEventGetResponse
from ....types.cloudforce_one.threat_event_edit_response import ThreatEventEditResponse
from ....types.cloudforce_one.threat_event_list_response import ThreatEventListResponse
from ....types.cloudforce_one.threat_event_create_response import ThreatEventCreateResponse
from ....types.cloudforce_one.threat_event_bulk_create_response import ThreatEventBulkCreateResponse
from ....types.cloudforce_one.threat_event_bulk_create_relationships_response import (
    ThreatEventBulkCreateRelationshipsResponse,
)

__all__ = ["ThreatEventsResource", "AsyncThreatEventsResource"]


class ThreatEventsResource(SyncAPIResource):
    @cached_property
    def aggregate(self) -> AggregateResource:
        return AggregateResource(self._client)

    @cached_property
    def graphql(self) -> GraphqlResource:
        return GraphqlResource(self._client)

    @cached_property
    def graph(self) -> GraphResource:
        return GraphResource(self._client)

    @cached_property
    def queries(self) -> QueriesResource:
        return QueriesResource(self._client)

    @cached_property
    def relationships(self) -> RelationshipsResource:
        return RelationshipsResource(self._client)

    @cached_property
    def indicators(self) -> IndicatorsResource:
        return IndicatorsResource(self._client)

    @cached_property
    def attackers(self) -> AttackersResource:
        return AttackersResource(self._client)

    @cached_property
    def categories(self) -> CategoriesResource:
        return CategoriesResource(self._client)

    @cached_property
    def countries(self) -> CountriesResource:
        return CountriesResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def raw(self) -> RawResource:
        return RawResource(self._client)

    @cached_property
    def relate(self) -> RelateResource:
        return RelateResource(self._client)

    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def event_tags(self) -> EventTagsResource:
        return EventTagsResource(self._client)

    @cached_property
    def target_industries(self) -> TargetIndustriesResource:
        return TargetIndustriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreatEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ThreatEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreatEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ThreatEventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        path_account_id: str,
        category: str,
        date: Union[str, datetime],
        event: str,
        raw: threat_event_create_params.Raw,
        tlp: str,
        body_account_id: float | Omit = omit,
        attacker: Optional[str] | Omit = omit,
        attacker_country: str | Omit = omit,
        dataset_id: str | Omit = omit,
        indicator: str | Omit = omit,
        indicators: Iterable[threat_event_create_params.Indicator] | Omit = omit,
        indicator_type: str | Omit = omit,
        insight: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_country: str | Omit = omit,
        target_industry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventCreateResponse:
        """
        To create a dataset, see the
        [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/)
        endpoint. When `datasetId` parameter is unspecified, it will be created in a
        default dataset named `Cloudforce One Threat Events`.

        Args:
          path_account_id: Account ID.

          indicators: Array of indicators for this event. Supports multiple indicators per event for
              complex scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_account_id:
            raise ValueError(f"Expected a non-empty value for `path_account_id` but received {path_account_id!r}")
        return self._post(
            path_template("/accounts/{path_account_id}/cloudforce-one/events/create", path_account_id=path_account_id),
            body=maybe_transform(
                {
                    "category": category,
                    "date": date,
                    "event": event,
                    "raw": raw,
                    "tlp": tlp,
                    "body_account_id": body_account_id,
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "dataset_id": dataset_id,
                    "indicator": indicator,
                    "indicators": indicators,
                    "indicator_type": indicator_type,
                    "insight": insight,
                    "tags": tags,
                    "target_country": target_country,
                    "target_industry": target_industry,
                },
                threat_event_create_params.ThreatEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventCreateResponse,
        )

    def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_id: SequenceNotStr[str] | Omit = omit,
        force_refresh: bool | Omit = omit,
        format: Literal["json", "stix2", "taxii"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        search: Iterable[threat_event_list_params.Search] | Omit = omit,
        source: Literal["do", "r2catalog"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventListResponse:
        """
        Use `datasetId=all` or `datasetId=*` to query all event datasets for the account
        (limited to 50). When `datasetId` is unspecified, events are listed from the
        default Cloudforce One Threat Events dataset. To list existing datasets, use the
        [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/)
        endpoint.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          cursor: Cursor for pagination. When provided, filters are embedded in the cursor so you
              only need to pass cursor and pageSize. Returned in the previous response's
              result_info.cursor field. Use cursor-based pagination for deep pagination
              (beyond 100,000 records) or for optimal performance.

          dataset_id: Dataset IDs to query events from (array of UUIDs), or special value 'all' or
              '\\**' to query all event datasets for the account. If not provided, uses the
              default dataset.

          page: Page number (1-indexed) for offset-based pagination. Limited to offset of
              100,000 records. For deep pagination, use cursor-based pagination instead.

          page_size: Number of results per page. Maximum 25,000.

          source: Read backend. 'do' (default) reads Durable Object storage. 'r2catalog' reads R2
              Data Catalog (admin-only, experimental; supports a subset of search fields — no
              'tags').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cache": cache,
                        "cursor": cursor,
                        "dataset_id": dataset_id,
                        "force_refresh": force_refresh,
                        "format": format,
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "source": source,
                    },
                    threat_event_list_params.ThreatEventListParams,
                ),
            ),
            cast_to=ThreatEventListResponse,
        )

    def bulk_create(
        self,
        *,
        account_id: str,
        data: Iterable[threat_event_bulk_create_params.Data],
        dataset_id: str,
        include_created_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventBulkCreateResponse:
        """The `datasetId` parameter must be defined.

        To list existing datasets (and their
        IDs) in your account, use the
        [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/)
        endpoint.

        Args:
          account_id: Account ID.

          include_created_events: When true, response includes array of created event UUIDs and shard IDs. Useful
              for tracking which events were created and where.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/create/bulk", account_id=account_id),
            body=maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                    "include_created_events": include_created_events,
                },
                threat_event_bulk_create_params.ThreatEventBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateResponse,
        )

    @typing_extensions.deprecated("This endpoint is deprecated and will be removed in a future version.")
    def bulk_create_relationships(
        self,
        *,
        account_id: str,
        data: Iterable[threat_event_bulk_create_relationships_params.Data],
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventBulkCreateRelationshipsResponse:
        """This method is deprecated.

        Please use `event_create_bulk` instead

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/create/bulk/relationships", account_id=account_id
            ),
            body=maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                threat_event_bulk_create_relationships_params.ThreatEventBulkCreateRelationshipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateRelationshipsResponse,
        )

    def edit(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        attacker: Optional[str] | Omit = omit,
        attacker_country: str | Omit = omit,
        category: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        event: str | Omit = omit,
        indicator: str | Omit = omit,
        indicator_type: str | Omit = omit,
        insight: str | Omit = omit,
        raw: threat_event_edit_params.Raw | Omit = omit,
        target_country: str | Omit = omit,
        target_industry: str | Omit = omit,
        tlp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventEditResponse:
        """
        Update an existing event by its identifier.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          dataset_id: Dataset ID containing the event to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}", account_id=account_id, event_id=event_id
            ),
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "created_at": created_at,
                    "date": date,
                    "event": event,
                    "indicator": indicator,
                    "indicator_type": indicator_type,
                    "insight": insight,
                    "raw": raw,
                    "target_country": target_country,
                    "target_industry": target_industry,
                    "tlp": tlp,
                },
                threat_event_edit_params.ThreatEventEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventEditResponse,
        )

    @typing_extensions.deprecated(
        "Use datasets.events.get instead (GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/events/{event_id})."
    )
    def get(
        self,
        event_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventGetResponse:
        """This Method is deprecated.

        Please use
        /events/dataset/:dataset_id/events/:event_id instead.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}", account_id=account_id, event_id=event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventGetResponse,
        )


class AsyncThreatEventsResource(AsyncAPIResource):
    @cached_property
    def aggregate(self) -> AsyncAggregateResource:
        return AsyncAggregateResource(self._client)

    @cached_property
    def graphql(self) -> AsyncGraphqlResource:
        return AsyncGraphqlResource(self._client)

    @cached_property
    def graph(self) -> AsyncGraphResource:
        return AsyncGraphResource(self._client)

    @cached_property
    def queries(self) -> AsyncQueriesResource:
        return AsyncQueriesResource(self._client)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResource:
        return AsyncRelationshipsResource(self._client)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResource:
        return AsyncIndicatorsResource(self._client)

    @cached_property
    def attackers(self) -> AsyncAttackersResource:
        return AsyncAttackersResource(self._client)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        return AsyncCategoriesResource(self._client)

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        return AsyncCountriesResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def raw(self) -> AsyncRawResource:
        return AsyncRawResource(self._client)

    @cached_property
    def relate(self) -> AsyncRelateResource:
        return AsyncRelateResource(self._client)

    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def event_tags(self) -> AsyncEventTagsResource:
        return AsyncEventTagsResource(self._client)

    @cached_property
    def target_industries(self) -> AsyncTargetIndustriesResource:
        return AsyncTargetIndustriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreatEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreatEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreatEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncThreatEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        path_account_id: str,
        category: str,
        date: Union[str, datetime],
        event: str,
        raw: threat_event_create_params.Raw,
        tlp: str,
        body_account_id: float | Omit = omit,
        attacker: Optional[str] | Omit = omit,
        attacker_country: str | Omit = omit,
        dataset_id: str | Omit = omit,
        indicator: str | Omit = omit,
        indicators: Iterable[threat_event_create_params.Indicator] | Omit = omit,
        indicator_type: str | Omit = omit,
        insight: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        target_country: str | Omit = omit,
        target_industry: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventCreateResponse:
        """
        To create a dataset, see the
        [`Create Dataset`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/create/)
        endpoint. When `datasetId` parameter is unspecified, it will be created in a
        default dataset named `Cloudforce One Threat Events`.

        Args:
          path_account_id: Account ID.

          indicators: Array of indicators for this event. Supports multiple indicators per event for
              complex scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_account_id:
            raise ValueError(f"Expected a non-empty value for `path_account_id` but received {path_account_id!r}")
        return await self._post(
            path_template("/accounts/{path_account_id}/cloudforce-one/events/create", path_account_id=path_account_id),
            body=await async_maybe_transform(
                {
                    "category": category,
                    "date": date,
                    "event": event,
                    "raw": raw,
                    "tlp": tlp,
                    "body_account_id": body_account_id,
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "dataset_id": dataset_id,
                    "indicator": indicator,
                    "indicators": indicators,
                    "indicator_type": indicator_type,
                    "insight": insight,
                    "tags": tags,
                    "target_country": target_country,
                    "target_industry": target_industry,
                },
                threat_event_create_params.ThreatEventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventCreateResponse,
        )

    async def list(
        self,
        *,
        account_id: str,
        cache: Literal["from-graph"] | Omit = omit,
        cursor: str | Omit = omit,
        dataset_id: SequenceNotStr[str] | Omit = omit,
        force_refresh: bool | Omit = omit,
        format: Literal["json", "stix2", "taxii"] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_by: str | Omit = omit,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        search: Iterable[threat_event_list_params.Search] | Omit = omit,
        source: Literal["do", "r2catalog"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventListResponse:
        """
        Use `datasetId=all` or `datasetId=*` to query all event datasets for the account
        (limited to 50). When `datasetId` is unspecified, events are listed from the
        default Cloudforce One Threat Events dataset. To list existing datasets, use the
        [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/)
        endpoint.

        Args:
          account_id: Account ID.

          cache: Cache strategy. 'from-graph' serves results from the graph-node KV cache when
              all requested UUIDs are cached; falls back to normal path on partial/zero hit.

          cursor: Cursor for pagination. When provided, filters are embedded in the cursor so you
              only need to pass cursor and pageSize. Returned in the previous response's
              result_info.cursor field. Use cursor-based pagination for deep pagination
              (beyond 100,000 records) or for optimal performance.

          dataset_id: Dataset IDs to query events from (array of UUIDs), or special value 'all' or
              '\\**' to query all event datasets for the account. If not provided, uses the
              default dataset.

          page: Page number (1-indexed) for offset-based pagination. Limited to offset of
              100,000 records. For deep pagination, use cursor-based pagination instead.

          page_size: Number of results per page. Maximum 25,000.

          source: Read backend. 'do' (default) reads Durable Object storage. 'r2catalog' reads R2
              Data Catalog (admin-only, experimental; supports a subset of search fields — no
              'tags').

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/cloudforce-one/events", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cache": cache,
                        "cursor": cursor,
                        "dataset_id": dataset_id,
                        "force_refresh": force_refresh,
                        "format": format,
                        "order": order,
                        "order_by": order_by,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "source": source,
                    },
                    threat_event_list_params.ThreatEventListParams,
                ),
            ),
            cast_to=ThreatEventListResponse,
        )

    async def bulk_create(
        self,
        *,
        account_id: str,
        data: Iterable[threat_event_bulk_create_params.Data],
        dataset_id: str,
        include_created_events: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventBulkCreateResponse:
        """The `datasetId` parameter must be defined.

        To list existing datasets (and their
        IDs) in your account, use the
        [`List Datasets`](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/datasets/methods/list/)
        endpoint.

        Args:
          account_id: Account ID.

          include_created_events: When true, response includes array of created event UUIDs and shard IDs. Useful
              for tracking which events were created and where.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/cloudforce-one/events/create/bulk", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                    "include_created_events": include_created_events,
                },
                threat_event_bulk_create_params.ThreatEventBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateResponse,
        )

    @typing_extensions.deprecated("This endpoint is deprecated and will be removed in a future version.")
    async def bulk_create_relationships(
        self,
        *,
        account_id: str,
        data: Iterable[threat_event_bulk_create_relationships_params.Data],
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventBulkCreateRelationshipsResponse:
        """This method is deprecated.

        Please use `event_create_bulk` instead

        Args:
          account_id: Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/create/bulk/relationships", account_id=account_id
            ),
            body=await async_maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                threat_event_bulk_create_relationships_params.ThreatEventBulkCreateRelationshipsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateRelationshipsResponse,
        )

    async def edit(
        self,
        event_id: str,
        *,
        account_id: str,
        dataset_id: str,
        attacker: Optional[str] | Omit = omit,
        attacker_country: str | Omit = omit,
        category: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        date: Union[str, datetime] | Omit = omit,
        event: str | Omit = omit,
        indicator: str | Omit = omit,
        indicator_type: str | Omit = omit,
        insight: str | Omit = omit,
        raw: threat_event_edit_params.Raw | Omit = omit,
        target_country: str | Omit = omit,
        target_industry: str | Omit = omit,
        tlp: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventEditResponse:
        """
        Update an existing event by its identifier.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          dataset_id: Dataset ID containing the event to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}", account_id=account_id, event_id=event_id
            ),
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "created_at": created_at,
                    "date": date,
                    "event": event,
                    "indicator": indicator,
                    "indicator_type": indicator_type,
                    "insight": insight,
                    "raw": raw,
                    "target_country": target_country,
                    "target_industry": target_industry,
                    "tlp": tlp,
                },
                threat_event_edit_params.ThreatEventEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventEditResponse,
        )

    @typing_extensions.deprecated(
        "Use datasets.events.get instead (GET /accounts/{account_id}/cloudforce-one/events/dataset/{dataset_id}/events/{event_id})."
    )
    async def get(
        self,
        event_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ThreatEventGetResponse:
        """This Method is deprecated.

        Please use
        /events/dataset/:dataset_id/events/:event_id instead.

        Args:
          account_id: Account ID.

          event_id: Event UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/cloudforce-one/events/{event_id}", account_id=account_id, event_id=event_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventGetResponse,
        )


class ThreatEventsResourceWithRawResponse:
    def __init__(self, threat_events: ThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = to_raw_response_wrapper(
            threat_events.create,
        )
        self.list = to_raw_response_wrapper(
            threat_events.list,
        )
        self.bulk_create = to_raw_response_wrapper(
            threat_events.bulk_create,
        )
        self.bulk_create_relationships = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                threat_events.bulk_create_relationships,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = to_raw_response_wrapper(
            threat_events.edit,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                threat_events.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def aggregate(self) -> AggregateResourceWithRawResponse:
        return AggregateResourceWithRawResponse(self._threat_events.aggregate)

    @cached_property
    def graphql(self) -> GraphqlResourceWithRawResponse:
        return GraphqlResourceWithRawResponse(self._threat_events.graphql)

    @cached_property
    def graph(self) -> GraphResourceWithRawResponse:
        return GraphResourceWithRawResponse(self._threat_events.graph)

    @cached_property
    def queries(self) -> QueriesResourceWithRawResponse:
        return QueriesResourceWithRawResponse(self._threat_events.queries)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithRawResponse:
        return RelationshipsResourceWithRawResponse(self._threat_events.relationships)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithRawResponse:
        return IndicatorsResourceWithRawResponse(self._threat_events.indicators)

    @cached_property
    def attackers(self) -> AttackersResourceWithRawResponse:
        return AttackersResourceWithRawResponse(self._threat_events.attackers)

    @cached_property
    def categories(self) -> CategoriesResourceWithRawResponse:
        return CategoriesResourceWithRawResponse(self._threat_events.categories)

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        return CountriesResourceWithRawResponse(self._threat_events.countries)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._threat_events.datasets)

    @cached_property
    def raw(self) -> RawResourceWithRawResponse:
        return RawResourceWithRawResponse(self._threat_events.raw)

    @cached_property
    def relate(self) -> RelateResourceWithRawResponse:
        return RelateResourceWithRawResponse(self._threat_events.relate)

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._threat_events.tags)

    @cached_property
    def event_tags(self) -> EventTagsResourceWithRawResponse:
        return EventTagsResourceWithRawResponse(self._threat_events.event_tags)

    @cached_property
    def target_industries(self) -> TargetIndustriesResourceWithRawResponse:
        return TargetIndustriesResourceWithRawResponse(self._threat_events.target_industries)


class AsyncThreatEventsResourceWithRawResponse:
    def __init__(self, threat_events: AsyncThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = async_to_raw_response_wrapper(
            threat_events.create,
        )
        self.list = async_to_raw_response_wrapper(
            threat_events.list,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            threat_events.bulk_create,
        )
        self.bulk_create_relationships = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                threat_events.bulk_create_relationships,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = async_to_raw_response_wrapper(
            threat_events.edit,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                threat_events.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithRawResponse:
        return AsyncAggregateResourceWithRawResponse(self._threat_events.aggregate)

    @cached_property
    def graphql(self) -> AsyncGraphqlResourceWithRawResponse:
        return AsyncGraphqlResourceWithRawResponse(self._threat_events.graphql)

    @cached_property
    def graph(self) -> AsyncGraphResourceWithRawResponse:
        return AsyncGraphResourceWithRawResponse(self._threat_events.graph)

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithRawResponse:
        return AsyncQueriesResourceWithRawResponse(self._threat_events.queries)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithRawResponse:
        return AsyncRelationshipsResourceWithRawResponse(self._threat_events.relationships)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithRawResponse:
        return AsyncIndicatorsResourceWithRawResponse(self._threat_events.indicators)

    @cached_property
    def attackers(self) -> AsyncAttackersResourceWithRawResponse:
        return AsyncAttackersResourceWithRawResponse(self._threat_events.attackers)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithRawResponse:
        return AsyncCategoriesResourceWithRawResponse(self._threat_events.categories)

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        return AsyncCountriesResourceWithRawResponse(self._threat_events.countries)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._threat_events.datasets)

    @cached_property
    def raw(self) -> AsyncRawResourceWithRawResponse:
        return AsyncRawResourceWithRawResponse(self._threat_events.raw)

    @cached_property
    def relate(self) -> AsyncRelateResourceWithRawResponse:
        return AsyncRelateResourceWithRawResponse(self._threat_events.relate)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._threat_events.tags)

    @cached_property
    def event_tags(self) -> AsyncEventTagsResourceWithRawResponse:
        return AsyncEventTagsResourceWithRawResponse(self._threat_events.event_tags)

    @cached_property
    def target_industries(self) -> AsyncTargetIndustriesResourceWithRawResponse:
        return AsyncTargetIndustriesResourceWithRawResponse(self._threat_events.target_industries)


class ThreatEventsResourceWithStreamingResponse:
    def __init__(self, threat_events: ThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = to_streamed_response_wrapper(
            threat_events.create,
        )
        self.list = to_streamed_response_wrapper(
            threat_events.list,
        )
        self.bulk_create = to_streamed_response_wrapper(
            threat_events.bulk_create,
        )
        self.bulk_create_relationships = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                threat_events.bulk_create_relationships,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = to_streamed_response_wrapper(
            threat_events.edit,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                threat_events.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def aggregate(self) -> AggregateResourceWithStreamingResponse:
        return AggregateResourceWithStreamingResponse(self._threat_events.aggregate)

    @cached_property
    def graphql(self) -> GraphqlResourceWithStreamingResponse:
        return GraphqlResourceWithStreamingResponse(self._threat_events.graphql)

    @cached_property
    def graph(self) -> GraphResourceWithStreamingResponse:
        return GraphResourceWithStreamingResponse(self._threat_events.graph)

    @cached_property
    def queries(self) -> QueriesResourceWithStreamingResponse:
        return QueriesResourceWithStreamingResponse(self._threat_events.queries)

    @cached_property
    def relationships(self) -> RelationshipsResourceWithStreamingResponse:
        return RelationshipsResourceWithStreamingResponse(self._threat_events.relationships)

    @cached_property
    def indicators(self) -> IndicatorsResourceWithStreamingResponse:
        return IndicatorsResourceWithStreamingResponse(self._threat_events.indicators)

    @cached_property
    def attackers(self) -> AttackersResourceWithStreamingResponse:
        return AttackersResourceWithStreamingResponse(self._threat_events.attackers)

    @cached_property
    def categories(self) -> CategoriesResourceWithStreamingResponse:
        return CategoriesResourceWithStreamingResponse(self._threat_events.categories)

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        return CountriesResourceWithStreamingResponse(self._threat_events.countries)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._threat_events.datasets)

    @cached_property
    def raw(self) -> RawResourceWithStreamingResponse:
        return RawResourceWithStreamingResponse(self._threat_events.raw)

    @cached_property
    def relate(self) -> RelateResourceWithStreamingResponse:
        return RelateResourceWithStreamingResponse(self._threat_events.relate)

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._threat_events.tags)

    @cached_property
    def event_tags(self) -> EventTagsResourceWithStreamingResponse:
        return EventTagsResourceWithStreamingResponse(self._threat_events.event_tags)

    @cached_property
    def target_industries(self) -> TargetIndustriesResourceWithStreamingResponse:
        return TargetIndustriesResourceWithStreamingResponse(self._threat_events.target_industries)


class AsyncThreatEventsResourceWithStreamingResponse:
    def __init__(self, threat_events: AsyncThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = async_to_streamed_response_wrapper(
            threat_events.create,
        )
        self.list = async_to_streamed_response_wrapper(
            threat_events.list,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            threat_events.bulk_create,
        )
        self.bulk_create_relationships = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                threat_events.bulk_create_relationships,  # pyright: ignore[reportDeprecated],
            )
        )
        self.edit = async_to_streamed_response_wrapper(
            threat_events.edit,
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                threat_events.get,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def aggregate(self) -> AsyncAggregateResourceWithStreamingResponse:
        return AsyncAggregateResourceWithStreamingResponse(self._threat_events.aggregate)

    @cached_property
    def graphql(self) -> AsyncGraphqlResourceWithStreamingResponse:
        return AsyncGraphqlResourceWithStreamingResponse(self._threat_events.graphql)

    @cached_property
    def graph(self) -> AsyncGraphResourceWithStreamingResponse:
        return AsyncGraphResourceWithStreamingResponse(self._threat_events.graph)

    @cached_property
    def queries(self) -> AsyncQueriesResourceWithStreamingResponse:
        return AsyncQueriesResourceWithStreamingResponse(self._threat_events.queries)

    @cached_property
    def relationships(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        return AsyncRelationshipsResourceWithStreamingResponse(self._threat_events.relationships)

    @cached_property
    def indicators(self) -> AsyncIndicatorsResourceWithStreamingResponse:
        return AsyncIndicatorsResourceWithStreamingResponse(self._threat_events.indicators)

    @cached_property
    def attackers(self) -> AsyncAttackersResourceWithStreamingResponse:
        return AsyncAttackersResourceWithStreamingResponse(self._threat_events.attackers)

    @cached_property
    def categories(self) -> AsyncCategoriesResourceWithStreamingResponse:
        return AsyncCategoriesResourceWithStreamingResponse(self._threat_events.categories)

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        return AsyncCountriesResourceWithStreamingResponse(self._threat_events.countries)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._threat_events.datasets)

    @cached_property
    def raw(self) -> AsyncRawResourceWithStreamingResponse:
        return AsyncRawResourceWithStreamingResponse(self._threat_events.raw)

    @cached_property
    def relate(self) -> AsyncRelateResourceWithStreamingResponse:
        return AsyncRelateResourceWithStreamingResponse(self._threat_events.relate)

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._threat_events.tags)

    @cached_property
    def event_tags(self) -> AsyncEventTagsResourceWithStreamingResponse:
        return AsyncEventTagsResourceWithStreamingResponse(self._threat_events.event_tags)

    @cached_property
    def target_industries(self) -> AsyncTargetIndustriesResourceWithStreamingResponse:
        return AsyncTargetIndustriesResourceWithStreamingResponse(self._threat_events.target_industries)
