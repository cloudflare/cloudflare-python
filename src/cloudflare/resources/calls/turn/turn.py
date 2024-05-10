# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TURNResource", "AsyncTURNResource"]


class TURNResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> TURNResourceWithRawResponse:
        return TURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TURNResourceWithStreamingResponse:
        return TURNResourceWithStreamingResponse(self)


class AsyncTURNResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTURNResourceWithRawResponse:
        return AsyncTURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTURNResourceWithStreamingResponse:
        return AsyncTURNResourceWithStreamingResponse(self)


class TURNResourceWithRawResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._turn.keys)


class AsyncTURNResourceWithRawResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._turn.keys)


class TURNResourceWithStreamingResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._turn.keys)


class AsyncTURNResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._turn.keys)
