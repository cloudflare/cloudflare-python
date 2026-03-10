# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GoogleTagGatewayResource", "AsyncGoogleTagGatewayResource"]


class GoogleTagGatewayResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> GoogleTagGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GoogleTagGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoogleTagGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GoogleTagGatewayResourceWithStreamingResponse(self)


class AsyncGoogleTagGatewayResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGoogleTagGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoogleTagGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoogleTagGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGoogleTagGatewayResourceWithStreamingResponse(self)


class GoogleTagGatewayResourceWithRawResponse:
    def __init__(self, google_tag_gateway: GoogleTagGatewayResource) -> None:
        self._google_tag_gateway = google_tag_gateway

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._google_tag_gateway.config)


class AsyncGoogleTagGatewayResourceWithRawResponse:
    def __init__(self, google_tag_gateway: AsyncGoogleTagGatewayResource) -> None:
        self._google_tag_gateway = google_tag_gateway

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._google_tag_gateway.config)


class GoogleTagGatewayResourceWithStreamingResponse:
    def __init__(self, google_tag_gateway: GoogleTagGatewayResource) -> None:
        self._google_tag_gateway = google_tag_gateway

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._google_tag_gateway.config)


class AsyncGoogleTagGatewayResourceWithStreamingResponse:
    def __init__(self, google_tag_gateway: AsyncGoogleTagGatewayResource) -> None:
        self._google_tag_gateway = google_tag_gateway

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._google_tag_gateway.config)
