# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .inspect import (
    InspectResource,
    AsyncInspectResource,
    InspectResourceWithRawResponse,
    AsyncInspectResourceWithRawResponse,
    InspectResourceWithStreamingResponse,
    AsyncInspectResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SPFResource", "AsyncSPFResource"]


class SPFResource(SyncAPIResource):
    @cached_property
    def inspect(self) -> InspectResource:
        return InspectResource(self._client)

    @cached_property
    def with_raw_response(self) -> SPFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SPFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SPFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SPFResourceWithStreamingResponse(self)


class AsyncSPFResource(AsyncAPIResource):
    @cached_property
    def inspect(self) -> AsyncInspectResource:
        return AsyncInspectResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSPFResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSPFResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSPFResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSPFResourceWithStreamingResponse(self)


class SPFResourceWithRawResponse:
    def __init__(self, spf: SPFResource) -> None:
        self._spf = spf

    @cached_property
    def inspect(self) -> InspectResourceWithRawResponse:
        return InspectResourceWithRawResponse(self._spf.inspect)


class AsyncSPFResourceWithRawResponse:
    def __init__(self, spf: AsyncSPFResource) -> None:
        self._spf = spf

    @cached_property
    def inspect(self) -> AsyncInspectResourceWithRawResponse:
        return AsyncInspectResourceWithRawResponse(self._spf.inspect)


class SPFResourceWithStreamingResponse:
    def __init__(self, spf: SPFResource) -> None:
        self._spf = spf

    @cached_property
    def inspect(self) -> InspectResourceWithStreamingResponse:
        return InspectResourceWithStreamingResponse(self._spf.inspect)


class AsyncSPFResourceWithStreamingResponse:
    def __init__(self, spf: AsyncSPFResource) -> None:
        self._spf = spf

    @cached_property
    def inspect(self) -> AsyncInspectResourceWithStreamingResponse:
        return AsyncInspectResourceWithStreamingResponse(self._spf.inspect)
