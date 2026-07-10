# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tlds.tlds import (
    TLDsResource,
    AsyncTLDsResource,
    TLDsResourceWithRawResponse,
    AsyncTLDsResourceWithRawResponse,
    TLDsResourceWithStreamingResponse,
    AsyncTLDsResourceWithStreamingResponse,
)
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def tlds(self) -> TLDsResource:
        return TLDsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return TopResourceWithStreamingResponse(self)


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def tlds(self) -> AsyncTLDsResource:
        return AsyncTLDsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncTopResourceWithStreamingResponse(self)


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TLDsResourceWithRawResponse:
        return TLDsResourceWithRawResponse(self._top.tlds)


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTLDsResourceWithRawResponse:
        return AsyncTLDsResourceWithRawResponse(self._top.tlds)


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TLDsResourceWithStreamingResponse:
        return TLDsResourceWithStreamingResponse(self._top.tlds)


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTLDsResourceWithStreamingResponse:
        return AsyncTLDsResourceWithStreamingResponse(self._top.tlds)
