# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime

import httpx

from .raw import (
    RawResource,
    AsyncRawResource,
    RawResourceWithRawResponse,
    AsyncRawResourceWithRawResponse,
    RawResourceWithStreamingResponse,
    AsyncRawResourceWithStreamingResponse,
)
from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from .crons import (
    CronsResource,
    AsyncCronsResource,
    CronsResourceWithRawResponse,
    AsyncCronsResourceWithRawResponse,
    CronsResourceWithStreamingResponse,
    AsyncCronsResourceWithStreamingResponse,
)
from .relate import (
    RelateResource,
    AsyncRelateResource,
    RelateResourceWithRawResponse,
    AsyncRelateResourceWithRawResponse,
    RelateResourceWithStreamingResponse,
    AsyncRelateResourceWithStreamingResponse,
)
from .datasets import (
    DatasetsResource,
    AsyncDatasetsResource,
    DatasetsResourceWithRawResponse,
    AsyncDatasetsResourceWithRawResponse,
    DatasetsResourceWithStreamingResponse,
    AsyncDatasetsResourceWithStreamingResponse,
)
from .insights import (
    InsightsResource,
    AsyncInsightsResource,
    InsightsResourceWithRawResponse,
    AsyncInsightsResourceWithRawResponse,
    InsightsResourceWithStreamingResponse,
    AsyncInsightsResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
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
from ...._compat import cached_property
from .categories import (
    CategoriesResource,
    AsyncCategoriesResource,
    CategoriesResourceWithRawResponse,
    AsyncCategoriesResourceWithRawResponse,
    CategoriesResourceWithStreamingResponse,
    AsyncCategoriesResourceWithStreamingResponse,
)
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
from ...._base_client import make_request_options
from .indicator_types import (
    IndicatorTypesResource,
    AsyncIndicatorTypesResource,
    IndicatorTypesResourceWithRawResponse,
    AsyncIndicatorTypesResourceWithRawResponse,
    IndicatorTypesResourceWithStreamingResponse,
    AsyncIndicatorTypesResourceWithStreamingResponse,
)
from .target_industries import (
    TargetIndustriesResource,
    AsyncTargetIndustriesResource,
    TargetIndustriesResourceWithRawResponse,
    AsyncTargetIndustriesResourceWithRawResponse,
    TargetIndustriesResourceWithStreamingResponse,
    AsyncTargetIndustriesResourceWithStreamingResponse,
)
from ....types.cloudforce_one import (
    threat_event_edit_params,
    threat_event_create_params,
    threat_event_bulk_create_params,
)
from ....types.cloudforce_one.threat_event_get_response import ThreatEventGetResponse
from ....types.cloudforce_one.threat_event_edit_response import ThreatEventEditResponse
from ....types.cloudforce_one.threat_event_create_response import ThreatEventCreateResponse
from ....types.cloudforce_one.threat_event_delete_response import ThreatEventDeleteResponse
from ....types.cloudforce_one.threat_event_bulk_create_response import ThreatEventBulkCreateResponse

__all__ = ["ThreatEventsResource", "AsyncThreatEventsResource"]


class ThreatEventsResource(SyncAPIResource):
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
    def crons(self) -> CronsResource:
        return CronsResource(self._client)

    @cached_property
    def datasets(self) -> DatasetsResource:
        return DatasetsResource(self._client)

    @cached_property
    def indicator_types(self) -> IndicatorTypesResource:
        return IndicatorTypesResource(self._client)

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
    def insights(self) -> InsightsResource:
        return InsightsResource(self._client)

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
        path_account_id: float,
        attacker: str,
        attacker_country: str,
        category: str,
        date: Union[str, datetime],
        event: str,
        indicator_type: str,
        raw: threat_event_create_params.Raw,
        tlp: str,
        body_account_id: float | NotGiven = NOT_GIVEN,
        dataset_id: str | NotGiven = NOT_GIVEN,
        indicator: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        target_country: str | NotGiven = NOT_GIVEN,
        target_industry: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventCreateResponse:
        """
        Creates a new event

        Args:
          path_account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{path_account_id}/cloudforce-one/events/create",
            body=maybe_transform(
                {
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "date": date,
                    "event": event,
                    "indicator_type": indicator_type,
                    "raw": raw,
                    "tlp": tlp,
                    "body_account_id": body_account_id,
                    "dataset_id": dataset_id,
                    "indicator": indicator,
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

    def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventDeleteResponse:
        """
        Deletes an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventDeleteResponse,
        )

    def bulk_create(
        self,
        *,
        account_id: float,
        data: Iterable[threat_event_bulk_create_params.Data],
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventBulkCreateResponse:
        """
        Creates bulk events

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/cloudforce-one/events/create/bulk",
            body=maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                threat_event_bulk_create_params.ThreatEventBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateResponse,
        )

    def edit(
        self,
        event_id: str,
        *,
        account_id: float,
        attacker: str | NotGiven = NOT_GIVEN,
        attacker_country: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event: str | NotGiven = NOT_GIVEN,
        indicator: str | NotGiven = NOT_GIVEN,
        indicator_type: str | NotGiven = NOT_GIVEN,
        target_country: str | NotGiven = NOT_GIVEN,
        target_industry: str | NotGiven = NOT_GIVEN,
        tlp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventEditResponse:
        """
        Updates an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
            body=maybe_transform(
                {
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "date": date,
                    "event": event,
                    "indicator": indicator,
                    "indicator_type": indicator_type,
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

    def get(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventGetResponse:
        """
        Reads an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventGetResponse,
        )


class AsyncThreatEventsResource(AsyncAPIResource):
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
    def crons(self) -> AsyncCronsResource:
        return AsyncCronsResource(self._client)

    @cached_property
    def datasets(self) -> AsyncDatasetsResource:
        return AsyncDatasetsResource(self._client)

    @cached_property
    def indicator_types(self) -> AsyncIndicatorTypesResource:
        return AsyncIndicatorTypesResource(self._client)

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
    def insights(self) -> AsyncInsightsResource:
        return AsyncInsightsResource(self._client)

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
        path_account_id: float,
        attacker: str,
        attacker_country: str,
        category: str,
        date: Union[str, datetime],
        event: str,
        indicator_type: str,
        raw: threat_event_create_params.Raw,
        tlp: str,
        body_account_id: float | NotGiven = NOT_GIVEN,
        dataset_id: str | NotGiven = NOT_GIVEN,
        indicator: str | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        target_country: str | NotGiven = NOT_GIVEN,
        target_industry: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventCreateResponse:
        """
        Creates a new event

        Args:
          path_account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{path_account_id}/cloudforce-one/events/create",
            body=await async_maybe_transform(
                {
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "date": date,
                    "event": event,
                    "indicator_type": indicator_type,
                    "raw": raw,
                    "tlp": tlp,
                    "body_account_id": body_account_id,
                    "dataset_id": dataset_id,
                    "indicator": indicator,
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

    async def delete(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventDeleteResponse:
        """
        Deletes an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventDeleteResponse,
        )

    async def bulk_create(
        self,
        *,
        account_id: float,
        data: Iterable[threat_event_bulk_create_params.Data],
        dataset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventBulkCreateResponse:
        """
        Creates bulk events

        Args:
          account_id: Account ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/cloudforce-one/events/create/bulk",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "dataset_id": dataset_id,
                },
                threat_event_bulk_create_params.ThreatEventBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ThreatEventBulkCreateResponse,
        )

    async def edit(
        self,
        event_id: str,
        *,
        account_id: float,
        attacker: str | NotGiven = NOT_GIVEN,
        attacker_country: str | NotGiven = NOT_GIVEN,
        category: str | NotGiven = NOT_GIVEN,
        date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        event: str | NotGiven = NOT_GIVEN,
        indicator: str | NotGiven = NOT_GIVEN,
        indicator_type: str | NotGiven = NOT_GIVEN,
        target_country: str | NotGiven = NOT_GIVEN,
        target_industry: str | NotGiven = NOT_GIVEN,
        tlp: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventEditResponse:
        """
        Updates an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
            body=await async_maybe_transform(
                {
                    "attacker": attacker,
                    "attacker_country": attacker_country,
                    "category": category,
                    "date": date,
                    "event": event,
                    "indicator": indicator,
                    "indicator_type": indicator_type,
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

    async def get(
        self,
        event_id: str,
        *,
        account_id: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ThreatEventGetResponse:
        """
        Reads an event

        Args:
          account_id: Account ID

          event_id: Event UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            f"/accounts/{account_id}/cloudforce-one/events/{event_id}",
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
        self.delete = to_raw_response_wrapper(
            threat_events.delete,
        )
        self.bulk_create = to_raw_response_wrapper(
            threat_events.bulk_create,
        )
        self.edit = to_raw_response_wrapper(
            threat_events.edit,
        )
        self.get = to_raw_response_wrapper(
            threat_events.get,
        )

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
    def crons(self) -> CronsResourceWithRawResponse:
        return CronsResourceWithRawResponse(self._threat_events.crons)

    @cached_property
    def datasets(self) -> DatasetsResourceWithRawResponse:
        return DatasetsResourceWithRawResponse(self._threat_events.datasets)

    @cached_property
    def indicator_types(self) -> IndicatorTypesResourceWithRawResponse:
        return IndicatorTypesResourceWithRawResponse(self._threat_events.indicator_types)

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

    @cached_property
    def insights(self) -> InsightsResourceWithRawResponse:
        return InsightsResourceWithRawResponse(self._threat_events.insights)


class AsyncThreatEventsResourceWithRawResponse:
    def __init__(self, threat_events: AsyncThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = async_to_raw_response_wrapper(
            threat_events.create,
        )
        self.delete = async_to_raw_response_wrapper(
            threat_events.delete,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            threat_events.bulk_create,
        )
        self.edit = async_to_raw_response_wrapper(
            threat_events.edit,
        )
        self.get = async_to_raw_response_wrapper(
            threat_events.get,
        )

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
    def crons(self) -> AsyncCronsResourceWithRawResponse:
        return AsyncCronsResourceWithRawResponse(self._threat_events.crons)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithRawResponse:
        return AsyncDatasetsResourceWithRawResponse(self._threat_events.datasets)

    @cached_property
    def indicator_types(self) -> AsyncIndicatorTypesResourceWithRawResponse:
        return AsyncIndicatorTypesResourceWithRawResponse(self._threat_events.indicator_types)

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

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithRawResponse:
        return AsyncInsightsResourceWithRawResponse(self._threat_events.insights)


class ThreatEventsResourceWithStreamingResponse:
    def __init__(self, threat_events: ThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = to_streamed_response_wrapper(
            threat_events.create,
        )
        self.delete = to_streamed_response_wrapper(
            threat_events.delete,
        )
        self.bulk_create = to_streamed_response_wrapper(
            threat_events.bulk_create,
        )
        self.edit = to_streamed_response_wrapper(
            threat_events.edit,
        )
        self.get = to_streamed_response_wrapper(
            threat_events.get,
        )

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
    def crons(self) -> CronsResourceWithStreamingResponse:
        return CronsResourceWithStreamingResponse(self._threat_events.crons)

    @cached_property
    def datasets(self) -> DatasetsResourceWithStreamingResponse:
        return DatasetsResourceWithStreamingResponse(self._threat_events.datasets)

    @cached_property
    def indicator_types(self) -> IndicatorTypesResourceWithStreamingResponse:
        return IndicatorTypesResourceWithStreamingResponse(self._threat_events.indicator_types)

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

    @cached_property
    def insights(self) -> InsightsResourceWithStreamingResponse:
        return InsightsResourceWithStreamingResponse(self._threat_events.insights)


class AsyncThreatEventsResourceWithStreamingResponse:
    def __init__(self, threat_events: AsyncThreatEventsResource) -> None:
        self._threat_events = threat_events

        self.create = async_to_streamed_response_wrapper(
            threat_events.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            threat_events.delete,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            threat_events.bulk_create,
        )
        self.edit = async_to_streamed_response_wrapper(
            threat_events.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            threat_events.get,
        )

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
    def crons(self) -> AsyncCronsResourceWithStreamingResponse:
        return AsyncCronsResourceWithStreamingResponse(self._threat_events.crons)

    @cached_property
    def datasets(self) -> AsyncDatasetsResourceWithStreamingResponse:
        return AsyncDatasetsResourceWithStreamingResponse(self._threat_events.datasets)

    @cached_property
    def indicator_types(self) -> AsyncIndicatorTypesResourceWithStreamingResponse:
        return AsyncIndicatorTypesResourceWithStreamingResponse(self._threat_events.indicator_types)

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

    @cached_property
    def insights(self) -> AsyncInsightsResourceWithStreamingResponse:
        return AsyncInsightsResourceWithStreamingResponse(self._threat_events.insights)
