# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .webhooks import (
    Webhooks,
    AsyncWebhooks,
    WebhooksWithRawResponse,
    AsyncWebhooksWithRawResponse,
    WebhooksWithStreamingResponse,
    AsyncWebhooksWithStreamingResponse,
)
from .eligibles import (
    Eligibles,
    AsyncEligibles,
    EligiblesWithRawResponse,
    AsyncEligiblesWithRawResponse,
    EligiblesWithStreamingResponse,
    AsyncEligiblesWithStreamingResponse,
)
from ....._compat import cached_property
from .pagerduties import (
    Pagerduties,
    AsyncPagerduties,
    PagerdutiesWithRawResponse,
    AsyncPagerdutiesWithRawResponse,
    PagerdutiesWithStreamingResponse,
    AsyncPagerdutiesWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def eligibles(self) -> Eligibles:
        return Eligibles(self._client)

    @cached_property
    def pagerduties(self) -> Pagerduties:
        return Pagerduties(self._client)

    @cached_property
    def webhooks(self) -> Webhooks:
        return Webhooks(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self)


class AsyncDestinations(AsyncAPIResource):
    @cached_property
    def eligibles(self) -> AsyncEligibles:
        return AsyncEligibles(self._client)

    @cached_property
    def pagerduties(self) -> AsyncPagerduties:
        return AsyncPagerduties(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        return AsyncWebhooks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self)


class DestinationsWithRawResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> EligiblesWithRawResponse:
        return EligiblesWithRawResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> PagerdutiesWithRawResponse:
        return PagerdutiesWithRawResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> WebhooksWithRawResponse:
        return WebhooksWithRawResponse(self._destinations.webhooks)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> AsyncEligiblesWithRawResponse:
        return AsyncEligiblesWithRawResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> AsyncPagerdutiesWithRawResponse:
        return AsyncPagerdutiesWithRawResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithRawResponse:
        return AsyncWebhooksWithRawResponse(self._destinations.webhooks)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> EligiblesWithStreamingResponse:
        return EligiblesWithStreamingResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> PagerdutiesWithStreamingResponse:
        return PagerdutiesWithStreamingResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> WebhooksWithStreamingResponse:
        return WebhooksWithStreamingResponse(self._destinations.webhooks)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> AsyncEligiblesWithStreamingResponse:
        return AsyncEligiblesWithStreamingResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> AsyncPagerdutiesWithStreamingResponse:
        return AsyncPagerdutiesWithStreamingResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithStreamingResponse:
        return AsyncWebhooksWithStreamingResponse(self._destinations.webhooks)
