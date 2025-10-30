# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .telemetry import (
    TelemetryResource,
    AsyncTelemetryResource,
    TelemetryResourceWithRawResponse,
    AsyncTelemetryResourceWithRawResponse,
    TelemetryResourceWithStreamingResponse,
    AsyncTelemetryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ObservabilityResource", "AsyncObservabilityResource"]


class ObservabilityResource(SyncAPIResource):
    @cached_property
    def telemetry(self) -> TelemetryResource:
        return TelemetryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ObservabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ObservabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ObservabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ObservabilityResourceWithStreamingResponse(self)


class AsyncObservabilityResource(AsyncAPIResource):
    @cached_property
    def telemetry(self) -> AsyncTelemetryResource:
        return AsyncTelemetryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncObservabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncObservabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncObservabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncObservabilityResourceWithStreamingResponse(self)


class ObservabilityResourceWithRawResponse:
    def __init__(self, observability: ObservabilityResource) -> None:
        self._observability = observability

    @cached_property
    def telemetry(self) -> TelemetryResourceWithRawResponse:
        return TelemetryResourceWithRawResponse(self._observability.telemetry)


class AsyncObservabilityResourceWithRawResponse:
    def __init__(self, observability: AsyncObservabilityResource) -> None:
        self._observability = observability

    @cached_property
    def telemetry(self) -> AsyncTelemetryResourceWithRawResponse:
        return AsyncTelemetryResourceWithRawResponse(self._observability.telemetry)


class ObservabilityResourceWithStreamingResponse:
    def __init__(self, observability: ObservabilityResource) -> None:
        self._observability = observability

    @cached_property
    def telemetry(self) -> TelemetryResourceWithStreamingResponse:
        return TelemetryResourceWithStreamingResponse(self._observability.telemetry)


class AsyncObservabilityResourceWithStreamingResponse:
    def __init__(self, observability: AsyncObservabilityResource) -> None:
        self._observability = observability

    @cached_property
    def telemetry(self) -> AsyncTelemetryResourceWithStreamingResponse:
        return AsyncTelemetryResourceWithStreamingResponse(self._observability.telemetry)
