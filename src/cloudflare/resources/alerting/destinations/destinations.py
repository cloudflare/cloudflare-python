# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .eligible import (
    Eligible,
    AsyncEligible,
    EligibleWithRawResponse,
    AsyncEligibleWithRawResponse,
    EligibleWithStreamingResponse,
    AsyncEligibleWithStreamingResponse,
)
from .webhooks import (
    Webhooks,
    AsyncWebhooks,
    WebhooksWithRawResponse,
    AsyncWebhooksWithRawResponse,
    WebhooksWithStreamingResponse,
    AsyncWebhooksWithStreamingResponse,
)
from .pagerduty import (
    Pagerduty,
    AsyncPagerduty,
    PagerdutyWithRawResponse,
    AsyncPagerdutyWithRawResponse,
    PagerdutyWithStreamingResponse,
    AsyncPagerdutyWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def eligible(self) -> Eligible:
        return Eligible(self._client)

    @cached_property
    def pagerduty(self) -> Pagerduty:
        return Pagerduty(self._client)

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
    def eligible(self) -> AsyncEligible:
        return AsyncEligible(self._client)

    @cached_property
    def pagerduty(self) -> AsyncPagerduty:
        return AsyncPagerduty(self._client)

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
    def eligible(self) -> EligibleWithRawResponse:
        return EligibleWithRawResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> PagerdutyWithRawResponse:
        return PagerdutyWithRawResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> WebhooksWithRawResponse:
        return WebhooksWithRawResponse(self._destinations.webhooks)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> AsyncEligibleWithRawResponse:
        return AsyncEligibleWithRawResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyWithRawResponse:
        return AsyncPagerdutyWithRawResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithRawResponse:
        return AsyncWebhooksWithRawResponse(self._destinations.webhooks)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> EligibleWithStreamingResponse:
        return EligibleWithStreamingResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> PagerdutyWithStreamingResponse:
        return PagerdutyWithStreamingResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> WebhooksWithStreamingResponse:
        return WebhooksWithStreamingResponse(self._destinations.webhooks)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligible(self) -> AsyncEligibleWithStreamingResponse:
        return AsyncEligibleWithStreamingResponse(self._destinations.eligible)

    @cached_property
    def pagerduty(self) -> AsyncPagerdutyWithStreamingResponse:
        return AsyncPagerdutyWithStreamingResponse(self._destinations.pagerduty)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithStreamingResponse:
        return AsyncWebhooksWithStreamingResponse(self._destinations.webhooks)
