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
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .available_alerts import (
    AvailableAlertsResource,
    AsyncAvailableAlertsResource,
    AvailableAlertsResourceWithRawResponse,
    AsyncAvailableAlertsResourceWithRawResponse,
    AvailableAlertsResourceWithStreamingResponse,
    AsyncAvailableAlertsResourceWithStreamingResponse,
)
from .destinations.destinations import (
    DestinationsResource,
    AsyncDestinationsResource,
    DestinationsResourceWithRawResponse,
    AsyncDestinationsResourceWithRawResponse,
    DestinationsResourceWithStreamingResponse,
    AsyncDestinationsResourceWithStreamingResponse,
)

__all__ = ["AlertingResource", "AsyncAlertingResource"]


class AlertingResource(SyncAPIResource):
    @cached_property
    def available_alerts(self) -> AvailableAlertsResource:
        return AvailableAlertsResource(self._client)

    @cached_property
    def destinations(self) -> DestinationsResource:
        return DestinationsResource(self._client)

    @cached_property
    def history(self) -> HistoryResource:
        return HistoryResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AlertingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AlertingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AlertingResourceWithStreamingResponse(self)


class AsyncAlertingResource(AsyncAPIResource):
    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsResource:
        return AsyncAvailableAlertsResource(self._client)

    @cached_property
    def destinations(self) -> AsyncDestinationsResource:
        return AsyncDestinationsResource(self._client)

    @cached_property
    def history(self) -> AsyncHistoryResource:
        return AsyncHistoryResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAlertingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAlertingResourceWithStreamingResponse(self)


class AlertingResourceWithRawResponse:
    def __init__(self, alerting: AlertingResource) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AvailableAlertsResourceWithRawResponse:
        return AvailableAlertsResourceWithRawResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsResourceWithRawResponse:
        return DestinationsResourceWithRawResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        return HistoryResourceWithRawResponse(self._alerting.history)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._alerting.policies)


class AsyncAlertingResourceWithRawResponse:
    def __init__(self, alerting: AsyncAlertingResource) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsResourceWithRawResponse:
        return AsyncAvailableAlertsResourceWithRawResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithRawResponse:
        return AsyncDestinationsResourceWithRawResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        return AsyncHistoryResourceWithRawResponse(self._alerting.history)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._alerting.policies)


class AlertingResourceWithStreamingResponse:
    def __init__(self, alerting: AlertingResource) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AvailableAlertsResourceWithStreamingResponse:
        return AvailableAlertsResourceWithStreamingResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> DestinationsResourceWithStreamingResponse:
        return DestinationsResourceWithStreamingResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        return HistoryResourceWithStreamingResponse(self._alerting.history)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._alerting.policies)


class AsyncAlertingResourceWithStreamingResponse:
    def __init__(self, alerting: AsyncAlertingResource) -> None:
        self._alerting = alerting

    @cached_property
    def available_alerts(self) -> AsyncAvailableAlertsResourceWithStreamingResponse:
        return AsyncAvailableAlertsResourceWithStreamingResponse(self._alerting.available_alerts)

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithStreamingResponse:
        return AsyncDestinationsResourceWithStreamingResponse(self._alerting.destinations)

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        return AsyncHistoryResourceWithStreamingResponse(self._alerting.history)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._alerting.policies)
