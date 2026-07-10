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
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CmbResource", "AsyncCmbResource"]


class CmbResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> CmbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CmbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CmbResourceWithStreamingResponse(self)


class AsyncCmbResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCmbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCmbResourceWithStreamingResponse(self)


class CmbResourceWithRawResponse:
    def __init__(self, cmb: CmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._cmb.config)


class AsyncCmbResourceWithRawResponse:
    def __init__(self, cmb: AsyncCmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._cmb.config)


class CmbResourceWithStreamingResponse:
    def __init__(self, cmb: CmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._cmb.config)


class AsyncCmbResourceWithStreamingResponse:
    def __init__(self, cmb: AsyncCmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._cmb.config)
