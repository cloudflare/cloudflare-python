# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .destinations import (
    Destinations,
    AsyncDestinations,
    DestinationsWithRawResponse,
    AsyncDestinationsWithRawResponse,
    DestinationsWithStreamingResponse,
    AsyncDestinationsWithStreamingResponse,
)
from .available_alerts import (
    AvailableAlerts,
    AsyncAvailableAlerts,
    AvailableAlertsWithRawResponse,
    AsyncAvailableAlertsWithRawResponse,
    AvailableAlertsWithStreamingResponse,
    AsyncAvailableAlertsWithStreamingResponse,
)
from .destinations.destinations import Destinations, AsyncDestinations

__all__ = ["Alerting", "AsyncAlerting"]


class Alerting(SyncAPIResource):
    @cached_property
    def available_alerts(self) -> AvailableAlerts:
        return AvailableAlerts(self._client)

    @cached_property
    def destinations(self) -> Destinations:
        return Destinations(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> AlertingWithRawResponse:
        return AlertingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertingWithStreamingResponse:
        return AlertingWithStreamingResponse(self)


class AsyncAlerting(AsyncAPIResource):
    @cached_property
    def available_alerts(self) -> AsyncAvailableAlerts:
        return AsyncAvailableAlerts(self._client)

    @cached_property
    def destinations(self) -> AsyncDestinations:
        return AsyncDestinations(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlertingWithRawResponse:
        return AsyncAlertingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertingWithStreamingResponse:
        return AsyncAlertingWithStreamingResponse(self)


class AlertingWithRawResponse:
    def __init__(self, alerting: Alerting) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AvailableAlertsWithRawResponse:
        return AvailableAlertsWithRawResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._alerting.history)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._alerting.policies)


class AsyncAlertingWithRawResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsWithRawResponse:
        return AsyncAvailableAlertsWithRawResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._alerting.history)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._alerting.policies)


class AlertingWithStreamingResponse:
    def __init__(self, alerting: Alerting) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AvailableAlertsWithStreamingResponse:
        return AvailableAlertsWithStreamingResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._alerting.history)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._alerting.policies)


class AsyncAlertingWithStreamingResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsWithStreamingResponse:
        return AsyncAvailableAlertsWithStreamingResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._alerting.history)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._alerting.policies)
