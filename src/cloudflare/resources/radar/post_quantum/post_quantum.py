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
from .origin import (
    OriginResource,
    AsyncOriginResource,
    OriginResourceWithRawResponse,
    AsyncOriginResourceWithRawResponse,
    OriginResourceWithStreamingResponse,
    AsyncOriginResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PostQuantumResource", "AsyncPostQuantumResource"]


class PostQuantumResource(SyncAPIResource):
    @cached_property
    def origin(self) -> OriginResource:
        return OriginResource(self._client)

    @cached_property
    def tls(self) -> TLSResource:
        return TLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostQuantumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PostQuantumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostQuantumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PostQuantumResourceWithStreamingResponse(self)


class AsyncPostQuantumResource(AsyncAPIResource):
    @cached_property
    def origin(self) -> AsyncOriginResource:
        return AsyncOriginResource(self._client)

    @cached_property
    def tls(self) -> AsyncTLSResource:
        return AsyncTLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostQuantumResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostQuantumResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostQuantumResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPostQuantumResourceWithStreamingResponse(self)


class PostQuantumResourceWithRawResponse:
    def __init__(self, post_quantum: PostQuantumResource) -> None:
        self._post_quantum = post_quantum

    @cached_property
    def origin(self) -> OriginResourceWithRawResponse:
        return OriginResourceWithRawResponse(self._post_quantum.origin)

    @cached_property
    def tls(self) -> TLSResourceWithRawResponse:
        return TLSResourceWithRawResponse(self._post_quantum.tls)


class AsyncPostQuantumResourceWithRawResponse:
    def __init__(self, post_quantum: AsyncPostQuantumResource) -> None:
        self._post_quantum = post_quantum

    @cached_property
    def origin(self) -> AsyncOriginResourceWithRawResponse:
        return AsyncOriginResourceWithRawResponse(self._post_quantum.origin)

    @cached_property
    def tls(self) -> AsyncTLSResourceWithRawResponse:
        return AsyncTLSResourceWithRawResponse(self._post_quantum.tls)


class PostQuantumResourceWithStreamingResponse:
    def __init__(self, post_quantum: PostQuantumResource) -> None:
        self._post_quantum = post_quantum

    @cached_property
    def origin(self) -> OriginResourceWithStreamingResponse:
        return OriginResourceWithStreamingResponse(self._post_quantum.origin)

    @cached_property
    def tls(self) -> TLSResourceWithStreamingResponse:
        return TLSResourceWithStreamingResponse(self._post_quantum.tls)


class AsyncPostQuantumResourceWithStreamingResponse:
    def __init__(self, post_quantum: AsyncPostQuantumResource) -> None:
        self._post_quantum = post_quantum

    @cached_property
    def origin(self) -> AsyncOriginResourceWithStreamingResponse:
        return AsyncOriginResourceWithStreamingResponse(self._post_quantum.origin)

    @cached_property
    def tls(self) -> AsyncTLSResourceWithStreamingResponse:
        return AsyncTLSResourceWithStreamingResponse(self._post_quantum.tls)
