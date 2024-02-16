# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .vector import (
    Vector,
    AsyncVector,
    VectorWithRawResponse,
    AsyncVectorWithRawResponse,
    VectorWithStreamingResponse,
    AsyncVectorWithStreamingResponse,
)
from .industry import (
    Industry,
    AsyncIndustry,
    IndustryWithRawResponse,
    AsyncIndustryWithRawResponse,
    IndustryWithStreamingResponse,
    AsyncIndustryWithStreamingResponse,
)
from .protocol import (
    Protocol,
    AsyncProtocol,
    ProtocolWithRawResponse,
    AsyncProtocolWithRawResponse,
    ProtocolWithStreamingResponse,
    AsyncProtocolWithStreamingResponse,
)
from .vertical import (
    Vertical,
    AsyncVertical,
    VerticalWithRawResponse,
    AsyncVerticalWithRawResponse,
    VerticalWithStreamingResponse,
    AsyncVerticalWithStreamingResponse,
)
from .ip_version import (
    IPVersion,
    AsyncIPVersion,
    IPVersionWithRawResponse,
    AsyncIPVersionWithRawResponse,
    IPVersionWithStreamingResponse,
    AsyncIPVersionWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TimeseriesGroups", "AsyncTimeseriesGroups"]


class TimeseriesGroups(SyncAPIResource):
    @cached_property
    def industry(self) -> Industry:
        return Industry(self._client)

    @cached_property
    def ip_version(self) -> IPVersion:
        return IPVersion(self._client)

    @cached_property
    def protocol(self) -> Protocol:
        return Protocol(self._client)

    @cached_property
    def vector(self) -> Vector:
        return Vector(self._client)

    @cached_property
    def vertical(self) -> Vertical:
        return Vertical(self._client)

    @cached_property
    def with_raw_response(self) -> TimeseriesGroupsWithRawResponse:
        return TimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimeseriesGroupsWithStreamingResponse:
        return TimeseriesGroupsWithStreamingResponse(self)


class AsyncTimeseriesGroups(AsyncAPIResource):
    @cached_property
    def industry(self) -> AsyncIndustry:
        return AsyncIndustry(self._client)

    @cached_property
    def ip_version(self) -> AsyncIPVersion:
        return AsyncIPVersion(self._client)

    @cached_property
    def protocol(self) -> AsyncProtocol:
        return AsyncProtocol(self._client)

    @cached_property
    def vector(self) -> AsyncVector:
        return AsyncVector(self._client)

    @cached_property
    def vertical(self) -> AsyncVertical:
        return AsyncVertical(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTimeseriesGroupsWithRawResponse:
        return AsyncTimeseriesGroupsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimeseriesGroupsWithStreamingResponse:
        return AsyncTimeseriesGroupsWithStreamingResponse(self)


class TimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def industry(self) -> IndustryWithRawResponse:
        return IndustryWithRawResponse(self._timeseries_groups.industry)

    @cached_property
    def ip_version(self) -> IPVersionWithRawResponse:
        return IPVersionWithRawResponse(self._timeseries_groups.ip_version)

    @cached_property
    def protocol(self) -> ProtocolWithRawResponse:
        return ProtocolWithRawResponse(self._timeseries_groups.protocol)

    @cached_property
    def vector(self) -> VectorWithRawResponse:
        return VectorWithRawResponse(self._timeseries_groups.vector)

    @cached_property
    def vertical(self) -> VerticalWithRawResponse:
        return VerticalWithRawResponse(self._timeseries_groups.vertical)


class AsyncTimeseriesGroupsWithRawResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def industry(self) -> AsyncIndustryWithRawResponse:
        return AsyncIndustryWithRawResponse(self._timeseries_groups.industry)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithRawResponse:
        return AsyncIPVersionWithRawResponse(self._timeseries_groups.ip_version)

    @cached_property
    def protocol(self) -> AsyncProtocolWithRawResponse:
        return AsyncProtocolWithRawResponse(self._timeseries_groups.protocol)

    @cached_property
    def vector(self) -> AsyncVectorWithRawResponse:
        return AsyncVectorWithRawResponse(self._timeseries_groups.vector)

    @cached_property
    def vertical(self) -> AsyncVerticalWithRawResponse:
        return AsyncVerticalWithRawResponse(self._timeseries_groups.vertical)


class TimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: TimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def industry(self) -> IndustryWithStreamingResponse:
        return IndustryWithStreamingResponse(self._timeseries_groups.industry)

    @cached_property
    def ip_version(self) -> IPVersionWithStreamingResponse:
        return IPVersionWithStreamingResponse(self._timeseries_groups.ip_version)

    @cached_property
    def protocol(self) -> ProtocolWithStreamingResponse:
        return ProtocolWithStreamingResponse(self._timeseries_groups.protocol)

    @cached_property
    def vector(self) -> VectorWithStreamingResponse:
        return VectorWithStreamingResponse(self._timeseries_groups.vector)

    @cached_property
    def vertical(self) -> VerticalWithStreamingResponse:
        return VerticalWithStreamingResponse(self._timeseries_groups.vertical)


class AsyncTimeseriesGroupsWithStreamingResponse:
    def __init__(self, timeseries_groups: AsyncTimeseriesGroups) -> None:
        self._timeseries_groups = timeseries_groups

    @cached_property
    def industry(self) -> AsyncIndustryWithStreamingResponse:
        return AsyncIndustryWithStreamingResponse(self._timeseries_groups.industry)

    @cached_property
    def ip_version(self) -> AsyncIPVersionWithStreamingResponse:
        return AsyncIPVersionWithStreamingResponse(self._timeseries_groups.ip_version)

    @cached_property
    def protocol(self) -> AsyncProtocolWithStreamingResponse:
        return AsyncProtocolWithStreamingResponse(self._timeseries_groups.protocol)

    @cached_property
    def vector(self) -> AsyncVectorWithStreamingResponse:
        return AsyncVectorWithStreamingResponse(self._timeseries_groups.vector)

    @cached_property
    def vertical(self) -> AsyncVerticalWithStreamingResponse:
        return AsyncVerticalWithStreamingResponse(self._timeseries_groups.vertical)
