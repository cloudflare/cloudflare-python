# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .isps import (
    ISPsResource,
    AsyncISPsResource,
    ISPsResourceWithRawResponse,
    AsyncISPsResourceWithRawResponse,
    ISPsResourceWithStreamingResponse,
    AsyncISPsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def isps(self) -> ISPsResource:
        return ISPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DevicesResourceWithStreamingResponse(self)


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def isps(self) -> AsyncISPsResource:
        return AsyncISPsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDevicesResourceWithStreamingResponse(self)


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

    @cached_property
    def isps(self) -> ISPsResourceWithRawResponse:
        return ISPsResourceWithRawResponse(self._devices.isps)


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

    @cached_property
    def isps(self) -> AsyncISPsResourceWithRawResponse:
        return AsyncISPsResourceWithRawResponse(self._devices.isps)


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

    @cached_property
    def isps(self) -> ISPsResourceWithStreamingResponse:
        return ISPsResourceWithStreamingResponse(self._devices.isps)


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

    @cached_property
    def isps(self) -> AsyncISPsResourceWithStreamingResponse:
        return AsyncISPsResourceWithStreamingResponse(self._devices.isps)
