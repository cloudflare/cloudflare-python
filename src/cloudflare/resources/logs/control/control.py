# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cmb import (
    Cmb,
    AsyncCmb,
    CmbWithRawResponse,
    AsyncCmbWithRawResponse,
    CmbWithStreamingResponse,
    AsyncCmbWithStreamingResponse,
)
from .cmb.cmb import Cmb, AsyncCmb
from .retention import (
    Retention,
    AsyncRetention,
    RetentionWithRawResponse,
    AsyncRetentionWithRawResponse,
    RetentionWithStreamingResponse,
    AsyncRetentionWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .retention.retention import Retention, AsyncRetention

__all__ = ["Control", "AsyncControl"]


class Control(SyncAPIResource):
    @cached_property
    def retention(self) -> Retention:
        return Retention(self._client)

    @cached_property
    def cmb(self) -> Cmb:
        return Cmb(self._client)

    @cached_property
    def with_raw_response(self) -> ControlWithRawResponse:
        return ControlWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlWithStreamingResponse:
        return ControlWithStreamingResponse(self)


class AsyncControl(AsyncAPIResource):
    @cached_property
    def retention(self) -> AsyncRetention:
        return AsyncRetention(self._client)

    @cached_property
    def cmb(self) -> AsyncCmb:
        return AsyncCmb(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncControlWithRawResponse:
        return AsyncControlWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlWithStreamingResponse:
        return AsyncControlWithStreamingResponse(self)


class ControlWithRawResponse:
    def __init__(self, control: Control) -> None:
        self._control = control

    @cached_property
    def retention(self) -> RetentionWithRawResponse:
        return RetentionWithRawResponse(self._control.retention)

    @cached_property
    def cmb(self) -> CmbWithRawResponse:
        return CmbWithRawResponse(self._control.cmb)


class AsyncControlWithRawResponse:
    def __init__(self, control: AsyncControl) -> None:
        self._control = control

    @cached_property
    def retention(self) -> AsyncRetentionWithRawResponse:
        return AsyncRetentionWithRawResponse(self._control.retention)

    @cached_property
    def cmb(self) -> AsyncCmbWithRawResponse:
        return AsyncCmbWithRawResponse(self._control.cmb)


class ControlWithStreamingResponse:
    def __init__(self, control: Control) -> None:
        self._control = control

    @cached_property
    def retention(self) -> RetentionWithStreamingResponse:
        return RetentionWithStreamingResponse(self._control.retention)

    @cached_property
    def cmb(self) -> CmbWithStreamingResponse:
        return CmbWithStreamingResponse(self._control.cmb)


class AsyncControlWithStreamingResponse:
    def __init__(self, control: AsyncControl) -> None:
        self._control = control

    @cached_property
    def retention(self) -> AsyncRetentionWithStreamingResponse:
        return AsyncRetentionWithStreamingResponse(self._control.retention)

    @cached_property
    def cmb(self) -> AsyncCmbWithStreamingResponse:
        return AsyncCmbWithStreamingResponse(self._control.cmb)
