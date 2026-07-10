# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .apps.apps import (
    AppsResource,
    AsyncAppsResource,
    AppsResourceWithRawResponse,
    AsyncAppsResourceWithRawResponse,
    AppsResourceWithStreamingResponse,
    AsyncAppsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["FlagshipResource", "AsyncFlagshipResource"]


class FlagshipResource(SyncAPIResource):
    @cached_property
    def apps(self) -> AppsResource:
        return AppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FlagshipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return FlagshipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FlagshipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return FlagshipResourceWithStreamingResponse(self)


class AsyncFlagshipResource(AsyncAPIResource):
    @cached_property
    def apps(self) -> AsyncAppsResource:
        return AsyncAppsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFlagshipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFlagshipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFlagshipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncFlagshipResourceWithStreamingResponse(self)


class FlagshipResourceWithRawResponse:
    def __init__(self, flagship: FlagshipResource) -> None:
        self._flagship = flagship

    @cached_property
    def apps(self) -> AppsResourceWithRawResponse:
        return AppsResourceWithRawResponse(self._flagship.apps)


class AsyncFlagshipResourceWithRawResponse:
    def __init__(self, flagship: AsyncFlagshipResource) -> None:
        self._flagship = flagship

    @cached_property
    def apps(self) -> AsyncAppsResourceWithRawResponse:
        return AsyncAppsResourceWithRawResponse(self._flagship.apps)


class FlagshipResourceWithStreamingResponse:
    def __init__(self, flagship: FlagshipResource) -> None:
        self._flagship = flagship

    @cached_property
    def apps(self) -> AppsResourceWithStreamingResponse:
        return AppsResourceWithStreamingResponse(self._flagship.apps)


class AsyncFlagshipResourceWithStreamingResponse:
    def __init__(self, flagship: AsyncFlagshipResource) -> None:
        self._flagship = flagship

    @cached_property
    def apps(self) -> AsyncAppsResourceWithStreamingResponse:
        return AsyncAppsResourceWithStreamingResponse(self._flagship.apps)
