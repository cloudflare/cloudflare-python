# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tlds import (
    TldsResource,
    AsyncTldsResource,
    TldsResourceWithRawResponse,
    AsyncTldsResourceWithRawResponse,
    TldsResourceWithStreamingResponse,
    AsyncTldsResourceWithStreamingResponse,
)
from .tlds.tlds import TldsResource, AsyncTldsResource
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def tlds(self) -> TldsResource:
        return TldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self)


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def tlds(self) -> AsyncTldsResource:
        return AsyncTldsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self)


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsResourceWithRawResponse:
        return TldsResourceWithRawResponse(self._top.tlds)


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsResourceWithRawResponse:
        return AsyncTldsResourceWithRawResponse(self._top.tlds)


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsResourceWithStreamingResponse:
        return TldsResourceWithStreamingResponse(self._top.tlds)


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsResourceWithStreamingResponse:
        return AsyncTldsResourceWithStreamingResponse(self._top.tlds)
