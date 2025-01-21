# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)

__all__ = ["HostnamesResource", "AsyncHostnamesResource"]


class HostnamesResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HostnamesResourceWithStreamingResponse(self)


class AsyncHostnamesResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHostnamesResourceWithStreamingResponse(self)


class HostnamesResourceWithRawResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._hostnames.settings)


class AsyncHostnamesResourceWithRawResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._hostnames.settings)


class HostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._hostnames.settings)


class AsyncHostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._hostnames.settings)
