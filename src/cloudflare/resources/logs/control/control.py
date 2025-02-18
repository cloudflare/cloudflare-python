# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .cmb.cmb import (
    CmbResource,
    AsyncCmbResource,
    CmbResourceWithRawResponse,
    AsyncCmbResourceWithRawResponse,
    CmbResourceWithStreamingResponse,
    AsyncCmbResourceWithStreamingResponse,
)
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
