# File generated from our OpenAPI spec by Stainless.

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
from ...._compat import cached_property
from .retentions import (
    Retentions,
    AsyncRetentions,
    RetentionsWithRawResponse,
    AsyncRetentionsWithRawResponse,
    RetentionsWithStreamingResponse,
    AsyncRetentionsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from .retentions.retentions import Retentions, AsyncRetentions

__all__ = ["Controls", "AsyncControls"]


class Controls(SyncAPIResource):
    @cached_property
    def retentions(self) -> Retentions:
        return Retentions(self._client)

    @cached_property
    def cmb(self) -> Cmb:
        return Cmb(self._client)

    @cached_property
    def with_raw_response(self) -> ControlsWithRawResponse:
        return ControlsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlsWithStreamingResponse:
        return ControlsWithStreamingResponse(self)


class AsyncControls(AsyncAPIResource):
    @cached_property
    def retentions(self) -> AsyncRetentions:
        return AsyncRetentions(self._client)

    @cached_property
    def cmb(self) -> AsyncCmb:
        return AsyncCmb(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncControlsWithRawResponse:
        return AsyncControlsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlsWithStreamingResponse:
        return AsyncControlsWithStreamingResponse(self)


class ControlsWithRawResponse:
    def __init__(self, controls: Controls) -> None:
        self._controls = controls

    @cached_property
    def retentions(self) -> RetentionsWithRawResponse:
        return RetentionsWithRawResponse(self._controls.retentions)

    @cached_property
    def cmb(self) -> CmbWithRawResponse:
        return CmbWithRawResponse(self._controls.cmb)


class AsyncControlsWithRawResponse:
    def __init__(self, controls: AsyncControls) -> None:
        self._controls = controls

    @cached_property
    def retentions(self) -> AsyncRetentionsWithRawResponse:
        return AsyncRetentionsWithRawResponse(self._controls.retentions)

    @cached_property
    def cmb(self) -> AsyncCmbWithRawResponse:
        return AsyncCmbWithRawResponse(self._controls.cmb)


class ControlsWithStreamingResponse:
    def __init__(self, controls: Controls) -> None:
        self._controls = controls

    @cached_property
    def retentions(self) -> RetentionsWithStreamingResponse:
        return RetentionsWithStreamingResponse(self._controls.retentions)

    @cached_property
    def cmb(self) -> CmbWithStreamingResponse:
        return CmbWithStreamingResponse(self._controls.cmb)


class AsyncControlsWithStreamingResponse:
    def __init__(self, controls: AsyncControls) -> None:
        self._controls = controls

    @cached_property
    def retentions(self) -> AsyncRetentionsWithStreamingResponse:
        return AsyncRetentionsWithStreamingResponse(self._controls.retentions)

    @cached_property
    def cmb(self) -> AsyncCmbWithStreamingResponse:
        return AsyncCmbWithStreamingResponse(self._controls.cmb)
