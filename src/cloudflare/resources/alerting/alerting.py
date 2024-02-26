# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .v3 import (
    V3,
    AsyncV3,
    V3WithRawResponse,
    AsyncV3WithRawResponse,
    V3WithStreamingResponse,
    AsyncV3WithStreamingResponse,
)
from .v3.v3 import V3, AsyncV3
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Alerting", "AsyncAlerting"]


class Alerting(SyncAPIResource):
    @cached_property
    def v3(self) -> V3:
        return V3(self._client)

    @cached_property
    def with_raw_response(self) -> AlertingWithRawResponse:
        return AlertingWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertingWithStreamingResponse:
        return AlertingWithStreamingResponse(self)


class AsyncAlerting(AsyncAPIResource):
    @cached_property
    def v3(self) -> AsyncV3:
        return AsyncV3(self._client)

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
    def v3(self) -> V3WithRawResponse:
        return V3WithRawResponse(self._alerting.v3)


class AsyncAlertingWithRawResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3(self) -> AsyncV3WithRawResponse:
        return AsyncV3WithRawResponse(self._alerting.v3)


class AlertingWithStreamingResponse:
    def __init__(self, alerting: Alerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3(self) -> V3WithStreamingResponse:
        return V3WithStreamingResponse(self._alerting.v3)


class AsyncAlertingWithStreamingResponse:
    def __init__(self, alerting: AsyncAlerting) -> None:
        self._alerting = alerting

    @cached_property
    def v3(self) -> AsyncV3WithStreamingResponse:
        return AsyncV3WithStreamingResponse(self._alerting.v3)
