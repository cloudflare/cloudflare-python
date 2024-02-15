# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .live import (
    Live,
    AsyncLive,
    LiveWithRawResponse,
    AsyncLiveWithRawResponse,
    LiveWithStreamingResponse,
    AsyncLiveWithStreamingResponse,
)
from .devices import (
    Devices,
    AsyncDevices,
    DevicesWithRawResponse,
    AsyncDevicesWithRawResponse,
    DevicesWithStreamingResponse,
    AsyncDevicesWithStreamingResponse,
)
from .over_time import (
    OverTime,
    AsyncOverTime,
    OverTimeWithRawResponse,
    AsyncOverTimeWithRawResponse,
    OverTimeWithStreamingResponse,
    AsyncOverTimeWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FleetStatus", "AsyncFleetStatus"]


class FleetStatus(SyncAPIResource):
    @cached_property
    def devices(self) -> Devices:
        return Devices(self._client)

    @cached_property
    def live(self) -> Live:
        return Live(self._client)

    @cached_property
    def over_time(self) -> OverTime:
        return OverTime(self._client)

    @cached_property
    def with_raw_response(self) -> FleetStatusWithRawResponse:
        return FleetStatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FleetStatusWithStreamingResponse:
        return FleetStatusWithStreamingResponse(self)


class AsyncFleetStatus(AsyncAPIResource):
    @cached_property
    def devices(self) -> AsyncDevices:
        return AsyncDevices(self._client)

    @cached_property
    def live(self) -> AsyncLive:
        return AsyncLive(self._client)

    @cached_property
    def over_time(self) -> AsyncOverTime:
        return AsyncOverTime(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFleetStatusWithRawResponse:
        return AsyncFleetStatusWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFleetStatusWithStreamingResponse:
        return AsyncFleetStatusWithStreamingResponse(self)


class FleetStatusWithRawResponse:
    def __init__(self, fleet_status: FleetStatus) -> None:
        self._fleet_status = fleet_status

    @cached_property
    def devices(self) -> DevicesWithRawResponse:
        return DevicesWithRawResponse(self._fleet_status.devices)

    @cached_property
    def live(self) -> LiveWithRawResponse:
        return LiveWithRawResponse(self._fleet_status.live)

    @cached_property
    def over_time(self) -> OverTimeWithRawResponse:
        return OverTimeWithRawResponse(self._fleet_status.over_time)


class AsyncFleetStatusWithRawResponse:
    def __init__(self, fleet_status: AsyncFleetStatus) -> None:
        self._fleet_status = fleet_status

    @cached_property
    def devices(self) -> AsyncDevicesWithRawResponse:
        return AsyncDevicesWithRawResponse(self._fleet_status.devices)

    @cached_property
    def live(self) -> AsyncLiveWithRawResponse:
        return AsyncLiveWithRawResponse(self._fleet_status.live)

    @cached_property
    def over_time(self) -> AsyncOverTimeWithRawResponse:
        return AsyncOverTimeWithRawResponse(self._fleet_status.over_time)


class FleetStatusWithStreamingResponse:
    def __init__(self, fleet_status: FleetStatus) -> None:
        self._fleet_status = fleet_status

    @cached_property
    def devices(self) -> DevicesWithStreamingResponse:
        return DevicesWithStreamingResponse(self._fleet_status.devices)

    @cached_property
    def live(self) -> LiveWithStreamingResponse:
        return LiveWithStreamingResponse(self._fleet_status.live)

    @cached_property
    def over_time(self) -> OverTimeWithStreamingResponse:
        return OverTimeWithStreamingResponse(self._fleet_status.over_time)


class AsyncFleetStatusWithStreamingResponse:
    def __init__(self, fleet_status: AsyncFleetStatus) -> None:
        self._fleet_status = fleet_status

    @cached_property
    def devices(self) -> AsyncDevicesWithStreamingResponse:
        return AsyncDevicesWithStreamingResponse(self._fleet_status.devices)

    @cached_property
    def live(self) -> AsyncLiveWithStreamingResponse:
        return AsyncLiveWithStreamingResponse(self._fleet_status.live)

    @cached_property
    def over_time(self) -> AsyncOverTimeWithStreamingResponse:
        return AsyncOverTimeWithStreamingResponse(self._fleet_status.over_time)
