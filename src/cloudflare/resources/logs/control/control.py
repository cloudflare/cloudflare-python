# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cmb import (
    CmbResource,
    AsyncCmbResource,
    CmbResourceWithRawResponse,
    AsyncCmbResourceWithRawResponse,
    CmbResourceWithStreamingResponse,
    AsyncCmbResourceWithStreamingResponse,
)
from .cmb.cmb import CmbResource, AsyncCmbResource
from .retention import (
    RetentionResource,
    AsyncRetentionResource,
    RetentionResourceWithRawResponse,
    AsyncRetentionResourceWithRawResponse,
    RetentionResourceWithStreamingResponse,
    AsyncRetentionResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ControlResource", "AsyncControlResource"]


class ControlResource(SyncAPIResource):
    @cached_property
    def retention(self) -> RetentionResource:
        return RetentionResource(self._client)

    @cached_property
    def cmb(self) -> CmbResource:
        return CmbResource(self._client)

    @cached_property
    def with_raw_response(self) -> ControlResourceWithRawResponse:
        return ControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlResourceWithStreamingResponse:
        return ControlResourceWithStreamingResponse(self)


class AsyncControlResource(AsyncAPIResource):
    @cached_property
    def retention(self) -> AsyncRetentionResource:
        return AsyncRetentionResource(self._client)

    @cached_property
    def cmb(self) -> AsyncCmbResource:
        return AsyncCmbResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncControlResourceWithRawResponse:
        return AsyncControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlResourceWithStreamingResponse:
        return AsyncControlResourceWithStreamingResponse(self)


class ControlResourceWithRawResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

    @cached_property
    def retention(self) -> RetentionResourceWithRawResponse:
        return RetentionResourceWithRawResponse(self._control.retention)

    @cached_property
    def cmb(self) -> CmbResourceWithRawResponse:
        return CmbResourceWithRawResponse(self._control.cmb)


class AsyncControlResourceWithRawResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

    @cached_property
    def retention(self) -> AsyncRetentionResourceWithRawResponse:
        return AsyncRetentionResourceWithRawResponse(self._control.retention)

    @cached_property
    def cmb(self) -> AsyncCmbResourceWithRawResponse:
        return AsyncCmbResourceWithRawResponse(self._control.cmb)


class ControlResourceWithStreamingResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

    @cached_property
    def retention(self) -> RetentionResourceWithStreamingResponse:
        return RetentionResourceWithStreamingResponse(self._control.retention)

    @cached_property
    def cmb(self) -> CmbResourceWithStreamingResponse:
        return CmbResourceWithStreamingResponse(self._control.cmb)


class AsyncControlResourceWithStreamingResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

    @cached_property
    def retention(self) -> AsyncRetentionResourceWithStreamingResponse:
        return AsyncRetentionResourceWithStreamingResponse(self._control.retention)

    @cached_property
    def cmb(self) -> AsyncCmbResourceWithStreamingResponse:
        return AsyncCmbResourceWithStreamingResponse(self._control.cmb)
