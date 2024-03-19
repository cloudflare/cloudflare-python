# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tlds import (
    Tlds,
    AsyncTlds,
    TldsWithRawResponse,
    AsyncTldsWithRawResponse,
    TldsWithStreamingResponse,
    AsyncTldsWithStreamingResponse,
)
from .tlds.tlds import Tlds, AsyncTlds
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Top", "AsyncTop"]


class Top(SyncAPIResource):
    @cached_property
    def tlds(self) -> Tlds:
        return Tlds(self._client)

    @cached_property
    def with_raw_response(self) -> TopWithRawResponse:
        return TopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopWithStreamingResponse:
        return TopWithStreamingResponse(self)


class AsyncTop(AsyncAPIResource):
    @cached_property
    def tlds(self) -> AsyncTlds:
        return AsyncTlds(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopWithRawResponse:
        return AsyncTopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopWithStreamingResponse:
        return AsyncTopWithStreamingResponse(self)


class TopWithRawResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsWithRawResponse:
        return TldsWithRawResponse(self._top.tlds)


class AsyncTopWithRawResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsWithRawResponse:
        return AsyncTldsWithRawResponse(self._top.tlds)


class TopWithStreamingResponse:
    def __init__(self, top: Top) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> TldsWithStreamingResponse:
        return TldsWithStreamingResponse(self._top.tlds)


class AsyncTopWithStreamingResponse:
    def __init__(self, top: AsyncTop) -> None:
        self._top = top

    @cached_property
    def tlds(self) -> AsyncTldsWithStreamingResponse:
        return AsyncTldsWithStreamingResponse(self._top.tlds)
