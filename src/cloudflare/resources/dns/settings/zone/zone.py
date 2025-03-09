# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .views import (
    ViewsResource,
    AsyncViewsResource,
    ViewsResourceWithRawResponse,
    AsyncViewsResourceWithRawResponse,
    ViewsResourceWithStreamingResponse,
    AsyncViewsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ZoneResource", "AsyncZoneResource"]


class ZoneResource(SyncAPIResource):
    @cached_property
    def views(self) -> ViewsResource:
        return ViewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ZoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ZoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ZoneResourceWithStreamingResponse(self)


class AsyncZoneResource(AsyncAPIResource):
    @cached_property
    def views(self) -> AsyncViewsResource:
        return AsyncViewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncZoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncZoneResourceWithStreamingResponse(self)


class ZoneResourceWithRawResponse:
    def __init__(self, zone: ZoneResource) -> None:
        self._zone = zone

    @cached_property
    def views(self) -> ViewsResourceWithRawResponse:
        return ViewsResourceWithRawResponse(self._zone.views)


class AsyncZoneResourceWithRawResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

    @cached_property
    def views(self) -> AsyncViewsResourceWithRawResponse:
        return AsyncViewsResourceWithRawResponse(self._zone.views)


class ZoneResourceWithStreamingResponse:
    def __init__(self, zone: ZoneResource) -> None:
        self._zone = zone

    @cached_property
    def views(self) -> ViewsResourceWithStreamingResponse:
        return ViewsResourceWithStreamingResponse(self._zone.views)


class AsyncZoneResourceWithStreamingResponse:
    def __init__(self, zone: AsyncZoneResource) -> None:
        self._zone = zone

    @cached_property
    def views(self) -> AsyncViewsResourceWithStreamingResponse:
        return AsyncViewsResourceWithStreamingResponse(self._zone.views)
