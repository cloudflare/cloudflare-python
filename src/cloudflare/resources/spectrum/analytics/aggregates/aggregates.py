# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .currents import (
    Currents,
    AsyncCurrents,
    CurrentsWithRawResponse,
    AsyncCurrentsWithRawResponse,
    CurrentsWithStreamingResponse,
    AsyncCurrentsWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Aggregates", "AsyncAggregates"]


class Aggregates(SyncAPIResource):
    @cached_property
    def currents(self) -> Currents:
        return Currents(self._client)

    @cached_property
    def with_raw_response(self) -> AggregatesWithRawResponse:
        return AggregatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregatesWithStreamingResponse:
        return AggregatesWithStreamingResponse(self)


class AsyncAggregates(AsyncAPIResource):
    @cached_property
    def currents(self) -> AsyncCurrents:
        return AsyncCurrents(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAggregatesWithRawResponse:
        return AsyncAggregatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregatesWithStreamingResponse:
        return AsyncAggregatesWithStreamingResponse(self)


class AggregatesWithRawResponse:
    def __init__(self, aggregates: Aggregates) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> CurrentsWithRawResponse:
        return CurrentsWithRawResponse(self._aggregates.currents)


class AsyncAggregatesWithRawResponse:
    def __init__(self, aggregates: AsyncAggregates) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> AsyncCurrentsWithRawResponse:
        return AsyncCurrentsWithRawResponse(self._aggregates.currents)


class AggregatesWithStreamingResponse:
    def __init__(self, aggregates: Aggregates) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> CurrentsWithStreamingResponse:
        return CurrentsWithStreamingResponse(self._aggregates.currents)


class AsyncAggregatesWithStreamingResponse:
    def __init__(self, aggregates: AsyncAggregates) -> None:
        self._aggregates = aggregates

    @cached_property
    def currents(self) -> AsyncCurrentsWithStreamingResponse:
        return AsyncCurrentsWithStreamingResponse(self._aggregates.currents)
