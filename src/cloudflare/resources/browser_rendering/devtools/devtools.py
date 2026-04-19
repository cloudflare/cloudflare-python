# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .browser.browser import (
    BrowserResource,
    AsyncBrowserResource,
    BrowserResourceWithRawResponse,
    AsyncBrowserResourceWithRawResponse,
    BrowserResourceWithStreamingResponse,
    AsyncBrowserResourceWithStreamingResponse,
)

__all__ = ["DevtoolsResource", "AsyncDevtoolsResource"]


class DevtoolsResource(SyncAPIResource):
    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def browser(self) -> BrowserResource:
        return BrowserResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevtoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return DevtoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevtoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return DevtoolsResourceWithStreamingResponse(self)


class AsyncDevtoolsResource(AsyncAPIResource):
    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def browser(self) -> AsyncBrowserResource:
        return AsyncBrowserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevtoolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevtoolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevtoolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncDevtoolsResourceWithStreamingResponse(self)


class DevtoolsResourceWithRawResponse:
    def __init__(self, devtools: DevtoolsResource) -> None:
        self._devtools = devtools

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._devtools.session)

    @cached_property
    def browser(self) -> BrowserResourceWithRawResponse:
        return BrowserResourceWithRawResponse(self._devtools.browser)


class AsyncDevtoolsResourceWithRawResponse:
    def __init__(self, devtools: AsyncDevtoolsResource) -> None:
        self._devtools = devtools

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._devtools.session)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithRawResponse:
        return AsyncBrowserResourceWithRawResponse(self._devtools.browser)


class DevtoolsResourceWithStreamingResponse:
    def __init__(self, devtools: DevtoolsResource) -> None:
        self._devtools = devtools

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._devtools.session)

    @cached_property
    def browser(self) -> BrowserResourceWithStreamingResponse:
        return BrowserResourceWithStreamingResponse(self._devtools.browser)


class AsyncDevtoolsResourceWithStreamingResponse:
    def __init__(self, devtools: AsyncDevtoolsResource) -> None:
        self._devtools = devtools

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._devtools.session)

    @cached_property
    def browser(self) -> AsyncBrowserResourceWithStreamingResponse:
        return AsyncBrowserResourceWithStreamingResponse(self._devtools.browser)
