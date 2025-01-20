# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tls import (
    TLSResource,
    AsyncTLSResource,
    TLSResourceWithRawResponse,
    AsyncTLSResourceWithRawResponse,
    TLSResourceWithStreamingResponse,
    AsyncTLSResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def tls(self) -> TLSResource:
        return TLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def tls(self) -> AsyncTLSResource:
        return AsyncTLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSResourceWithRawResponse:
        return TLSResourceWithRawResponse(self._settings.tls)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSResourceWithRawResponse:
        return AsyncTLSResourceWithRawResponse(self._settings.tls)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSResourceWithStreamingResponse:
        return TLSResourceWithStreamingResponse(self._settings.tls)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSResourceWithStreamingResponse:
        return AsyncTLSResourceWithStreamingResponse(self._settings.tls)
